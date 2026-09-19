# INSTITUTIONAL ENTRANCE KIT: OFFICIAL SYLLABUS, TECHNICAL LEVELING GUIDE & DIAGNOSTIC ASSESSMENT
### *Applied Quantitative Research: Systematic Modeling, Factor Investing & Risk Allocation in Python*

**Author & Instructor:** Lucca Simeoni Pavan, Ph.D.  
*Former Head of Quantitative Strategies & Portfolio Allocation Manager • Ph.D. in Economics*  
**Exclusive Material for VIP Waitlist Applicants**

---

## 🧭 Welcome to Your Quantitative Launchpad

This kit was designed to serve as a pivotal bridge in your journey into institutional quantitative finance and systematic asset management. It is structured into three complementary parts:

1. **Part 1: Official Program Curriculum & Structure:** The complete 30-hour hands-on curriculum across 6 specialized modules, detailing every empirical skill and production model you will construct from scratch.
2. **Part 2: Technical Leveling Guide:** Essential mathematical, statistical, and computational foundations (including a production-ready Python script calculating an institutional multi-asset scorecard).
3. **Part 3: Diagnostic Assessment (Self-Evaluation):** 10 practical multiple-choice questions reflecting standard buy-side technical screens, accompanied by detailed solution explanations and an institutional readiness scoring rubric.

---

# PART 1: OFFICIAL PROGRAM CURRICULUM

* **Program Title:** Applied Quantitative Research: Systematic Modeling, Factor Investing & Risk Allocation in Python
* **Workload:** 30 hours (Live interactive workshops + full HD recordings + hands-on Python coding laboratories).
* **Technology Stack:** Python 3.10+, Pandas, NumPy, Statsmodels, SciPy, Matplotlib, Seaborn, yfinance.
* **Core Objective:** Empower quantitative researchers, analysts, economists, and data scientists to construct end-to-end institutional pipelines, from point-in-time financial data hygiene to bias-free backtesting and robust Ledoit-Wolf / HRP risk parity allocation.

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

# PART 2: TECHNICAL LEVELING GUIDE

## 1. The Mathematics of Financial Returns

A fundamental flaw among engineers and data scientists entering quantitative finance is conflating simple arithmetic returns with continuously compounded log returns.

### 1.1 Simple Arithmetic Return
Measures the percentage price change between two points in time:
$$R_t = \frac{P_t - P_{t-1}}{P_{t-1}} = \frac{P_t}{P_{t-1}} - 1$$

* **Fundamental Property:** Simple returns add linearly across assets in space (cross-section). If a portfolio allocates weights $w_i$, the total daily portfolio return is strictly the weighted sum:
$$R_{p, t} = \sum_{i=1}^N w_i R_{i, t}$$

### 1.2 Logarithmic Return (Continuously Compounded)
Defined as the difference between natural logarithms of prices:
$$r_t = \ln\left(\frac{P_t}{P_{t-1}}\right) = \ln(P_t) - \ln(P_{t-1})$$

* **Fundamental Property:** Log returns add linearly across time (time series). The compounded multi-period return across $T$ periods is simply the direct sum of daily log returns:
$$r_{total} = \sum_{t=1}^{T} r_t$$

> **The Golden Rules for Quantitative Analysts:**  
> • Use **simple returns** for portfolio NAV calculation, accounting, and performance attribution.  
> • Use **log returns** for statistical modeling, volatility estimation, distribution fitting, and econometric regressions.

---

## 2. Annualization Standards (252 Business Days)

In global equity markets, return and volatility annualization follows the standard 252 business days convention:

* **Compounded Annualized Return:**
$$\bar{R}_{annual} = (1 + \bar{R}_{daily})^{252} - 1$$

* **Annualized Volatility (Square Root of Time Rule):**
$$\sigma_{annual} = \sigma_{daily} \times \sqrt{252}$$

---

## 3. Institutional Performance & Risk Metrics

1. **Sharpe Ratio:**
   $$\text{Sharpe} = \frac{\bar{R}_p - R_f}{\sigma_p}$$
   Where $R_f$ is the annualized risk-free rate.

2. **Sortino Ratio (Penalizing Downside Volatility Only):**
   $$\text{Sortino} = \frac{\bar{R}_p - R_f}{\sigma_{down}}$$
   $$\sigma_{down} = \sqrt{\frac{1}{T} \sum_{t=1}^T \min(0, R_{p,t} - R_{f,t})^2 \times 252}$$

