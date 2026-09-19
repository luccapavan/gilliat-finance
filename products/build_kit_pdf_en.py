"""
Institutional PDF Builder for the Quantitative Research Syllabus, Leveling Guide & Diagnostic Test (English Edition)
Generates styled HTML and compiles into high-resolution A4 PDF via Chrome/Edge headless.
Author: Lucca Simeoni Pavan, Ph.D.
"""
import os
import sys
from pathlib import Path
import shutil

ROOT_DIR = Path(__file__).resolve().parent.parent
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(str(ROOT_DIR))
from pdf_engine.builder import convert_html_to_pdf

KIT_HTML_TEMPLATE_EN = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Applied Quantitative Research: Official Syllabus, Leveling Guide & Diagnostic Assessment - Lucca Simeoni Pavan, Ph.D.</title>
  <link rel="stylesheet" href="../../pdf_engine/theme.css">
  <style>
    .section-num { color: var(--accent-cyan); font-weight: 700; margin-right: 6px; }
    .toc-item { display: flex; justify-content: space-between; border-bottom: 1px dotted var(--border-light); padding: 5px 0; margin-bottom: 3px; font-size: 9.5pt; }
    .toc-page { font-family: 'JetBrains Mono', monospace; font-weight: 600; color: var(--accent-blue); }
    .formula-box {
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      border-left: 4px solid var(--primary-navy);
      padding: 10px 16px;
      margin: 12px 0;
      border-radius: 4px;
      text-align: center;
    }
    .question-box {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-left: 4px solid var(--accent-blue);
      padding: 12px 16px;
      margin-bottom: 14px;
      border-radius: 4px;
      page-break-inside: avoid;
    }
    .question-title {
      font-weight: 700;
      color: var(--primary-navy);
      font-size: 10.5pt;
      margin-bottom: 6px;
    }
    .question-options {
      margin-left: 10px;
      font-size: 9pt;
      line-height: 1.6;
      color: #334155;
    }
    .answer-box {
      background: #F0FDF4;
      border: 1px solid #BBF7D0;
      border-left: 4px solid #16A34A;
      padding: 10px 14px;
      margin-bottom: 10px;
      border-radius: 4px;
      page-break-inside: avoid;
    }
    .answer-title {
      font-weight: 700;
      color: #166534;
      font-size: 9.5pt;
      margin-bottom: 3px;
    }
    .answer-desc {
      font-size: 8.8pt;
      color: #1E293B;
      line-height: 1.5;
    }
    .module-card {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-left: 4px solid var(--accent-cyan);
      padding: 10px 14px;
      margin-bottom: 12px;
      border-radius: 4px;
      page-break-inside: avoid;
    }
    .module-title {
      font-weight: 700;
      color: var(--primary-navy);
      font-size: 10pt;
      margin-bottom: 4px;
    }
    .module-list {
      margin: 0;
      padding-left: 18px;
      font-size: 8.8pt;
      color: #334155;
      line-height: 1.5;
    }
    mjx-container[jax="SVG"] {
      font-size: 105% !important;
    }
  </style>

  <!-- MathJax Configuration & Vector SVG Engine -->
  <script>
  window.MathJax = {
    tex: {
      inlineMath: [['\\(', '\\)']],
      displayMath: [['$$', '$$'], ['\\[', '\\]']],
      processEscapes: true
    },
    svg: {
      fontCache: 'local'
    }
  };
  </script>
  <script src="../../pdf_engine/mathjax/tex-svg.js"></script>
