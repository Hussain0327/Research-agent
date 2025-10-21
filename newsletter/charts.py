from __future__ import annotations

import base64
import io
import logging
from typing import Optional
import pandas as pd

logger = logging.getLogger(__name__)


class ChartGenerator:
    """Generates embedded charts for HTML newsletters."""

    def __init__(self):
        self._matplotlib_available = False

        try:
            import matplotlib
            matplotlib.use('Agg')  # Non-interactive backend
            import matplotlib.pyplot as plt
            self.plt = plt
            self._matplotlib_available = True
        except ImportError:
            logger.warning("matplotlib not installed - chart generation will be unavailable")

    def create_price_chart(
        self,
        data: pd.DataFrame,
        title: str = "Price Chart",
        figsize: tuple = (10, 6)
    ) -> Optional[str]:
        """
        Create a line chart from price data and return as base64 embedded image.

        Args:
            data: DataFrame with price data (must have 'Close' column)
            title: Chart title
            figsize: Figure size (width, height)

        Returns:
            Base64-encoded PNG image string for HTML embedding, or None if fails
        """
        if not self._matplotlib_available:
            logger.error("matplotlib not available")
            return None

        if data is None or data.empty:
            logger.warning("No data provided for chart")
            return None

        try:
            fig, ax = self.plt.subplots(figsize=figsize)

            # Plot closing price
            ax.plot(data.index, data['Close'], linewidth=2, color='#1f77b4')
            ax.set_title(title, fontsize=14, fontweight='bold')
            ax.set_xlabel('Date', fontsize=11)
            ax.set_ylabel('Price ($)', fontsize=11)
            ax.grid(True, alpha=0.3)

            # Format x-axis dates
            fig.autofmt_xdate()

            # Tight layout
            self.plt.tight_layout()

            # Convert to base64
            img_data = self._fig_to_base64(fig)
            self.plt.close(fig)

            return img_data

        except Exception as e:
            logger.error(f"Failed to create price chart: {e}")
            return None

    def create_comparison_chart(
        self,
        data_dict: dict[str, pd.DataFrame],
        title: str = "Comparison Chart",
        figsize: tuple = (10, 6)
    ) -> Optional[str]:
        """
        Create a multi-line comparison chart.

        Args:
            data_dict: Dict mapping labels to DataFrames (each with 'Close' column)
            title: Chart title
            figsize: Figure size

        Returns:
            Base64-encoded PNG image string or None if fails
        """
        if not self._matplotlib_available:
            logger.error("matplotlib not available")
            return None

        if not data_dict:
            logger.warning("No data provided for comparison chart")
            return None

        try:
            fig, ax = self.plt.subplots(figsize=figsize)

            # Normalize each series to start at 100 for easier comparison
            for label, data in data_dict.items():
                if data is not None and not data.empty:
                    normalized = (data['Close'] / data['Close'].iloc[0]) * 100
                    ax.plot(normalized.index, normalized, linewidth=2, label=label)

            ax.set_title(title, fontsize=14, fontweight='bold')
            ax.set_xlabel('Date', fontsize=11)
            ax.set_ylabel('Normalized Price (Base=100)', fontsize=11)
            ax.legend(loc='best')
            ax.grid(True, alpha=0.3)

            fig.autofmt_xdate()
            self.plt.tight_layout()

            img_data = self._fig_to_base64(fig)
            self.plt.close(fig)

            return img_data

        except Exception as e:
            logger.error(f"Failed to create comparison chart: {e}")
            return None

    def create_returns_chart(
        self,
        data: pd.DataFrame,
        title: str = "Returns Distribution",
        figsize: tuple = (10, 6)
    ) -> Optional[str]:
        """
        Create a histogram of daily returns.

        Args:
            data: DataFrame with price data (must have 'Close' column)
            title: Chart title
            figsize: Figure size

        Returns:
            Base64-encoded PNG image string or None if fails
        """
        if not self._matplotlib_available:
            logger.error("matplotlib not available")
            return None

        if data is None or data.empty:
            logger.warning("No data provided for returns chart")
            return None

        try:
            # Calculate daily returns
            returns = data['Close'].pct_change().dropna()

            fig, ax = self.plt.subplots(figsize=figsize)

            ax.hist(returns, bins=50, alpha=0.7, color='#2ca02c', edgecolor='black')
            ax.set_title(title, fontsize=14, fontweight='bold')
            ax.set_xlabel('Daily Return (%)', fontsize=11)
            ax.set_ylabel('Frequency', fontsize=11)
            ax.axvline(returns.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {returns.mean():.2%}')
            ax.legend()
            ax.grid(True, alpha=0.3)

            self.plt.tight_layout()

            img_data = self._fig_to_base64(fig)
            self.plt.close(fig)

            return img_data

        except Exception as e:
            logger.error(f"Failed to create returns chart: {e}")
            return None

    def _fig_to_base64(self, fig) -> str:
        """Convert matplotlib figure to base64-encoded PNG."""
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()
        return f"data:image/png;base64,{img_base64}"


def embed_chart_in_html(img_data: str, alt_text: str = "Chart") -> str:
    """
    Create HTML img tag for embedded chart.

    Args:
        img_data: Base64-encoded image data URI
        alt_text: Alt text for the image

    Returns:
        HTML img tag string
    """
    if img_data:
        return f'<img src="{img_data}" alt="{alt_text}" style="max-width: 100%; height: auto;">'
    return ""
