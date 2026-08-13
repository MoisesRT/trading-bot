# trading-bot

Claude-driven options analysis and stock screening. The "bot" is Claude Code
operating inside this repo, using two MCP servers for live market data plus
local math helpers. It analyzes options and screens stocks - it does **not**
place trades.

## How it works

- **Equibles MCP** (hosted, HTTP) - option chains, live quotes, greeks, fundamentals, screeners.
- **TradingView MCP** (local, via `uvx`) - live option bid/ask, top movers, unusual activity, volume scanners.
- **`options_math.py`** - pure-math helpers (fair value, profit targets, IV scaling, P&L). No network.
- **`.claude/skills/`** - skills that tell Claude how to drive the MCPs:
  - `analyze-option` - full analysis of one contract.
  - `screen-stocks` - find and rank tickers.

MCPs are called by Claude, not by a standalone script. To use this repo, open
it in Claude Code and ask (e.g. "analyze the CSCO Jan 2027 115 call, I paid 10.60").

## Prerequisites

- **[Claude Code](https://claude.com/claude-code)** - the agent that runs the analysis.
- **Python 3.10-3.13** - for `options_math.py`.
- **[uv](https://docs.astral.sh/uv/)** - runs the TradingView MCP server:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

## Setup

1. Clone and open in Claude Code:
   ```bash
   git clone https://github.com/MoisesRT/trading-bot.git
   cd trading-bot
   ```
2. The `.mcp.json` in this repo registers both MCP servers automatically. Claude
   Code will prompt to approve them on first launch (project-scoped MCPs require
   approval). Approve `equibles` and `tradingview`.
3. (Optional) For news/sentiment tools, copy `.env.example` to `.env` and add a
   free [Marketaux](https://www.marketaux.com/) token. Everything else works without it.
4. Verify the servers connected:
   ```bash
   claude mcp list
   ```
   Both should show `Connected`.

## Usage examples

- "Analyze the CSCO 2027-01-15 $115 call, I paid $10.60 - what's it worth and what's my 2x target?"
- "Screen for large-cap tech with low P/E."
- "Show today's top gainers and any unusual options activity."

## Testing the math helpers

```bash
python3 -c "import options_math as m; print(m.expiry_target_for_multiple(10.60, 115, 2))"
# -> 136.2
```

## Disclaimer

For analysis and education only. Not financial advice. Verify live bid/ask in
your broker before trading; market data here may be delayed.