</head>
<body>

  <!-- ================= COVER PAGE ================= -->
  <div class="cover-page">
    <div class="cover-header">
      <span class="cover-badge">EXCLUSIVE MATERIAL • VIP WAITLIST ENTRANCE KIT</span>
      <div class="cover-title">APPLIED QUANTITATIVE<br>RESEARCH</div>
      <div class="cover-subtitle">Official 30-Hour Syllabus, Technical Leveling Guide in Python & 10-Question Diagnostic Assessment</div>
      <div class="cover-accent-line"></div>
    </div>

    <div style="margin: 20px 0;">
      <div style="font-family: 'JetBrains Mono', monospace; font-size: 8.5pt; color: #94A3B8; line-height: 2.2;">
        <div>▪ PART 1: Official Program Curriculum (30h • 6 Institutional Modules)</div>
        <div>▪ PART 2: Technical Leveling Guide (Return Math, Risk Metrics & Python Code)</div>
        <div>▪ PART 3: Diagnostic Assessment (10 Institutional Questions & Solutions)</div>
        <div>▪ BONUS: Self-Evaluation Scorecard & Career Acceleration Roadmap</div>
      </div>
    </div>

    <div class="cover-footer">
      <p class="author-name">Lucca Simeoni Pavan, Ph.D.</p>
      <p class="author-title">Former Head of Quantitative Strategies & Portfolio Allocation Manager</p>
      <p class="author-desc">Ph.D. in Economics • Specialist in Factor Investing, Time Series, Risk & Asset Allocation</p>
    </div>
  </div>

  <!-- ================= PAGE 2: PRESENTATION AND TOC ================= -->
  <div class="content-wrapper">
    <h1>Institutional Entrance Kit Overview</h1>
    
    <p>Welcome! This document has been structured to serve as a pivotal bridge in your journey into institutional quantitative finance and systematic asset management. It compiles, within a single auditable reference, the complete curriculum and the foundational concepts required for the upcoming formation:</p>

    <div class="callout callout-info" style="margin: 16px 0;">
      <div class="callout-title">💡 3-Part Modular Structure</div>
      <ol style="margin: 5px 0 0 16px; padding: 0; font-size: 9.2pt; line-height: 1.6;">
        <li><strong>Part 1 (Official Syllabus):</strong> Review the complete 30-hour curriculum across 6 specialized modules covering everything from point-in-time data hygiene to FWL partial factor regressions and Hierarchical Risk Parity (HRP).</li>
        <li><strong>Part 2 (Technical Leveling Guide):</strong> Refresh essential time-series foundations: arithmetic vs. logarithmic returns, institutional annualization conventions, and run the attached production-grade Python scorecard script.</li>
        <li><strong>Part 3 (Diagnostic Assessment):</strong> Solve 10 practical multiple-choice questions reflecting standard buy-side technical screens, review full solutions, and diagnose your quantitative readiness.</li>
      </ol>
    </div>

    <h2>Table of Contents</h2>
    <div style="margin: 15px 0;">
      <div class="toc-item"><span><strong>Part 1:</strong> Official Course Syllabus (Program Overview & Modules 1 to 6)</span><span class="toc-page">Page 3</span></div>
      <div class="toc-item"><span><strong>Part 2:</strong> Technical Leveling Guide in Python & Financial Time Series</span><span class="toc-page">Page 5</span></div>
      <div class="toc-item"><span><strong>Part 3:</strong> Diagnostic Assessment (10 Multiple-Choice Institutional Questions)</span><span class="toc-page">Page 7</span></div>
      <div class="toc-item"><span><strong>Solutions & Diagnostics:</strong> Detailed Answer Explanations & Scoring Rubric</span><span class="toc-page">Page 9</span></div>
    </div>

    <div class="page-break"></div>

    <!-- ================= PAGES 3-4: SYLLABUS ================= -->
    <h1><span class="section-num">1.</span> Official Course Curriculum (30 Hours)</h1>
    
    <div style="background: #F1F5F9; padding: 12px 16px; border-radius: 6px; margin-bottom: 16px; font-size: 9pt;">
      <div><strong>Course Title:</strong> Applied Quantitative Research: Systematic Modeling, Factor Investing & Risk Allocation in Python</div>
      <div><strong>Estimated Workload:</strong> 30 hours (Live workshops + Full HD Recordings + Hands-On Python Code Laboratories)</div>
      <div><strong>Technology Stack:</strong> Python 3.10+, Pandas, NumPy, Statsmodels, SciPy, Matplotlib, Seaborn, yfinance</div>
      <div><strong>Core Objective:</strong> Empower quantitative researchers, analysts, economists, and data scientists to construct end-to-end institutional pipelines, from point-in-time data cleaning to bias-free backtesting and robust Ledoit-Wolf / HRP risk parity allocation.</div>
    </div>

    <div class="module-card">
      <div class="module-title">Module 1: Institutional Financial Data Pipelines & Data Hygiene (5 Hours)</div>
      <ul class="module-list">
        <li><strong>Lecture 1.1:</strong> Quantitative pipeline architecture: multidimensional time-series data structures (multi-index DataFrames and panels).</li>
        <li><strong>Lecture 1.2:</strong> Institutional data ingestion: connecting to central bank APIs, regulatory filings, and market exchange feeds.</li>
        <li><strong>Lecture 1.3:</strong> Critical data treatment: cash dividend adjustments, splits, reverse splits, spin-offs, and trading calendar conventions.</li>
        <li><strong>Lecture 1.4:</strong> The invisible hazard: identifying and eradicating survivorship bias and look-ahead bias with Point-in-Time (PIT) lags.</li>
        <li><strong>Hands-On Lab:</strong> Constructing a clean, bias-free historical dataset covering 10+ years of equity trading with timestamp integrity.</li>
      </ul>
    </div>

    <div class="module-card">
      <div class="module-title">Module 2: Return Statistics & Institutional Risk Metrics (5 Hours)</div>
      <ul class="module-list">
        <li><strong>Lecture 2.1:</strong> Simple arithmetic vs. logarithmic returns: mathematical properties and exact modeling applications.</li>
        <li><strong>Lecture 2.2:</strong> Empirical return distributions: non-normality, fat tails, negative skewness, and excess kurtosis.</li>
        <li><strong>Lecture 2.3:</strong> Performance metrics beyond Sharpe: Sortino Ratio (downside semi-variance), Calmar Ratio, and Information Ratio.</li>
        <li><strong>Lecture 2.4:</strong> Drawdown dynamics: analytical computation of Maximum Drawdown (MDD), drawdown duration, and time to recovery.</li>
        <li><strong>Lecture 2.5:</strong> Coherent Tail Risk: Parametric and Historical Value at Risk (VaR 95%) and Conditional VaR (Expected Shortfall / CVaR).</li>
        <li><strong>Hands-On Lab:</strong> Developing an automated module ingesting price feeds and spitting out institutional Risk Tear Sheets.</li>
      </ul>
    </div>

    <div class="module-card">
      <div class="module-title">Module 3: Factor Investing & Multi-Factor Research (5 Hours)</div>
      <ul class="module-list">
        <li><strong>Lecture 3.1:</strong> Evolution of asset pricing theories: From Single-Index CAPM to Fama-French 5 Factors and Carhart.</li>
        <li><strong>Lecture 3.2:</strong> Momentum anomalies: Cross-Sectional Momentum (winners vs losers relative ranking) vs. Time-Series Momentum (trend following).</li>
        <li><strong>Lecture 3.3:</strong> Fundamental factors: Value (Earnings Yield E/P, Book-to-Market) and Quality (ROE, ROIC, Net Margin, Accruals).</li>
        <li><strong>Lecture 3.4:</strong> Risk factors: Low Beta / Low Volatility anomaly and Size (Small-Cap premium).</li>
        <li><strong>Lecture 3.5:</strong> Surviving the "Factor Zoo": t-statistic significance thresholds (t > 2.5), Bonferroni corrections, and out-of-sample testing.</li>
        <li><strong>Hands-On Lab:</strong> Multi-factor ranking engine with cross-sectional Z-Scores generating isolated alpha spreads.</li>
      </ul>
    </div>

    <div class="page-break"></div>

    <div class="module-card">
      <div class="module-title">Module 4: Realistic Institutional Backtesting Framework (5 Hours)</div>
      <ul class="module-list">
        <li><strong>Lecture 4.1:</strong> Backtesting paradigms: Vectorized (fast hypothesis exploration) vs. Event-Driven (precise execution fidelity).</li>
        <li><strong>Lecture 4.2:</strong> Modeling market frictions: exchange fees, clearing fees, borrow rates on short legs, and dividend taxes.</li>
        <li><strong>Lecture 4.3:</strong> Slippage & Market Impact: Average Daily Trading Volume (ADTV) participation limits and Almgren-Chriss square-root impact.</li>
        <li><strong>Lecture 4.4:</strong> Periodic rebalancing: optimal frequencies (weekly, monthly), turnover tolerance bands, and transaction fee drag.</li>
        <li><strong>Lecture 4.5:</strong> Walk-Forward Analysis and Purged & Embargoed Cross-Validation for financial time series without leakage.</li>
        <li><strong>Hands-On Lab:</strong> Running a multi-year backtest of a quantitative factor strategy with complete friction accounting and auditable equity curves.</li>
      </ul>
    </div>

    <div class="module-card">
      <div class="module-title">Module 5: Portfolio Optimization & Risk Allocation (5 Hours)</div>
      <ul class="module-list">
        <li><strong>Lecture 5.1:</strong> Markowitz Mean-Variance Optimization: extreme sensitivity to estimation noise and sample instability.</li>
        <li><strong>Lecture 5.2:</strong> Covariance matrix regularization: Ledoit-Wolf analytical shrinkage and Random Matrix Theory (RMT) eigenvalue cleaning.</li>
        <li><strong>Lecture 5.3:</strong> Risk Parity & Marginal Risk Contributions: ensuring volatile assets do not dominate total portfolio risk budgets.</li>
        <li><strong>Lecture 5.4:</strong> Hierarchical Risk Parity (HRP): unsupervised machine learning tree clustering bypassing matrix inversion entirely.</li>
        <li><strong>Hands-On Lab:</strong> Empirical horse-race benchmark: 1/N vs. Mean-Variance vs. Ledoit-Wolf vs. HRP under practical turnover bounds.</li>
      </ul>
    </div>

    <div class="module-card">
      <div class="module-title">Module 6: Final Capstone & Production Deployment (5 Hours)</div>
      <ul class="module-list">
        <li><strong>Lecture 6.1:</strong> Structuring quantitative Python codebases: modularity, typing, testing, reproducibility, and CI/CD pipelines.</li>
        <li><strong>Lecture 6.2:</strong> Automated executive reporting: generating interactive HTML/PDF risk dashboards for investment committees.</li>
        <li><strong>Capstone Challenge:</strong> Developing a complete proprietary quantitative strategy (ingestion -> factor scoring -> friction-penalized backtest -> risk allocation -> tear sheet) with 1-on-1 code review and grading rubric.</li>
      </ul>
    </div>

    <div class="page-break"></div>

    <!-- ================= PAGES 5-6: LEVELING GUIDE ================= -->
    <h1><span class="section-num">2.</span> Technical Leveling Guide</h1>
    
    <h2>2.1 Simple Returns vs. Logarithmic Returns</h2>
    <p>A foundational premise in quantitative research is the strict mathematical distinction between simple arithmetic and log returns:</p>

    <div class="formula-box">
      $$R_t = \frac{P_t - P_{t-1}}{P_{t-1}} = \frac{P_t}{P_{t-1}} - 1 \quad \text{(Simple Return)}$$
      $$r_t = \ln\left(\frac{P_t}{P_{t-1}}\right) = \ln(P_t) - \ln(P_{t-1}) \quad \text{(Log Return)}$$
    </div>

    <p><strong>The Golden Rules for Quantitative Analysts:</strong></p>
    <ul>
      <li><strong>Additivity in Space (Cross-Section):</strong> Simple returns aggregate linearly across assets. If a portfolio allocates weights \(w_i\), the daily portfolio return is strictly linear: \(R_{p,t} = \sum_{i=1}^N w_i R_{i,t}\). Never sum weighted log returns to calculate portfolio valuation!</li>
      <li><strong>Additivity in Time (Time Series):</strong> Log returns aggregate linearly across time. The multi-period compounded return over \(T\) periods is simply the direct sum: \(r_{total} = \sum_{t=1}^T r_t\). Use log returns for volatility estimation, distribution fitting, and econometric models.</li>
    </ul>

    <h2>2.2 Annualization Conventions (252 Business Days)</h2>
    <p>In global institutional markets, equity volatility and returns follow the standard 252 business days convention:</p>
    <div class="formula-box">
      $$\bar{R}_{annual} = (1 + \bar{R}_{daily})^{252} - 1 \qquad \sigma_{annual} = \sigma_{daily} \times \sqrt{252}$$
    </div>

    <h2>2.3 Institutional Performance & Risk Metrics</h2>
    <ul>
      <li><strong>Sharpe Ratio:</strong> Measures excess return above the risk-free rate (\(R_f\)) per unit of total standard deviation: \(\text{Sharpe} = \frac{\bar{R}_p - R_f}{\sigma_p}\).</li>
      <li><strong>Sortino Ratio:</strong> Penalizes only downside volatility below target or risk-free threshold: \(\text{Sortino} = \frac{\bar{R}_p - R_f}{\sigma_{down}}\). Essential for strategies displaying positive return skewness.</li>
      <li><strong>Maximum Drawdown (MDD):</strong> The worst peak-to-trough drop over the investment horizon: \(MDD = \min_t \left(\frac{NAV_t - \max_{\tau \le t}(NAV_\tau)}{\max_{\tau \le t}(NAV_\tau)}\right)\).</li>
    </ul>

    <h2>2.4 Production Python Leveling Script: Multi-Asset Scorecard</h2>
    <p>Execute the snippet below in your Python 3.10+ environment to compute an institutional scorecard:</p>

    <pre><code>import numpy as np
