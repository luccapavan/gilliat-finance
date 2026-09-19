import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
"""
Module 1: Financial Time Series & Vector Autoregression (VAR)
Applied Financial Econometrics Toolkit — Lucca Simeoni Pavan, Ph.D.
Former Head of Quantitative Strategies & Portfolio Allocation Manager
"""

import numpy as np
import pandas as pd

def estimate_var_model(data: pd.DataFrame, lags: int = 2) -> dict:
    """
    Estimates a Vector Autoregressive model of order p via Ordinary Least Squares.
    
    Model Equation: Y_t = c + A_1 * Y_{t-1} + ... + A_p * Y_{t-p} + e_t
    
    Returns:
    - coefficients (matrix B containing constant and parameter matrices A_i)
    - residual covariance matrix (Sigma_u)
    - information criteria (AIC and BIC)
    """
    T, K = data.shape
    eff_T = T - lags
    
    # Construct lagged regressor design matrix (X)
    X_list = [np.ones((eff_T, 1))]  # Constant intercept
    for l in range(1, lags + 1):
        X_list.append(data.shift(l).iloc[lags:].values)
    
    X = np.hstack(X_list)
    Y = data.iloc[lags:].values
    
    # OLS Solution: B = (X'X)^(-1) X'Y
    try:
        B = np.linalg.inv(X.T @ X) @ (X.T @ Y)
    except np.linalg.LinAlgError:
        B = np.linalg.pinv(X.T @ X) @ (X.T @ Y)
        
    residuals = Y - X @ B
    Sigma_u = (residuals.T @ residuals) / eff_T
    
    # Information criteria
    det_sigma = np.linalg.det(Sigma_u)
    if det_sigma <= 0:
        det_sigma = 1e-10
        
    log_det = np.log(det_sigma)
    total_params = K * (1 + K * lags)
    
    aic = log_det + (2.0 * total_params) / eff_T
    bic = log_det + (total_params * np.log(eff_T)) / eff_T
    
    return {
        "lags": lags,
        "n_obs": eff_T,
        "n_vars": K,
        "coefficients": pd.DataFrame(B, columns=data.columns),
        "cov_residuals": pd.DataFrame(Sigma_u, index=data.columns, columns=data.columns),
        "AIC": aic,
        "BIC": bic
    }

if __name__ == "__main__":
    np.random.seed(42)
    dates = pd.date_range("2023-01-01", periods=250, freq="B")
    
    # Simulating 3 endogenous macroeconomic variables: Rates, Inflation, Equities
    rates = np.random.normal(0, 0.005, 250).cumsum()
    inflation = 0.5 * rates + np.random.normal(0, 0.003, 250).cumsum()
    equities = -0.4 * rates - 0.2 * inflation + np.random.normal(0, 0.01, 250).cumsum()
    
    macro_df = pd.DataFrame({
        "Policy_Rate": rates,
        "Inflation_CPI": inflation,
        "Equity_Index": equities
    }, index=dates)
    
    var_res = estimate_var_model(macro_df, lags=2)
    
    print("=" * 60)
    print("VECTOR AUTOREGRESSION (VAR) ESTIMATION - ENGLISH")
    print("=" * 60)
    print(f"Observations (eff_T): {var_res['n_obs']}")
    print(f"Endogenous Variables (K): {var_res['n_vars']}")
    print(f"Lags: {var_res['lags']}")
    print(f"AIC: {var_res['AIC']:.4f} | BIC: {var_res['BIC']:.4f}")
    print("\nParameter Matrix (B):")
    print(var_res["coefficients"].round(4))
