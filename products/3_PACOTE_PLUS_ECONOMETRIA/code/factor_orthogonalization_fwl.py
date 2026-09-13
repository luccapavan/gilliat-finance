"""
Template de Código: Ortogonalização de Fatores via Teorema Frisch-Waugh-Lovell (FWL)
Parte integrante de: The Institutional Quant Toolkit & Playbook
Autor: Lucca Simeoni Pavan, Ph.D. | Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação

Objetivo:
Isolar o alfa estatisticamente puro de um novo sinal candidato através da matriz
aniquiladora residual M_X = I - X(X'X)^(-1)X', eliminando a colinearidade com
fatores estabelecidos de mercado (Mercado, Tamanho, Valor, Momentum).
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm

def fwl_orthogonalize(candidate_factor: pd.Series, benchmark_factors: pd.DataFrame) -> dict:
    """
    Aplica o Teorema de Frisch-Waugh-Lovell (FWL) para ortogonalizar um fator candidato
    em relação a uma matriz de fatores benchmark conhecidos.
    
    Parâmetros:
    - candidate_factor: Série temporal do novo sinal que se deseja testar.
    - benchmark_factors: DataFrame contendo as séries dos fatores já estabelecidos (ex: Mkt, SMB, HML, MOM).
    
    Retorna:
    - Um dicionário com os resíduos ortogonalizados, métricas de regressão e diagnóstico de alfa.
    """
    # Alinhamento temporal e remoção de valores nulos
    combined_data = pd.concat([candidate_factor.rename("Candidate"), benchmark_factors], axis=1).dropna()
    
    y = combined_data["Candidate"]
    X = combined_data.drop(columns=["Candidate"])
    X_with_const = sm.add_constant(X)
    
    # 1. Regressão OLS do fator candidato contra a matriz de benchmarks
    model = sm.OLS(y, X_with_const).fit()
    
    # 2. Extração dos resíduos puros (vetor ortogonal aos benchmarks)
    # Pelo Teorema FWL: Resíduo = M_X * Candidate
    orthogonal_residuals = model.resid
    
    # 3. Estatísticas de Diagnóstico
    alpha = model.params.get("const", 0.0)
    alpha_tstat = model.tvalues.get("const", 0.0)
    alpha_pvalue = model.pvalues.get("const", 1.0)
    r_squared = model.rsquared
    
    # Critério de Decisão Institucional:
    # Se R² for muito alto (> 0.70), o fator é colinear e redundante (Factor Zoo).
    # Se Alpha tiver t-stat > 2.0 (ou > 2.5 segundo Harvey et al., 2016), temos Alpha genuíno.
    is_genuine_alpha = abs(alpha_tstat) >= 2.0 and r_squared < 0.60
    
    diagnosis = (
        "ALPHA GENUÍNO DETECTADO: O sinal possui resíduo ortogonal estatisticamente significante "
        "e não é mera combinação linear dos benchmarks."
        if is_genuine_alpha else
        "SINAL REDUNDANTE (FACTOR ZOO): O sinal é fortemente explicado por fatores pré-existentes "
        "ou não possui significância estatística residual."
    )
    
    return {
        "model_summary": model.summary(),
        "orthogonal_factor_series": orthogonal_residuals,
        "alpha_intercept": alpha,
        "alpha_tstat": alpha_tstat,
        "alpha_pvalue": alpha_pvalue,
        "r_squared": r_squared,
        "is_genuine_alpha": is_genuine_alpha,
        "institutional_diagnosis": diagnosis
    }

if __name__ == "__main__":
    print("=" * 70)
    print("DEMONSTRAÇÃO INSTITUCIONAL: TEOREMA FWL & PURIFICAÇÃO DE FATORES")
    print("=" * 70)
    
    # Simulação de dados sintéticos para teste
    np.random.seed(42)
    dates = pd.date_range(start="2020-01-01", periods=500, freq="B")
    
    # Fatores Benchmark (Mercado, Valor, Momentum)
    mkt = np.random.normal(0.0005, 0.012, size=len(dates))
    val = np.random.normal(0.0002, 0.008, size=len(dates))
    mom = np.random.normal(0.0003, 0.009, size=len(dates))
    benchmarks_df = pd.DataFrame({"MKT": mkt, "VAL": val, "MOM": mom}, index=dates)
    
    # Caso 1: Fator Falso (80% dependente de Mercado e Momentum + ruído)
    fake_signal = 0.6 * mkt + 0.4 * mom + np.random.normal(0, 0.003, size=len(dates))
    fake_series = pd.Series(fake_signal, index=dates, name="NovoSinalFalso")
    
    res_fake = fwl_orthogonalize(fake_series, benchmarks_df)
    print("\n[TESTE 1] Sinal Falso (Disfarçado):")
    print(f"R² com Benchmarks: {res_fake['r_squared']:.2%}")
    print(f"Alpha t-stat:      {res_fake['alpha_tstat']:.2f}")
    print(f"Diagnóstico:       {res_fake['institutional_diagnosis']}")
    
    # Caso 2: Fator com Alpha Genuíno (ortogonal aos benchmarks + retorno autônomo consistente)
    true_signal = 0.0008 + np.random.normal(0, 0.005, size=len(dates))
    true_series = pd.Series(true_signal, index=dates, name="NovoSinalAlpha")
    
    res_true = fwl_orthogonalize(true_series, benchmarks_df)
    print("\n[TESTE 2] Sinal Genuíno:")
    print(f"R² com Benchmarks: {res_true['r_squared']:.2%}")
    print(f"Alpha t-stat:      {res_true['alpha_tstat']:.2f}")
    print(f"Diagnóstico:       {res_true['institutional_diagnosis']}")
    print("\n" + "=" * 70)