import pandas as pd
import yfinance as yf

# 1. Ingest dividend- and split-adjusted daily closes
tickers = ['SPY', 'QQQ', 'AAPL', 'NVDA', 'TLT']
data = yf.download(tickers, start='2021-01-01', end='2026-01-01', progress=False)
prices = data['Adj Close'].dropna()
returns = prices.pct_change().dropna()

# 2. Institutional Quantitative Risk Function
def compute_scorecard(series, rf_annual=0.045):
    rf_daily = (1 + rf_annual) ** (1 / 252) - 1
    ann_return = (1 + series.mean()) ** 252 - 1
    ann_vol = series.std() * np.sqrt(252)
    sharpe = (ann_return - rf_annual) / ann_vol if ann_vol > 0 else 0.0
    
    excess_ret = series - rf_daily
    downside_vol = excess_ret[excess_ret < 0].std() * np.sqrt(252)
    sortino = (ann_return - rf_annual) / downside_vol if downside_vol > 0 else 0.0
    
    cum_ret = (1 + series).cumprod()
    mdd = ((cum_ret - cum_ret.cummax()) / cum_ret.cummax()).min()
    
    return pd.Series({
        'Ann. Return': f"{ann_return * 100:.2f}%",
        'Ann. Volatility': f"{ann_vol * 100:.2f}%",
        'Sharpe Ratio': f"{sharpe:.2f}",
        'Sortino Ratio': f"{sortino:.2f}",
        'Max Drawdown': f"{mdd * 100:.2f}%"
    })

