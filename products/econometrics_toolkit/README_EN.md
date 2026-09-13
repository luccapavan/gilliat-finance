# Applied Financial Econometrics Toolkit (Python)
**Econometric Models & Quantitative Analysis Library for Finance**  
*Developed by Lucca Simeoni Pavan, Ph.D.*

---

## 🎯 What is this Toolkit?
The **Applied Financial Econometrics Toolkit** is a collection of production-ready, research-grade Python modules designed to save weeks of development in essential financial econometrics and quantitative portfolio management workflows.

Each module follows rigorous empirical literature standards and comes fully documented with mathematical formulations and reproducible practical examples.

---

## 📦 Module Overview

### 1. `modelos_series_temporais.py` (Financial Time Series & Vector Autoregression)
* **Stationarity Tests:** Augmented Dickey-Fuller (ADF) and KPSS with automated interpretation.
* **Vector Autoregressive (VAR) Models:** Optimal lag selection via Information Criteria (AIC, BIC, HQIC) and OLS parameter estimation.
* **Covariance Matrix & Residual Diagnostics:** Residual covariance ($\Sigma_u$) estimation and log-determinant computation for multivariate time series.

### 2. `analise_estilo_sharpe.py` (Sharpe Returns-Based Style Analysis - RBSA)
* **William Sharpe's RBSA Algorithm:** Uncovers an investment fund's real asset allocation and style exposures over time using only historical return series—no open portfolio holdings required.
* **Constrained Quadratic Optimization:** Solved via `scipy.optimize` enforcing full investment ($\sum w_i = 1$) and long-only weights ($0 \le w_i \le 1$, with easy customization for levered funds).
* **Style Statistics:** Calculates Style $R^2$ (allocation consistency) and annualized Tracking Error against the factor portfolio.

---

## 🚀 Quick Start & Usage

```bash
# Install dependencies
pip install numpy pandas scipy statsmodels

# Run Sharpe Style Analysis test
python analise_estilo_sharpe.py

# Run Vector Autoregressive (VAR) model test
python modelos_series_temporais.py
```
