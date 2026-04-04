#!/usr/bin/env python3
"""
MCP Server for Vietnamese Stock Market Data.

Combines two data sources:
  - DNSE LightSpeed API: OHLC price/volume data (fast, official)
  - vnstock3 library: Financial statements, ratios, company info (comprehensive)

Rate limiting is enforced for vnstock3 Community tier (55 req/min with safety margin).

    Environment Variables:
      DNSE_API_KEY     - (Optional/Deprecated) DNSE LightSpeed API Key
      DNSE_API_SECRET  - (Optional/Deprecated) DNSE LightSpeed API Secret
      API_KEY          - vnstock API key for Community tier (60 req/min)
    """

import asyncio
import csv
import json
import os
import traceback
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel, Field, ConfigDict, field_validator
from mcp.server.fastmcp import FastMCP

from rate_limiter import vnstock_limiter
from dnse_client import DNSEClient, DNSEAuthError

# ──────────────────────────────────────────────────────────────────────
# Load .env file (for DNSE credentials and vnstock API key)
# ──────────────────────────────────────────────────────────────────────
def _load_env():
    """Load environment variables from .env file in project root."""
    # Walk up from this file to find the project root .env
    current = Path(__file__).resolve().parent
    for _ in range(5):  # max 5 levels up
        env_path = current / ".env"
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, _, value = line.partition("=")
                        os.environ.setdefault(key.strip(), value.strip())
            return
        current = current.parent

_load_env()

# ──────────────────────────────────────────────────────────────────────
# Initialize MCP Server
# ──────────────────────────────────────────────────────────────────────
mcp = FastMCP("vnstock_mcp")

# ──────────────────────────────────────────────────────────────────────
# Register vnstock API key for Community tier (60 req/min)
# ──────────────────────────────────────────────────────────────────────
_vnstock_registered = False

def _register_vnstock_api_key():
    """Register vnstock API key from environment for higher rate limits."""
    global _vnstock_registered
    if _vnstock_registered:
        return
    api_key = os.environ.get("API_KEY", "")
    if api_key and api_key.startswith("vnstock_"):
        try:
            from vnstock import register_user
            register_user(api_key=api_key)
            _vnstock_registered = True
        except Exception:
            pass  # Fall back to guest tier

# ──────────────────────────────────────────────────────────────────────
# Lazy-loaded vnstock to avoid import overhead at startup
# ──────────────────────────────────────────────────────────────────────
_vnstock_module = None

def _get_vnstock():
    """Lazy import vnstock and register API key."""
    global _vnstock_module
    if _vnstock_module is None:
        _register_vnstock_api_key()
        from vnstock import Vnstock
        _vnstock_module = Vnstock
    return _vnstock_module


def _get_stock(symbol: str, source: str = "KBS"):
    """Create a vnstock stock object for a given ticker."""
    Vnstock = _get_vnstock()
    return Vnstock().stock(symbol=symbol, source=source)


# ──────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────
def _df_to_json(df, max_rows: int = 100) -> str:
    """Convert a pandas DataFrame to JSON string for MCP response."""
    if df is None or df.empty:
        return json.dumps({"data": [], "message": "No data returned"})

    # Truncate if too large
    truncated = len(df) > max_rows
    if truncated:
        df = df.head(max_rows)

    records = json.loads(df.to_json(orient="records", date_format="iso", force_ascii=False))
    result = {
        "count": len(records),
        "data": records,
    }
    if truncated:
        result["warning"] = f"Results truncated to {max_rows} rows. Total available: {len(df)}"

    return json.dumps(result, ensure_ascii=False, indent=2)


def _handle_error(e: Exception, context: str = "") -> str:
    """Format error messages consistently across all tools."""
    prefix = f"Error in {context}: " if context else "Error: "

    if isinstance(e, DNSEAuthError):
        return (
            f"{prefix}DNSE authentication failed. "
            "Please set DNSE_API_KEY and DNSE_API_SECRET environment variables. "
            "Register at: https://entradex.dnse.com.vn/thong-tin-ca-nhan/light-speed"
        )
    if isinstance(e, TimeoutError):
        return (
            f"{prefix}Rate limit timeout. vnstock3 Community tier allows 60 requests/min. "
            f"Current remaining: {vnstock_limiter.remaining}, "
            f"reset in: {vnstock_limiter.reset_in:.0f}s. "
            "Try again in a minute or reduce the number of concurrent requests."
        )
    if "429" in str(e) or "rate" in str(e).lower():
        return (
            f"{prefix}Rate limited by upstream API. "
            "Please wait 60 seconds before retrying. "
            f"Details: {e}"
        )

    return f"{prefix}{type(e).__name__}: {e}"


