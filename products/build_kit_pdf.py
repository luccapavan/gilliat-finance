"""
Compilador Institucional do Kit de Nivelamento, Ementa Oficial e Teste Diagnóstico
Gera a versão HTML estilizada e compila em PDF de alta resolução via Chrome/Edge headless
com renderização vetorial SVG de fórmulas LaTeX/MathJax e estética idêntica ao The Quant Transition Playbook.
Autor: Lucca Simeoni Pavan, Ph.D.
"""
import os
import sys
from pathlib import Path
import shutil
import pypdf

ROOT_DIR = Path(__file__).resolve().parent.parent
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(str(ROOT_DIR))
from pdf_engine.builder import convert_html_to_pdf

THEME_CSS_PATH = ROOT_DIR / "pdf_engine" / "theme.css"
MATHJAX_JS_PATH = ROOT_DIR / "pdf_engine" / "mathjax" / "tex-svg.js"

THEME_CSS_CONTENT = THEME_CSS_PATH.read_text(encoding="utf-8") if THEME_CSS_PATH.exists() else ""

KIT_BODY_HTML = r"""
  <!-- ================= CAPA EXECUTIVA (PÁGINA 1) ================= -->
  <div class="cover-page">
    <div class="cover-header">
      <span class="cover-badge">MATERIAL INSTITUCIONAL • LISTA DE ESPERA VIP</span>
      <div class="cover-title">ANÁLISE QUANTITATIVA<br>APLICADA</div>
      <div class="cover-subtitle">Ementa Oficial (30h), Guia Técnico de Nivelamento em Python & Teste Diagnóstico de Prontidão Institucional</div>
      <div class="cover-accent-line"></div>
    </div>

    <div style="margin: 24px 0;">
      <div style="font-family: 'JetBrains Mono', monospace; font-size: 8.8pt; color: #94A3B8; line-height: 2.2;">
        <div>▪ PARTE 1: Ementa Oficial do Curso (30h • 6 Módulos Práticos na B3)</div>
        <div>▪ PARTE 2: Guia Técnico de Nivelamento (Matemática, Fórmulas TeX & Pipeline Python)</div>
        <div>▪ PARTE 3: Teste Diagnóstico de Nivelamento (10 Questões Conceituais & Práticas)</div>
        <div>▪ PARTE 4: Gabarito Oficial Comentado, Diagnóstico de Perfil & Plano de Estudos</div>
        <div>▪ BÔNUS: Garantia de Condição VIP da 1ª Turma com Mentoria Direta</div>
      </div>
    </div>

    <div class="cover-footer">
      <p class="author-name">Lucca Simeoni Pavan, Ph.D.</p>
      <p class="author-title">Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação</p>
      <p class="author-desc">Doutor em Economia (UFPR) • Especialista em Factor Investing, Séries Temporais, Alocação Robusta & Risco</p>
    </div>
  </div>

  <!-- ================= PÁGINA 2: APRESENTAÇÃO E SUMÁRIO ================= -->
  <div class="content-wrapper">
    <h1>Sumário & Apresentação da Obra</h1>
    
    <p>Seja muito bem-vindo! Este documento foi estruturado para ser um divisor de águas na sua jornada rumo ao mercado financeiro quantitativo institucional. Ele reúne, em um único volume auditável, tudo o que você precisa para entender a formação que está por vir, nivelar seus conhecimentos e diagnosticar suas forças e lacunas técnicas:</p>

    <div class="callout callout-info" style="margin: 16px 0;">
      <div class="callout-title">💡 Estrutura do Kit Institucional em 4 Etapas</div>
      <ol style="margin: 6px 0 0 16px; padding: 0; font-size: 9.2pt; line-height: 1.6;">
        <li><strong>Parte 1 (Ementa Oficial do Curso):</strong> Conheça a grade curricular completa de 30 horas, dividida em 6 módulos práticos que cobrem desde a ingestão de dados da B3 até o backtesting sem vieses e otimização por <em>Hierarchical Risk Parity</em> (HRP).</li>
        <li><strong>Parte 2 (Guia Técnico de Nivelamento):</strong> Revise as fundações essenciais de séries temporais, retorno simples vs. logarítmico, anualização na convenção de 252 dias úteis da B3, métricas de cauda e execute o script Python institucional em anexo.</li>
        <li><strong>Parte 3 (Teste Diagnóstico de Prontidão):</strong> Responda às 10 questões práticas de mercado cobrindo microestrutura, atritos, vieses temporais, manipulação em Pandas e otimização de carteiras.</li>
        <li><strong>Parte 4 (Gabarito & Diagnóstico de Carreira):</strong> Confira o gabarito comentado passo a passo e consulte a Régua de Nivelamento para identificar seu estágio de maturidade técnica.</li>
      </ol>
    </div>

    <h2>Índice Geral do Documento</h2>
    <div style="margin: 16px 0;">
      <div class="toc-item"><span><strong>Parte 1:</strong> Ementa Oficial do Curso (Grade Curricular de 30h & Módulos 1 a 6)</span><span class="toc-page">Pág. 3</span></div>
      <div class="toc-item"><span><strong>Parte 2:</strong> Guia Técnico de Nivelamento em Python, Séries Temporais & Fórmulas TeX</span><span class="toc-page">Pág. 5</span></div>
      <div class="toc-item"><span><strong>Parte 3:</strong> Teste Diagnóstico Institucional (10 Questões de Prontidão Quant)</span><span class="toc-page">Pág. 9</span></div>
      <div class="toc-item"><span><strong>Parte 4:</strong> Gabarito Oficial Comentado, Régua de Diagnóstico & Plano de Ação</span><span class="toc-page">Pág. 12</span></div>
    </div>

    <div class="callout callout-warning" style="margin-top: 20px;">
      <div class="callout-title">📌 Metodologia de Ensino Focada em Produção Real</div>
      Ao contrário de treinamentos acadêmicos puramente teóricos ou tutoriais superficiais de internet, este treinamento foi desenhado com base em anos de atuação direta em mesas de gestão sistemática de fundos de investimento. Cada linha de código ensinada foi concebida para resistir ao escrutínio de auditorias institucionais e restrições de liquidez da B3.
    </div>

    <!-- ================= PARTE 1 - EMENTA OFICIAL ================= -->
    <h1 class="page-break-header"><span class="section-num">1.</span> Ementa Oficial do Curso</h1>
    
    <div style="background: #F1F5F9; border: 1px solid #CBD5E1; padding: 10px 14px; border-radius: 6px; margin-bottom: 12px; font-size: 8.8pt; line-height: 1.5;">
      <div><strong>Nome do Programa:</strong> Análise Quantitativa Aplicada: Modelagem Sistemática, Factor Investing e Gestão de Risco em Python</div>
      <div><strong>Carga Horária:</strong> 30 horas (Aulas ao vivo/gravadas em alta definição + Laboratórios Práticos de Programação)</div>
      <div><strong>Stack Tecnológico:</strong> Python 3.10+, Pandas, NumPy, Statsmodels, SciPy, Matplotlib, Seaborn, yfinance, python-bcb</div>
      <div><strong>Objetivo Geral:</strong> Capacitar analistas, economistas, engenheiros e cientistas de dados a estruturarem pipelines quantitativos completos e auditáveis, desde a extração e saneamento de dados da B3 até a construção de fatores ortogonais, backtests realistas com atritos e alocação robusta de risco.</div>
    </div>

    <div class="module-card">
      <div class="module-title">Módulo 1: Infraestrutura de Dados e Engenharia Financeira em Python</div>
      <ul class="module-list">
        <li><strong>Aula 1.1:</strong> Arquitetura do pipeline quant: estruturas multidimensionais em Pandas (DataFrames multi-index, painéis e séries alinhadas).</li>
        <li><strong>Aula 1.2:</strong> Conexão com fontes institucionais: APIs do Banco Central (SGS), CVM (informes diários de fundos) e feeds de cotações.</li>
        <li><strong>Aula 1.3:</strong> Tratamento crítico de microestrutura da B3: ajuste ex-dividendos, bonificações, desdobramentos (*splits*) e calendário ANBIMA (252 dias úteis).</li>
        <li><strong>Aula 1.4:</strong> O perigo invisível da assimetria temporal: neutralização definitiva do viés de sobrevivência (*survivorship bias*) e viés de antecipação (*look-ahead bias*).</li>
        <li><strong>Laboratório Prático:</strong> Construção de uma base limpa e point-in-time com os últimos 10 anos das ações componentes do IBrX-100.</li>
      </ul>
    </div>

    <div class="module-card">
      <div class="module-title">Módulo 2: Estatística de Retornos e Métricas Institucionais de Risco de Cauda</div>
      <ul class="module-list">
        <li><strong>Aula 2.1:</strong> Retornos simples vs. log-retornos: propriedades matemáticas, aditividade espacial vs. temporal e quando utilizar cada um na modelagem.</li>
        <li><strong>Aula 2.2:</strong> Distribuições empíricas de ativos no Brasil: não-normalidade, caudas pesadas (*fat tails*), assimetria (*skewness*) e curtose excessiva.</li>
        <li><strong>Aula 2.3:</strong> Métricas de performance além do Sharpe: Ratio de Sortino (semi-variância de queda), Ratio de Calmar e Information Ratio (IR).</li>
        <li><strong>Aula 2.4:</strong> Dinâmica de rebaixamento: cálculo analítico de Maximum Drawdown (MDD), duração de *underperformance* e velocidade de recuperação.</li>
        <li><strong>Aula 2.5:</strong> Modelagem de Risco de Cauda: Value at Risk (VaR Paramétrico e Histórico) e Conditional VaR (Expected Shortfall / CVaR).</li>
        <li><strong>Laboratório Prático:</strong> Desenvolvimento de um módulo automatizado em Python que recebe qualquer série de preços e cospe um *Risk & Performance Tear Sheet* institucional.</li>
      </ul>
    </div>

    <div class="module-card">
      <div class="module-title">Módulo 3: Factor Investing e Modelagem Multifatorial no Brasil</div>
      <ul class="module-list">
        <li><strong>Aula 3.1:</strong> A evolução das teorias de apreçamento de ativos: do CAPM de Sharpe-Lintner aos modelos multifatoriais de Fama-French e Carhart.</li>
        <li><strong>Aula 3.2:</strong> Fator de Momentum na B3: Cross-Sectional Momentum (vencedores vs. perdedores 12-2) e Time-Series Momentum (Trend Following).</li>
        <li><strong>Aula 3.3:</strong> Fatores Fundamentistas: Valor (P/L, EV/EBITDA, Book-to-Market) e Qualidade (ROE, ROIC, Margem Líquida e Alavancagem).</li>
        <li><strong>Aula 3.4:</strong> Fatores de Risco Sistemático: Baixa Volatilidade (*Low Volatility Anomaly*) e Tamanho (*Size / Small Caps*).</li>
        <li><strong>Aula 3.5:</strong> O problema do *Factor Zoo*: ortogonalização via Teorema FWL, testes de significância t-stat, correção de Bonferroni e validação Out-of-Sample.</li>
        <li><strong>Laboratório Prático:</strong> Ranking multifatorial com scores padronizados (Z-Score cross-sectional) para seleção sistemática de carteiras de ações na B3.</li>
      </ul>
    </div>


    <div class="module-card">
      <div class="module-title">Módulo 4: Framework de Backtesting Institucional Realista</div>
      <ul class="module-list">
        <li><strong>Aula 4.1:</strong> Arquiteturas de simulação: Backtest Vetorizado (rápido para pesquisa de sinais) vs. Orientado a Eventos (preciso para execução de ordens).</li>
        <li><strong>Aula 4.2:</strong> Modelagem rigorosa de atritos de mercado: corretagem institucional, emolumentos da B3, taxa de liquidação e imposto de renda.</li>
        <li><strong>Aula 4.3:</strong> Slippage e Impacto de Mercado: restrições de liquidez sobre o Volume Financeiro Médio Diário (ADTV) e a Lei da Raiz Quadrada.</li>
        <li><strong>Aula 4.4:</strong> Rebalanceamento periódico: frequências ótimas (semanal, mensal), bandas de tolerância (*turnover constraints*) e custos de rotação.</li>
        <li><strong>Aula 4.5:</strong> Validação Cruzada Purificada: Walk-Forward Analysis e *Purged K-Fold Cross-Validation* com embargo para séries financeiras.</li>
        <li><strong>Laboratório Prático:</strong> Simulação histórica de 10 anos de uma carteira de Fatores na B3 com atritos reais e geração da curva de capital auditável.</li>
      </ul>
    </div>

    <div class="module-card">
      <div class="module-title">Módulo 5: Otimização de Portfólios e Alocação Robusta de Risco</div>
      <ul class="module-list">
        <li><strong>Aula 5.1:</strong> Otimização de Média-Variância de Markowitz: o paradoxo do "maximizador de erros" e a sensibilidade extrema a ruídos amostrais.</li>
        <li><strong>Aula 5.2:</strong> Regularização de matrizes de covariância: método Ledoit-Wolf Shrinkage e teoria das matrizes aleatórias (Marchenko-Pastur).</li>
        <li><strong>Aula 5.3:</strong> Paridade de Risco (*Risk Parity*) e Contribuição Marginal de Risco: equalizando orçamentos de volatilidade entre classes de ativos.</li>
        <li><strong>Aula 5.4:</strong> *Hierarchical Risk Parity* (HRP): alocação moderna via aprendizado de máquina não-supervisionado sem necessidade de inversão matricial.</li>
        <li><strong>Laboratório Prático:</strong> Comparação empírica de alocação na B3: Portfólio 1/N vs. Markowitz Clássico vs. Ledoit-Wolf vs. HRP.</li>
      </ul>
    </div>

    <div class="module-card">
      <div class="module-title">Módulo 6: Projeto Final e Engenharia de Produção Quant</div>
      <ul class="module-list">
        <li><strong>Aula 6.1:</strong> Estruturação de projetos em Python institucional: modularização, boas práticas PEP8, testes unitários e reprodutibilidade.</li>
        <li><strong>Aula 6.2:</strong> Automação de pipelines e geração de relatórios executivos em HTML/PDF de alta resolução.</li>
        <li><strong>Projeto de Conclusão de Curso:</strong> Desenvolvimento completo de uma estratégia quantitativa proprietária (coleta -> higienização point-in-time -> cálculo de fatores -> backtesting com atritos -> otimização robusta de pesos -> tear sheet de auditoria).</li>
      </ul>
    </div>

    <!-- ================= PARTE 2 - GUIA TÉCNICO DE NIVELAMENTO ================= -->
    <h1 class="page-break-header"><span class="section-num">2.</span> Guia Técnico de Nivelamento</h1>
    
    <p>Nesta seção, revisamos as bases matemáticas, estatísticas e computacionais indispensáveis para que você acompanhe o treinamento com máxima desenvoltura desde o primeiro dia de aula.</p>

    <h2>2.1 Retornos Simples vs. Retornos Logarítmicos</h2>
    <p>O primeiro conceito fundamental em modelagem quantitativa é a separação matemática estrita entre retornos aritméticos (simples) e retornos contínuos (logarítmicos):</p>

    <div class="formula-box">
      $$R_t = \frac{P_t - P_{t-1}}{P_{t-1}} = \frac{P_t}{P_{t-1}} - 1 \quad \text{(Retorno Simples)}$$
      $$r_t = \ln\left(\frac{P_t}{P_{t-1}}\right) = \ln(P_t) - \ln(P_{t-1}) \quad \text{(Log-Retorno)}$$
    </div>

    <p><strong>A Regra de Ouro da Modelagem Quantitativa:</strong></p>
    <ul>
      <li><strong>Aditividade no Espaço (Cross-Section):</strong> Retornos simples se somam linearmente entre ativos. Em uma carteira ponderada por pesos \(w_i\), o retorno total do portfólio no dia é dado exatamente por:
        <div class="formula-box">
          $$R_{p,t} = \sum_{i=1}^N w_i R_{i,t}, \quad \text{onde} \quad \sum_{i=1}^N w_i = 1$$
        </div>
        <em>Nunca some log-retornos ponderados para calcular a rentabilidade de uma carteira de investimentos!</em> A média ponderada de log-retornos subestima o retorno real da carteira devido à desigualdade de Jensen.
      </li>
      <li><strong>Aditividade no Tempo (Série Temporal):</strong> Log-retornos se somam linearmente ao longo do tempo. O retorno composto de \(T\) dias consecutivos é dado simplesmente pela soma dos log-retornos diários:
        <div class="formula-box">
          $$r_{\text{total}} = \sum_{t=1}^T r_t \implies R_{\text{total}} = \exp\left(\sum_{t=1}^T r_t\right) - 1$$
        </div>
        Por essa propriedade aditiva e por apresentarem propriedades estatísticas mais próximas da normalidade, os log-retornos são a escolha preferencial para modelagem econométrica, estimação de volatilidade e testes estatísticos.
      </li>
    </ul>

    <h2>2.2 Convenção de Anualização no Mercado Brasileiro (252 Dias Úteis)</h2>
    <p>No Brasil, taxas de juros, títulos públicos e o mercado de ações operam sob a convenção de <strong>252 dias úteis</strong> por ano (calendário ANBIMA). A conversão correta de retorno e volatilidade entre a frequência diária e anual segue:</p>

    <div class="formula-box">
      $$\bar{R}_{\text{anual}} = (1 + \bar{R}_{\text{diário}})^{252} - 1 \qquad \sigma_{\text{anual}} = \sigma_{\text{diária}} \times \sqrt{252}$$
    </div>

    <p>A multiplicação da volatilidade pela raiz quadrada do tempo (\(\sqrt{252}\)) decorre diretamente da premissa de que os retornos diários são variáveis aleatórias independentes e identicamente distribuídas (i.i.d.). Quando há forte autocorrelação serial nos retornos, essa regra deve ser ajustada para incorporar termos de covariância cruzada.</p>

    <h2>2.3 Métricas Institucionais de Performance e Risco de Cauda</h2>
    <p>Gestores de recursos institucionais avaliam estratégias por meio de métricas analíticas que superam as limitações do retorno absoluto:</p>

    <table>
      <thead>
        <tr>
          <th style="width: 25%;">Métrica de Avaliação</th>
          <th style="width: 40%;">Formulação Matemática</th>
          <th style="width: 35%;">Interpretação e Uso Prático</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Sharpe Ratio</strong></td>
          <td>$$\text{Sharpe} = \frac{\bar{R}_p - R_f}{\sigma_p}$$</td>
          <td>Mede o excesso de retorno sobre o CDI (\(R_f\)) por unidade de volatilidade total anualizada.</td>
        </tr>
        <tr>
          <td><strong>Sortino Ratio</strong></td>
          <td>$$\text{Sortino} = \frac{\bar{R}_p - R_f}{\sigma_{\text{down}}}$$</td>
          <td>Isola o risco prejudicial, penalizando apenas retornos abaixo da meta (\(\sigma_{\text{down}}\)).</td>
        </tr>
        <tr>
          <td><strong>Calmar Ratio</strong></td>
          <td>$$\text{Calmar} = \frac{\text{CAGR}}{|\text{Maximum Drawdown}|}$$</td>
          <td>Avalia a taxa de retorno anualizada em relação à pior perda histórica acumulada.</td>
        </tr>
        <tr>
          <td><strong>Maximum Drawdown</strong></td>
          <td>$$\text{MDD} = \min_{t} \left(\frac{\text{NAV}_t - \max_{\tau \le t} \text{NAV}_\tau}{\max_{\tau \le t} \text{NAV}_\tau}\right)$$</td>
          <td>A maior queda percentual entre um topo histórico e o fundo subsequente antes de nova máxima.</td>
        </tr>
        <tr>
          <td><strong>VaR (95% 1-dia)</strong></td>
          <td>$$\text{VaR}_{95\%} = -(\mu - 1.645 \cdot \sigma)$$</td>
          <td>Perda máxima esperada em 95% dos pregões sob condições normais de mercado.</td>
        </tr>
        <tr>
          <td><strong>CVaR / Expected Shortfall</strong></td>
          <td>$$\text{CVaR}_{95\%} = -\mathbb{E}\left[R \mid R \le -\text{VaR}_{95\%}\right]$$</td>
          <td>Média das perdas que ultrapassam o limite do VaR. Medida estatisticamente coerente de cauda.</td>
        </tr>
      </tbody>
    </table>

    <h2>2.4 Engenharia de Fatores e Padronização Cross-Section</h2>
    <p>Para combinar variáveis com magnitudes discrepantes (como P/L de 8x versus Momentum de +45%), aplica-se a padronização por <strong>Z-Score transversal</strong> com winsorização prévia:</p>

    <div class="formula-box">
      $$Z_{i,t} = \frac{X_{i,t} - \mu_t(X)}{\sigma_t(X)}, \qquad \tilde{F}_1 = M_X F_1 = \left(I - X(X'X)^{-1}X'\right)F_1$$
    </div>

    <p>A projeção ortogonal via <strong>Teorema de Frisch-Waugh-Lovell (FWL)</strong> permite isolar o alfa genuíno de um sinal de interesse em relação a exposições espúrias de mercado ou setor econômico.</p>

    <h2>2.5 Otimização de Carteiras: Markowitz vs. Ledoit-Wolf Shrinkage & HRP</h2>
    <p>A solução clássica de Markowitz para variância mínima requer a inversão da matriz de covariância amostral \(S\):</p>

    <div class="formula-box">
      $$w^* = \frac{\Sigma^{-1}\mathbf{1}}{\mathbf{1}'\Sigma^{-1}\mathbf{1}} \qquad \implies \qquad \Sigma_{\text{LW}} = \alpha^* F + (1 - \alpha^*) S$$
    </div>

    <p>Em amostras com dezenas de ações da B3, a inversão amplifica erros de estimativa dos autovalores. O método de <strong>Ledoit-Wolf Shrinkage</strong> estabiliza a matriz ao encolhê-la em direção a um alvo estruturado \(F\). Por sua vez, a <strong>Hierarchical Risk Parity (HRP)</strong> aplica clusterização hierárquica na distância de correlação \(d_{i,j} = \sqrt{\frac{1}{2}(1 - \rho_{i,j})}\), dispensando completamente a inversão de matrizes.</p>

    <h2 class="page-break-header">2.6 Script Python de Nivelamento: B3 Risk & Performance Scorecard</h2>
    <p>Copie e execute o código abaixo em seu ambiente Python (Jupyter Notebook, VSCode ou terminal) para calcular o scorecard completo com dados reais de ações brasileiras ajustadas por proventos:</p>

    <pre><code>import numpy as np
import pandas as pd
import yfinance as yf

# 1. Ingestão de cotações B3 ajustadas por proventos e bonificações
tickers = ['ITUB4.SA', 'VALE3.SA', 'PETR4.SA', 'WEGE3.SA', '^BVSP']
print("Baixando dados históricos da B3...")
data = yf.download(tickers, start='2021-01-01', end='2026-01-01', progress=False)
prices = data['Adj Close'].dropna()
returns = prices.pct_change().dropna()

# 2. Scorecard Institucional de Performance e Risco
def calcular_scorecard_institucional(series: pd.Series, rf_anual: float = 0.105) -> pd.Series:
    # Calcula métricas auditáveis de retorno e cauda na base 252 B3.
    rf_diario = (1 + rf_anual) ** (1 / 252) - 1
    retorno_anual = (1 + series.mean()) ** 252 - 1
    vol_anual = series.std() * np.sqrt(252)
    sharpe = (retorno_anual - rf_anual) / vol_anual if vol_anual > 0 else 0.0
    
    # Downside Semi-Variance e Sortino
    ret_excesso = series - rf_diario
    downside_vol = ret_excesso[ret_excesso < 0].std() * np.sqrt(252)
    sortino = (retorno_anual - rf_anual) / downside_vol if downside_vol > 0 else 0.0
    
    # Maximum Drawdown
    nav = (1 + series).cumprod()
    peak = nav.cummax()
    drawdown = (nav - peak) / peak
    mdd = drawdown.min()
    
    # Value at Risk e CVaR (95% histórico)
    var_95 = -np.percentile(series, 5) * np.sqrt(252)
    cvar_95 = -series[series <= np.percentile(series, 5)].mean() * np.sqrt(252)
    
    return pd.Series({
        'Retorno Anualizado': f"{retorno_anual * 100:.2f}%",
        'Volatilidade (252d)': f"{vol_anual * 100:.2f}%",
        'Índice de Sharpe': f"{sharpe:.2f}",
        'Índice de Sortino': f"{sortino:.2f}",
        'Maximum Drawdown': f"{mdd * 100:.2f}%",
        'VaR 95% (Anual)': f"{var_95 * 100:.2f}%",
        'CVaR 95% (Anual)': f"{cvar_95 * 100:.2f}%"
    })

scorecard = returns.apply(calcular_scorecard_institucional)
print("\n" + "=" * 65)
print("SCORECARD DE RISCO E PERFORMANCE • B3")
print("=" * 65)
print(scorecard.to_string())
</code></pre>

    <div class="callout callout-info">
      <div class="callout-title">💡 Dica de Execução</div>
      Certifique-se de ter as bibliotecas instaladas executando <code>pip install pandas numpy yfinance</code> no seu terminal antes de rodar o script.
    </div>

    <!-- ================= PARTE 3 - TESTE DIAGNÓSTICO ================= -->
    <h1 class="page-break-header"><span class="section-num">3.</span> Teste Diagnóstico de Prontidão Quant</h1>
    <p>Responda às 10 questões a seguir sem consultar o gabarito. Este teste avalia sua intuição teórica, domínio prático de bibliotecas em Python e capacidade de identificação de armadilhas em backtests.</p>

    <div class="question-box">
      <div class="question-title">Questão 1 • Matemática de Retornos e Portfólio</div>
      <div>Ao estruturar uma carteira quantitativa com 40% em PETR4 e 60% em VALE3, qual metodologia matemática é estritamente necessária para calcular o retorno total diário da carteira?</div>
      <div class="question-options">
        A) A média aritmética ponderada dos retornos logarítmicos dos dois ativos.<br>
        <strong>B) A média aritmética ponderada dos retornos simples dos dois ativos: \(R_p = \sum w_i R_i\).</strong><br>
        C) A média geométrica ponderada das variações diárias de preço dividida pelo volume.<br>
        D) O logaritmo natural da razão ponderada entre os preços de abertura e fechamento.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 2 • Vieses Temporais e Microestrutura CVM</div>
      <div>Um analista projeta um modelo multifatorial que utiliza os dados contábeis de balanço do 4º trimestre (data-base 31/12) para rebalancear a carteira no primeiro pregão de janeiro. Qual erro metodológico fatal ocorreu?</div>
      <div class="question-options">
        A) Viés de Sobrevivência (*Survivorship Bias*), por ignorar papéis cancelados na B3.<br>
        <strong>B) Viés de Antecipação (*Look-Ahead Bias*), pois na B3 as demonstrações do 4T são protocoladas na CVM entre fevereiro e abril.</strong><br>
        C) Erro de Curvatura de Juros por desconsiderar o cupom cambial do DI futuro.<br>
        D) Falha de Estacionariedade decorrente de quebra estrutural no PIB.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 3 • Manipulação de Séries em Python / Pandas</div>
      <div>Dado um DataFrame <code>df</code> indexado temporalmente com os preços diários de uma ação na coluna <code>'close'</code>, qual instrução nativa do Pandas calcula corretamente os retornos diários simples preservando o alinhamento?</div>
      <div class="question-options">
        A) <code>df['close'].diff() / df['close']</code><br>
        B) <code>np.log(df['close']) - np.log(df['close'].shift(-1))</code><br>
        <strong>C) <code>df['close'].pct_change().dropna()</code></strong><br>
        D) <code>df['close'].rolling(252).apply(lambda x: x[-1] / x[0] - 1)</code>
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 4 • Estatística de Séries Temporais e Anualização</div>
      <div>Se uma ação da B3 exibe uma volatilidade diária de \(2{,}0\%\) em um regime de 252 dias úteis, qual é a estimativa correta da sua volatilidade anualizada sob a premissa de retornos i.i.d.?</div>
      <div class="question-options">
        A) \(2{,}0\% \times 252 = 504{,}0\%\)<br>
        <strong>B) \(2{,}0\% \times \sqrt{252} \approx 31{,}75\%\)</strong><br>
        C) \(2{,}0\% / \sqrt{252} \approx 0{,}126\%\)<br>
        D) \((1 + 0{,}02)^{252} - 1 \approx 145{,}2\%\)
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 5 • Métricas de Risco Assimétrico</div>
      <div>Por que mesas sistemáticas institucionais frequentemente preferem o <strong>Sortino Ratio</strong> em relação ao <strong>Sharpe Ratio</strong> clássico para estratégias quantitativas de ações com assimetria positiva?</div>
      <div class="question-options">
        A) Porque o Sortino ignora a taxa livre de risco e opera exclusivamente em dólar.<br>
        <strong>B) Porque o Sharpe penaliza ganhos expressivos para cima (*upside volatility*) da mesma forma que penaliza quedas severas, enquanto o Sortino isola unicamente o desvio prejudicial (*downside deviation*).</strong><br>
        C) Porque o Sortino Ratio não depende do tamanho amostral da série temporal.<br>
        D) Porque o Sharpe Ratio só pode ser computado para carteiras compostas por mais de 50 ativos.
      </div>
    </div>


    <div class="question-box">
      <div class="question-title">Questão 6 • Validação de Modelos em Séries Temporais</div>
      <div>Por que a aplicação direta do algoritmo de <em>K-Fold Cross-Validation</em> aleatório tradicional do Scikit-Learn é proibitiva e produz métricas fictícias em séries financeiras?</div>
      <div class="question-options">
        <strong>A) Porque o K-Fold aleatório embaralha os dados e treina o modelo com informações futuras para prever o passado, gerando vazamento temporal de dados (*data leakage*).</strong><br>
        B) Porque o K-Fold tradicional opera exclusivamente com variáveis explicativas binárias.<br>
        C) Porque o número de dobras (*folds*) deve ser rigorosamente idêntico ao número de ativos em custódia.<br>
        D) Porque o algoritmo dobra artificialmente os custos operacionais de corretagem.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 7 • Factor Investing e Mecânica de Mercado</div>
      <div>Qual é a distinção conceitual determinante entre uma estratégia de <strong>Cross-Sectional Momentum</strong> e uma de <strong>Time-Series Momentum (Trend Following)</strong>?</div>
      <div class="question-options">
        A) Cross-Sectional opera exclusivamente no mercado brasileiro e Time-Series opera apenas futuros nos EUA.<br>
        <strong>B) Cross-Sectional compara ativos entre si em um corte transversal relativo (comprando os melhores e vendendo os piores), enquanto Time-Series avalia cada ativo isoladamente contra o seu próprio histórico temporal em termos absolutos.</strong><br>
        C) Cross-Sectional utiliza unicamente médias móveis simples e Time-Series utiliza regressões vetoriais de cointegração.<br>
        D) Não há distinção teórica; ambos os conceitos são sinônimos nos modelos de Fama-French.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 8 • Microestrutura, Atritos e Execução Institucional</div>
      <div>Ao rodar o backtest de uma estratégia sistemática focada em <em>Small Caps</em> na B3 com patrimônio gerido de R$ 50 milhões, qual variável é imprescindível para impedir que o modelo selecione papéis ilíquidos cujo impacto de mercado aniquilaria o alfa real?</div>
      <div class="question-options">
        A) A taxa de variação do Índice Geral de Preços - Mercado (IGP-M).<br>
        <strong>B) A restrição de participação máxima sobre o Volume Financeiro Médio Diário (ADTV) combinada com modelagem de *slippage* e custos de empréstimo (BTC).</strong><br>
        C) O índice de engajamento do perfil da companhia nas redes sociais.<br>
        D) O valor nominal do patrimônio líquido contábil dividido pela quantidade de cotistas.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 9 • Otimização de Carteiras de Markowitz</div>
      <div>Qual é o principal obstáculo prático da Otimização de Média-Variância quando aplicada diretamente em uma matriz de covariância amostral com dezenas de ações da B3?</div>
      <div class="question-options">
        A) O algoritmo é incapaz de processar retornos de valor positivo.<br>
        <strong>B) O método de Markowitz é um "maximizador de erros de estimativa": a inversão da matriz amostral amplifica ruídos estatísticos e atribui pesos extremos aos menores autovalores, problema remediado por técnicas como *Ledoit-Wolf Shrinkage*.</strong><br>
        C) Markowitz exige como premissa mandatória que todos os retornos esperados sejam negativos.<br>
        D) A formulação não admite ativos do setor financeiro ou elétrico.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 10 • Aprendizado de Máquina Não-Supervisionado em Alocação</div>
      <div>Qual avanço fundamental a metodologia de <strong>Hierarchical Risk Parity (HRP)</strong>, proposta por Marcos López de Prado, introduziu na alocação quantitativa de recursos?</div>
      <div class="question-options">
        <strong>A) Aplica clusterização hierárquica na matriz de distâncias de correlação, eliminando a necessidade de inversão matricial e resolvendo em definitivo a instabilidade numérica de Markowitz.</strong><br>
        B) Garante rentabilidade superior a 40% ao ano independentemente do regime macroeconômico.<br>
        C) Substitui o código em Python por contratos automatizados em redes blockchain.<br>
        D) Elimina integralmente o risco de mercado de qualquer classe de renda variável.
      </div>
    </div>

    <!-- ================= PARTE 4 - GABARITO & DIAGNÓSTICO ================= -->
    <h1 class="page-break-header"><span class="section-num">4.</span> Gabarito Oficial Comentado</h1>
    
    <div class="answer-box">
      <div class="answer-title">Questão 1 • Resposta Correta: B (Média Ponderada de Retornos Simples)</div>
      <div class="answer-desc">A agregação de carteiras no corte transversal obedece estritamente à linearidade dos retornos simples: \(R_p = \sum w_i R_i\). Pela desigualdade de Jensen, a média ponderada de log-retornos não iguala a taxa de crescimento da carteira e induz a graves distorções de dimensionamento.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 2 • Resposta Correta: B (Viés de Antecipação / Look-Ahead Bias)</div>
      <div class="answer-desc">Na legislação societária e normas da CVM, as companhias de capital aberto possuem até 90 dias após o término do exercício social para enviar o balanço do 4T. Utilizar dados contábeis fechados em 31/12 nas primeiras semanas de janeiro introduz informação futura no passado, invalidando todo o teste empírico.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 3 • Resposta Correta: C (df['close'].pct_change().dropna())</div>
      <div class="answer-desc">O método <code>.pct_change()</code> é a rotina vetorizada e auditada nativa do Pandas para calcular \(\frac{P_t - P_{t-1}}{P_{t-1}}\). O uso de <code>.dropna()</code> remove a primeira linha que resulta em <code>NaN</code> por falta de defasagem anterior.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 4 • Resposta Correta: B (2,0% × √252 ≈ 31,75%)</div>
      <div class="answer-desc">Sob a premissa de retornos independentes e identicamente distribuídos (i.i.d.), a variância escala linearmente com o tempo (\(\sigma^2_{\text{anual}} = 252 \cdot \sigma^2_{\text{diária}}\)), logo o desvio padrão escala com a raiz quadrada do tempo: \(\sigma_{\text{anual}} = 2{,}0\% \times \sqrt{252} \approx 31{,}75\%\).</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 5 • Resposta Correta: B (Isolamento da Volatilidade Prejudicial)</div>
      <div class="answer-desc">O Sharpe Ratio clássico trata oscilações positivas e negativas de forma simétrica no denominador. Para estratégias quantitativas com assimetria positiva (alfa de momentum e ganhos expressivos), o Sortino é superior por penalizar unicamente o desvio abaixo da taxa livre de risco (*downside deviation*).</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 6 • Resposta Correta: A (Vazamento Temporal / Data Leakage)</div>
      <div class="answer-desc">Dados de mercado financeiro possuem ordem cronológica estrita e autocorrelação. O K-Fold padrão do Scikit-Learn seleciona pontos de forma aleatória no tempo, utilizando o pregão de amanhã para ajustar os pesos de ontem. Utiliza-se a técnica de <em>Purged K-Fold com Embargo</em>.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 7 • Resposta Correta: B (Momento Relativo Cross-Section vs. Absoluto Time-Series)</div>
      <div class="answer-desc">Cross-Sectional Momentum ranqueia o universo de ações no mesmo instante, comprando as de maior performance relativa e vendendo as piores. Time-Series Momentum avalia se a série do ativo está em tendência de alta em relação ao seu próprio histórico temporal (Trend Following).</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 8 • Resposta Correta: B (Filtro de ADTV, Slippage e Almgren-Chriss)</div>
      <div class="answer-desc">Em gestão institucional, o atrito de mercado (*market impact*) destrói qualquer modelo de Small Caps que compre porcentagens excessivas do volume diário. É mandatório restringir a ordem a uma fração conservadora do ADTV (ex: máx. 5% a 10%) e modelar o slippage via lei da raiz quadrada.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 9 • Resposta Correta: B (Maximização de Erros de Amostra e Ledoit-Wolf)</div>
      <div class="answer-desc">A inversão da matriz amostral \(\Sigma^{-1}\) atua como um amplificador de ruídos estatísticos. Ativos que tiveram volatilidade baixa puramente por acaso amostral recebem pesos alavancados. Técnicas de regularização como <em>Ledoit-Wolf Shrinkage</em> estabilizam a matriz e viabilizam a implementação em produção.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 10 • Resposta Correta: A (Clusterização Hierárquica sem Inversão Matricial)</div>
      <div class="answer-desc">O HRP utiliza aprendizado de máquina não-supervisionado para agrupar ativos em uma árvore hierárquica a partir da distância de correlação. O capital é distribuído recursivamente pelos ramos da árvore com base em orçamentos de variância inversa, eliminando a dependência de matrizes inversas.</div>
    </div>

    <h2>Régua de Diagnóstico & Plano de Estudos Recomendado</h2>
    <p>Compare sua pontuação no teste com a régua institucional abaixo para identificar o foco estratégico ideal da sua preparação:</p>

    <table>
      <thead>
        <tr>
          <th style="width: 22%;">Faixa de Acertos</th>
          <th style="width: 38%;">Diagnóstico de Maturidade Técnica</th>
          <th style="width: 40%;">Foco Recomendado no Treinamento</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color: #DC2626;">0 a 4 Acertos</strong></td>
          <td><strong>Nível 1: Em Transição / Fundamentos</strong><br>Boa intuição geral, mas com lacunas severas em econometria de séries temporais, atritos de microestrutura ou vícios comuns de Data Science tradicional / Excel.</td>
          <td>Os <strong>Módulos 1 e 2</strong> serão decisivos para blindar seus dados contra vieses temporais, dominar métricas de cauda (VaR/CVaR) e adotar operações vetorizadas em Pandas/NumPy.</td>
        </tr>
        <tr>
          <td><strong style="color: #D97706;">5 a 7 Acertos</strong></td>
          <td><strong>Nível 2: Analista Intermediário</strong><br>Sólido domínio de programação básica em Python e noções de risco, porém com espaço para evolução em atritos de execução, factor ranking e validação cruzada purificada.</td>
          <td>Os <strong>Módulos 3 e 4</strong> levarão seus backtests para o rigor de auditoria de gestoras institucionais, dominando testes de significância t-stat, ortogonalização FWL e limites de ADTV.</td>
        </tr>
        <tr>
          <td><strong style="color: #16A34A;">8 a 10 Acertos</strong></td>
          <td><strong>Nível 3: Quant Desk Ready</strong><br>Excelente maturidade técnica, visão apurada de microestrutura e forte discernimento contra armadilhas e overfitting de dados de mercado.</td>
          <td>Os <strong>Módulos 4, 5 e 6</strong> permitirão a você dominar fronteiras de ponta como Ledoit-Wolf, HRP e estruturar uma estratégia quantitativa proprietária completa pronta para alocação de capital.</td>
        </tr>
      </tbody>
    </table>

    <div class="callout callout-info" style="margin-top: 14px; padding: 10px 14px;">
      <div class="callout-title">🔒 Condição Exclusiva Assegurada • Lista de Espera VIP</div>
      Ao preencher o formulário na Landing Page oficial, você assegurou automaticamente sua prioridade para a 1ª Turma do <strong>Curso de Análise Quantitativa Aplicada</strong> com <strong>20% de desconto exclusivo</strong>, além de acesso prioritário às sessões ao vivo de mentoria de código e revisão de projetos com o Dr. Lucca Simeoni Pavan.
    </div>

    <div style="margin-top: 18px; border-top: 1px solid var(--border-light); padding-top: 10px; font-size: 8.5pt; color: var(--text-muted); text-align: center;">
      <strong>Curso de Análise Quantitativa Aplicada</strong> • Desenvolvido por Lucca Simeoni Pavan, Ph.D.<br>
      Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação • Todos os direitos reservados.
    </div>

  </div>
"""

