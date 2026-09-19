import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
"""
Production Code Engine: Multi-Factor Equity Backtester (Value + Momentum)
Part of: The Quant Transition Playbook & Institutional Toolkit
Author: Lucca Simeoni Pavan, Ph.D.
"""

import numpy as np
import pandas as pd

def compute_cross_sectional_z_score(df: pd.DataFrame) -> pd.DataFrame:
    """Standardizes factor scores cross-sectionally across constituents at each timestamp."""
    return df.sub(df.mean(axis=1), axis=0).div(df.std(axis=1), axis=0)

def simulate_multifactor_strategy(
    prices: pd.DataFrame,
    pe_ratios: pd.DataFrame,
    rebalance_freq: str = "M",
    top_n: int = 5,
    transaction_cost: float = 0.0015
) -> pd.DataFrame:
    """
    Executes a fully vectorized multi-factor backtest (Value + Momentum).
    
    Parameters:
    - prices: DataFrame of adjusted daily close prices (assets as columns, dates as index)
    - pe_ratios: DataFrame of Price-to-Earnings ratios (fundamental multiple)
    - rebalance_freq: Frequency of portfolio rebalancing ('M' = monthly)
    - top_n: Number of highest-ranked assets to hold in the top quintile
    - transaction_cost: Cost per one-way turnover (15 bps default)
    """
    returns = prices.pct_change()
    
    # 1. Momentum Factor: 12-month return excluding most recent month (t-12 to t-2)
    momentum_factor = prices.shift(21) / prices.shift(252) - 1
    
    # 2. Value Factor: Earnings Yield (E/P = 1 / (P/E))
    value_factor = 1.0 / pe_ratios.replace(0, np.nan)
    
    # Cross-Sectional Z-Score Standardization
    z_mom = compute_cross_sectional_z_score(momentum_factor)
    z_val = compute_cross_sectional_z_score(value_factor)
    
    # Composite Score: 50% Momentum + 50% Value
    composite_score = 0.5 * z_mom + 0.5 * z_val
    
    # Identify periodic rebalancing dates
    rebalance_dates = prices.resample(rebalance_freq).last().index
    portfolio_weights = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)
    
    for date in rebalance_dates:
        if date in composite_score.index:
            scores = composite_score.loc[date].dropna()
            if len(scores) >= top_n:
                selected_assets = scores.nlargest(top_n).index
                portfolio_weights.loc[date, selected_assets] = 1.0 / top_n
                
    portfolio_weights = portfolio_weights.replace(0.0, np.nan).ffill().fillna(0.0)
    
    # Shift weights by 1 day to prevent lookahead execution leakage
    weights_lagged = portfolio_weights.shift(1).fillna(0.0)
    
    # Gross portfolio return
    gross_returns = (weights_lagged * returns).sum(axis=1)
    
    # Turnover friction
    turnover = weights_lagged.diff().abs().sum(axis=1)
    net_returns = gross_returns - (turnover * transaction_cost)
    
    # Equity curve
    equity_curve = (1 + net_returns).cumprod()
    
    return pd.DataFrame({
        "Gross_Return": gross_returns,
        "Turnover": turnover,
        "Net_Return": net_returns,
        "Equity_Curve": equity_curve
    })

if __name__ == "__main__":
    np.random.seed(42)
    dates = pd.date_range("2021-01-01", "2026-01-01", freq="B")
    assets = [f"STOCK_{i}" for i in range(1, 21)]
    
    sim_returns = pd.DataFrame(np.random.normal(0.0005, 0.015, (len(dates), len(assets))), index=dates, columns=assets)
    sim_prices = (1 + sim_returns).cumprod() * 100.0
    sim_pe = pd.DataFrame(np.random.uniform(5.0, 30.0, (len(dates), len(assets))), index=dates, columns=assets)
    
    res = simulate_multifactor_strategy(sim_prices, sim_pe)
    print("=" * 60)
    print("VECTORIZED MULTI-FACTOR BACKTEST ENGINE - ENGLISH")
    print("=" * 60)
    print(f"Total Periods: {len(res)}")
    print(f"Cumulative Return: {(res['Equity_Curve'].iloc[-1] - 1.0) * 100:.2f}%")
    print(f"Annualized Return: {((res['Equity_Curve'].iloc[-1] ** (252 / len(res))) - 1.0) * 100:.2f}%")
    print(f"Average Daily Turnover: {res['Turnover'].mean() * 100:.3f}%")
