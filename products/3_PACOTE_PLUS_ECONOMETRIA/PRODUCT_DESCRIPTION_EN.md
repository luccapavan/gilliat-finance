# The Institutional Quant & Econometrics Suite (Plus Edition)
**Product Description & Sales Copy**  
**Author:** Lucca Simeoni Pavan, Ph.D. | *Former Head of Quantitative Strategies & Portfolio Allocation Manager*

---

## 🏷️ Product Overview
* **Product Name:** The Institutional Quant & Econometrics Suite: Plus Edition (All-in-One Flagship)
* **Subtitle / Tagline:** The definitive flagship suite: 13-page Dossier + Anti-Bias Checklists + 4 Factor Investing Engines + Applied Financial Econometrics Toolkit (VAR & Sharpe Style Analysis).
* **Price:** $27.00 - $37.00 USD (One-time payment via Stripe / PayPal / Card)
* **Delivery File:** Compressed ZIP archive `3_PACOTE_PLUS_ECONOMETRIA.zip` (1.47 MB)

---

## ⚡ Short Description (Storefront, Checkout & Social Media)
> The most comprehensive quantitative finance suite available for researchers, portfolio managers, and quants. You receive **everything in the Intermediate Edition** (the 4 bilingual PDFs and the 4 Python factor investing engines) **PLUS the Applied Financial Econometrics Toolkit**: Vector Autoregressive (VAR) multivariate modeling with optimal lag selection (AIC/BIC), and William Sharpe’s Returns-Based Style Analysis (RBSA via constrained quadratic optimization in Scipy) to reverse-engineer any fund's true asset allocation and style exposures without open holdings.

---

## 📄 Full Description (Sales Page / Gumroad Store)

### Combining Factor Investing and Advanced Financial Econometrics
At the highest levels of institutional asset management, top quantitative researchers and portfolio managers do not operate in isolated silos. They master two intertwined disciplines simultaneously:
1. **Factor Investing & Equity Microstructure:** Generating systematic alpha, constructing market-neutral portfolios, and managing coherent tail risk;
2. **Financial Econometrics & Multivariate Modeling:** Evaluating dynamic macroeconomic transmission shocks (interest rates, currencies, inflation) and reverse-engineering the true style exposures of external fund managers.

The **Plus Edition** is our flagship offering. It merges **The Institutional Quant Toolkit & Playbook** with the **Applied Financial Econometrics Toolkit**, delivering an end-to-end infrastructure for quantitative research and institutional asset management.

---

### 📦 What You Receive Inside (`3_PACOTE_PLUS_ECONOMETRIA.zip`):

#### 1. Methodological Dossiers & Checklists in PDF (EN & PT):
* `The_Quant_Transition_Playbook_EN.pdf` & `The_Quant_Transition_Playbook_PT.pdf` (13-page institutional dossiers)
* `Quant_Anti_Bias_Checklist_EN.pdf` & `Quant_Anti_Bias_Checklist_PT.pdf` (2-page anti-bias audit checklists)

#### 2. The 4 Factor Investing Python Engines (`code/`):
* **`backtest_multifactor.py`:** Complete multi-factor equity simulation (Value + Momentum) with native vectorization, cross-sectional standardization (Z-score), 12-2 execution lag, and turnover penalties.
* **`risk_performance_metrics.py`:** Institutional tail risk suite featuring CVaR 95% (Expected Shortfall), parametric/historical VaR, annualized Sharpe, Sortino, and Calmar ratios.
* **`factor_orthogonalization_fwl.py`:** Frisch-Waugh-Lovell matrix projection theorem to purge collinear market betas and isolate pure orthogonal alpha residuals.
* **`ledoit_wolf_covariance.py`:** Robust portfolio optimization via Ledoit-Wolf analytical covariance shrinkage, eliminating Markowitz sample error.

#### 3. Applied Financial Econometrics Toolkit (`econometrics_toolkit/`):
* **Econometric Engine 1: Sharpe Returns-Based Style Analysis (`analise_estilo_sharpe.py`)**
  * Exact algorithmic implementation of William Sharpe’s RBSA framework.
  * Constrained quadratic optimization (`scipy.optimize SLSQP`) enforcing budget constraints ($\sum w_i = 1$) and long-only exposures ($0 \le w_i \le 1$).
  * Reverse-engineers any fund's hidden factor tilts and asset allocations using only its historical net-of-fees NAV return series.
  * Automated calculation of Style $R^2$ (consistency metric) and annualized Tracking Error against the factor proxy portfolio.
* **Econometric Engine 2: Vector Autoregression & Time Series (`modelos_series_temporais.py`)**
  * Multivariate OLS estimation of VAR models to analyze dynamic interdependencies between macroeconomic and financial variables (e.g., yield curves, FX rates, equity indices).
  * Automated optimal lag selection using Akaike (AIC) and Bayesian/Schwarz (BIC) Information Criteria.
  * Residual covariance matrix extraction and econometric diagnostics.
* **Full Bilingual Documentation:** `README_EN.md` (English) and `README.md` (Portuguese) with step-by-step reproduction scripts.

---

### 🎯 Who This Package Is Built For:
* **Quantitative Researchers & Economists:** Seamlessly integrate systematic single-stock factor models with macro multivariate econometric forecasting.
* **Fund Allocators, Family Offices & CIOs:** Use Sharpe Style Analysis to audit external hedge funds, verifying whether managers are delivering true alpha or simply charging 2/20 for disguised market beta.
* **Senior Quant Candidates:** Stand out decisively in interview processes by showcasing an expansive, production-grade technical repository combining both computer science and econometric rigor.

---

### 👤 About the Author
**Lucca Simeoni Pavan, Ph.D.**  
Ph.D. in Economics. Former Head of Quantitative Strategies and Investment Product Manager in Brazilian asset management, specializing in systematic equities, multi-factor models, and institutional portfolio construction.
