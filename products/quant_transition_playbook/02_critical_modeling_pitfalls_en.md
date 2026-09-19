# Module 2: Critical Modeling & Backtesting Pitfalls

In quantitative finance, Ronald Coase's famous adage is a daily operational reality: *"If you torture the data long enough, it will confess to anything"*. The vast majority of backtests fail in production because researchers unwittingly fool themselves during the testing process.

---

## 1. Look-Ahead Bias
Occurs when information from the future leaks into historical decision points.
* **Classic Factor Investing Example:** Using quarterly financial statement numbers on the exact calendar quarter end (e.g. March 31). In reality, audited corporate 10-Q/10-K filings are only publicized 30 to 60 days later.
* **How to Mitigate:**
  * Enforce strict timestamp filtering on *publication timestamps* (`filing_date`) rather than fiscal *period end dates* (`reference_date`).
  * When computing trading returns, decisions made at timestamp $t$ (e.g. today's close) must only be executed at timestamp $t+1$ open (`shift(1)` rule).

---

## 2. Survivorship Bias
Occurs when historical backtest universes consist exclusively of entities that survived until today.
* **Impact:** If you backtest an equity strategy from 2010 to 2026 using today's index constituents, you have retroactively deleted every single company that went bankrupt, faced delisting, or plummeted 95%. Apparent strategy Sharpe ratios are artificially inflated by orders of magnitude.
* **How to Mitigate:**
  * Utilize Point-in-Time reconstituting datasets that preserve complete historical constituent rosters, including liquidated and delisted tickers.

---

## 3. Real-World Execution Frictions & Market Microstructure
A frictionless backtest is pure fiction. In live markets, every trade incurs operational drag:
1. **Exchange Fees & Commissions:** Trading and clearing levies.
2. **Bid-Ask Spread:** Crossing the spread in low-liquidity names rapidly erodes theoretical alpha.
3. **Borrow Rates (Short Financing Fees):** In long-short strategies, short positions incur continuous stock loan fees.
4. **Non-Linear Market Impact:** Institutional order sizes push market prices adversely against execution (Almgren-Chriss square-root impact).

---

## 4. Cross-Validation: Why Standard K-Fold is Dangerous
In standard machine learning, datasets are randomly shuffled into $K$ folds. **In financial time series, random shuffling is strictly forbidden**, as it trains models on future bars to forecast the past, creating catastrophic information leakage.

### The Institutional Standard: Purged & Embargoed Cross-Validation
1. **Purging:** Removes training observations whose return outcome window overlaps with test fold intervals.
2. **Embargo:** Inserts an operational cooling-off buffer immediately following test sets to prevent autoregressive memory from bleeding into subsequent training folds.
