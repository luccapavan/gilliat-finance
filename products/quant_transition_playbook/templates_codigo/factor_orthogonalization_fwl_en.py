import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
"""
Production Code Engine: Factor Orthogonalization via Frisch-Waugh-Lovell Theorem
Author: Lucca Simeoni Pavan, Ph.D.
"""

import numpy as np
import pandas as pd
from scipy import stats

def fwl_factor_orthogonalization(y_alpha: np.ndarray, X_redundant: np.ndarray) -> dict:
    """
    Applies the Frisch-Waugh-Lovell (FWL) projection theorem:
    M_X = I - X(X'X)^(-1)X'
    y_pure = M_X * y_alpha
    """
    N = len(y_alpha)
    X = np.column_stack([np.ones(N), X_redundant])
    
    # OLS beta projection
    beta = np.linalg.inv(X.T @ X) @ (X.T @ y_alpha)
    y_fitted = X @ beta
    y_orthogonal = y_alpha - y_fitted
    
    # Residual variance and standard error
    k = X.shape[1]
    sigma2 = np.sum(y_orthogonal ** 2) / (N - k)
    alpha_intercept = beta[0]
    var_b = np.diag(sigma2 * np.linalg.inv(X.T @ X))
    se_alpha = np.sqrt(var_b[0])
    t_stat = alpha_intercept / se_alpha if se_alpha > 0 else 0.0
    p_val = 2 * (1 - stats.t.cdf(abs(t_stat), df=N - k))
    
    return {
        "pure_alpha_vector": y_orthogonal,
        "intercept_alpha": alpha_intercept,
        "t_stat": t_stat,
        "p_value": p_val,
        "is_genuine_alpha": abs(t_stat) > 2.5
    }

if __name__ == "__main__":
    np.random.seed(42)
    N = 500
    market_beta = np.random.normal(0, 1, N)
    size_beta = np.random.normal(0, 1, N)
    redundant_matrix = np.column_stack([market_beta, size_beta])
    
    # Alpha candidate with genuine orthogonal edge
    raw_alpha = 0.8 * market_beta + 0.5 * size_beta + 0.05 + np.random.normal(0, 0.3, N)
    res = fwl_factor_orthogonalization(raw_alpha, redundant_matrix)
    
    print("=" * 60)
    print("FWL FACTOR ORTHOGONALIZATION ENGINE - ENGLISH")
    print("=" * 60)
    print(f"Raw Alpha Intercept: {res['intercept_alpha']:.4f}")
    print(f"t-statistic: {res['t_stat']:.2f}")
    print(f"p-value: {res['p_value']:.4e}")
    print(f"Institutional Edge Validated (t > 2.5): {res['is_genuine_alpha']}")
