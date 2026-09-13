# ============================================================
# 🇧🇷 VERSÃO EM PORTUGUÊS (COPIAR E COLAR NA VERSÃO 2 DO GUMROAD)
# ============================================================

### 💻 Adicional Desta Versão: 4 Motores Vetorizados em Python
*(Inclui todo o material da versão básica + os 4 scripts de código de nível de asset management)*

Ao selecionar esta versão, você adiciona à sua biblioteca os 4 motores de código em Python vetorizados (NumPy/Pandas), comentados linha a linha e prontos para rodar em produção ou apresentar em desafios técnicos (Take-Home de 48h):

* **1. Motor de Backtest Multifatorial Vetorizado (`backtest_multifactor.py`)**
  * Simulação quantitativa combinando fatores de Value (Earnings Yield) e Momentum (12-2).
  * Código 100% vetorizado (zero loops iterativos `for`), garantindo velocidade profissional.
  * Normalização transversal (*Cross-Sectional Z-Score*) recalculada a cada corte temporal.
  * Lag estrito de 21 dias para eliminar ruído de reversão de curto prazo e lookahead bias.
  * Dedução realista de custos de corretagem, emolumentos e atrito de giro (*turnover*).

* **2. Motor de Risco de Cauda & Performance (`risk_performance_metrics.py`)**
  * Cálculo institucional de **CVaR 95% (Expected Shortfall)**, além de VaR paramétrico e histórico.
  * Métricas padrão de comitê de risco: Sharpe Anualizado ponderado pela taxa livre de risco/CDI, Índice de Sortino (*downside deviation*), Drawdown Máximo, Duração de Drawdown e Índice de Calmar.

* **3. Motor de Ortogonalização de Fatores FWL (`factor_orthogonalization_fwl.py`)**
  * Implementação algorítmica do Teorema de Frisch-Waugh-Lovell via projeção matricial QR/OLS.
  * Purifica sinais de investimento: expurga a correlação espúria com betas redundantes de mercado e isola o resíduo puro de alpha com teste t e significância estatística.

* **4. Covariância Robusta com Encolhimento de Ledoit-Wolf (`ledoit_wolf_covariance.py`)**
  * Elimina a instabilidade numérica da matriz de covariância amostral tradicional de Markowitz.
  * Calcula analiticamente a intensidade ótima de encolhimento (*shrinkage*) em direção a um alvo estruturado, gerando carteiras de variância mínima e tangência matematicamente estáveis.

* **5. Manual Técnico & Dependências:**
  * Arquivo `README_TOOLKIT.md` com explicações de execução e interpretação de saídas.
  * Arquivo `requirements.txt` pronto para instalação (`pip install -r requirements.txt`).


# ============================================================
# 🇺🇸 ENGLISH VERSION (COPY & PASTE INTO GUMROAD VERSION 2)
# ============================================================

### 💻 Added in this Version: 4 Vectorized Python Production Engines
*(Includes all materials from the Basic Edition + the 4 institutional Python engines)*

By selecting this version, you add 4 production-grade Python engines to your toolkit, natively vectorized in NumPy and Pandas, tested, and commented line-by-line for production use and 48-hour take-home technical challenges:

* **1. Vectorized Multi-Factor Backtester (`backtest_multifactor.py`)**
  * Full systematic equity simulation combining Value (Earnings Yield) and Momentum (12-2).
  * 100% vectorized in NumPy and Pandas (zero iterative loops), ensuring institutional execution speed.
  * Point-in-time cross-sectional standardization (Z-score) recalculated across universe constituents at each rebalancing stamp.
  * Strict 21-day execution lag to eliminate short-term reversal microstructural noise.
  * Realistic transaction costs and turnover-penalized return calculations.

* **2. Tail Risk & Performance Metrics Suite (`risk_performance_metrics.py`)**
  * Institutional calculation of **CVaR 95% (Conditional VaR / Expected Shortfall)**, parametric VaR, and historical VaR.
  * Investment committee standard metrics: Annualized Sharpe relative to benchmark/risk-free rate, Sortino Ratio (downside volatility), Maximum Drawdown, Drawdown Duration, and Calmar Ratio.

* **3. Factor Orthogonalization via FWL Theorem (`factor_orthogonalization_fwl.py`)**
  * Algorithmic projection of the Frisch-Waugh-Lovell theorem via QR/OLS matrix decomposition.
  * Purifies raw alpha signals: strips away collinearity with redundant market and size betas, isolating pure orthogonal alpha residuals with full t-statistic reporting.

* **4. Robust Ledoit-Wolf Covariance Shrinkage (`ledoit_wolf_covariance.py`)**
  * Eliminates the numerical instability of Markowitz sample covariance matrices.
  * Computes analytical optimal shrinkage intensity towards structured targets and yields stable, invertible minimum variance and tangency portfolios.

* **5. Quick-Start Documentation & Dependencies:**
  * `README_TOOLKIT.md` with step-by-step reproduction instructions and command-line guides.
  * `requirements.txt` for immediate one-command environment setup.