# ──────────────────────────────────────────────────────────────────────
# Enums & Input Models
# ──────────────────────────────────────────────────────────────────────
class OHLCResolution(str, Enum):
    MIN_1 = "1"
    MIN_3 = "3"
    MIN_5 = "5"
    MIN_15 = "15"
    MIN_30 = "30"
    HOUR_1 = "1h"
    DAY_1 = "1D"
    WEEK_1 = "1W"


class AssetType(str, Enum):
    STOCK = "STOCK"
    DERIVATIVE = "DERIVATIVE"
    INDEX = "INDEX"


class FinancialPeriod(str, Enum):
    QUARTER = "quarter"
    YEAR = "year"


class OHLCInput(BaseModel):
    """Input for DNSE OHLC historical data."""
    model_config = ConfigDict(str_strip_whitespace=True)

    symbol: str = Field(
        ...,
        description="Stock ticker symbol (e.g., 'FPT', 'VCB', 'HPG') or index name (e.g., 'VNINDEX', 'VN30')",
        min_length=1,
        max_length=20,
    )
    asset_type: AssetType = Field(
        default=AssetType.STOCK,
        description="Asset type: 'STOCK' for equities, 'INDEX' for market indices, 'DERIVATIVE' for futures",
    )
    resolution: OHLCResolution = Field(
        default=OHLCResolution.DAY_1,
        description="Candle timeframe: '1','3','5','15','30' (minutes), '1h' (hour), '1D' (day), '1W' (week)",
    )
    start_date: Optional[str] = Field(
        default=None,
        description="Start date in YYYY-MM-DD format. Default: 1 year ago",
    )
    end_date: Optional[str] = Field(
        default=None,
        description="End date in YYYY-MM-DD format. Default: today",
    )

    @field_validator("symbol")
    @classmethod
    def upper_symbol(cls, v: str) -> str:
        return v.upper().strip()


class FinancialInput(BaseModel):
    """Input for vnstock3 financial data tools."""
    model_config = ConfigDict(str_strip_whitespace=True)

    symbol: str = Field(
        ...,
        description="Stock ticker symbol (e.g., 'FPT', 'VCB', 'HPG')",
        min_length=1,
        max_length=10,
    )
    period: FinancialPeriod = Field(
        default=FinancialPeriod.QUARTER,
        description="Reporting period: 'quarter' or 'year'",
    )

    @field_validator("symbol")
    @classmethod
    def upper_symbol(cls, v: str) -> str:
        return v.upper().strip()


class BacktestUniverseInput(BaseModel):
    """Input for querying the backtest stock universe."""
    model_config = ConfigDict(str_strip_whitespace=True)

    exchange: Optional[str] = Field(
        default=None,
        description="Filter by exchange: 'HSX', 'HNX', 'UPCOM', or None for all",
    )
    min_win_rate: Optional[float] = Field(
        default=None,
        description="Minimum win rate (%) to filter stocks. E.g., 40.0",
    )
    min_total_return: Optional[float] = Field(
        default=None,
        description="Minimum total return (%) to filter stocks. E.g., 50.0",
    )
    top_n: Optional[int] = Field(
        default=None,
        description="Return only top N stocks sorted by total_return_pct descending",
    )


class CompanyInput(BaseModel):
    """Input for company overview."""
    model_config = ConfigDict(str_strip_whitespace=True)

    symbol: str = Field(
        ...,
        description="Stock ticker symbol (e.g., 'FPT', 'VCB')",
        min_length=1,
        max_length=10,
    )

    @field_validator("symbol")
    @classmethod
    def upper_symbol(cls, v: str) -> str:
        return v.upper().strip()