print(returns.apply(compute_scorecard).to_string())
</code></pre>

    <div class="page-break"></div>

    <!-- ================= PAGES 7-8: DIAGNOSTIC ASSESSMENT ================= -->
    <h1><span class="section-num">3.</span> Diagnostic Assessment: 10 Institutional Questions</h1>
    <p>Answer the following 10 questions without checking the solutions to evaluate your technical readiness.</p>

    <div class="question-box">
      <div class="question-title">Question 1 • Portfolio Return Mathematics</div>
      <div>When constructing a systematic portfolio allocating 40% in Asset A and 60% in Asset B, which mathematical formulation correctly computes the daily total return of the portfolio?</div>
      <div class="question-options">
        A) The weighted arithmetic average of the logarithmic returns.<br>
        <strong>B) The weighted arithmetic average of the simple arithmetic returns.</strong><br>
        C) The geometric mean of simple returns.<br>
        D) The logarithm of closing prices divided by volume.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Question 2 • Backtest Biases & Microstructure</div>
      <div>A researcher builds a multi-factor strategy that utilizes Q4 financial statements (fiscal period ending Dec 31) to rebalance stock holdings on the first trading session of January. What fatal quantitative error has occurred?</div>
      <div class="question-options">
        A) Survivorship bias due to delisted companies.<br>
        <strong>B) Look-ahead bias, because audited annual 10-K financial statements are filed and publicized months later in March or April.</strong><br>
        C) Specification error by using calendar days instead of trading days.<br>
        D) Convexity bias in volatility annualization.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Question 3 • Python / Pandas Vectorization</div>
      <div>Given a date-indexed pandas DataFrame <code>df</code> containing adjusted prices in column <code>'close'</code>, which statement correctly computes daily simple arithmetic returns while preserving chronological alignment?</div>
      <div class="question-options">
        A) <code>df['close'].diff() / df['close']</code><br>
        B) <code>np.log(df['close']) - np.log(df['close'].shift(-1))</code><br>
        <strong>C) <code>df['close'].pct_change().dropna()</code></strong><br>
        D) <code>df['close'].rolling(252).mean()</code>
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Question 4 • Volatility Annualization Standards</div>
      <div>An equity asset displays a daily return standard deviation of 2.0% in a market with 252 business days. Under the standard assumption of independent and identically distributed (i.i.d.) returns, what is its annualized volatility?</div>
      <div class="question-options">
        A) \(2.0\% \times 252 = 504.0\%\)<br>
        <strong>B) \(2.0\% \times \sqrt{252} \approx 31.75\%\)</strong><br>
        C) \(2.0\% / \sqrt{252} \approx 0.126\%\)<br>
        D) \((1 + 0.02)^{252} - 1 \approx 145.2\%\)
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Question 5 • Asymmetric Risk Metrics</div>
      <div>Why do institutional quantitative managers frequently favor the <strong>Sortino Ratio</strong> over the <strong>Sharpe Ratio</strong> for strategies characterized by positive return skewness?</div>
      <div class="question-options">
        A) The Sortino Ratio ignores the risk-free rate entirely.<br>
        <strong>B) The Sharpe Ratio penalizes upside return spikes identically to catastrophic drawdowns, whereas Sortino penalizes only downside volatility.</strong><br>
        C) The Sortino Ratio is independent of sample size.<br>
        D) The Sharpe Ratio cannot be calculated when returns are non-negative.
      </div>
    </div>

    <div class="page-break"></div>

    <div class="question-box">
      <div class="question-title">Question 6 • Time-Series Cross-Validation</div>
      <div>Why is the direct application of standard Scikit-Learn <em>K-Fold Cross-Validation</em> considered invalid and dangerously misleading for financial asset pricing models?</div>
      <div class="question-options">
        <strong>A) Because standard K-Fold shuffles observations and trains on future data to predict the past, introducing severe temporal data leakage and autocorrelation contamination.</strong><br>
        B) Because K-Fold is computationally restricted to binary classification tasks only.<br>
        C) Because the number of folds must match the number of assets in the universe.<br>
        D) Because K-Fold artificially doubles transaction fee estimates.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Question 7 • Factor Modeling Paradigms</div>
      <div>What is the core distinction between a <strong>Cross-Sectional Momentum</strong> strategy and a <strong>Time-Series Momentum (Trend Following)</strong> strategy?</div>
      <div class="question-options">
        A) Cross-Sectional is applied to fixed income and Time-Series is applied to equities.<br>
        <strong>B) Cross-Sectional ranks assets relative to one another at a given timestamp (buying top decile, shorting bottom decile), while Time-Series evaluates each asset's own historical return trajectory against its own history in absolute terms.</strong><br>
        C) Cross-Sectional uses single moving averages while Time-Series uses multiple regressions.<br>
        D) Both terms are synonymous in empirical asset pricing literature.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Question 8 • Microstructure Frictions & Execution Slippage</div>
      <div>When backtesting a systematic small-cap strategy with $20M in AUM, which parameter is crucial to prevent the model from capturing illusory alpha on illiquid names that cannot be executed in live trading?</div>
      <div class="question-options">
        A) Consumer Price Index (CPI) inflation lags.<br>
        <strong>B) Average Daily Trading Volume (ADTV) participation limits (e.g. max 5-10% of ADTV) and nonlinear market impact / slippage models.</strong><br>
        C) Social media follower count of listed management.<br>
        D) Book-to-market ratio divided by the number of shares outstanding.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Question 9 • Covariance Estimation & Markowitz Optimization</div>
      <div>What is the central empirical drawback of traditional Markowitz Mean-Variance Optimization when applied directly to sample covariance matrices across dozens of assets?</div>
      <div class="question-options">
        A) The algorithm is unable to process positive returns.<br>
        <strong>B) Inverting an ill-conditioned sample covariance matrix acts as an "estimation error maximizer", concentrating extreme, unstable weights on noisy assets; a flaw solved by Ledoit-Wolf shrinkage.</strong><br>
        C) Markowitz requires that all portfolio returns be zero.<br>
        D) The solver requires unconstrained shorting in all scenarios.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Question 10 • Hierarchical Risk Parity (HRP)</div>
      <div>What breakthrough did Marcos López de Prado's <strong>Hierarchical Risk Parity (HRP)</strong> algorithm introduce to institutional portfolio construction?</div>
      <div class="question-options">
        <strong>A) It uses machine learning unsupervised tree clustering on the correlation matrix to allocate risk recursively, completely bypassing covariance matrix inversion and eliminating numerical instability.</strong><br>
        B) It guarantees 0% drawdown across all market regimes.<br>
        C) It replaces mathematical solvers with natural language processing.<br>
        D) It optimizes option strike prices for high-frequency trading.
      </div>
    </div>

    <div class="page-break"></div>

    <!-- ================= PAGES 9-10: SOLUTIONS & DIAGNOSTICS ================= -->
    <h1><span class="section-num">4.</span> Official Solutions & Scoring Rubric</h1>
    
    <div class="answer-box">
      <div class="answer-title">Question 1 • Correct Answer: B</div>
      <div class="answer-desc">Cross-sectional aggregation of multiple assets obeys linear addition of simple arithmetic returns: \(R_{p,t} = \sum w_i R_{i,t}\). Summing weighted logarithmic returns produces mathematically invalid portfolio valuations.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Question 2 • Correct Answer: B</div>
      <div class="answer-desc">Annual financial statements (10-K) are published 60 to 90 days after fiscal year end. Utilizing year-end figures on Jan 1 is pure lookahead bias, invalidating the historical backtest.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Question 3 • Correct Answer: C</div>
      <div class="answer-desc">The <code>.pct_change()</code> method is the native, vector-optimized pandas implementation of \(\frac{P_t - P_{t-1}}{P_{t-1}}\).</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Question 4 • Correct Answer: B</div>
      <div class="answer-desc">Under the i.i.d. assumption, return variance scales linearly with time \(T\), meaning standard deviation scales with the <strong>square root of time</strong>: \(\sigma_{ann} = 2.0\% \times \sqrt{252} \approx 31.75\%\).</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Question 5 • Correct Answer: B</div>
      <div class="answer-desc">The standard Sharpe ratio penalizes upside volatility as risk. The Sortino ratio substitutes the denominator with downside semi-deviation, rewarding asymmetric upside strategies.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Question 6 • Correct Answer: A</div>
      <div class="answer-desc">Financial time series exhibit sequential temporal dependence and autocorrelation. Standard K-fold shuffles future data into training folds, causing catastrophic information leakage. Purged walk-forward cross-validation is mandatory.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Question 7 • Correct Answer: B</div>
      <div class="answer-desc">Cross-sectional momentum produces relative asset rankings at a single snapshot in time. Time-series momentum evaluates an individual asset's own trend across time in absolute terms.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Question 8 • Correct Answer: B</div>
      <div class="answer-desc">Without volume participation limits (e.g., capping trading at 10% of ADTV) and nonlinear market impact models (Almgren-Chriss / Kyle's lambda), small-cap strategy alphas evaporate under real-world order execution.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Question 9 • Correct Answer: B</div>
      <div class="answer-desc">Inverting sample covariance matrices with high asset dimensionality amplifies random noise. Ledoit-Wolf shrinkage shrinks the noisy sample covariance toward a structured target, yielding robust, stable asset weights.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Question 10 • Correct Answer: A</div>
      <div class="answer-desc">Hierarchical Risk Parity (HRP) structures assets into a dendrogram via machine learning hierarchical clustering, allocating risk recursively along clusters without inverting matrices, conferring stability during structural regime shifts.</div>
    </div>

    <h2>Diagnostic Scoring & Recommended Focus</h2>
    <table style="width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 8.8pt;">
      <thead>
        <tr style="background: var(--primary-navy); color: white;">
          <th style="padding: 8px; text-align: left; width: 25%;">Score</th>
          <th style="padding: 8px; text-align: left; width: 35%;">Institutional Diagnostic Level</th>
          <th style="padding: 8px; text-align: left; width: 40%;">Recommended Program Focus</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background: #F8FAFC; border-bottom: 1px solid #E2E8F0;">
          <td style="padding: 8px; font-weight: 700; color: #DC2626;">0 to 4 Correct</td>
          <td style="padding: 8px;"><strong>Level 1: Foundations / In Transition</strong><br>Analytical background, but common habits from generic Data Science or manual spreadsheets.</td>
          <td style="padding: 8px;"><strong>Modules 1 & 2</strong> will be transformative for building uncompromised data pipelines, bias-free series, and tail metrics.</td>
        </tr>
        <tr style="background: #FFFFFF; border-bottom: 1px solid #E2E8F0;">
          <td style="padding: 8px; font-weight: 700; color: #D97706;">5 to 7 Correct</td>
          <td style="padding: 8px;"><strong>Level 2: Intermediate Quant Analyst</strong><br>Solid Python syntax and basic stats, with gaps in friction modeling and multi-factor isolation.</td>
          <td style="padding: 8px;"><strong>Modules 3 & 4</strong> will elevate your backtesting to buy-side desk standards (FWL partialing, slippage, and factor spreads).</td>
        </tr>
        <tr style="background: #F0FDF4;">
          <td style="padding: 8px; font-weight: 700; color: #16A34A;">8 to 10 Correct</td>
          <td style="padding: 8px;"><strong>Level 3: Quant Desk Ready</strong><br>Strong conceptual maturity and sharpened intuition for microstructure and risk budgeting.</td>
          <td style="padding: 8px;"><strong>Modules 4, 5 & 6</strong> will solidify your mastery of Ledoit-Wolf, HRP allocators, and production-grade take-home challenges.</td>
        </tr>
      </tbody>
    </table>

    <div class="callout callout-info" style="margin-top: 18px;">
      <div class="callout-title">🔒 Exclusive VIP Waitlist Advantage</div>
      By submitting your details on the official landing page, you have secured your priority spot for the 1st Cohort of the <strong>Applied Quantitative Research Program</strong> with an <strong>exclusive 20% launch discount</strong> and direct code review mentoring sessions with Dr. Lucca Simeoni Pavan.
    </div>

  </div>

</body>
</html>
"""

def main():
    print("=" * 60)
    print("🚀 Institutional English Entrance Kit PDF Generator")
    print("=" * 60)
    
    html_prod = ROOT_DIR / "products" / "kit_quant_research_syllabus_leveling_guide_en.html"
    html_down = ROOT_DIR / "landing_pages" / "downloads" / "kit_quant_research_syllabus_leveling_guide_en.html"
    
    html_prod.write_text(KIT_HTML_TEMPLATE_EN, encoding="utf-8")
    html_down.write_text(KIT_HTML_TEMPLATE_EN, encoding="utf-8")
    print("✅ HTML written to products/ and landing_pages/downloads/")
    
    pdf_prod = ROOT_DIR / "products" / "Kit_Quant_Research_Syllabus_Leveling_Guide_EN.pdf"
    pdf_down = ROOT_DIR / "landing_pages" / "downloads" / "Kit_Quant_Research_Syllabus_Leveling_Guide_EN.pdf"
    
    print("⏳ Converting HTML to high-resolution PDF via headless browser...")
    success = convert_html_to_pdf(str(html_prod), str(pdf_prod))
    
    if success and pdf_prod.exists():
        size_kb = pdf_prod.stat().st_size / 1024
        print(f"✅ English PDF generated successfully! Size: {size_kb:.1f} KB")
        shutil.copy2(str(pdf_prod), str(pdf_down))
        print(f"✅ English PDF copied to landing_pages/downloads/Kit_Quant_Research_Syllabus_Leveling_Guide_EN.pdf")
    else:
        print("❌ Failed to compile PDF.")

if __name__ == "__main__":
    main()
