# AI Research Agent (Quant Edition) with Market Data and Charts

A quant newsletter generator that uses LLMs, live market data (Yahoo Finance and FRED), and inline charts. Configured through `.env`. Built for researchers, traders, and founders who care more about data than hype.

## What is inside

* **Quant-focused search**: Uses Tavily with filters for finance and quant sources like arXiv, SSRN, Bloomberg, FT, WSJ, Reuters, and similar sites.
* **Live market data**: Snapshots for SPY, Dow, Nasdaq, VIX, plus macro data like Fed Funds, CPI, and the 10Y yield.
* **Inline charts**: Price charts, comparisons, and return histograms as base64 PNGs, so they embed directly in HTML.
* **Basic production hygiene**: Error handling, logging, configurable temperature, tests, and a simple pipeline that is easy to run again.

---

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
````

Generate a newsletter:

```bash
python -m newsletter \
  --topic "AI and Machine Learning in Trading" \
  --tone "Professional" \
  --audience "Quantitative Researchers"
```

View the output:

```bash
python -m http.server --directory output 8000
# Then open http://localhost:8000/newsletter.html
```

---

## Configuration (.env)

```env
# LLM behavior
LLM_TEMPERATURE=0.7  # e.g., 0.5 for more deterministic output

# Market data feature flags
ENABLE_MARKET_DATA=true    # turn market data and charts on or off
MARKET_DATA_POSITION=0     # 0 = first section, -1 = last
```

---

## Key features

* **Quant-specific search** (Tavily advanced mode): trims long queries and prefers finance and quant domains:

  * Academic: `arxiv.org`, `ssrn.com`, `quantpedia.com`
  * News: `bloomberg.com`, `ft.com`, `wsj.com`, `reuters.com`, `marketwatch.com`, `seekingalpha.com`

* **LLM calls with error handling**: Wrapped in try and except with clear logs so a single failure does not kill the whole run.

* **Charts**: VIX chart, asset comparisons (for example SPY vs QQQ), and return histograms.

* **Topic-based tickers**:

  * Mentions *crypto/bitcoin* → `BTC-USD`, `ETH-USD`
  * Mentions *tech/AI* → `QQQ`, Nasdaq
  * Mentions *bonds/treasury* → `TLT`, `IEF`
  * Default → `SPY` (plus `^VIX` by default)

---

## How it works (modules)

* `newsletter/search.py`
  Quant-aware search using Tavily, domain filters, and safe truncation for long prompts.

* `newsletter/llm.py`
  OpenAI or Anthropic calls with error handling, simple logging, and configurable temperature.

* `newsletter/data.py`
  Data helpers:

  * `get_stock_data()` (Yahoo Finance)
  * `get_fred_data()` (FRED)
  * `get_market_summary()` (SPX, Dow, Nasdaq, VIX)
  * `get_economic_indicators()` (rates, CPI, unemployment)

* `newsletter/charts.py`
  `matplotlib` charts:

  * `create_price_chart()`
  * `create_comparison_chart()`
  * `create_returns_chart()`
    Each returns a base64 PNG string that can be embedded directly in HTML.

* `newsletter/pipeline.py`
  Orchestrates the flow: topic → search results → LLM writing → market data section and charts.

* `newsletter/templates/newsletter.html.j2`
  HTML layout with:

  * `.market-data-section` for the market snapshot
  * `.chart-container` for responsive charts
  * `.chart-caption` for short descriptions

Example demo:

```bash
python examples/data_and_charts_demo.py
```

---

## Example output (tested)

* VIX chart embedded (around 65 KB PNG)
* Market snapshot: SPY daily percent change, VIX, Dow, Nasdaq
* Economic indicators: 10Y Treasury, Fed Funds, CPI, unemployment
* Six LLM written sections tailored to the topic and audience

---

## File tree (condensed)

```text
├── README.md
├── examples/
│   └── data_and_charts_demo.py
├── newsletter/
│   ├── __init__.py
│   ├── __main__.py
│   ├── charts.py
│   ├── config.py
│   ├── data.py
│   ├── emailer.py
│   ├── llm.py
│   ├── models.py
│   ├── pipeline.py
│   ├── search.py
│   └── templates/
│       └── newsletter.html.j2
├── output/
│   ├── index.html
│   ├── newsletter.html
│   └── subject.txt
└── requirements.txt
```

---

## Roadmap: StatArb factor backtester integration

**Goal:** Add a research pipeline that computes factor signals (for example momentum, value, quality) and embeds performance snapshots into each newsletter.

*Planned module*: `newsletter/factors/`

* `load_universe()` for a liquid equity universe
* `compute_factors()` for the selected factor set
* `backtest_walkforward()` with proper splits, transaction costs, and turnover limits

*Planned outputs in the newsletter*:

* **Performance table**: Sharpe, max drawdown, hit rate
* **Charts**: equity curve, factor contribution, turnover
* **Checks**: look ahead and survivorship checks, plus cost sensitivity

*Planned controls*:

* `.env`: `ENABLE_FACTOR_SECTION=true`
* `.env`: `FACTOR_LOOKBACK_DAYS=252`
* `.env`: `TRANSACTION_COST_BPS=5`

This would make each issue include current factor context and charts that are reproducible from code.

---

## Troubleshooting

* **No charts**
  Check the `.env` flags and confirm `matplotlib` is installed from `requirements.txt`.

* **Data fetch failed**
  You still get a newsletter. The logs show which call failed.

* **LLM timeouts**
  Lower `LLM_TEMPERATURE` or run again. Errors are logged with context.

---

## License

MIT. Use and modify freely.

---

# Complete summary of changes

**What changed and why**

1. **Search for quant sources**
   Switched Tavily to advanced mode, trimmed long prompts, and restricted results to finance and quant sites. This reduces generic blog spam and surfaces more useful sources.

2. **LLM reliability**
   Wrapped all provider calls in try and except blocks with clear error messages. If one call fails, the rest of the pipeline can still finish.

3. **Style control**
   Added `LLM_TEMPERATURE` in `.env` so you can adjust how focused or creative the writing should be for a given issue.

4. **Market data and charts**
   Added a data layer (Yahoo Finance and FRED) and a chart layer (matplotlib). The pipeline chooses tickers based on the topic and always includes VIX. Charts are embedded as base64 strings, so the HTML file is self contained.

5. **Pipeline integration**
   Wired the market section so it can appear at the start or end of the newsletter, controlled through `.env`. If data calls fail, the rest of the content still renders.

6. **Docs and examples**
   Updated `README.md`, added a demo script, expanded `.env.example`, and updated `requirements.txt`.

**Files created**:
`newsletter/data.py`, `newsletter/charts.py`, `examples/data_and_charts_demo.py`, `CHANGES.md`

**Files modified**:
`newsletter/search.py`, `newsletter/llm.py`, `newsletter/config.py`, `newsletter/pipeline.py`, `newsletter/templates/newsletter.html.j2`, `requirements.txt`, `README.md`, `.env.example`

**How to run**:

```bash
python -m newsletter --topic "Quantitative Trading" --tone "Professional" --audience "Traders"
```