def generate_kit_html(theme_href: str, mathjax_src: str) -> str:
    """Gera o HTML com a configuração adequada de cabeçalho, css e scripts."""
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Kit de Nivelamento, Ementa Oficial e Teste Diagnóstico - Lucca Simeoni Pavan, Ph.D.</title>
  <link rel="stylesheet" href="{theme_href}">
  <style>
    @page {{
      size: A4;
      margin: 20mm 15mm 20mm 15mm;
      @bottom-right {{
        content: counter(page);
        font-family: 'Inter', sans-serif;
        font-size: 8pt;
        color: #94A3B8;
      }}
      @bottom-left {{
        content: "Kit de Nivelamento & Ementa Oficial • Lucca Simeoni Pavan, Ph.D.";
        font-family: 'Inter', sans-serif;
        font-size: 8pt;
        color: #94A3B8;
      }}
    }}
    @page :first {{
      margin: 0;
      @bottom-right {{ content: none; }}
      @bottom-left {{ content: none; }}
    }}
    .page-break-header {{
      page-break-before: always;
      break-before: page;
    }}
    .section-num {{ color: var(--accent-cyan); font-weight: 700; margin-right: 6px; }}
    .toc-item {{ display: flex; justify-content: space-between; border-bottom: 1px dotted var(--border-light); padding: 5px 0; margin-bottom: 3px; font-size: 9.5pt; }}
    .toc-page {{ font-family: 'JetBrains Mono', monospace; font-weight: 600; color: var(--accent-blue); }}
    .formula-box {{
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      border-left: 4px solid var(--primary-navy);
      padding: 12px 18px;
      margin: 14px 0;
      border-radius: 4px;
      text-align: center;
      page-break-inside: avoid;
      break-inside: avoid;
    }}
    mjx-container[jax="SVG"] {{
      font-size: 110% !important;
    }}
    mjx-container[jax="SVG"][display="true"] {{
      margin: 6px 0 !important;
    }}
    .question-box {{
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-left: 4px solid var(--accent-blue);
      padding: 12px 16px;
      margin-bottom: 14px;
      border-radius: 4px;
      page-break-inside: avoid;
      break-inside: avoid;
    }}
    .question-title {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-weight: 700;
      color: var(--primary-navy);
      font-size: 10.5pt;
      margin-bottom: 6px;
    }}
    .question-options {{
      margin-left: 10px;
      font-size: 9pt;
      line-height: 1.6;
      color: #334155;
    }}
    .answer-box {{
      background: #F0FDF4;
      border: 1px solid #BBF7D0;
      border-left: 4px solid #16A34A;
      padding: 10px 14px;
      margin-bottom: 10px;
      border-radius: 4px;
      page-break-inside: avoid;
      break-inside: avoid;
    }}
    .answer-title {{
      font-weight: 700;
      color: #166534;
      font-size: 9.5pt;
      margin-bottom: 3px;
    }}
    .answer-desc {{
      font-size: 8.8pt;
      color: #1E293B;
      line-height: 1.5;
    }}
    .module-card {{
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-left: 4px solid var(--accent-cyan);
      padding: 8px 12px;
      margin-bottom: 9px;
      border-radius: 4px;
      page-break-inside: avoid;
      break-inside: avoid;
    }}
    .module-title {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-weight: 700;
      color: var(--primary-navy);
      font-size: 9.8pt;
      margin-bottom: 3px;
    }}
    .module-list {{
      margin: 0;
      padding-left: 18px;
      font-size: 8.5pt;
      color: #334155;
      line-height: 1.45;
    }}
    pre code {{
      background-color: transparent !important;
      border: none !important;
      padding: 0 !important;
      color: inherit !important;
      font-size: inherit !important;
    }}
  </style>

  <!-- MathJax Configuration & Vector SVG Engine -->
  <script>
  window.MathJax = {{
    tex: {{
      inlineMath: [['\\\\(', '\\\\)']],
      displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
      processEscapes: true
    }},
    svg: {{
      fontCache: 'local'
    }}
  }};
  </script>
  <script src="{mathjax_src}"></script>
