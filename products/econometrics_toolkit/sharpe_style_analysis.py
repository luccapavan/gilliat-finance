import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
"""
Module 2: Sharpe Returns-Based Style Analysis (RBSA)
Applied Financial Econometrics Toolkit — Lucca Simeoni Pavan, Ph.D.
Former Head of Quantitative Strategies & Portfolio Allocation Manager
"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize

def sharpe_style_analysis(fund_returns: pd.Series, benchmarks: pd.DataFrame) -> dict:
    """
    Estimates an investment fund's implicit factor exposures and style weights
    using only historical return series (William Sharpe's RBSA algorithm).
    
    Constrained Quadratic Optimization:
    Minimize sum (R_fund - sum w_i * R_bench_i)^2
    Subject to:
      sum(w_i) = 1.0 (full investment budget)
      0.0 <= w_i <= 1.0 (long-only weights, no unconstrained leverage)
    """
    common_idx = fund_returns.dropna().index.intersection(benchmarks.dropna().index)
    y = fund_returns.loc[common_idx].values
    X = benchmarks.loc[common_idx].values
    n_benchmarks = X.shape[1]
    
    # Objective function: Sum of squared residuals
    def loss(weights):
        portfolio_ret = X @ weights
        return np.sum((y - portfolio_ret) ** 2)
    
    # Constraint: sum of weights equals 1
    constraints = {"type": "eq", "fun": lambda w: np.sum(w) - 1.0}
    
    # Bounds: weights between 0 and 1
    bounds = [(0.0, 1.0) for _ in range(n_benchmarks)]
    
    # Initial guess: equal weights
    w0 = np.full(n_benchmarks, 1.0 / n_benchmarks)
    
    res = minimize(loss, w0, method="SLSQP", bounds=bounds, constraints=constraints)
    
    if not res.success:
        raise ValueError(f"Optimization failed: {res.message}")
        
    optimal_weights = res.x
    fitted_returns = X @ optimal_weights
    residuals = y - fitted_returns
    
    # Style R-squared (goodness of style fit)
    total_var = np.sum((y - np.mean(y)) ** 2)
    unexplained_var = np.sum(residuals ** 2)
    style_r2 = 1.0 - (unexplained_var / total_var) if total_var > 0 else 0.0
    
    weights_series = pd.Series(optimal_weights, index=benchmarks.columns, name="Style_Weights")
    
    return {
        "weights": weights_series.round(4),
        "style_r2": f"{style_r2:.2%}",
        "annual_tracking_error": f"{np.std(residuals) * np.sqrt(252):.2%}"
    }

if __name__ == "__main__":
    np.random.seed(42)
    dates = pd.date_range("2023-01-01", periods=252, freq="B")
    
    # Simulated Benchmark Returns
    equities = np.random.normal(0.0005, 0.015, len(dates))
    fixed_income = np.random.normal(0.0003, 0.004, len(dates))
    foreign_fx = np.random.normal(0.0002, 0.010, len(dates))
    
    benchmarks_df = pd.DataFrame({
        "Equities_Index": equities,
        "Fixed_Income_Index": fixed_income,
        "FX_Currency_Index": foreign_fx
    }, index=dates)
    
    # Simulated True Fund: 50% Equities, 35% Fixed Income, 15% FX + noise
    true_fund = (
        0.50 * equities + 
        0.35 * fixed_income + 
        0.15 * foreign_fx + 
        np.random.normal(0, 0.002, len(dates))
    )
    fund_series = pd.Series(true_fund, index=dates, name="Fund_NAV")
    
    result = sharpe_style_analysis(fund_series, benchmarks_df)
    
    print("=" * 60)
    print("SHARPE RETURNS-BASED STYLE ANALYSIS (RBSA) - ENGLISH")
    print("=" * 60)
    print("\nEstimated Factor Weights:")
    print(result["weights"])
    print(f"\nStyle R-Squared: {result['style_r2']}")
    print(f"Annualized Tracking Error: {result['annual_tracking_error']}")
