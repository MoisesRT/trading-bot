# trading-bot

Claude-driven options analysis and stock screening. Claude drives two market-data
MCP servers plus local math helpers. It analyzes and screens - it does not place trades.

## Data source routing

**Default to TradingView MCP** for prices and quotes. Reach for Equibles only when
TradingView cannot answer the question.

### Use TradingView MCP first

For anything price- or quote-related:

- Stock prices and quotes: `stock_prices`, `yahoo_price`, `stock_extended_hours`
- Option quotes / chains (live bid/ask): `stock_options_chain`, `stock_options_unusual_activity`
- Movers and scans: `top_gainers`, `top_losers`, `volume_breakout_scanner`,
  `smart_volume_scanner`, `bollinger_scan`, `market_snapshot`, `market_sentiment`
- Technicals and TA analysis: `combined_analysis`, `multi_timeframe_analysis`,
  `multi_agent_analysis`, `financial_news`

### Go to Equibles MCP only for the complicated stuff

When the question needs data TradingView does not provide:

- Fundamentals and financials: statements, KPIs, valuation multiples, revenue breakdown, guidance
- Ownership and flow: institutional 13F, insider transactions, congressional trades, short interest
- Greeks and detailed option contract data: `GetOptionContract`, `GetOptionChain` greeks
- Screening on fundamental criteria: `ScreenStocks`
- Filings, earnings-call transcripts, economic indicators, IPOs, funds

Rule of thumb: if it is a live price, quote, or a quick technical scan, use
TradingView. If it requires fundamentals, ownership, greeks, or deep filings, use Equibles.

## Local math

`options_math.py` - pure-math helpers (fair value, profit targets, IV scaling, P&L).
No network. Use it for the arithmetic; use the MCPs for live data.

## Skills

- `analyze-option` - full analysis of one contract.
- `screen-stocks` - find and rank tickers.

## Disclaimer

For analysis and education only. Not financial advice.
