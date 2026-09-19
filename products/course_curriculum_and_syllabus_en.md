# Program Curriculum & Course Syllabus

**Instructor:** Lucca Simeoni Pavan, Ph.D.  
*Former Head of Quantitative Strategies & Portfolio Allocation Manager • Ph.D. in Economics*

---

# PROGRAM 1: Applied Quantitative Research
### *Systematic Modeling, Factor Investing & Risk Allocation in Python*

* **Overall Objective:** Equip quantitative researchers, economists, analysts, and data scientists to architect end-to-end production pipelines: from point-in-time financial data ingestion and hygiene to bias-free backtesting and robust Ledoit-Wolf / HRP risk parity portfolio allocation.
* **Workload:** 30 hours (Live interactive workshops + recordings + hands-on Python coding laboratories).
* **Technology Stack:** Python 3.10+, Pandas, NumPy, Statsmodels, SciPy, Matplotlib, Seaborn, yfinance.

---

### Module 1: Institutional Financial Data Pipelines & Data Hygiene (5 Hours)
* **Lecture 1.1:** Quantitative pipeline architecture: multidimensional time-series data structures (multi-index DataFrames and panels).
* **Lecture 1.2:** Institutional data ingestion: connecting to central bank APIs, regulatory filings, and market exchange feeds.
* **Lecture 1.3:** Critical data treatment: cash dividend adjustments, splits, reverse splits, spin-offs, and trading calendar conventions.
* **Lecture 1.4:** The invisible hazard: identifying and eradicating survivorship bias and look-ahead bias with Point-in-Time (PIT) lags.
* **Hands-On Lab:** Constructing a clean, bias-free historical dataset covering 10+ years of equity trading with timestamp integrity.

---

### Module 2: Return Statistics & Institutional Risk Metrics (5 Hours)
* **Lecture 2.1:** Simple arithmetic vs. logarithmic returns: mathematical properties and exact modeling applications.
* **Lecture 2.2:** Empirical return distributions: non-normality, fat tails, negative skewness, and excess kurtosis.
* **Lecture 2.3:** Performance metrics beyond Sharpe: Sortino Ratio (downside semi-variance), Calmar Ratio, and Information Ratio.
* **Lecture 2.4:** Drawdown dynamics: analytical computation of Maximum Drawdown (MDD), drawdown duration, and time to recovery.
* **Lecture 2.5:** Coherent Tail Risk: Parametric and Historical Value at Risk (VaR 95%) and Conditional VaR (Expected Shortfall / CVaR).
* **Hands-On Lab:** Developing an automated module ingesting price feeds and spitting out institutional Risk Tear Sheets.

---

### Module 3: Factor Investing & Multi-Factor Research (5 Hours)
* **Lecture 3.1:** Evolution of asset pricing theories: From Single-Index CAPM to Fama-French 5 Factors and Carhart.
* **Lecture 3.2:** Momentum anomalies: Cross-Sectional Momentum (winners vs losers relative ranking) vs. Time-Series Momentum (trend following).
* **Lecture 3.3:** Fundamental factors: Value (Earnings Yield E/P, Book-to-Market) and Quality (ROE, ROIC, Net Margin, Accruals).
* **Lecture 3.4:** Risk factors: Low Beta / Low Volatility anomaly and Size (Small-Cap premium).
* **Lecture 3.5:** Surviving the "Factor Zoo": t-statistic significance thresholds (t > 2.5), Bonferroni corrections, and out-of-sample testing.
* **Hands-On Lab:** Multi-factor ranking engine with cross-sectional Z-Scores generating isolated alpha spreads.

---

### Module 4: Realistic Institutional Backtesting Framework (5 Hours)
* **Lecture 4.1:** Backtesting paradigms: Vectorized (fast hypothesis exploration) vs. Event-Driven (precise execution fidelity).
* **Lecture 4.2:** Modeling market frictions: exchange fees, clearing fees, borrow rates on short legs, and dividend taxes.
* **Lecture 4.3:** Slippage & Market Impact: Average Daily Trading Volume (ADTV) participation limits and Almgren-Chriss square-root impact.
* **Lecture 4.4:** Periodic rebalancing: optimal frequencies (weekly, monthly), turnover tolerance bands, and transaction fee drag.
* **Lecture 4.5:** Walk-Forward Analysis and Purged & Embargoed Cross-Validation for financial time series without leakage.
* **Hands-On Lab:** Running a multi-year backtest of a quantitative factor strategy with complete friction accounting and auditable equity curves.

---

### Module 5: Portfolio Optimization & Risk Allocation (5 Hours)
* **Lecture 5.1:** Markowitz Mean-Variance Optimization: extreme sensitivity to estimation noise and sample instability.
* **Lecture 5.2:** Covariance matrix regularization: Ledoit-Wolf analytical shrinkage and Random Matrix Theory (RMT) eigenvalue cleaning.
* **Lecture 5.3:** Risk Parity & Marginal Risk Contributions: ensuring volatile assets do not dominate total portfolio risk budgets.
* **Lecture 5.4:** Hierarchical Risk Parity (HRP): unsupervised machine learning tree clustering bypassing matrix inversion entirely.
* **Hands-On Lab:** Empirical horse-race benchmark: 1/N vs. Mean-Variance vs. Ledoit-Wolf vs. HRP under practical turnover bounds.

---

### Module 6: Final Capstone & Production Deployment (5 Hours)
* **Lecture 6.1:** Structuring quantitative Python codebases: modularity, typing, testing, reproducibility, and CI/CD pipelines.
* **Lecture 6.2:** Automated executive reporting: generating interactive HTML/PDF risk dashboards for investment committees.
* **Capstone Challenge:** Developing a complete proprietary quantitative strategy (ingestion -> factor scoring -> friction-penalized backtest -> risk allocation -> tear sheet) with 1-on-1 code review and grading rubric.

---

# PROGRAM 2: Quantitative Macroeconomics & Asset Allocation for Advisors
### *Systematic Regimes, Factor Allocations & Portfolio Construction*

* **Workload:** 24 hours
* **Target Audience:** Wealth managers, investment advisors (EAA / RIAs), family office analysts, and multi-asset allocators.
* **Core Modules:**
  * Module 1: The New Paradigm of Financial Advisory (Moving from Ad-Hoc Stock Picking to Factor & Regime Allocation)
  * Module 2: Quantitative Macroeconomic Ingestion & Inflation/Yield Curve Forecasting
  * Module 3: Quantitative Dynamic Asset Allocation (All-Weather, Risk Parity, Momentum Overlays)
  * Module 4: Due Diligence, Hedge Fund Style Analysis (Sharpe RBSA) & Executive Client Dashboards
