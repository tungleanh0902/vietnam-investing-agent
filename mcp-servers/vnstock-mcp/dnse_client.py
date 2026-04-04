"""
DNSE LightSpeed API client for historical OHLC data.

Authentication uses HMAC-SHA256 signatures with API Key + Secret.
Base URL: https://openapi.dnse.com.vn

Required environment variables:
  - DNSE_API_KEY: Your API key from DNSE LightSpeed registration
  - DNSE_API_SECRET: Your API secret (shown once during registration)
"""

import hashlib
import hmac
import os
import time
from datetime import datetime, timezone
from typing import Any, Optional
from email.utils import formatdate

import httpx


DNSE_BASE_URL = "https://openapi.dnse.com.vn"

# Valid resolution values for OHLC endpoint
VALID_RESOLUTIONS = {"1", "3", "5", "15", "30", "1h", "1D", "1W"}

# Valid asset types
VALID_TYPES = {"STOCK", "DERIVATIVE", "INDEX"}


class DNSEAuthError(Exception):
    """Raised when DNSE API authentication fails."""
    pass


class DNSEClient:
    """Async client for DNSE LightSpeed API (Market Data)."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        base_url: str = DNSE_BASE_URL,
        timeout: float = 30.0,
    ):
        self.api_key = api_key or os.environ.get("DNSE_API_KEY", "")
        self.api_secret = api_secret or os.environ.get("DNSE_API_SECRET", "")
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        if not self.api_key or not self.api_secret:
            raise DNSEAuthError(
                "DNSE API credentials not found. Set DNSE_API_KEY and DNSE_API_SECRET "
                "environment variables, or pass them to the DNSEClient constructor. "
                "Register at: https://entradex.dnse.com.vn/thong-tin-ca-nhan/light-speed"
            )

    def _generate_signature(
        self, method: str, path: str, timestamp: str, query_string: str = ""
    ) -> str:
        """Generate HMAC-SHA256 signature for request authentication.

        The signature is computed over: METHOD + PATH + TIMESTAMP + QUERY_STRING
        using the API Secret as the HMAC key.
        """
        # Build the canonical string to sign
        # Format: METHOD\nPATH\nTIMESTAMP\nQUERY_PARAMS
        message_parts = [method.upper(), path, timestamp]
        if query_string:
            message_parts.append(query_string)

        message = "\n".join(message_parts)

        signature = hmac.new(
            self.api_secret.encode("utf-8"),
            message.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()

        return signature

    def _build_headers(self, method: str, path: str, query_string: str = "") -> dict[str, str]:
        """Build authentication headers for a DNSE API request."""
        # RFC 2822 formatted date
        timestamp = formatdate(timeval=None, localtime=False, usegmt=True)

        signature = self._generate_signature(method, path, timestamp, query_string)

        return {
            "X-API-Key": self.api_key,
            "X-Aux-Date": timestamp,
            "X-Signature": signature,
            "Accept": "application/json",
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
            resolution: Candle timeframe - '1','3','5','15','30','1h','1D','1W'
            from_ts: Start timestamp (Unix seconds). Default: 1 year ago
            to_ts: End timestamp (Unix seconds). Default: now

        Returns:
            List of dicts with keys: time, open, high, low, close, volume
        """
        if resolution not in VALID_RESOLUTIONS:
            raise ValueError(
                f"Invalid resolution '{resolution}'. Must be one of: {VALID_RESOLUTIONS}"
            )

        if asset_type.upper() not in VALID_TYPES:
            raise ValueError(
                f"Invalid type '{asset_type}'. Must be one of: {VALID_TYPES}"
            )

        # Default time range: 1 year of data
        now = int(time.time())
        if to_ts is None:
            to_ts = now
        if from_ts is None:
            from_ts = to_ts - (365 * 24 * 60 * 60)

        path = "/price/ohlc"
        params = {
            "symbol": symbol.upper(),
            "type": asset_type.upper(),
            "resolution": resolution,
            "from": str(from_ts),
            "to": str(to_ts),
        }

        # Build sorted query string for signature
        query_string = "&".join(f"{k}={v}" for k, v in sorted(params.items()))

        headers = self._build_headers("GET", path, query_string)

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(
                f"{self.base_url}{path}",
                params=params,
                headers=headers,
            )
            response.raise_for_status()
            data = response.json()

        # Transform TradingView array format to row-based format
        # DNSE returns: {t: [...], o: [...], h: [...], l: [...], c: [...], v: [...]}
        return self._transform_ohlc(data)

    @staticmethod
    def _transform_ohlc(data: dict[str, Any]) -> list[dict[str, Any]]:
        """Transform TradingView-format arrays into row-based records.

        Input:  {"t": [ts1, ts2], "o": [o1, o2], ...}
        Output: [{"time": ts1, "open": o1, ...}, {"time": ts2, "open": o2, ...}]
        """
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