3. **Maximum Drawdown (MDD):**
   $$DD_t = \frac{\text{NAV}_t - \max_{\tau \le t}(\text{NAV}_\tau)}{\max_{\tau \le t}(\text{NAV}_\tau)}, \quad MDD = \min_t(DD_t)$$

---

## 4. Production Python Leveling Script: Multi-Asset Scorecard

Execute the script below in your Python 3.10+ environment to compute an institutional scorecard across multi-asset tickers:

```python
import numpy as np
import pandas as pd
import yfinance as yf

# 1. Define Multi-Asset Institutional Universe
tickers = ['SPY', 'QQQ', 'AAPL', 'NVDA', 'TLT']
start_date = '2021-01-01'
end_date = '2026-01-01'

print("📥 Fetching institutional market data...")
data = yf.download(tickers, start=start_date, end=end_date, progress=False)

# 2. Use Split- and Dividend-Adjusted Close Prices
prices = data['Adj Close'].dropna()

# 3. Compute Daily Simple Arithmetic Returns
returns = prices.pct_change().dropna()

# 4. Institutional Quantitative Scorecard Function
def compute_institutional_scorecard(series, rf_annual=0.045):
    rf_daily = (1 + rf_annual) ** (1 / 252) - 1
    ann_return = (1 + series.mean()) ** 252 - 1
    ann_vol = series.std() * np.sqrt(252)
    
    # Sharpe Ratio
    sharpe = (ann_return - rf_annual) / ann_vol if ann_vol > 0 else 0.0
    
    # Sortino Ratio (Penalizing Downside Volatility Only)
    excess_ret = series - rf_daily
    downside_vol = excess_ret[excess_ret < 0].std() * np.sqrt(252)
    sortino = (ann_return - rf_annual) / downside_vol if downside_vol > 0 else 0.0
    
    # Maximum Drawdown (MDD)
    cum_returns = (1 + series).cumprod()
    peak = cum_returns.cummax()
    drawdown = (cum_returns - peak) / peak
    mdd = drawdown.min()
    
    return pd.Series({
        'Ann. Return': f"{ann_return * 100:.2f}%",
        'Ann. Volatility': f"{ann_vol * 100:.2f}%",
        'Sharpe Ratio': f"{sharpe:.2f}",
        'Sortino Ratio': f"{sortino:.2f}",
        'Max Drawdown': f"{mdd * 100:.2f}%"
    })

scorecard = returns.apply(compute_institutional_scorecard)
print("\n" + "=" * 65)
print("📊 INSTITUTIONAL QUANTITATIVE SCORECARD")
print("=" * 65)
print(scorecard.to_string())

# 5. Linear Correlation Matrix
print("\n🔗 Linear Correlation Matrix:")
print(np.round(returns.corr(), 2).to_string())
```

---

# PART 3: DIAGNOSTIC ASSESSMENT: 10 INSTITUTIONAL QUESTIONS
### *Self-Evaluation of Quantitative Readiness*

Answer the following 10 questions without looking at the solutions. Then check your explained answers and find your institutional maturity level.

---

### Question 1 (Portfolio Return Mathematics)
When constructing a systematic portfolio allocating 40% in Asset A and 60% in Asset B, which mathematical formulation correctly computes the daily total return of the portfolio?
* A) The weighted arithmetic average of the logarithmic returns.
* B) The weighted arithmetic average of the simple arithmetic returns.
* C) The geometric mean of simple returns.
* D) The logarithm of the ratio between total volume and closing prices.

---

### Question 2 (Backtest Biases & Microstructure)
A researcher builds a multi-factor strategy that utilizes Q4 financial statements (fiscal period ending Dec 31) to rebalance stock holdings on the first trading session of January. What fatal quantitative error has occurred?
* A) Survivorship bias due to delisted companies.
* B) Look-ahead bias, because audited annual 10-K financial statements are filed and publicized months later in March or April.
* C) Specification error by using calendar days instead of trading days.
* D) Convexity bias in volatility annualization.

---

