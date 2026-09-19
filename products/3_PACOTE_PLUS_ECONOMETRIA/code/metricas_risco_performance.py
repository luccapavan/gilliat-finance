"""
Motor de Cálculo de Métricas de Performance e Risco Financeiro
Parte integrante de: The Quant Transition Playbook (por Lucca Simeoni Pavan, Ph.D.)
"""

import numpy as np
import pandas as pd

def calculate_performance_metrics(returns: pd.Series, risk_free_rate: float = 0.10, periods_per_year: int = 252) -> dict:
    """
    Calcula os principais indicadores de risco e retorno utilizados por gestores e comitês de risco.
    
    Parâmetros:
    - returns: Série temporal de retornos diários da estratégia.
    - risk_free_rate: Taxa livre de risco anualizada (ex: CDI / Selic de 10% a.a.).
    - periods_per_year: Dias úteis no ano (padrão Brasil = 252).
    """
    clean_returns = returns.dropna()
    rf_daily = (1 + risk_free_rate) ** (1 / periods_per_year) - 1
    
    # 1. Retorno Anualizado (CAGR)
    cum_return = (1 + clean_returns).prod()
    n_years = len(clean_returns) / periods_per_year
    cagr = cum_return ** (1 / n_years) - 1 if n_years > 0 else 0.0
    
    # 2. Volatilidade Anualizada
    vol_annualized = clean_returns.std() * np.sqrt(periods_per_year)
    
    # 3. Índice de Sharpe Anualizado
    excess_returns = clean_returns - rf_daily
    sharpe_ratio = (excess_returns.mean() / clean_returns.std()) * np.sqrt(periods_per_year) if clean_returns.std() != 0 else np.nan
    
    # 4. Índice de Sortino (penaliza apenas downside volatility)
    downside_returns = clean_returns[clean_returns < 0]
    downside_std = downside_returns.std() * np.sqrt(periods_per_year)
    sortino_ratio = (excess_returns.mean() * periods_per_year) / downside_std if downside_std != 0 else np.nan
    
    # 5. Maximum Drawdown & Drawdown Duration
    cum_series = (1 + clean_returns).cumprod()
    running_max = cum_series.cummax()
    drawdown_series = (cum_series - running_max) / running_max
    max_drawdown = drawdown_series.min()
    
    # 6. Índice de Calmar (CAGR / |Max Drawdown|)
    calmar_ratio = cagr / abs(max_drawdown) if max_drawdown != 0 else np.nan
    
    # 7. Value at Risk (VaR 95% diário - Histórico e Paramétrico)
    var_95_historical = np.percentile(clean_returns, 5)
    var_95_parametric = clean_returns.mean() - 1.645 * clean_returns.std()
    
    # 8. Conditional Value at Risk (CVaR / Expected Shortfall 95%)
    cvar_95 = clean_returns[clean_returns <= var_95_historical].mean()
    
    return {
        "CAGR (Retorno Anualizado)": f"{cagr:.2%}",
        "Volatilidade Anualizada": f"{vol_annualized:.2%}",
        "Sharpe Ratio": f"{sharpe_ratio:.2f}",
        "Sortino Ratio": f"{sortino_ratio:.2f}",
        "Max Drawdown": f"{max_drawdown:.2%}",
        "Calmar Ratio": f"{calmar_ratio:.2f}",
        "VaR 95% Diário (Histórico)": f"{var_95_historical:.2%}",
        "VaR 95% Diário (Paramétrico)": f"{var_95_parametric:.2%}",
        "CVaR 95% Diário (Expected Shortfall)": f"{cvar_95:.2%}"
    }

if __name__ == "__main__":
    np.random.seed(42)
    mock_rets = pd.Series(np.random.normal(0.0006, 0.012, 1000))
    metrics = calculate_performance_metrics(mock_rets)
    print("\n--- Relatório de Risco e Performance ---")
    for k, v in metrics.items():
        print(f"{k}: {v}")
