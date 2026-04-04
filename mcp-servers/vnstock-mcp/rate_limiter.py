"""
Rate limiter for vnstock3 free tier (Guest: 20 requests/min).

Uses a sliding window approach to stay within limits. Each call to `acquire()`
blocks until a request slot is available, ensuring we never exceed the configured
rate even when many MCP tool calls happen concurrently.
"""

import asyncio
import time
from collections import deque
from typing import Optional


class SlidingWindowRateLimiter:
    """Sliding window rate limiter.

    Tracks request timestamps in a deque and blocks new requests
    if the window is full. Thread-safe via asyncio.Lock.
    """

    def __init__(self, max_requests: int = 20, window_seconds: float = 60.0):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._timestamps: deque[float] = deque()
        self._lock = asyncio.Lock()

    def _cleanup(self) -> None:
        """Remove timestamps older than the current window."""
        now = time.monotonic()
        cutoff = now - self.window_seconds
        while self._timestamps and self._timestamps[0] < cutoff:
            self._timestamps.popleft()

    async def acquire(self, timeout: Optional[float] = 120.0) -> None:
        """Wait until a request slot is available.

        Args:
            timeout: Maximum seconds to wait. None means wait forever.

        Raises:
            TimeoutError: If the slot didn't free up within timeout.
        """
        deadline = time.monotonic() + timeout if timeout else None

        while True:
            async with self._lock:
                self._cleanup()

                if len(self._timestamps) < self.max_requests:
                    self._timestamps.append(time.monotonic())
                    return

                # Calculate wait time until the oldest request expires
                wait_time = self._timestamps[0] + self.window_seconds - time.monotonic()

            if deadline and time.monotonic() + wait_time > deadline:
                raise TimeoutError(
                    f"Rate limiter timeout: waited {timeout}s but no slot available. "
                    f"Current window has {len(self._timestamps)} requests."
                )

            # Wait just long enough for the oldest request to expire, plus a small buffer
            await asyncio.sleep(max(wait_time + 0.1, 0.5))

    @property
    def remaining(self) -> int:
        """Number of requests remaining in the current window."""
        self._cleanup()
        return max(0, self.max_requests - len(self._timestamps))

    @property
    def reset_in(self) -> float:
        """Seconds until the next slot frees up."""
        self._cleanup()
        if not self._timestamps or len(self._timestamps) < self.max_requests:
            return 0.0
        return max(0.0, self._timestamps[0] + self.window_seconds - time.monotonic())


# Singleton instance for the entire MCP server
# Community tier: 60 req/min, using 55 as safety margin
vnstock_limiter = SlidingWindowRateLimiter(max_requests=55, window_seconds=60.0)