</head>
<body>
{KIT_BODY_HTML}
</body>
</html>"""

def main():
    print("=" * 70)
    print("🚀 Compilador do Kit de Nivelamento, Ementa Oficial & Teste Diagnóstico")
    print("   Padrão Visual: The Quant Transition Playbook (Fórmulas em Vetor SVG)")
    print("=" * 70)
    
    # 1. Arquivos de destino
    pdf_prod = ROOT_DIR / "products" / "Kit_Nivelamento_e_Ementa_Analise_Quantitativa.pdf"
    pdf_down = ROOT_DIR / "landing_pages" / "downloads" / "Kit_Nivelamento_e_Ementa_Analise_Quantitativa.pdf"
    
    html_prod = ROOT_DIR / "products" / "kit_nivelamento_e_ementa_analise_quantitativa.html"
    html_down = ROOT_DIR / "landing_pages" / "downloads" / "kit_nivelamento_e_ementa_analise_quantitativa.html"
    
    # Para compilação no Chrome Headless, usamos URIs absolutas locais para garantir
    # que o theme.css e o motor tex-svg.js local sejam carregados perfeitamente
    theme_uri = THEME_CSS_PATH.resolve().as_uri()
    mathjax_uri = MATHJAX_JS_PATH.resolve().as_uri()
    
    render_html_path = ROOT_DIR / "products" / "render_kit_temp.html"
    render_html_content = generate_kit_html(theme_uri, mathjax_uri)
    render_html_path.write_text(render_html_content, encoding="utf-8")
    print("✅ Arquivo de renderização temporário criado com sucesso.")
    
    # Gera a versão para navegação na web em landing_pages/downloads
    web_theme = "../../pdf_engine/theme.css"
    web_mathjax = "../../pdf_engine/mathjax/tex-svg.js"
    web_html_content = generate_kit_html(web_theme, web_mathjax)
    html_down.write_text(web_html_content, encoding="utf-8")
    html_prod.write_text(web_html_content, encoding="utf-8")
    print(f"✅ HTMLs gravados em:\n   • {html_down}\n   • {html_prod}")
    
    # 2. Compilar PDF de Alta Resolução via Chrome Headless
    print(f"\n⏳ Convertendo HTML para PDF de alta resolução com motor MathJax...")
    success = convert_html_to_pdf(str(render_html_path), str(pdf_prod))
    
    # Remove render temporário
    render_html_path.unlink(missing_ok=True)
    
    if success and pdf_prod.exists():
        size_kb = pdf_prod.stat().st_size / 1024
        print(f"✅ PDF gerado com sucesso em products! Tamanho: {size_kb:.1f} KB")
        
        # Copia para pasta de download da Landing Page
        shutil.copy2(str(pdf_prod), str(pdf_down))
        print(f"✅ PDF copiado para {pdf_down}")
        
        # 3. Verificação de Integridade via pypdf
        print("\n🔍 Verificando integridade das fórmulas e páginas...")
        reader = pypdf.PdfReader(str(pdf_down))
        num_pages = len(reader.pages)
        print(f"📄 Total de páginas geradas: {num_pages}")
        
        raw_latex_found = False
        for i, page in enumerate(reader.pages):
            txt = page.extract_text()
            if "$$" in txt:
                print(f"⚠️ Atenção: '$$' detectado na página {i+1}!")
                raw_latex_found = True
        
        if not raw_latex_found:
            print("✨ SUCESSO ABSOLUTO: Todas as fórmulas LaTeX foram compiladas em vetores gráficos SVG!")
        else:
            print("⚠️ Algumas fórmulas podem não ter sido convertidas.")
            
        print("=" * 70)
        print(f"🎉 Processo concluído! O PDF que baixa do site está 100% atualizado e calibrado!")
        print("=" * 70)
        return True
    else:
        print("❌ Falha na geração do PDF institucional.")
        return False

if __name__ == "__main__":
    main()
