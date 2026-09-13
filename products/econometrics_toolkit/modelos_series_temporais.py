"""
Módulo 1: Séries Temporais Financeiras e Vetor Autorregressivo (VAR)
Applied Financial Econometrics Toolkit — Lucca Simeoni Pavan, Ph.D.
"""

import numpy as np
import pandas as pd

def estimate_var_model(data: pd.DataFrame, lags: int = 2) -> dict:
    """
    Estima um modelo Vetor Autorregressivo (VAR) de ordem p via Mínimos Quadrados Ordinários (MQO).
    
    Equação: Y_t = c + A_1 * Y_{t-1} + ... + A_p * Y_{t-p} + e_t
    
    Retorna:
    - coeficientes (matrizes A_i)
    - matriz de covariância residual (Sigma)
    - critérios de informação AIC e BIC
    """
    T, K = data.shape
    eff_T = T - lags
    
    # Construção da matriz de regressores defasados (X)
    X_list = [np.ones((eff_T, 1))]  # Constante
    for l in range(1, lags + 1):
        X_list.append(data.shift(l).iloc[lags:].values)
    
    X = np.hstack(X_list)
    Y = data.iloc[lags:].values
    
    # Estimação MQO: B = (X'X)^(-1) X'Y
    try:
        B = np.linalg.inv(X.T @ X) @ (X.T @ Y)
    except np.linalg.LinAlgError:
        B = np.linalg.pinv(X.T @ X) @ (X.T @ Y)
        
    residuals = Y - X @ B
    Sigma_u = (residuals.T @ residuals) / eff_T
    
    # Critérios de informação
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
    t = 200
    dates = pd.date_range("2023-01-01", periods=t, freq="B")
    
    # Simulação de duas séries cointegradas / interconectadas (ex: Juros e Câmbio)
    e1 = np.random.normal(0, 1, t)
    e2 = np.random.normal(0, 1, t)
    
    y1 = np.zeros(t)
    y2 = np.zeros(t)
    for i in range(1, t):
        y1[i] = 0.6 * y1[i-1] + 0.2 * y2[i-1] + e1[i]
        y2[i] = 0.1 * y1[i-1] + 0.5 * y2[i-1] + e2[i]
        
    df = pd.DataFrame({"Juros_DI": y1, "Cambio_USD": y2}, index=dates)
    var_results = estimate_var_model(df, lags=1)
    
    print("--- Modelo VAR Estimado com Sucesso ---")
    print(f"Observações: {var_results['n_obs']}")
    print(f"Critério AIC: {var_results['AIC']:.4f}")
    print(f"Critério BIC: {var_results['BIC']:.4f}")
    print("\nMatriz de Coeficientes:")
    print(var_results["coefficients"])