### Question 3 (Python & Pandas Vectorization)
Given a date-indexed pandas DataFrame `df` containing adjusted prices in column `'close'`, which statement correctly computes daily simple arithmetic returns while preserving chronological alignment?
* A) `df['close'].diff() / df['close']`
* B) `np.log(df['close']) - np.log(df['close'].shift(-1))`
* C) `df['close'].pct_change().dropna()`
* D) `df['close'].rolling(252).mean()`

---

### Question 4 (Volatility Annualization Standards)
An equity asset displays a daily return standard deviation of 2.0% in a market with 252 business days. Under the standard assumption of independent and identically distributed (i.i.d.) returns, what is its annualized volatility?
* A) $2.0\% \times 252 = 504.0\%$
* B) $2.0\% \times \sqrt{252} \approx 31.75\%$
* C) $2.0\% / \sqrt{252} \approx 0.126\%$
* D) $(1 + 0.02)^{252} - 1 \approx 145.2\%$

---

### Question 5 (Asymmetric Risk Metrics)
Why do institutional quantitative managers frequently favor the **Sortino Ratio** over the **Sharpe Ratio** for strategies characterized by positive return skewness?
* A) The Sortino Ratio does not require a risk-free benchmark.
* B) The Sharpe Ratio penalizes upside return spikes identically to catastrophic drawdowns, whereas Sortino penalizes only downside volatility.
* C) The Sortino Ratio is independent of sample size.
* D) The Sharpe Ratio cannot be calculated when returns are non-negative.

---

### Question 6 (Time-Series Cross-Validation)
Why is the direct application of standard Scikit-Learn *K-Fold Cross-Validation* considered invalid and dangerously misleading for financial asset pricing models?
* A) Standard K-Fold shuffles observations and trains on future data to predict the past, introducing severe temporal data leakage and autocorrelation contamination.
* B) K-Fold is computationally restricted to binary classification tasks only.
* C) The number of folds must match the number of assets in the universe.
* D) K-Fold artificially increases transaction fee estimates.

---

### Question 7 (Factor Modeling Paradigms)
What is the core distinction between a **Cross-Sectional Momentum** strategy and a **Time-Series Momentum (Trend Following)** strategy?
* A) Cross-Sectional is applied to fixed income and Time-Series is applied to equities.
* B) Cross-Sectional ranks assets relative to one another at a given timestamp (buying top decile, shorting bottom decile), while Time-Series evaluates each asset's own historical return trajectory against its own history in absolute terms.
* C) Cross-Sectional uses single moving averages while Time-Series uses multiple regressions.
* D) Both terms are synonymous in empirical asset pricing literature.

---

### Question 8 (Microstructure Frictions & Execution Slippage)
When backtesting a systematic small-cap strategy with $20M in AUM, which parameter is crucial to prevent the model from capturing illusory alpha on illiquid names that cannot be executed in live trading?
* A) Consumer Price Index (CPI) inflation lags.
* B) Average Daily Trading Volume (ADTV) participation limits (e.g. max 5-10% of ADTV) and nonlinear market impact / slippage models.
* C) Social media follower count of listed management.
* D) Book-to-market ratio divided by the number of shares outstanding.

---

### Question 9 (Covariance Estimation & Markowitz Optimization)
What is the central empirical drawback of traditional Markowitz Mean-Variance Optimization when applied directly to sample covariance matrices across dozens of assets?
* A) The algorithm is unable to process positive returns.
* B) Inverting an ill-conditioned sample covariance matrix acts as an "estimation error maximizer", concentrating extreme, unstable weights on noisy assets; a flaw solved by Ledoit-Wolf shrinkage.
* C) Markowitz requires that all portfolio returns be zero.
* D) The solver requires unconstrained shorting in all scenarios.

---

### Question 10 (Hierarchical Risk Parity - HRP)
What breakthrough did Marcos López de Prado's **Hierarchical Risk Parity (HRP)** algorithm introduce to institutional portfolio construction?
* A) It uses machine learning unsupervised tree clustering on the correlation matrix to allocate risk recursively, completely bypassing covariance matrix inversion and eliminating numerical instability.
* B) It guarantees 0% drawdown across all market cycles.
* C) It replaces mathematical solvers with natural language processing.
* D) It optimizes option strike prices for high-frequency trading.

---

# OFFICIAL DETAILED SOLUTIONS & EXPLANATIONS

