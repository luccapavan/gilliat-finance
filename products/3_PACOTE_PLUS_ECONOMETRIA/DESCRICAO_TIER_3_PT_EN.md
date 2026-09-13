# ============================================================
# 🇧🇷 VERSÃO EM PORTUGUÊS (COPIAR E COLAR NA VERSÃO 3 DO GUMROAD)
# ============================================================

### 📈 Adicional Desta Versão: Applied Financial Econometrics Toolkit
*(Inclui tudo da Versão Básica + os 4 Motores em Python + a Suíte de Econometria Financeira)*

Ao selecionar a **Edição Plus**, você adiciona a suíte completa de **Econometria Financeira Aplicada** para modelagem macroeconômica multivariada e auditoria de fundos de terceiros:

* **1. Motor de Análise de Estilo de Sharpe (`analise_estilo_sharpe.py`)**
  * Implementação exata do algoritmo de *Returns-Based Style Analysis (RBSA)* de William Sharpe via otimização quadrática restrita (`scipy.optimize SLSQP`).
  * Desvende a alocação real de ativos e a exposição a fatores de qualquer fundo multimercado ou de ações usando apenas o histórico de cotas, sem precisar abrir a carteira.
  * Restrição orçamentária completa ($\sum w_i = 1$) e limites de posições compradas ($0 \le w_i \le 1$).
  * Cálculo automático do $R^2$ de consistência de estilo de gestão e Tracking Error anualizado.

* **2. Motor de Séries Temporais & Vetor Autorregressivo (`modelos_series_temporais.py`)**
  * Estimação matricial de modelos *Vetor Autorregressivo (VAR)* multivariados via MQO para análise dinâmica conjunta de variáveis macroeconômicas e financeiras (Juros, Câmbio, Inflação, Índices).
  * Seleção automática de ordem ótima de defasagem através dos Critérios de Informação de Akaike (AIC) e Bayesiano/Schwarz (BIC).
  * Extração da matriz de covariância dos resíduos e diagnósticos econométricos.

* **3. Documentação Bilíngue dos Modelos:**
  * `README.md` (Manual em português com exemplos práticos reproduzíveis).
  * `README_EN.md` (English documentation and reproduction guide).


# ============================================================
# 🇺🇸 ENGLISH VERSION (COPY & PASTE INTO GUMROAD VERSION 3)
# ============================================================

### 📈 Added in this Version: Applied Financial Econometrics Toolkit
*(Includes everything in the Basic Edition + the 4 Python Factor Engines + the Econometrics Suite)*

By selecting the **Plus Edition**, you add the complete **Applied Financial Econometrics Suite** for multivariate macroeconomic modeling and external fund auditing:

* **1. Sharpe Returns-Based Style Analysis Engine (`analise_estilo_sharpe.py`)**
  * Exact algorithmic implementation of William Sharpe’s RBSA framework via constrained quadratic optimization (`scipy.optimize SLSQP`).
  * Reverse-engineer any fund’s hidden asset allocation and factor exposures using solely its historical NAV return series—no open portfolio holdings required.
  * Strict full investment budget constraints ($\sum w_i = 1$) and long-only weight bounds ($0 \le w_i \le 1$).
  * Automated computation of Style $R^2$ (consistency metric) and annualized Tracking Error against factor benchmarks.

* **2. Vector Autoregression (VAR) & Dynamic Time Series (`modelos_series_temporais.py`)**
  * Multivariate OLS estimation of VAR models to analyze dynamic transmission shocks across macroeconomic and financial variables (Interest Rates, FX Rates, Inflation, Equity Indices).
  * Automated optimal lag selection using Akaike (AIC) and Bayesian/Schwarz (BIC) Information Criteria.
  * Residual covariance matrix extraction and full econometric diagnostic outputs.

* **3. Full Bilingual Documentation:**
  * `README_EN.md` (Complete documentation with reproducible usage examples).
  * `README.md` (Portuguese reference manual).
