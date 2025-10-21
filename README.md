# AI research agent (Quant Edition) — with Market Data & Charts

A fast, reliable **quant newsletter generator** that blends curated sources, LLM writing, **live market data (Yahoo Finance + FRED)**, and **embedded charts**—all configurable via `.env`. Built for researchers, traders, and founders who want signal over fluff.

## What’s inside

* **Topic-aware research**: Higher-quality search tuned to quant/finance domains (arXiv, SSRN, Bloomberg, FT, WSJ, Reuters, etc.).
* **Live market data**: Snapshots for SPY/Dow/Nasdaq/VIX + key macro (Fed Funds, CPI, 10Y yield).
* **Embedded charts**: Price, comparison, and returns histograms as base64 PNGs—no external hosting.
* **Production hygiene**: Error handling, logging, deterministic temperature controls, tests, and a clean pipeline.

---

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  
```

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
ENABLE_MARKET_DATA=true    # turn market data & charts on/off
MARKET_DATA_POSITION=0     # 0 = first section, -1 = last
```

---

## Key Features

* **Quant-specific search** (Tavily advanced mode): trims long queries, filters to credible domains:

  * Academic: `arxiv.org`, `ssrn.com`, `quantpedia.com`
  * News: `bloomberg.com`, `ft.com`, `wsj.com`, `reuters.com`, `marketwatch.com`, `seekingalpha.com`
* **Robust LLM calls**: Graceful failure with clear logs; no hard crashes.
* **Charts everywhere**: VIX 3-month chart, asset comparisons (e.g., SPY vs. QQQ), returns histograms.
* **Topic-aware tickers**:

  * Mentions *crypto/bitcoin* → `BTC-USD`, `ETH-USD`
  * Mentions *tech/AI* → `QQQ`, Nasdaq
  * Mentions *bonds/treasury* → `TLT`, `IEF`
  * Default → `SPY` (+ always `^VIX`)

---

## How it works (modules)

* `newsletter/search.py` — smarter search for quant content (advanced depth, domain filters, safe truncation).
* `newsletter/llm.py` — OpenAI/Anthropic calls with try/except, contextual logging, configurable temperature.
* `newsletter/data.py` — data fetchers:

  * `get_stock_data()` (Yahoo Finance)
  * `get_fred_data()` (FRED)
  * `get_market_summary()` (SPX/Dow/Nasdaq/VIX)
  * `get_economic_indicators()` (rates, CPI, unemployment)
* `newsletter/charts.py` — `matplotlib` chart makers:

  * `create_price_chart()`, `create_comparison_chart()`, `create_returns_chart()`
  * Returns base64 PNGs for direct HTML embedding.
* `newsletter/pipeline.py` — orchestrates topic → sources → writing → market section + charts.
* `newsletter/templates/newsletter.html.j2` — polished layout with:

  * `.market-data-section` (styled box)
  * `.chart-container` (responsive)
  * `.chart-caption` (concise context)

Example demo:

```bash
python examples/data_and_charts_demo.py
```

---

## Example Output (tested)

* VIX chart embedded (≈65KB PNG)
* Market snapshot: SPY daily % change, VIX, Dow, Nasdaq
* Economic indicators: 10Y Treasury, Fed Funds, CPI, unemployment
* 6 AI-written sections tailored to topic and audience

---

## File Tree (condensed)

```
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

## Roadmap — Project Three: **StatArb Factor Backtester** (integration)

**Goal:** Add a lean research pipeline that computes factor signals (e.g., momentum, value, quality) and **auto-embeds** performance snapshots into each newsletter.

* **Module**: `newsletter/factors/` (planned)

  * `load_universe()` (liquid equities)
  * `compute_factors()` (your chosen set)
  * `backtest_walkforward()` (proper splits, costs, turnover caps)
* **Outputs in newsletter**:

  * **Performance table**: Sharpe, max drawdown, hit rate
  * **Charts**: equity curve, factor contribution, turnover
  * **Sanity checks**: look-ahead and survivorship defenses, cost sensitivity
* **Controls**:

  * `.env`: `ENABLE_FACTOR_SECTION=true`, `FACTOR_LOOKBACK_DAYS=252`, `TRANSACTION_COST_BPS=5`

*This keeps the newsletter actionable: every issue ships with fresh factor context and reproducible charts.*

---

## Troubleshooting

* **No charts?** Check `.env` flags and confirm `matplotlib` installed from `requirements.txt`.
* **Data fetch failed?** You’ll still get a newsletter; logs will show which data call failed.
* **LLM timeouts?** Lower `LLM_TEMPERATURE` or retry; errors are logged with context.

---

## License

MIT — use freely, ship confidently.

---

# Complete Summary of Changes (human write-up)

**What I changed and why**

1. **Search quality (quant domains)**
   Switched Tavily to advanced mode, trimmed long prompts, and whitelisted credible finance/quant sites. You’ll get fewer generic blog posts and more first-rate sources.

2. **LLM reliability**
   Wrapped provider calls in try/except with explicit error messages. Failures degrade gracefully instead of killing the run.

3. **Controlled style**
   Added `LLM_TEMPERATURE` so you can tighten or loosen writing tone per issue.

4. **Live market data + charts**
   Built a small data layer (Yahoo + FRED) and a chart layer (matplotlib). The pipeline auto-chooses tickers from the topic and always includes a VIX snapshot. Charts are embedded as base64, so the newsletter is portable.

5. **Pipeline integration**
   Wired market data as a first/last section (configurable). If data calls hiccup, the rest of the newsletter still renders.

6. **Docs & examples**
   Updated `README.md`, added a demo script, expanded `.env.example`, and bumped `requirements.txt`.

**Files created**: `newsletter/data.py`, `newsletter/charts.py`, `examples/data_and_charts_demo.py`, `CHANGES.md`
**Files modified**: `newsletter/search.py`, `newsletter/llm.py`, `newsletter/config.py`, `newsletter/pipeline.py`, `newsletter/templates/newsletter.html.j2`, `requirements.txt`, `README.md`, `.env.example`

**How to run** (one-liner):

```bash
python -m newsletter --topic "Quantitative Trading" --tone "Professional" --audience "Traders"
```

