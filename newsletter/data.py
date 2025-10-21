from __future__ import annotations

import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import pandas as pd

logger = logging.getLogger(__name__)


class FinancialDataFetcher:
    """Fetches real financial data from yfinance, FRED, and other sources."""

    def __init__(self):
        self._yfinance_available = False
        self._fred_available = False

        try:
            import yfinance as yf
            self._yfinance_available = True
            self.yf = yf
        except ImportError:
            logger.warning("yfinance not installed - stock data will be unavailable")

        try:
            import pandas_datareader as pdr
            self._fred_available = True
            self.pdr = pdr
        except ImportError:
            logger.warning("pandas-datareader not installed - FRED data will be unavailable")

    def get_stock_data(
        self,
        ticker: str,
        period: str = "1mo",
        interval: str = "1d"
    ) -> Optional[pd.DataFrame]:
        """
        Fetch stock price data from Yahoo Finance.

        Args:
            ticker: Stock ticker symbol (e.g., "SPY", "AAPL")
            period: Time period (e.g., "1d", "5d", "1mo", "3mo", "1y", "5y")
            interval: Data interval (e.g., "1m", "5m", "1h", "1d", "1wk", "1mo")

        Returns:
            DataFrame with OHLCV data or None if fetch fails
        """
        if not self._yfinance_available:
            logger.error("yfinance not available")
            return None

        try:
            ticker_obj = self.yf.Ticker(ticker)
            data = ticker_obj.history(period=period, interval=interval)
            logger.info(f"Fetched {len(data)} rows for {ticker}")
            return data
        except Exception as e:
            logger.error(f"Failed to fetch stock data for {ticker}: {e}")
            return None

    def get_stock_info(self, ticker: str) -> Optional[Dict[str, Any]]:
        """
        Get stock metadata and key statistics.

        Args:
            ticker: Stock ticker symbol

        Returns:
            Dict with stock info or None if fetch fails
        """
        if not self._yfinance_available:
            logger.error("yfinance not available")
            return None

        try:
            ticker_obj = self.yf.Ticker(ticker)
            info = ticker_obj.info
            logger.info(f"Fetched info for {ticker}")
            return info
        except Exception as e:
            logger.error(f"Failed to fetch stock info for {ticker}: {e}")
            return None

    def get_fred_data(
        self,
        series_id: str,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None
    ) -> Optional[pd.DataFrame]:
        """
        Fetch economic data from FRED (Federal Reserve Economic Data).

        Common series IDs:
        - DGS10: 10-Year Treasury Constant Maturity Rate
        - DFF: Federal Funds Effective Rate
        - UNRATE: Unemployment Rate
        - CPIAUCSL: Consumer Price Index
        - GDP: Gross Domestic Product

        Args:
            series_id: FRED series identifier
            start: Start date (defaults to 1 year ago)
            end: End date (defaults to today)

        Returns:
            DataFrame with time series data or None if fetch fails
        """
        if not self._fred_available:
            logger.error("pandas-datareader not available")
            return None

        if start is None:
            start = datetime.now() - timedelta(days=365)
        if end is None:
            end = datetime.now()

        try:
            data = self.pdr.data.DataReader(series_id, "fred", start, end)
            logger.info(f"Fetched {len(data)} rows for FRED series {series_id}")
            return data
        except Exception as e:
            logger.error(f"Failed to fetch FRED data for {series_id}: {e}")
            return None

    def get_market_summary(self, tickers: List[str] = None) -> Dict[str, Any]:
        """
        Get a summary of key market metrics.

        Args:
            tickers: List of ticker symbols (defaults to major indices)

        Returns:
            Dict with market summary data
        """
        if tickers is None:
            tickers = ["^GSPC", "^DJI", "^IXIC", "^VIX"]  # S&P 500, Dow, Nasdaq, VIX

        summary = {}
        for ticker in tickers:
            data = self.get_stock_data(ticker, period="5d", interval="1d")
            if data is not None and not data.empty:
                latest = data.iloc[-1]
                prev = data.iloc[-2] if len(data) > 1 else latest

                summary[ticker] = {
                    "latest_close": latest["Close"],
                    "prev_close": prev["Close"],
                    "change_pct": ((latest["Close"] - prev["Close"]) / prev["Close"] * 100),
                    "volume": latest["Volume"],
                }

        return summary

    def get_economic_indicators(self) -> Dict[str, Any]:
        """
        Fetch key economic indicators from FRED.

        Returns:
            Dict with latest values of key economic metrics
        """
        indicators = {
            "DGS10": "10Y Treasury Yield",
            "DFF": "Fed Funds Rate",
            "UNRATE": "Unemployment Rate",
            "CPIAUCSL": "CPI",
        }

        results = {}
        for series_id, name in indicators.items():
            data = self.get_fred_data(series_id, start=datetime.now() - timedelta(days=90))
            if data is not None and not data.empty:
                latest = data.iloc[-1].values[0]
                results[name] = {
                    "value": latest,
                    "series_id": series_id,
                    "as_of": data.index[-1].strftime("%Y-%m-%d"),
                }

        return results


def format_market_summary(summary: Dict[str, Any]) -> str:
    """Format market summary data for inclusion in newsletter."""
    lines = ["## Market Snapshot", ""]

    ticker_names = {
        "^GSPC": "S&P 500",
        "^DJI": "Dow Jones",
        "^IXIC": "Nasdaq",
        "^VIX": "VIX",
    }

    for ticker, data in summary.items():
        name = ticker_names.get(ticker, ticker)
        change = data["change_pct"]
        sign = "+" if change >= 0 else ""
        lines.append(
            f"- **{name}**: {data['latest_close']:.2f} ({sign}{change:.2f}%)"
        )

    return "\n".join(lines)


def format_economic_indicators(indicators: Dict[str, Any]) -> str:
    """Format economic indicators for inclusion in newsletter."""
    lines = ["## Economic Indicators", ""]

    for name, data in indicators.items():
        lines.append(f"- **{name}**: {data['value']:.2f} (as of {data['as_of']})")

    return "\n".join(lines)
