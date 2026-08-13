---
name: screen-stocks
description: Use when the user wants to find or rank stocks by criteria - screening by fundamentals, spotting top gainers/losers, unusual options activity, volume breakouts, or correlated names. Triggers "screen for", "find stocks that", "top movers today", "unusual options activity", "what's correlated with X".
---

# Screen Stocks

Find and rank tickers across markets, then hand off promising names for deeper analysis.

## Data sources
- **Equibles MCP** `ScreenStocks` - fundamentals-based screening (valuation, growth, ownership).
- **Equibles MCP** `GetCorrelatedStocks(ticker, scope, direction)` - co-movers or hedges.
- **TradingView MCP** `top_gainers` / `top_losers` - session movers by market.
- **TradingView MCP** `stock_options_unusual_activity` - unusual options flow.
- **TradingView MCP** `volume_breakout_scanner` / `smart_volume_scanner` - volume-driven candidates.
- **TradingView MCP** `stock_screener` - multi-market technical screening.

## Steps
1. Clarify the universe (US / EGX / crypto / futures) and the ranking criterion if ambiguous.
2. Run the matching screener tool. Prefer one focused call over many broad ones.
3. Present a ranked table: ticker, key metric(s), and why it surfaced.
4. Offer to hand the top names to the `analyze-option` skill or pull price history for deeper work.

## Always flag
- Screens are point-in-time snapshots; note the session/date the data came from.
- Thin/illiquid names that clear a screen but would be hard to trade.

## Do not
- Do not place trades or give financial advice. This surfaces candidates for the user to research.
