import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
"""
Production Code Engine: Ledoit-Wolf Analytical Covariance Shrinkage
Author: Lucca Simeoni Pavan, Ph.D.
"""

import numpy as np
import pandas as pd
from sklearn.covariance import LedoitWolf

def robust_covariance_regularization(returns_df: pd.DataFrame) -> dict:
    """
    Stabilizes noisy sample covariance matrices using Ledoit-Wolf analytical shrinkage.
    Eliminates Markowitz's 'estimation error maximizer' flaw.
    """
    X = returns_df.values
    
    # 1. Noisy sample covariance
    sample_cov = np.cov(X, rowvar=False)
    cond_sample = np.linalg.cond(sample_cov)
    
    # 2. Ledoit-Wolf analytical shrinkage
    lw = LedoitWolf().fit(X)
    shrunk_cov = lw.covariance_
    shrinkage_intensity = lw.shrinkage_
    cond_shrunk = np.linalg.cond(shrunk_cov)
    
    # 3. Global Minimum Variance (GMV) portfolio weights: w = Sigma^(-1) * 1 / (1' Sigma^(-1) 1)
    inv_sample = np.linalg.pinv(sample_cov)
    ones = np.ones(sample_cov.shape[0])
    w_sample = inv_sample @ ones / (ones.T @ inv_sample @ ones)
    
    inv_shrunk = np.linalg.inv(shrunk_cov)
    w_shrunk = inv_shrunk @ ones / (ones.T @ inv_shrunk @ ones)
    
    return {
        "sample_condition_number": cond_sample,
        "shrunk_condition_number": cond_shrunk,
        "optimal_shrinkage_intensity": shrinkage_intensity,
        "weights_sample": pd.Series(w_sample, index=returns_df.columns),
        "weights_stabilized": pd.Series(w_shrunk, index=returns_df.columns)
    }

if __name__ == "__main__":
    np.random.seed(42)
    # Ill-conditioned panel: 30 assets, only 50 observations
    T, N = 50, 20
    assets = [f"EQ_{i}" for i in range(1, N + 1)]
    sim_rets = pd.DataFrame(np.random.normal(0, 0.02, (T, N)), columns=assets)
    
    out = robust_covariance_regularization(sim_rets)
    print("=" * 60)
    print("LEDOIT-WOLF COVARIANCE REGULARIZATION - ENGLISH")
    print("=" * 60)
    print(f"Sample Covariance Condition Number: {out['sample_condition_number']:.2f}")
    print(f"Ledoit-Wolf Stabilized Condition Number: {out['shrunk_condition_number']:.2f}")
    print(f"Optimal Shrinkage Parameter (Delta): {out['optimal_shrinkage_intensity']:.4f}")
    print("\nSample GMV Weights (Min / Max):", f"{out['weights_sample'].min():.2f} / {out['weights_sample'].max():.2f}")
    print("Stabilized GMV Weights (Min / Max):", f"{out['weights_stabilized'].min():.2f} / {out['weights_stabilized'].max():.2f}")