# ──────────────────────────────────────────────────────────────────────
# Tool 1: DNSE OHLC Data
# ──────────────────────────────────────────────────────────────────────
@mcp.tool(
    name="dnse_get_ohlc",
    annotations={
        "title": "Get Stock OHLC Price Data (DNSE)",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def dnse_get_ohlc(params: OHLCInput) -> str:
    """Fetch historical OHLC (Open/High/Low/Close/Volume) candlestick data from DNSE.

    Retrieves price and volume data for Vietnamese stocks, indices (VN-Index, VN30),
    and derivatives. Supports multiple timeframes from 1-minute to weekly candles.

    Data source: DNSE Chart/Market Data API (public, no auth required).

    Returns:
        JSON with list of candle records, each containing:
        - time (int): Unix timestamp
        - date (str): Human-readable date
        - open, high, low, close (float): Price data
        - volume (int): Trading volume
    """
    try:
        client = DNSEClient()

        # Parse dates to Unix timestamps
        from_ts = None
        to_ts = None

        if params.start_date:
            dt = datetime.strptime(params.start_date, "%Y-%m-%d")
            from_ts = int(dt.timestamp())

        if params.end_date:
            dt = datetime.strptime(params.end_date, "%Y-%m-%d")
            # End of day
            dt = dt.replace(hour=23, minute=59, second=59)
            to_ts = int(dt.timestamp())

        rows = await client.get_ohlc(
            symbol=params.symbol,
            asset_type=params.asset_type.value,
            resolution=params.resolution.value,
            from_ts=from_ts,
            to_ts=to_ts,
        )

        result = {
            "symbol": params.symbol,
            "type": params.asset_type.value,
            "resolution": params.resolution.value,
            "count": len(rows),
            "data": rows,
        }

        return json.dumps(result, ensure_ascii=False, indent=2)

    except Exception as e:
        return _handle_error(e, "dnse_get_ohlc")


# ──────────────────────────────────────────────────────────────────────
# Tool 2: Income Statement
# ──────────────────────────────────────────────────────────────────────
@mcp.tool(
    name="vnstock_income_statement",
    annotations={
        "title": "Get Income Statement (vnstock3)",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def vnstock_income_statement(params: FinancialInput) -> str:
    """Fetch income statement data for a Vietnamese listed company.

    Returns revenue, COGS, gross profit, operating income, EBIT, net income,
    EPS and other P&L items. Available in quarterly or annual periods.

    Rate limited: vnstock3 Community tier allows ~60 requests/minute.
    Max 8 periods returned for Community users.

    Returns:
        JSON with income statement data as rows (one per reporting period).
    """
    try:
        await vnstock_limiter.acquire()
        stock = _get_stock(params.symbol)

        # Run synchronous vnstock call in executor to not block event loop
        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(
            None,
            lambda: stock.finance.income_statement(
                period=params.period.value,
            ),
        )

        return _df_to_json(df)

    except Exception as e:
        return _handle_error(e, "vnstock_income_statement")


# ──────────────────────────────────────────────────────────────────────
# Tool 3: Balance Sheet
# ──────────────────────────────────────────────────────────────────────
@mcp.tool(
    name="vnstock_balance_sheet",
    annotations={
        "title": "Get Balance Sheet (vnstock3)",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def vnstock_balance_sheet(params: FinancialInput) -> str:
    """Fetch balance sheet data for a Vietnamese listed company.

    Returns total assets, total liabilities, shareholders' equity,
    current/non-current asset breakdown, and other balance sheet items.

    Rate limited: vnstock3 Community tier allows ~60 requests/minute.

    Returns:
        JSON with balance sheet data as rows (one per reporting period).
    """
    try:
        await vnstock_limiter.acquire()
        stock = _get_stock(params.symbol)

        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(
            None,
            lambda: stock.finance.balance_sheet(
                period=params.period.value,
            ),
        )

        return _df_to_json(df)

    except Exception as e:
        return _handle_error(e, "vnstock_balance_sheet")


# ──────────────────────────────────────────────────────────────────────
# Tool 4: Cash Flow Statement
# ──────────────────────────────────────────────────────────────────────
@mcp.tool(
    name="vnstock_cash_flow",
    annotations={
        "title": "Get Cash Flow Statement (vnstock3)",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def vnstock_cash_flow(params: FinancialInput) -> str:
    """Fetch cash flow statement for a Vietnamese listed company.

    Returns operating cash flow, investing cash flow, financing cash flow,
    free cash flow, and other cash flow items.

    Rate limited: vnstock3 free tier allows ~20 requests/minute.

    Returns:
        JSON with cash flow data as rows (one per reporting period).
    """
    try:
        await vnstock_limiter.acquire()
        stock = _get_stock(params.symbol)

        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(
            None,
            lambda: stock.finance.cash_flow(
                period=params.period.value,
            ),
        )

        return _df_to_json(df)

    except Exception as e:
        return _handle_error(e, "vnstock_cash_flow")


# ──────────────────────────────────────────────────────────────────────
# Tool 5: Financial Ratios
# ──────────────────────────────────────────────────────────────────────
@mcp.tool(
    name="vnstock_financial_ratios",
    annotations={
        "title": "Get Financial Ratios (vnstock3)",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def vnstock_financial_ratios(params: FinancialInput) -> str:
    """Fetch key financial ratios for a Vietnamese listed company.

    Returns P/E, P/B, ROE, ROA, EPS, debt-to-equity, gross margin,
    net margin, current ratio, and other valuation/profitability metrics.

    Rate limited: vnstock3 free tier allows ~20 requests/minute.

    Returns:
        JSON with financial ratio data as rows (one per reporting period).
    """
    try:
        await vnstock_limiter.acquire()
        stock = _get_stock(params.symbol)

        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(
            None,
            lambda: stock.finance.ratio(
                period=params.period.value,
            ),
        )

        return _df_to_json(df)

    except Exception as e:
        return _handle_error(e, "vnstock_financial_ratios")


# ──────────────────────────────────────────────────────────────────────
# Tool 6: Backtest Universe (from CSV)
# ──────────────────────────────────────────────────────────────────────

# Path to backtest results CSV (relative to project root)
_BACKTEST_CSV = None

def _find_backtest_csv() -> Path:
    """Find the backtest_results_combined.csv file."""
    global _BACKTEST_CSV
    if _BACKTEST_CSV and _BACKTEST_CSV.exists():
        return _BACKTEST_CSV

    current = Path(__file__).resolve().parent
    for _ in range(5):
        candidate = current / "results" / "backtest_results_combined.csv"
        if candidate.exists():
            _BACKTEST_CSV = candidate
            return candidate
        current = current.parent

    raise FileNotFoundError(
        "Could not find results/backtest_results_combined.csv in the project tree"
    )


def _load_backtest_universe(
    exchange: Optional[str] = None,
    min_win_rate: Optional[float] = None,
    min_total_return: Optional[float] = None,
    top_n: Optional[int] = None,
) -> list[dict[str, Any]]:
    """Load and optionally filter the backtest universe from CSV."""
    csv_path = _find_backtest_csv()

    rows = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric fields
            for key in row:
                if key not in ("symbol", "exchange"):
                    try:
                        row[key] = float(row[key]) if "." in str(row[key]) else int(row[key])
                    except (ValueError, TypeError):
                        pass
            rows.append(row)

    # Apply filters
    if exchange:
        rows = [r for r in rows if r.get("exchange", "").upper() == exchange.upper()]

    if min_win_rate is not None:
        rows = [r for r in rows if float(r.get("win_rate_pct", 0)) >= min_win_rate]

    if min_total_return is not None:
        rows = [r for r in rows if float(r.get("total_return_pct", 0)) >= min_total_return]

    # Sort by total_return descending
    rows.sort(key=lambda r: float(r.get("total_return_pct", 0)), reverse=True)

    if top_n is not None:
        rows = rows[:top_n]

    return rows


@mcp.tool(
    name="get_backtest_universe",
    annotations={
        "title": "Get Backtest Stock Universe",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
async def get_backtest_universe(params: BacktestUniverseInput) -> str:
    """Get the list of 262 Vietnamese stocks in the backtest universe.

    Returns stocks from backtest_results_combined.csv with their performance
    metrics including: symbol, exchange, total_trades, win_rate_pct,
    total_return_pct, sharpe_ratio, profit_factor, max_drawdown_pct.

    This is a LOCAL file read — no API call needed, no rate limit.

    Filters:
      - exchange: Filter by HSX/HNX/UPCOM
      - min_win_rate: Minimum win rate percentage
      - min_total_return: Minimum total return percentage
      - top_n: Return only top N stocks by total return

    Returns:
        JSON with list of stock records and their backtest performance.
    """
    try:
        rows = _load_backtest_universe(
            exchange=params.exchange,
            min_win_rate=params.min_win_rate,
            min_total_return=params.min_total_return,
            top_n=params.top_n,
        )

        symbols = [r["symbol"] for r in rows]
        result = {
            "count": len(rows),
            "symbols": symbols,
            "data": rows,
        }

        return json.dumps(result, ensure_ascii=False, indent=2)

    except Exception as e:
        return _handle_error(e, "get_backtest_universe")


# ──────────────────────────────────────────────────────────────────────
# Tool 7: Company Overview
# ──────────────────────────────────────────────────────────────────────
@mcp.tool(
    name="vnstock_company_overview",
    annotations={
        "title": "Get Company Overview (vnstock3)",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def vnstock_company_overview(params: CompanyInput) -> str:
    """Fetch company profile and overview for a Vietnamese listed company.

    Returns company name, industry, exchange, market cap, outstanding shares,
    description, and other profile information.

    Rate limited: vnstock3 free tier allows ~20 requests/minute.

    Returns:
        JSON with company overview data.
    """
    try:
        await vnstock_limiter.acquire()
        stock = _get_stock(params.symbol)

        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(
            None,
            lambda: stock.company.overview(),
        )

        return _df_to_json(df)

    except Exception as e:
        return _handle_error(e, "vnstock_company_overview")


# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    mcp.run()
