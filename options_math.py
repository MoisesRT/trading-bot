"""Pure-math helpers for option analysis. No network, no dependencies beyond stdlib.

Data (prices, IV, greeks) comes from the Equibles / TradingView MCP servers,
called by Claude. These functions just do the arithmetic on those numbers.
"""

from __future__ import annotations

import math


def _norm_cdf(x: float) -> float:
    """Standard normal CDF via the error function."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def black_scholes_call(spot: float, strike: float, t_years: float,
                       iv: float, rate: float = 0.04) -> float:
    """Black-Scholes fair value of a European call.

    iv is a decimal (0.37 for 37%), t_years is time to expiry in years.
    Dividends are ignored.
    """
    if t_years <= 0:
        return max(0.0, spot - strike)
    d1 = (math.log(spot / strike) + (rate + 0.5 * iv * iv) * t_years) / (iv * math.sqrt(t_years))
    d2 = d1 - iv * math.sqrt(t_years)
    return spot * _norm_cdf(d1) - strike * math.exp(-rate * t_years) * _norm_cdf(d2)


def expiry_target_for_multiple(entry_price: float, strike: float,
                               multiple: float) -> float:
    """Underlying price needed at expiration to hit `multiple`x the entry premium.

    At expiry a call is worth only intrinsic value, so target = strike + multiple*entry.
    """
    return strike + multiple * entry_price


def scale_iv_to_horizon(annual_iv: float, days: float) -> float:
    """Expected move (as a fraction of spot) over `days`, from annualized IV.

    Uses the sqrt-of-time rule with 365 calendar days.
    """
    return annual_iv * math.sqrt(days / 365.0)


def pnl(entry_price: float, current_price: float, contracts: int = 1) -> dict:
    """P&L on a long option position. One contract = 100 shares."""
    per_contract = (current_price - entry_price) * 100
    return {
        "per_contract": round(per_contract, 2),
        "total": round(per_contract * contracts, 2),
        "return_pct": round((current_price / entry_price - 1) * 100, 2),
    }
