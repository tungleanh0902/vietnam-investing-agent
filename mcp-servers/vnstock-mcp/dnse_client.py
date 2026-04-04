"""
DNSE LightSpeed API client for historical OHLC data (asynchronous).

Uses public API endpoints from entrade/banggia to fetch data directly
without needing complex authentication headers, preventing 400 Bad Request errors.
"""

import os
import time
from datetime import datetime, timezone
from typing import Any, Optional

import httpx

# Valid resolution values for OHLC endpoint
VALID_RESOLUTIONS = {"1", "3", "5", "15", "30", "1H", "1D", "1W"}

# Valid asset types
VALID_TYPES = {"STOCK", "DERIVATIVE", "INDEX"}

class DNSEAuthError(Exception):
    """Raised when DNSE API authentication fails (kept for compatibility)."""
    pass

class DNSEClient:
    """Async client for DNSE API (Market Data)."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        base_url: str = "https://services.entrade.com.vn/chart-api/v2",
        timeout: float = 30.0,
    ):
        # Stored for backward compatibility with server.py, but not used for auth
        self.api_key = api_key or os.environ.get("DNSE_API_KEY", "")
        self.api_secret = api_secret or os.environ.get("DNSE_API_SECRET", "")
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _build_headers(self) -> dict[str, str]:
        """Build headers required to bypass 401/403 for the public chart API."""
        return {
            "origin": "https://banggia.dnse.com.vn",
            "referer": "https://banggia.dnse.com.vn/",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    async def get_ohlc(
        self,
        symbol: str,
        asset_type: str = "STOCK",
        resolution: str = "1D",
        from_ts: Optional[int] = None,
        to_ts: Optional[int] = None,
    ) -> list[dict[str, Any]]:
        """Fetch historical OHLC data from DNSE.

        Args:
            symbol: Stock ticker (e.g. 'FPT', 'VCB', 'VNINDEX')
            asset_type: One of 'STOCK', 'DERIVATIVE', 'INDEX'
            resolution: Candle timeframe - '1','15','30','1H','1D', etc.
            from_ts: Start timestamp (Unix seconds). Default: 1 year ago
            to_ts: End timestamp (Unix seconds). Default: now

        Returns:
            List of dicts with keys: time, date, open, high, low, close, volume
        """
        resolution_map = {
            "1": "1",
            "3": "3",
            "5": "5",
            "15": "15",
            "30": "30",
            "1h": "1H",
            "1H": "1H",
            "1D": "1D",
            "1d": "1D",
            "1W": "1W",
            "1w": "1W"
        }
        
        res = resolution_map.get(resolution, "1D")

        now = int(time.time())
        if to_ts is None:
            to_ts = now
        if from_ts is None:
            # Default: 1 year of data
            from_ts = to_ts - (365 * 24 * 60 * 60)

        query_param = "stock"
        if asset_type.upper() == "INDEX":
            query_param = "index"

        path = f"/ohlcs/{query_param}"
        params = {
            "symbol": symbol.upper(),
            "resolution": res,
            "from": str(from_ts),
            "to": str(to_ts),
        }

        headers = self._build_headers()

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(
                f"{self.base_url}{path}",
                params=params,
                headers=headers,
            )
            response.raise_for_status()
            data = response.json()

        return self._transform_ohlc(data)

    @staticmethod
    def _transform_ohlc(data: dict[str, Any]) -> list[dict[str, Any]]:
        """Transform TradingView-format arrays into row-based records."""
        timestamps = data.get("t", [])
        opens = data.get("o", [])
        highs = data.get("h", [])
        lows = data.get("l", [])
        closes = data.get("c", [])
        volumes = data.get("v", [])

        if not timestamps:
            return []

        rows = []
        for i in range(len(timestamps)):
            dt = datetime.fromtimestamp(timestamps[i], tz=timezone.utc)
            rows.append({
                "time": timestamps[i],
                "date": dt.strftime("%Y-%m-%d"),
                "open": opens[i] if i < len(opens) else None,
                "high": highs[i] if i < len(highs) else None,
                "low": lows[i] if i < len(lows) else None,
                "close": closes[i] if i < len(closes) else None,
                "volume": volumes[i] if i < len(volumes) else None,
            })

        return rows
