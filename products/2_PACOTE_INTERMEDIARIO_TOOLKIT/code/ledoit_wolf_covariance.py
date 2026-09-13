"""
Template de Código: Encolhimento de Covariância de Ledoit-Wolf vs Markowitz Clássico
Parte integrante de: The Institutional Quant Toolkit & Playbook
Autor: Lucca Simeoni Pavan, Ph.D. | Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação

Objetivo:
Demonstrar a estabilização de carteiras de Média-Variância através do encolhimento
linear (Linear Shrinkage) da matriz de covariância amostral Sigma_LW = delta*F + (1-delta)*S,
eliminando a amplificação de erros de autovalores (Teoria de Matrizes Aleatórias).
"""

import numpy as np
import pandas as pd
from sklearn.covariance import LedoitWolf

def compute_ledoit_wolf_covariance(returns_df: pd.DataFrame) -> dict:
    """
    Calcula e compara a matriz de covariância amostral pura vs a matriz com encolhimento de Ledoit-Wolf.
    
    Parâmetros:
    - returns_df: DataFrame com séries temporais de retornos dos ativos (N ativos nas colunas, T períodos nas linhas).
    
    Retorna:
    - Um dicionário contendo as matrizes, a intensidade de encolhimento (shrinkage intensity)
      e a razão de condicionamento (condição espectral).
    """
    clean_returns = returns_df.dropna()
    t_obs, n_assets = clean_returns.shape
    
    # 1. Matriz Amostral Pura (Sample Covariance)
    sample_cov = clean_returns.cov().values
    
    # 2. Matriz com Encolhimento Ledoit-Wolf
    lw = LedoitWolf()
    lw.fit(clean_returns)
    lw_cov = lw.covariance_
    shrinkage_intensity = lw.shrinkage_
    
    # 3. Análise Espectral (Autovalores)
    sample_eigenvals = np.linalg.eigvalsh(sample_cov)
    lw_eigenvals = np.linalg.eigvalsh(lw_cov)
    
    # Número de Condição: Razão entre maior e menor autovalor (quanto menor, mais estável a inversão)
    cond_sample = sample_eigenvals[-1] / max(sample_eigenvals[0], 1e-12)
    cond_lw = lw_eigenvals[-1] / max(lw_eigenvals[0], 1e-12)
    
    # 4. Cálculo de Carteira de Mínima Variância Global (GMV)
    # w = Sigma^(-1) * 1 / (1' * Sigma^(-1) * 1)
    inv_sample = np.linalg.pinv(sample_cov)
    ones = np.ones(n_assets)
    w_sample = inv_sample.dot(ones) / ones.dot(inv_sample).dot(ones)
    
    inv_lw = np.linalg.pinv(lw_cov)
    w_lw = inv_lw.dot(ones) / ones.dot(inv_lw).dot(ones)
    
    return {
        "n_assets": n_assets,
        "t_observations": t_obs,
        "shrinkage_intensity": shrinkage_intensity,
        "condition_number_sample": cond_sample,
        "condition_number_ledoit_wolf": cond_lw,
        "stability_improvement": f"{(1 - cond_lw / cond_sample):.1%}",
        "sample_weights": pd.Series(w_sample, index=clean_returns.columns, name="Pesos_Amostral"),
        "ledoit_wolf_weights": pd.Series(w_lw, index=clean_returns.columns, name="Pesos_LedoitWolf")
    }

if __name__ == "__main__":
    print("=" * 70)
    print("DEMONSTRAÇÃO INSTITUCIONAL: ENCOLHIMENTO DE COVARIÂNCIA LEDOIT-WOLF")
    print("=" * 70)
    
    # Simulação de carteira com 50 ativos e 252 dias úteis (situação crítica onde N/T é alto)
    np.random.seed(42)
    n_assets = 30
    t_days = 252
    
    asset_names = [f"ATIVO_{i:02d}" for i in range(1, n_assets + 1)]
    # Fator comum de mercado + ruído idiossincrático
    market_factor = np.random.normal(0, 0.015, size=t_days)
    returns = np.array([
        0.8 * market_factor + np.random.normal(0, 0.02, size=t_days)
        for _ in range(n_assets)
    ]).T
    
    df_returns = pd.DataFrame(returns, columns=asset_names)
    
    metrics = compute_ledoit_wolf_covariance(df_returns)
    print(f"\nUniverso: {metrics['n_assets']} ativos | Histórico: {metrics['t_observations']} dias úteis")
    print(f"Intensidade de Encolhimento (Shrinkage Alpha): {metrics['shrinkage_intensity']:.4f}")
    print(f"Número de Condição Amostral (Erro Maximizer): {metrics['condition_number_sample']:.1f}")
    print(f"Número de Condição Ledoit-Wolf (Estabilizado):  {metrics['condition_number_ledoit_wolf']:.1f}")
    print(f"Melhoria na Estabilidade de Inversão:          {metrics['stability_improvement']}")
    
    print("\nComparativo dos 5 Primeiros Pesos na Carteira GMV:")
    comp_df = pd.concat([metrics['sample_weights'], metrics['ledoit_wolf_weights']], axis=1)
    print(comp_df.head(5))
    print("\n" + "=" * 70)
