import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
"""
Production Code Engine: Tail Risk & Performance Metrics Suite
Calculates CVaR 95%, Sortino, Calmar, Sharpe, Max Drawdown
Author: Lucca Simeoni Pavan, Ph.D.
"""

import numpy as np
import pandas as pd
from scipy import stats

def compute_institutional_risk_tear_sheet(returns: pd.Series, rf_annual: float = 0.045) -> dict:
    """Computes investment-committee grade performance and tail risk metrics."""
    s = returns.dropna()
    rf_daily = (1 + rf_annual) ** (1 / 252) - 1
    
    # 1. Annualized Return (CAGR)
    cum_return = (1 + s).cumprod().iloc[-1]
    n_days = len(s)
    cagr = (cum_return ** (252 / n_days)) - 1.0
    
    # 2. Annualized Volatility
    ann_vol = s.std() * np.sqrt(252)
    
    # 3. Sharpe Ratio
    excess_ret = s - rf_daily
    sharpe = (cagr - rf_annual) / ann_vol if ann_vol > 0 else 0.0
    
    # 4. Sortino Ratio (Downside Semi-Variance)
    downside = excess_ret[excess_ret < 0]
    downside_std = downside.std() * np.sqrt(252)
    sortino = (cagr - rf_annual) / downside_std if downside_std > 0 else 0.0
    
    # 5. Maximum Drawdown & Duration
    cum_equity = (1 + s).cumprod()
    peak = cum_equity.cummax()
    drawdown = (cum_equity - peak) / peak
    mdd = drawdown.min()
    
    # 6. Calmar Ratio
    calmar = cagr / abs(mdd) if abs(mdd) > 0 else 0.0
    
    # 7. Value at Risk (VaR 95%)
    var_95_hist = np.percentile(s, 5.0)
    
    # 8. Conditional Value at Risk (CVaR 95% / Expected Shortfall)
    cvar_95 = s[s <= var_95_hist].mean()
    
    return {
        "CAGR": f"{cagr * 100:.2f}%",
        "Annual_Volatility": f"{ann_vol * 100:.2f}%",
        "Sharpe_Ratio": f"{sharpe:.2f}",
        "Sortino_Ratio": f"{sortino:.2f}",
        "Max_Drawdown": f"{mdd * 100:.2f}%",
        "Calmar_Ratio": f"{calmar:.2f}",
        "VaR_95_Daily": f"{var_95_hist * 100:.2f}%",
        "CVaR_95_Daily": f"{cvar_95 * 100:.2f}%"
    }

if __name__ == "__main__":
    np.random.seed(42)
    sample_returns = pd.Series(np.random.normal(0.0006, 0.012, 1000))
    # Inject tail shock
    sample_returns.iloc[200] = -0.065
    sample_returns.iloc[450] = -0.072
    
    report = compute_institutional_risk_tear_sheet(sample_returns)
    print("=" * 60)
    print("INSTITUTIONAL TAIL RISK TEAR SHEET - ENGLISH")
    print("=" * 60)
    for k, v in report.items():
        print(f"{k.ljust(25)}: {v}")
