"""
Módulo 2: Análise de Estilo de Sharpe (Returns-Based Style Analysis - RBSA)
Applied Financial Econometrics Toolkit — Lucca Simeoni Pavan, Ph.D.
"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize

def sharpe_style_analysis(fund_returns: pd.Series, benchmarks: pd.DataFrame) -> dict:
    """
    Estima os pesos implícitos de um fundo em diferentes classes de ativos ou fatores de estilo.
    
    Problema de Otimização Quadrática:
    Minimizar sum (R_fund - sum w_i * R_bench_i)^2
    Sujeito a:
      sum(w_i) = 1 (investimento total)
      0 <= w_i <= 1 (sem alavancagem / restrição de posições vendidas)
    """
    common_idx = fund_returns.dropna().index.intersection(benchmarks.dropna().index)
    y = fund_returns.loc[common_idx].values
    X = benchmarks.loc[common_idx].values
    n_benchmarks = X.shape[1]
    
    # Função objetivo: Soma dos erros quadráticos
    def loss(weights):
        portfolio_ret = X @ weights
        return np.sum((y - portfolio_ret) ** 2)
    
    # Restrição: Soma dos pesos = 1
    constraints = {"type": "eq", "fun": lambda w: np.sum(w) - 1.0}
    
    # Limites: pesos entre 0 e 1
    bounds = [(0.0, 1.0) for _ in range(n_benchmarks)]
    
    # Chute inicial: pesos iguais
    w0 = np.full(n_benchmarks, 1.0 / n_benchmarks)
    
    res = minimize(loss, w0, method="SLSQP", bounds=bounds, constraints=constraints)
    
    if not res.success:
        raise ValueError(f"Otimização falhou: {res.message}")
        
    optimal_weights = res.x
    fitted_returns = X @ optimal_weights
    residuals = y - fitted_returns
    
    # R² de estilo (Qualidade do ajuste de estilo)
    total_var = np.sum((y - np.mean(y)) ** 2)
    unexplained_var = np.sum(residuals ** 2)
    style_r2 = 1.0 - (unexplained_var / total_var) if total_var > 0 else 0.0
    
    weights_series = pd.Series(optimal_weights, index=benchmarks.columns, name="Pesos_Estilo")
    
    return {
        "pesos": weights_series.round(4),
        "style_r2": f"{style_r2:.2%}",
        "tracking_error_anual": f"{np.std(residuals) * np.sqrt(252):.2%}"
    }

if __name__ == "__main__":
    np.random.seed(42)
    t = 252
    dates = pd.date_range("2023-01-01", periods=t, freq="B")
    
    # Benchmarks: Ações Brasil (IBOV), Renda Fixa (CDI), Dólar (USD), Small Caps (SMLL)
    benchmarks_df = pd.DataFrame({
        "IBOV": np.random.normal(0.0005, 0.015, t),
        "CDI": np.full(t, 0.0004),
        "DOLAR": np.random.normal(0.0001, 0.010, t),
        "SMALL_CAPS": np.random.normal(0.0006, 0.020, t)
    }, index=dates)
    
    # Fundo sintético composto por: 40% IBOV + 40% CDI + 20% SMALL_CAPS + ruído idiossincrático
    true_weights = np.array([0.40, 0.40, 0.00, 0.20])
    fund_ret = pd.Series(benchmarks_df.values @ true_weights + np.random.normal(0, 0.002, t), index=dates)
    
    style_result = sharpe_style_analysis(fund_ret, benchmarks_df)
    
    print("\n--- Resultados da Análise de Estilo de Sharpe (RBSA) ---")
    print(f"R² de Estilo (Consistência): {style_result['style_r2']}")
    print(f"Tracking Error Anualizado: {style_result['tracking_error_anual']}")
    print("\nExposição Estimada às Classes:")
    for bench, w in style_result["pesos"].items():
        print(f"  - {bench}: {w:.1%}")
