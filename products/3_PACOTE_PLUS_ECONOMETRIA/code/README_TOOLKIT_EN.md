# 🐍 The Institutional Quant Code Toolkit
**Developed by: Lucca Simeoni Pavan, Ph.D.**  
*Former Head of Quantitative Strategies & Portfolio Allocation Manager • Ph.D. in Economics*

This repository contains the 4 production-grade, vectorized Python engines accompanying **The Institutional Quant Toolkit & Playbook**.

---

## 📦 Included Engines

### 1. `backtest_multifactor.py` / `backtest_multifactor_en.py` (Multi-Factor Backtest Engine)
* **Objective:** Vectorized simulation of systematic equity portfolios combining **Value (Earnings Yield E/P)** and **Momentum (12-2)**.
* **Institutional Features:**
  * Cross-sectional Z-score standardization (`sub.div`).
  * Strict exclusion of the most recent month (`shift(21)`) to eliminate short-term reversal noise.
  * Realistic transaction costs and turnover-penalized return calculations.
  * 100% vectorized in pandas and numpy without iterative `for` loops.

### 2. `risk_performance_metrics.py` / `risk_performance_metrics_en.py` (Risk & Tail Metrics Suite)
* **Objective:** Comprehensive risk metrics meeting investment committee and due diligence standards.
* **Computed Metrics:**
  * Compounded Annual Growth Rate (CAGR)
  * Annualized Volatility
  * Annualized Sharpe Ratio (excess return over risk-free rate)
  * Sortino Ratio (downside semi-variance)
  * Maximum Drawdown (MDD) and Drawdown Duration
  * Calmar Ratio
  * Parametric & Historical Value-at-Risk (VaR 95%)
  * **Conditional Value-at-Risk (CVaR / Expected Shortfall 95%)**

### 3. `factor_orthogonalization_fwl.py` / `factor_orthogonalization_fwl_en.py` (FWL Theorem Alpha Filter)
* **Objective:** Matrix projection of the Frisch-Waugh-Lovell theorem to isolate pure orthogonal alpha and eradicate redundant signals in the *Factor Zoo*.
* **Features:**
  * Residual orthogonal projection matrix decomposition.
  * Institutional t-statistic thresholds ($t > 2.0 / 2.5$).
  * Automated diagnostic classification: *Genuine Alpha vs Redundant Beta*.

### 4. `ledoit_wolf_covariance.py` / `ledoit_wolf_covariance_en.py` (Ledoit-Wolf Shrinkage Regularization)
* **Objective:** Eradicates Markowitz's sample covariance "error maximizer" flaw through analytical linear shrinkage.
* **Features:**
  * Condition number analysis and spectral eigenvalue stabilization.
  * Global Minimum Variance (GMV) portfolio optimization.
  * Comparative visualization of noisy sample weights vs. stabilized shrinkage weights.

---

## 🚀 Quick Start & Usage

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Any Engine Directly from Terminal:
```bash
python backtest_multifactor.py
python risk_performance_metrics.py
python factor_orthogonalization_fwl.py
python ledoit_wolf_covariance.py
```
