#!/usr/bin/env python3
"""
Demo script showing how to use real financial data and chart generation.
"""

from newsletter.data import FinancialDataFetcher, format_market_summary, format_economic_indicators
from newsletter.charts import ChartGenerator, embed_chart_in_html


def main():
    print("=" * 60)
    print("Financial Data & Chart Generation Demo")
    print("=" * 60)

    # Initialize data fetcher and chart generator
    fetcher = FinancialDataFetcher()
    chart_gen = ChartGenerator()

    # Example 1: Get market summary
    print("\n1. Fetching market summary...")
    market_summary = fetcher.get_market_summary()
    print(format_market_summary(market_summary))

    # Example 2: Get economic indicators
    print("\n2. Fetching economic indicators...")
    indicators = fetcher.get_economic_indicators()
    print(format_economic_indicators(indicators))

    # Example 3: Get stock data and create chart
    print("\n3. Fetching SPY data and creating chart...")
    spy_data = fetcher.get_stock_data("SPY", period="3mo", interval="1d")
    if spy_data is not None:
        print(f"   Fetched {len(spy_data)} days of SPY data")
        chart_b64 = chart_gen.create_price_chart(spy_data, title="SPY - Last 3 Months")
        if chart_b64:
            print(f"   Created chart (base64 length: {len(chart_b64)})")
            # You can embed this in HTML like:
            # html_img = embed_chart_in_html(chart_b64, "SPY Chart")

    # Example 4: Comparison chart
    print("\n4. Creating comparison chart (SPY vs QQQ)...")
    qqq_data = fetcher.get_stock_data("QQQ", period="3mo", interval="1d")
    if spy_data is not None and qqq_data is not None:
        comparison_chart = chart_gen.create_comparison_chart(
            {"SPY": spy_data, "QQQ": qqq_data},
            title="SPY vs QQQ - Normalized Performance"
        )
        if comparison_chart:
            print(f"   Created comparison chart (base64 length: {len(comparison_chart)})")

    # Example 5: FRED data
    print("\n5. Fetching 10-Year Treasury Yield from FRED...")
    treasury_data = fetcher.get_fred_data("DGS10")
    if treasury_data is not None:
        print(f"   Fetched {len(treasury_data)} days of treasury data")
        latest = treasury_data.iloc[-1].values[0]
        print(f"   Latest 10Y yield: {latest:.2f}%")

    print("\n" + "=" * 60)
    print("Demo complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