* **Question 1: B**  
  *Explanation:* Cross-sectional aggregation of multiple assets obeys linear addition of simple arithmetic returns: $R_{p,t} = \sum w_i R_{i,t}$. Summing weighted logarithmic returns produces mathematically invalid portfolio valuations.
* **Question 2: B**  
  *Explanation:* Annual financial statements (10-K) are published 60 to 90 days after fiscal year end. Utilizing year-end figures on Jan 1 is pure lookahead bias, invalidating the historical backtest.
* **Question 3: C**  
  *Explanation:* `df['close'].pct_change().dropna()` is the native, vector-optimized pandas implementation of $\frac{P_t - P_{t-1}}{P_{t-1}}$.
* **Question 4: B**  
  *Explanation:* Under the i.i.d. assumption, return variance scales linearly with time $T$, meaning standard deviation scales with the **square root of time**: $\sigma_{ann} = 2.0\% \times \sqrt{252} \approx 31.75\%$.
* **Question 5: B**  
  *Explanation:* The standard Sharpe ratio penalizes upside volatility as risk. The Sortino ratio substitutes the denominator with downside semi-deviation, rewarding asymmetric upside strategies.
* **Question 6: A**  
  *Explanation:* Financial time series exhibit sequential temporal dependence and autocorrelation. Standard K-fold shuffles future data into training folds, causing catastrophic information leakage. Purged walk-forward cross-validation is mandatory.
* **Question 7: B**  
  *Explanation:* Cross-sectional momentum produces relative asset rankings at a single snapshot in time. Time-series momentum evaluates an individual asset's own trend across time in absolute terms.
* **Question 8: B**  
  *Explanation:* Without volume participation limits (e.g., capping trading at 10% of ADTV) and nonlinear market impact models (Almgren-Chriss / Kyle lambda), small-cap strategy alphas evaporate under real-world order execution.
* **Question 9: B**  
  *Explanation:* Inverting sample covariance matrices with high asset dimensionality amplifies random noise. Ledoit-Wolf shrinkage shrinks the noisy sample covariance toward a structured target, yielding robust, stable asset weights.
* **Question 10: A**  
  *Explanation:* Hierarchical Risk Parity (HRP) structures assets into a dendrogram via machine learning hierarchical clustering, allocating risk recursively along clusters without inverting matrices, conferring stability during structural regime shifts.

---

# DIAGNOSTIC SCORING & PROGRAM ROADMAP

Count your correct answers and locate your diagnostic profile:

```
┌─────────────────┬────────────────────────────────────────────────────────┐
│  SCORE          │  DIAGNOSTIC LEVEL & RECOMMENDED FOCUS                  │
├─────────────────┼────────────────────────────────────────────────────────┤
│  0 to 4 Correct │  LEVEL 1: FOUNDATIONS / IN TRANSITION                  │
│                 │  Solid analytical curiosity, but carrying habits from  │
│                 │  generic Data Science or manual spreadsheets.          │
│                 │  👉 RECOMMENDED FOCUS: Modules 1 & 2 will build        │
│                 │  uncompromised data pipelines & institutional metrics. │
├─────────────────┼────────────────────────────────────────────────────────┤
│  5 to 7 Correct │  LEVEL 2: INTERMEDIATE QUANT ANALYST                   │
│                 │  Strong Python syntax and foundational statistics,     │
│                 │  with gaps in real market frictions & factor modeling. │
│                 │  👉 RECOMMENDED FOCUS: Modules 3 & 4 will elevate your │
│                 │  backtesting to buy-side desk standards.               │
├─────────────────┼────────────────────────────────────────────────────────┤
│  8 to 10 Correct│  LEVEL 3: QUANT DESK READY                             │
│                 │  Strong conceptual maturity and refined intuition      │
│                 │  for market microstructure and risk budgeting.         │
│                 │  👉 RECOMMENDED FOCUS: Modules 4, 5 & 6 will cement    │
│                 │  your mastery of Ledoit-Wolf, HRP & capstone testing.  │
└─────────────────┴────────────────────────────────────────────────────────┘
```

---

> 🔒 **VIP Waitlist Guarantee:** Save this document. Applicants on the waitlist will receive early access to the 1st Cohort with an **exclusive 20% launch discount** and direct 1-on-1 code review mentoring with Dr. Lucca Simeoni Pavan.
