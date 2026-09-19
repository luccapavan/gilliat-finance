# Module 3: Technical Interview Guide & GitHub Portfolio

## 1. How Portfolio Managers Audit Your GitHub Portfolio

When recruiting for Quantitative Researcher or Asset Management Data Scientist roles, hiring managers receive hundreds of generic repository links. What separates top 5% candidates?

### ❌ What NOT to put on your GitHub:
* The clichéd "Stock Price Prediction with LSTM/GRU" with zero transaction costs.
* The Titanic or Iris dataset classification walkthrough.
* Massive unstructured Jupyter notebooks loaded with global variables and zero modular functions.

### ✅ What Impresses Quantitative Directors:
1. **Modular Architecture:** Clean code decoupled into production modules (`data_ingestion.py`, `factor_research.py`, `backtesting_engine.py`, `risk_allocator.py`).
2. **Explicit Market Frictions:** Code that dynamically models slippage, exchange fees, and borrow drag.
3. **Institutional Risk Tear Sheets:** Reporting not just Sharpe, but Sortino, Max Drawdown Duration, Calmar, Turnover, and Deflated Sharpe Ratio (DSR).
4. **Automated Unit Testing:** Pytest suites verifying no look-ahead leakage and zero forward-peeking shifts.

---

## 2. Classic Quantitative Interview Questions & Model Answers

### Question 1 (Econometrics & Time Series):
> *"What happens to OLS parameter estimators if the underlying time series possesses a unit root (non-stationarity)? How do you diagnose and correct this?"*
* **Model Answer:** OLS regressions between unit-root series suffer from spurious regression—exhibiting deceptively high $R^2$ values and inflated $t$-statistics without genuine economic relationships. Diagnosis: Augmented Dickey-Fuller (ADF) or Phillips-Perron tests. Correction: First-differencing the series or testing for cointegrating vectors via Engle-Granger / Johansen procedures.

### Question 2 (Factor Investing):
> *"How do you construct a cross-sectional Momentum factor, and why is the most recent month systematically excluded (12-2 momentum)?"*
* **Model Answer:** Canonical momentum (Jegadeesh & Titman) ranks assets by their cumulative 12-month trailing return, systematically excluding the most recent month ($t-1$). This exclusion is mandatory to neutralize the well-documented short-term reversal anomaly driven by temporary microstructural liquidity shocks.

### Question 3 (Quantitative Risk Management):
> *"What is the core conceptual and mathematical distinction between Value-at-Risk (VaR) and Conditional VaR (CVaR / Expected Shortfall)?"*
* **Model Answer:** VaR identifies the maximum expected loss at a given confidence interval (e.g. 95%), but offers zero information regarding the severity of losses once that threshold is breached. CVaR calculates the expected loss *conditional* on being in the tail beyond VaR. Crucially, CVaR is a coherent risk measure satisfying subadditivity ($f(X+Y) \le f(X) + f(Y)$), whereas VaR is non-subadditive.
