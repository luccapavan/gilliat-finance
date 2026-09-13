# 🐍 The Institutional Quant Code Toolkit
**Desenvolvido por: Lucca Simeoni Pavan, Ph.D.**  
*Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação*

Este repositório contém os 4 motores em Python de nível institucional que acompanham o **The Institutional Quant Toolkit & Playbook**.

---

## 📦 Motores Inclusos

### 1. `backtest_multifactor.py` (Motor de Backtest Multifatorial)
* **Objetivo:** Simulação vetorial de carteiras sistemáticas combinando fatores de **Value (E/P)** e **Momentum (12-2)**.
* **Recursos Institucionais:**
  * Padronização transversal por Z-Scores (`sub.div`).
  * Exclusão obrigatória de reversão de curto prazo (`shift(21)`).
  * Dedução realista de custos de transação e atrito de giro (turnover).
  * Execução 100% vetorizada em pandas/numpy sem loops `for`.

### 2. `risk_performance_metrics.py` (Motor de Risco & Cauda)
* **Objetivo:** Métricas completas para comitês de risco e due diligence de fundos.
* **Métricas Calculadas:**
  * CAGR (Retorno Anualizado Composto)
  * Volatilidade Anualizada
  * Índice de Sharpe Anualizado
  * Índice de Sortino (Downside Deviation)
  * Maximum Drawdown e Duração
  * Índice de Calmar
  * Value at Risk (VaR 95% Paramétrico e Histórico)
  * **Conditional Value at Risk (CVaR / Expected Shortfall 95%)**

### 3. `factor_orthogonalization_fwl.py` (Teorema FWL & Filtro de Alfa)
* **Objetivo:** Aplicação matricial do Teorema de Frisch-Waugh-Lovell para isolar alfa autêntico e eliminar fatores redundantes do *Factor Zoo*.
* **Recursos:**
  * Projeção ortogonal residual via matriz aniquiladora.
  * Teste t-stat de corte institucional (t > 2.0 / 2.5).
  * Diagnóstico automatizado: *Alpha Genuíno vs Sinal Redundante*.

### 4. `ledoit_wolf_covariance.py` (Estabilização Ledoit-Wolf)
* **Objetivo:** Eliminação do problema do "Error Maximizer" de Markowitz clássico através de encolhimento linear (Linear Shrinkage).
* **Recursos:**
  * Cálculo e comparação de autovalores e número de condição espectral.
  * Otimização de Carteira de Mínima Variância Global (GMV).
  * Comparativo de pesos amostrais vs pesos estabilizados.

---

## 🚀 Como Executar

### 1. Instale as dependências
```bash
pip install -r requirements.txt
```

### 2. Execute qualquer um dos módulos diretamente:
```bash
python backtest_multifactor.py
python metricas_risco_performance.py
python factor_orthogonalization_fwl.py
python ledoit_wolf_covariance.py
```

---
*Todos os códigos foram testados e validados em ambiente Python 3.10+.*
