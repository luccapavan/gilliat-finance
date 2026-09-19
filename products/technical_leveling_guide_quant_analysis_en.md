# Technical Leveling Guide: Python & Financial Mathematics for Quantitative Analysis

**Exclusive Material for VIP Waitlist Applicants**  
**Author:** Lucca Simeoni Pavan, Ph.D.  
*Former Head of Quantitative Strategies & Portfolio Allocation Manager • Ph.D. in Economics*

---

## 🎯 Purpose of this Guide
Welcome! This guide ensures you enter the **Applied Quantitative Research Program** with the exact mathematical, statistical, and programming foundations required by institutional quantitative desks.

Here you will master the concepts that separate amateurs relying on disconnected spreadsheets from professionals engineering robust quantitative models in Python.

---

## 1. Environment Setup

For research and production quantitative analysis, we recommend:
1. **Python 3.10+:** Industry standard for scientific and econometric libraries.
2. **VS Code with Jupyter Extension:** Fast prototyping and clean modular development.
3. **Dedicated Virtual Environment:**
   ```bash
   python -m venv venv_quant
   # On Windows (PowerShell):
   .\venv_quant\Scripts\Activate.ps1
   # On macOS/Linux:
   source venv_quant/bin/activate
   ```
4. **Required Libraries:**
   ```bash
   pip install numpy pandas matplotlib seaborn scipy statsmodels yfinance
   ```

---

## 2. The Mathematics of Financial Returns

### 2.1 Simple Arithmetic Return
Measures percentage price change between period $t-1$ and $t$:
$$R_t = \frac{P_t - P_{t-1}}{P_{t-1}} = \frac{P_t}{P_{t-1}} - 1$$

* **Core Property:** Linearity across assets in space (cross-section). In a portfolio with weights $w_i$:
$$R_{p, t} = \sum_{i=1}^N w_i R_{i, t}$$

### 2.2 Logarithmic Return (Continuously Compounded)
Defined as the difference between natural logarithms:
$$r_t = \ln\left(\frac{P_t}{P_{t-1}}\right) = \ln(P_t) - \ln(P_{t-1})$$

* **Core Property:** Linearity across time (time series). Total compounded return is the direct sum:
$$r_{total} = \sum_{t=1}^{T} r_t$$

> **The Golden Rule for Quants:**  
> • Use **simple returns** for portfolio NAV accounting, weighting, and performance attribution.  
> • Use **log returns** for econometric regressions, volatility forecasting, and distribution fitting.

---

## 3. Essential Risk & Performance Metrics

### 3.1 Annualization Standards (252 Business Days)
$$\bar{R}_{annual} = (1 + \bar{R}_{daily})^{252} - 1 \qquad \sigma_{annual} = \sigma_{daily} \times \sqrt{252}$$

### 3.2 Sharpe Ratio vs Sortino Ratio
* **Sharpe:** $\frac{\bar{R}_p - R_f}{\sigma_p}$ (penalizes upside and downside volatility equally).
* **Sortino:** $\frac{\bar{R}_p - R_f}{\sigma_{down}}$ (penalizes only downside semi-variance below risk-free benchmark).

### 3.3 Maximum Drawdown (MDD)
$$MDD = \min_t \left(\frac{\text{NAV}_t - \max_{\tau \le t}(\text{NAV}_\tau)}{\max_{\tau \le t}(\text{NAV}_\tau)}\right)$$

---

## 4. Production Python Scorecard Snippet

```python
import numpy as np
import pandas as pd
import yfinance as yf

# Ingest multi-asset universe
tickers = ['SPY', 'QQQ', 'AAPL', 'NVDA', 'TLT']
data = yf.download(tickers, start='2021-01-01', end='2026-01-01', progress=False)
prices = data['Adj Close'].dropna()
returns = prices.pct_change().dropna()

def compute_metrics(s, rf=0.045):
    rf_d = (1 + rf) ** (1/252) - 1
    r_ann = (1 + s.mean()) ** 252 - 1
    vol_ann = s.std() * np.sqrt(252)
    sharpe = (r_ann - rf) / vol_ann if vol_ann > 0 else 0
    down = s[s - rf_d < 0].std() * np.sqrt(252)
    sortino = (r_ann - rf) / down if down > 0 else 0
    cum = (1 + s).cumprod()
    mdd = ((cum - cum.cummax()) / cum.cummax()).min()
    return pd.Series({
        'Return': f"{r_ann*100:.2f}%",
        'Vol': f"{vol_ann*100:.2f}%",
        'Sharpe': f"{sharpe:.2f}",
        'Sortino': f"{sortino:.2f}",
        'MDD': f"{mdd*100:.2f}%"
    })

print(returns.apply(compute_metrics).to_string())
```
