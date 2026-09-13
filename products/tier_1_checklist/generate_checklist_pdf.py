"""
Gerador dos PDFs do Produto Tier 1 (PT e EN):
Checklist Anti-Vieses & Auditoria de Backtest
Preço: R$ 5,99 (Eduzz) / $5.99 USD (Gumroad)
Autor: Lucca Simeoni Pavan, Ph.D.
"""
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR))

from pdf_engine.builder import convert_html_to_pdf

HTML_PT = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Checklist Anti-Vieses & Auditoria de Backtest</title>
<style>
  @page {
    size: A4;
    margin: 18mm 15mm 18mm 15mm;
    @bottom-right {
      content: counter(page);
      font-family: 'Helvetica Neue', Arial, sans-serif;
      font-size: 8pt;
      color: #718096;
    }
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1a202c;
    line-height: 1.45;
    font-size: 9.5pt;
    margin: 0;
    padding: 0;
  }
  .header {
    border-bottom: 2px solid #2b6cb0;
    padding-bottom: 10px;
    margin-bottom: 16px;
  }
  .tag {
    display: inline-block;
    background: #ebf8ff;
    color: #2b6cb0;
    font-weight: 700;
    font-size: 8pt;
    padding: 2px 7px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  h1 {
    font-size: 16pt;
    color: #1a365d;
    margin: 6px 0 3px 0;
    font-weight: 800;
  }
  .subtitle {
    color: #4a5568;
    font-size: 9.5pt;
    margin: 0;
  }
  .author {
    color: #718096;
    font-size: 8pt;
    margin-top: 3px;
  }
  .box {
    background: #f7fafc;
    border-left: 4px solid #3182ce;
    padding: 10px 14px;
    margin-bottom: 14px;
    border-radius: 0 6px 6px 0;
  }
  .box-title {
    font-weight: 700;
    color: #2c5282;
    font-size: 10.5pt;
    margin-bottom: 6px;
  }
  .item {
    margin-bottom: 8px;
  }
  .item-title {
    font-weight: 700;
    color: #1a202c;
  }
  .item-desc {
    color: #4a5568;
    font-size: 8.8pt;
    margin: 2px 0 0 0;
  }
  .code-inline {
    background: #edf2f7;
    padding: 1px 4px;
    border-radius: 3px;
    font-family: "Courier New", monospace;
    font-size: 8.2pt;
    color: #c53030;
  }
  .page-break {
    page-break-before: always;
  }
  .footer-note {
    background: #edf2f7;
    padding: 10px;
    border-radius: 6px;
    font-size: 8.5pt;
    color: #4a5568;
    margin-top: 15px;
    text-align: center;
  }
</style>
</head>
<body>

<div class="header">
  <span class="tag">Guia de Bolso Institucional • Tier 1</span>
  <h1>Checklist de Auditoria Anti-Vieses em Backtesting</h1>
  <p class="subtitle">Os 10 pontos críticos que separam modelos lucrativos de backtests ficcionais eliminados em entrevistas quant</p>
  <p class="author">Por Lucca Simeoni Pavan, Ph.D. • Ex-Head de Estratégias Quant & Gerente de Alocação</p>
</div>

<div class="box">
  <div class="box-title">⚡ Pilar 1: Integridade Temporal & Eliminação de Look-Ahead Bias</div>
  
  <div class="item">
    <div class="item-title">1. Lag Obrigatório de Execução de Ordens</div>
    <p class="item-desc">Se os pesos da carteira são calculados no fechamento do dia <span class="code-inline">t</span>, a execução só ocorre no dia <span class="code-inline">t+1</span>. Sempre aplique <span class="code-inline">exec_weights = target_weights.shift(1)</span>. Calcular retornos no dia <span class="code-inline">t</span> usando pesos do dia <span class="code-inline">t</span> é eliminação sumária em testes técnicos.</p>
  </div>

  <div class="item">
    <div class="item-title">2. Ponto no Tempo (Point-in-Time Data) para Balanços</div>
    <p class="item-desc">Demonstrações contábeis e múltiplos (P/L, P/VP, ROE) possuem defasagem entre o fechamento contábil do trimestre e a publicação oficial na CVM/SEC. Nunca use a data do balanço; utilize estritamente a data oficial de divulgação pública (<span class="code-inline">filing_date</span>).</p>
  </div>

  <div class="item">
    <div class="item-title">3. Padronização Transversal Estrita (Cross-Sectional Z-Score)</div>
    <p class="item-desc">Ao normalizar indicadores, nunca use a média e desvio padrão de todo o período temporal (isso vaza o futuro). A padronização deve ser transversal para cada data: <span class="code-inline">df.sub(df.mean(axis=1), axis=0).div(df.std(axis=1), axis=0)</span>.</p>
  </div>
</div>

<div class="box">
  <div class="box-title">🛡️ Pilar 2: Microestrutura Real & Fricções Operacionais</div>

  <div class="item">
    <div class="item-title">4. Slippage Não-Linear e Lei da Raiz Quadrada</div>
    <p class="item-desc">Assumir execução no preço de fechamento ou spread fixo é irrealista na B3. O impacto de mercado obedece à relação côncava: <span class="code-inline">Impacto ≈ Y * Vol_Diária * sqrt(Q / ADV)</span>. Se a estratégia opera ativos com baixo volume diário (ADV), o alfa teórico será devorado pelo spread.</p>
  </div>

  <div class="item">
    <div class="item-title">5. Custo de Giro (Turnover Friction) & Corretagem</div>
    <p class="item-desc">Uma estratégia que gira 60% da carteira por mês precisa superar custos fixos de corretagem, emolumentos B3 e spread. Desconte no mínimo 15 bps (0,15%) por ponta negociada no backtester.</p>
  </div>

  <div class="item">
    <div class="item-title">6. Custo de Aluguel de Ações (BTC) na Ponta Vendida</div>
    <p class="item-desc">Em estratégias Long & Short ou Market Neutral, o custo do empréstimo de ações (tomador) pode variar de 2% a mais de 15% ao ano em ativos disputados. Ignorar o custo de BTC no backtest infla o retorno da ponta vendida.</p>
  </div>
</div>

<div class="page-break"></div>

<div class="box">
  <div class="box-title">📊 Pilar 3: Robustez Estatística & Prevenção ao p-Hacking</div>

  <div class="item">
    <div class="item-title">7. Eliminação do Viés de Sobrevivência (Survivorship Bias)</div>
    <p class="item-desc">Nunca monte seu universo histórico de teste usando a composição atual do índice Ibovespa ou IBrX. É obrigatório incluir as ações que foram deslistadas, faliram ou sofreram fusões durante a janela de teste.</p>
  </div>

  <div class="item">
    <div class="item-title">8. Validação Cruzada Purged K-Fold com Quarentena (Embargo)</div>
    <p class="item-desc">Em séries financeiras com memória serial, o K-Fold tradicional é proibido porque vaza dependência temporal entre treino e teste. Use K-Fold Purged e aplique um embargo temporal de alguns dias entre as janelas de calibração.</p>
  </div>

  <div class="item">
    <div class="item-title">9. Ajuste por Múltiplos Testes (Deflated Sharpe Ratio - DSR)</div>
    <p class="item-desc">Se você testou 2.000 combinações de parâmetros para encontrar um Sharpe de 2.0, o Teorema de Valores Extremos garante que seu resultado é mero ruído aleatório. Desconte o Sharpe observado pelo número total de tentativas e assimetria dos retornos.</p>
  </div>

  <div class="item">
    <div class="item-title">10. Risco de Cauda além do VaR (CVaR / Expected Shortfall)</div>
    <p class="item-desc">O VaR a 95% é cego para a severidade das perdas no dia em que a linha é cruzada. O comitê de risco institucional exige a média das perdas extremas: <span class="code-inline">CVaR_95 = E[R | R <= VaR_95]</span>.</p>
  </div>
</div>

<div class="footer-note">
  <strong>Precisa dos códigos em Python prontos para rodar e do Dossiê Completo?</strong><br>
  Conheça o <em>The Institutional Quant Toolkit & Playbook</em> com 4 motores completos em Python vetorizado:<br>
  👉 <a href="https://chk.eduzz.com/7sfhtm2a" style="color: #2b6cb0; font-weight: bold;">https://chk.eduzz.com/7sfhtm2a</a>
</div>

</body>
</html>
"""

HTML_EN = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Anti-Bias Backtesting Audit Checklist</title>
<style>
  @page {
    size: A4;
    margin: 18mm 15mm 18mm 15mm;
    @bottom-right {
      content: counter(page);
      font-family: 'Helvetica Neue', Arial, sans-serif;
      font-size: 8pt;
      color: #718096;
    }
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1a202c;
    line-height: 1.45;
    font-size: 9.5pt;
    margin: 0;
    padding: 0;
  }
  .header {
    border-bottom: 2px solid #2b6cb0;
    padding-bottom: 10px;
    margin-bottom: 16px;
  }
  .tag {
    display: inline-block;
    background: #ebf8ff;
    color: #2b6cb0;
    font-weight: 700;
    font-size: 8pt;
    padding: 2px 7px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  h1 {
    font-size: 16pt;
    color: #1a365d;
    margin: 6px 0 3px 0;
    font-weight: 800;
  }
  .subtitle {
    color: #4a5568;
    font-size: 9.5pt;
    margin: 0;
  }
  .author {
    color: #718096;
    font-size: 8pt;
    margin-top: 3px;
  }
  .box {
    background: #f7fafc;
    border-left: 4px solid #3182ce;
    padding: 10px 14px;
    margin-bottom: 14px;
    border-radius: 0 6px 6px 0;
  }
  .box-title {
    font-weight: 700;
    color: #2c5282;
    font-size: 10.5pt;
    margin-bottom: 6px;
  }
  .item {
    margin-bottom: 8px;
  }
  .item-title {
    font-weight: 700;
    color: #1a202c;
  }
  .item-desc {
    color: #4a5568;
    font-size: 8.8pt;
    margin: 2px 0 0 0;
  }
  .code-inline {
    background: #edf2f7;
    padding: 1px 4px;
    border-radius: 3px;
    font-family: "Courier New", monospace;
    font-size: 8.2pt;
    color: #c53030;
  }
  .page-break {
    page-break-before: always;
  }
  .footer-note {
    background: #edf2f7;
    padding: 10px;
    border-radius: 6px;
    font-size: 8.5pt;
    color: #4a5568;
    margin-top: 15px;
    text-align: center;
  }
</style>
</head>
<body>

<div class="header">
  <span class="tag">Institutional Pocket Guide • Tier 1</span>
  <h1>Anti-Bias Backtesting Audit Checklist</h1>
  <p class="subtitle">The 10 critical operational checkpoints separating production alpha from rejected take-home submissions</p>
  <p class="author">By Lucca Simeoni Pavan, Ph.D. • Former Head of Quantitative Strategies & Asset Allocation Manager</p>
</div>

<div class="box">
  <div class="box-title">⚡ Pillar 1: Temporal Integrity & Look-Ahead Elimination</div>
  
  <div class="item">
    <div class="item-title">1. Mandatory Order Execution Lag</div>
    <p class="item-desc">Portfolio weights computed at close <span class="code-inline">t</span> execute at <span class="code-inline">t+1</span>. Always enforce <span class="code-inline">exec_weights = target_weights.shift(1)</span>. Evaluating same-day returns with same-day weights causes instant disqualification on institutional desks.</p>
  </div>

  <div class="item">
    <div class="item-title">2. Point-in-Time Accounting Data</div>
    <p class="item-desc">Quarterly financial statements experience substantial latency between quarter-end and public release. Never index by fiscal period end date; strictly anchor to official public disclosure timestamps (<span class="code-inline">filing_date</span>).</p>
  </div>

  <div class="item">
    <div class="item-title">3. Cross-Sectional Z-Score Standardization</div>
    <p class="item-desc">Never standardize factor scores using full-sample means or standard deviations across time. Normalization must be strictly cross-sectional per date: <span class="code-inline">df.sub(df.mean(axis=1), axis=0).div(df.std(axis=1), axis=0)</span>.</p>
  </div>
</div>

<div class="box">
  <div class="box-title">🛡️ Pillar 2: Microstructure Realism & Execution Frictions</div>

  <div class="item">
    <div class="item-title">4. Non-Linear Slippage & Square-Root Law</div>
    <p class="item-desc">Assuming instantaneous fills at midpoint is financial fiction. Institutional market impact scales concavely: <span class="code-inline">Impact ≈ Y * Daily_Vol * sqrt(Q / ADV)</span>. Trading illiquid names erodes 100% of theoretical alpha.</p>
  </div>

  <div class="item">
    <div class="item-title">5. Turnover Friction & Exchange Fees</div>
    <p class="item-desc">High-turnover models must clear brokerage, exchange tariffs, and bid-ask spreads. Deduct a minimum of 15 bps (0.15%) per traded leg in simulation engines.</p>
  </div>

  <div class="item">
    <div class="item-title">6. Borrow Rates on Short Legs</div>
    <p class="item-desc">Market-neutral and long/short equity models require active stock borrowing. Borrow rates often range from 2% to 15%+ on hard-to-borrow stocks. Omitting borrow costs severely overstates short alpha.</p>
  </div>
</div>

<div class="page-break"></div>

<div class="box">
  <div class="box-title">📊 Pillar 3: Statistical Hygiene & p-Hacking Prevention</div>

  <div class="item">
    <div class="item-title">7. Survivorship Bias Elimination</div>
    <p class="item-desc">Never construct historical universes using current index constituents. Delisted, liquidated, and acquired entities must be systematically retained throughout historical windows.</p>
  </div>

  <div class="item">
    <div class="item-title">8. Purged & Embargoed K-Fold Cross-Validation</div>
    <p class="item-desc">Standard K-Fold is invalid on autocorrelated financial time series due to label overlap. Use Purged K-Fold with an explicit multi-day embargo quarantine between train and test splits.</p>
  </div>

  <div class="item">
    <div class="item-title">9. Multiple Testing Deflated Sharpe Ratio (DSR)</div>
    <p class="item-desc">If you screened 2,000 parameter permutations, Extreme Value Theory ensures the top Sharpe ratio is pure noise. Deflate observed Sharpe by total trials and return non-normality.</p>
  </div>

  <div class="item">
    <div class="item-title">10. Coherent Tail Risk (CVaR / Expected Shortfall)</div>
    <p class="item-desc">95% VaR is oblivious to the severity of catastrophic drawdowns beyond the cutoff. Institutional risk committees demand Conditional VaR: <span class="code-inline">CVaR_95 = E[R | R <= VaR_95]</span>.</p>
  </div>
</div>

<div class="footer-note">
  <strong>Looking for production-grade Python engines and the Complete Dossier?</strong><br>
  Explore <em>The Institutional Quant Toolkit & Playbook</em> with 4 vectorized Python engines:<br>
  👉 <a href="https://warrenjax.gumroad.com/l/fsrcmj" style="color: #2b6cb0; font-weight: bold;">https://warrenjax.gumroad.com/l/fsrcmj</a>
</div>

</body>
</html>
"""

def generate():
    out_dir = ROOT_DIR / "products"
    
    # PT
    html_pt = ROOT_DIR / "products" / "tier_1_checklist" / "checklist_pt.html"
    html_pt.write_text(HTML_PT, encoding="utf-8")
    pdf_pt = out_dir / "Quant_Anti_Bias_Checklist_PT.pdf"
    ok_pt = convert_html_to_pdf(str(html_pt), str(pdf_pt))
    if ok_pt:
        print(f"[OK] PDF Tier 1 (PT) gerado: {pdf_pt.name} ({pdf_pt.stat().st_size / 1024:.1f} KB)")
        
    # EN
    html_en = ROOT_DIR / "products" / "tier_1_checklist" / "checklist_en.html"
    html_en.write_text(HTML_EN, encoding="utf-8")
    pdf_en = out_dir / "Quant_Anti_Bias_Checklist_EN.pdf"
    ok_en = convert_html_to_pdf(str(html_en), str(pdf_en))
    if ok_en:
        print(f"[OK] PDF Tier 1 (EN) gerado: {pdf_en.name} ({pdf_en.stat().st_size / 1024:.1f} KB)")

if __name__ == "__main__":
    generate()
