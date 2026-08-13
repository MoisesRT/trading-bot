---
name: analyze-option
description: Use when the user wants to analyze a specific stock option (call or put) - fetch its live price, bid/ask, IV and greeks, compute fair value, P&L versus an entry price, and the underlying price needed to hit a profit multiple. Triggers "analyze this call", "what's my option worth", "price target for 2x", "is this option expensive".
---

# Analyze Option

Analyze a single equity option end to end: live quote, fair value, and profit targets.

## Data sources
- **TradingView MCP** `stock_options_chain(symbol, expiry)` - live bid/ask, last, volume, open interest, IV, in-the-money flag, and the underlying price. This is the primary quote source.
- **Equibles MCP** `GetOptionContract(ticker, contract)` - greeks (delta/gamma/theta/vega) and IV by OCC symbol. Use for delta when TradingView omits greeks.
- **Equibles MCP** `GetLiveQuote(tickers)` - cross-check the underlying's live price.
- Local `options_math.py` - fair value, 2x target, IV scaling, P&L arithmetic.

## Steps
1. Identify the contract: ticker, expiry (YYYY-MM-DD), strike, call/put. If given an OCC symbol like `CSCO270115C00115000`, parse it (ticker / YYMMDD / C or P / strike*1000).
2. Pull the chain with `stock_options_chain` for that expiry. Find the strike. Report **bid, ask, mid, last, volume, OI, IV** and the **underlying price**.
3. If the user gave an entry price, compute P&L with `options_math.pnl`.
4. If the user wants a profit multiple (e.g. 2x), compute the expiration target with `options_math.expiry_target_for_multiple`, and give a rough "sooner" target using delta (need `GetOptionContract` for delta).
5. Cross-check fair value with `options_math.black_scholes_call` using the live IV, and flag if the market price diverges far from model.

## Always flag
- **IV crush around earnings**: if IV is much higher than the stock's typical range, warn that a post-earnings IV drop can lose money even if the stock rises.
- **Stale data**: if the option session timestamp trails the live underlying, say the premium may not reflect the current spot.
- **Liquidity**: wide bid/ask or thin volume/OI means hard fills - say so.

## Do not
- Do not place trades or give financial advice. Present analysis of the data and let the user decide. State that these are estimates, not guarantees.
