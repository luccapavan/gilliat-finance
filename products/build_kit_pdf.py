"""
Compilador Institucional do Kit de Nivelamento, Ementa Oficial e Teste Diagnóstico
Gera a versão HTML estilizada e compila em PDF de alta resolução via Chrome/Edge headless.
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

KIT_HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Kit de Nivelamento, Ementa Oficial e Teste Diagnóstico - Lucca Simeoni Pavan, Ph.D.</title>
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

  <!-- ================= CAPA EXECUTIVA ================= -->
  <div class="cover-page">
    <div class="cover-header">
      <span class="cover-badge">MATERIAL EXCLUSIVO • LISTA DE ESPERA VIP</span>
      <div class="cover-title">ANÁLISE QUANTITATIVA<br>APLICADA</div>
      <div class="cover-subtitle">Ementa Oficial, Guia Técnico de Nivelamento em Python & Teste Diagnóstico de Prontidão Quant</div>
      <div class="cover-accent-line"></div>
    </div>

    <div style="margin: 20px 0;">
      <div style="font-family: 'JetBrains Mono', monospace; font-size: 8.5pt; color: #94A3B8; line-height: 2.2;">
        <div>▪ PARTE 1: Ementa Oficial do Curso (30h • 6 Módulos Práticos B3)</div>
        <div>▪ PARTE 2: Guia Técnico de Nivelamento (Matemática, Risco & Código Python)</div>
        <div>▪ PARTE 3: Teste Diagnóstico de Nivelamento (10 Questões & Gabarito Comentado)</div>
        <div>▪ BÔNUS: Régua de Autoavaliação e Diagnóstico de Perfil Institucional</div>
      </div>
    </div>

    <div class="cover-footer">
      <p class="author-name">Lucca Simeoni Pavan, Ph.D.</p>
      <p class="author-title">Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação</p>
      <p class="author-desc">Doutor em Economia (UFPR) • Especialista em Factor Investing, Séries Temporais, Alocação & Risco</p>
    </div>
  </div>

  <!-- ================= PÁGINA 2: APRESENTAÇÃO E SUMÁRIO ================= -->
  <div class="content-wrapper">
    <h1>Apresentação do Kit Institucional</h1>
    
    <p>Seja muito bem-vindo! Este documento foi estruturado para ser um divisor de águas na sua jornada rumo ao mercado financeiro quantitativo institucional. Ele reúne, em um único volume auditável, tudo o que você precisa para entender a formação que está por vir e nivelar seus conhecimentos:</p>

    <div class="callout callout-info" style="margin: 16px 0;">
      <div class="callout-title">💡 Estrutura em 3 Etapas</div>
      <ol style="margin: 5px 0 0 16px; padding: 0; font-size: 9.2pt; line-height: 1.6;">
        <li><strong>Parte 1 (Ementa do Curso):</strong> Conheça a grade curricular completa de 30 horas, dividida em 6 módulos que cobrem desde a ingestão de dados da B3 até o backtest institucional sem viés e otimização por HRP.</li>
        <li><strong>Parte 2 (Guia Técnico):</strong> Revise as fundações essenciais de séries temporais, retorno simples vs. logarítmico, anualização Brasil e execute o script Python institucional em anexo.</li>
        <li><strong>Parte 3 (Teste Diagnóstico):</strong> Responda às 10 questões práticas de mercado, confira o gabarito explicado e descubra em qual estágio de prontidão quant você está.</li>
      </ol>
    </div>

    <h2>Índice Geral</h2>
    <div style="margin: 15px 0;">
      <div class="toc-item"><span><strong>Parte 1:</strong> Ementa Oficial do Curso (Visão Geral & Módulos 1 a 6)</span><span class="toc-page">Pág. 3</span></div>
      <div class="toc-item"><span><strong>Parte 2:</strong> Guia de Nivelamento Técnico em Python & Séries Temporais</span><span class="toc-page">Pág. 5</span></div>
      <div class="toc-item"><span><strong>Parte 3:</strong> Teste Diagnóstico de Nivelamento (10 Questões de Múltipla Escolha)</span><span class="toc-page">Pág. 7</span></div>
      <div class="toc-item"><span><strong>Gabarito & Diagnóstico:</strong> Respostas Comentadas e Régua de Autoavaliação</span><span class="toc-page">Pág. 9</span></div>
    </div>

    <div class="page-break"></div>

    <!-- ================= PÁGINA 3-4: EMENTA OFICIAL ================= -->
    <h1><span class="section-num">1.</span> Ementa Oficial do Curso</h1>
    
    <div style="background: #F1F5F9; padding: 12px 16px; border-radius: 6px; margin-bottom: 16px; font-size: 9pt;">
      <div><strong>Nome do Curso:</strong> Análise Quantitativa Aplicada: Modelagem Sistemática, Factor Investing e Gestão de Risco em Python</div>
      <div><strong>Carga Horária:</strong> 30 horas (Aulas ao vivo/gravadas + Projetos Práticos de Programação)</div>
      <div><strong>Stack Tecnológica:</strong> Python 3.10+, Pandas, NumPy, Statsmodels, SciPy, Matplotlib, Seaborn, yfinance, python-bcb</div>
      <div><strong>Objetivo Geral:</strong> Capacitar analistas, economistas e cientistas de dados a estruturarem pipelines quantitativos completos, desde a coleta e tratamento de dados da B3 até o backtesting sem vieses e a alocação robusta de portfólios sistemáticos.</div>
    </div>

    <div class="module-card">
      <div class="module-title">Módulo 1: Infraestrutura de Dados e Engenharia Financeira em Python</div>
      <ul class="module-list">
        <li><strong>Aula 1.1:</strong> Arquitetura do pipeline quant: estruturas de dados multidimensionais (DataFrames multi-index e painéis).</li>
        <li><strong>Aula 1.2:</strong> Conexão com fontes institucionais: APIs do Banco Central (SGS), CVM (informes diários) e cotações de mercado.</li>
        <li><strong>Aula 1.3:</strong> Tratamento crítico de dados da B3: ajuste ex-dividendos, bonificações, splits e calendário ANBIMA (dias úteis).</li>
        <li><strong>Aula 1.4:</strong> O perigo invisível: neutralização do viés de sobrevivência (*survivorship bias*) e viés de antecipação (*look-ahead bias*).</li>
        <li><strong>Laboratório Prático:</strong> Construção de base limpa com os últimos 10 anos das ações do IBrX-100.</li>
      </ul>
    </div>

    <div class="module-card">
      <div class="module-title">Módulo 2: Estatística de Retornos e Métricas Institucionais de Risco</div>
      <ul class="module-list">
        <li><strong>Aula 2.1:</strong> Retornos simples vs. log-retornos: propriedades matemáticas e quando utilizar cada um na modelagem.</li>
        <li><strong>Aula 2.2:</strong> Distribuições empíricas de ativos: não-normalidade, caudas pesadas (*fat tails*), assimetria e curtose.</li>
        <li><strong>Aula 2.3:</strong> Métricas de performance além do Sharpe: Ratio de Sortino, Ratio de Calmar e Information Ratio.</li>
        <li><strong>Aula 2.4:</strong> Dinâmica de rebaixamento: cálculo analítico de Maximum Drawdown (MDD), duração e recuperação.</li>
        <li><strong>Aula 2.5:</strong> Modelos de Risco de Cauda: Value at Risk (VaR Paramétrico/Histórico) e Conditional VaR (Expected Shortfall / CVaR).</li>
        <li><strong>Laboratório Prático:</strong> Criação de módulo automatizado que recebe qualquer série de preços e cospe um *Risk Tear Sheet*.</li>
      </ul>
    </div>

    <div class="module-card">
      <div class="module-title">Módulo 3: Factor Investing e Modelagem Multifatorial no Brasil</div>
      <ul class="module-list">
        <li><strong>Aula 3.1:</strong> A evolução das teorias de apreçamento: do CAPM aos modelos multifatoriais de Fama-French e Carhart.</li>
        <li><strong>Aula 3.2:</strong> Fator de Momentum na B3: Cross-Sectional Momentum (vencedores vs. perdedores) e Time-Series Momentum.</li>
        <li><strong>Aula 3.3:</strong> Fatores Fundamentistas: Valor (P/L, EV/EBITDA, Book-to-Market) e Qualidade (ROE, ROIC, Margem Líquida).</li>
        <li><strong>Aula 3.4:</strong> Fatores de Risco: Baixa Volatilidade (*Low Vol*) e Tamanho (*Size / Small Caps*).</li>
        <li><strong>Aula 3.5:</strong> O problema do *Factor Zoo*: testes de significância t-stat, correção de Bonferroni e validação Out-of-Sample.</li>
        <li><strong>Laboratório Prático:</strong> Ranking multifatorial com scores padronizados (Z-Score) para seleção sistemática de carteiras na B3.</li>
      </ul>
    </div>

    <div class="page-break"></div>

    <div class="module-card">
      <div class="module-title">Módulo 4: Framework de Backtesting Institucional Realista</div>
      <ul class="module-list">
        <li><strong>Aula 4.1:</strong> Arquiteturas de Backtest: Vectorizado (rápido para prototipagem) vs. Orientado a Eventos (preciso para execução).</li>
        <li><strong>Aula 4.2:</strong> Modelagem de atritos de mercado: custos de corretagem, emolumentos B3, taxa de liquidação e impostos.</li>
        <li><strong>Aula 4.3:</strong> Slippage e Impacto de Mercado: restrições de liquidez com base no volume financeiro médio diário (ADTV).</li>
        <li><strong>Aula 4.4:</strong> Rebalanceamento periódico: frequências ótimas (semanal, mensal), bandas de tolerância (*turnover*) e rotação.</li>
        <li><strong>Aula 4.5:</strong> Walk-Forward Analysis e Validação Cruzada Purificada (Purged Cross-Validation para séries temporais).</li>
        <li><strong>Laboratório Prático:</strong> Backtest de 5 anos de uma carteira de Fatores na B3 com custos reais e curva de capital auditável.</li>
      </ul>
    </div>

    <div class="module-card">
      <div class="module-title">Módulo 5: Otimização de Portfólios e Alocação de Risco</div>
      <ul class="module-list">
        <li><strong>Aula 5.1:</strong> Otimização de Média-Variância de Markowitz: limites práticos e sensibilidade a erros de estimativa.</li>
        <li><strong>Aula 5.2:</strong> Regularização de matrizes de covariância: método Ledoit-Wolf Shrinkage e Random Matrix Theory (RMT).</li>
        <li><strong>Aula 5.3:</strong> Paridade de Risco (*Risk Parity*) e Contribuição Marginal de Risco: equalizando orçamentos de volatilidade.</li>
        <li><strong>Aula 5.4:</strong> *Hierarchical Risk Parity* (HRP): alocação via machine learning não-supervisionado sem inversão de matriz.</li>
        <li><strong>Laboratório Prático:</strong> Comparação empírica: 1/N vs. Média-Variância vs. HRP com ativos brasileiros e internacionais.</li>
      </ul>
    </div>

    <div class="module-card">
      <div class="module-title">Módulo 6: Projeto Final e Produção Quant</div>
      <ul class="module-list">
        <li><strong>Aula 6.1:</strong> Estruturação de projetos em Python: modularização, boas práticas e reprodutibilidade.</li>
        <li><strong>Aula 6.2:</strong> Geração de relatórios executivos em HTML/PDF com gráficos interativos.</li>
        <li><strong>Projeto de Conclusão:</strong> Desenvolvimento de uma estratégia quantitativa proprietária completa (extração -> cálculo de fatores -> backtest com atritos -> otimização de pesos -> tear sheet de risco).</li>
      </ul>
    </div>

    <div class="page-break"></div>

    <!-- ================= PÁGINA 5-6: GUIA TÉCNICO DE NIVELAMENTO ================= -->
    <h1><span class="section-num">2.</span> Guia Técnico de Nivelamento</h1>
    
    <h2>2.1 Retornos Simples vs. Retornos Logarítmicos</h2>
    <p>O primeiro conceito fundamental em modelagem quantitativa é a separação matemática estrita entre retornos aritméticos e logarítmicos:</p>

    <div class="formula-box">
      $$R_t = \frac{P_t - P_{t-1}}{P_{t-1}} = \frac{P_t}{P_{t-1}} - 1 \quad \text{(Retorno Simples)}$$
      $$r_t = \ln\left(\frac{P_t}{P_{t-1}}\right) = \ln(P_t) - \ln(P_{t-1}) \quad \text{(Log-Retorno)}$$
    </div>

    <p><strong>A Regra de Ouro do Analista Quant:</strong></p>
    <ul>
      <li><strong>Aditividade no Espaço (Cross-Section):</strong> Retornos simples se somam linearmente entre ativos. Em uma carteira ponderada por pesos \(w_i\), o retorno do portfólio no dia é exatamente \(R_{p,t} = \sum_{i=1}^N w_i R_{i,t}\). Nunca some log-retornos ponderados para calcular o valor de uma carteira!</li>
      <li><strong>Aditividade no Tempo (Série Temporal):</strong> Log-retornos se somam linearmente ao longo do tempo. O retorno composto de \(T\) dias é dado simplesmente pela soma dos retornos log diários: \(r_{total} = \sum_{t=1}^T r_t\). Utilize log-retornos para estimação econométrica e volatilidade.</li>
    </ul>

    <h2>2.2 Convenção de Anualização no Mercado Brasileiro (252 Dias Úteis)</h2>
    <p>No Brasil, taxas de juros e ações operam sob a base de 252 dias úteis (calendário ANBIMA):</p>
    <div class="formula-box">
      $$\bar{R}_{anual} = (1 + \bar{R}_{diário})^{252} - 1 \qquad \sigma_{anual} = \sigma_{diária} \times \sqrt{252}$$
    </div>

    <h2>2.3 Métricas Institucionais de Performance</h2>
    <ul>
      <li><strong>Sharpe Ratio:</strong> Mede o retorno excedente sobre o ativo livre de risco (\(R_f\), CDI anualizado) por unidade de volatilidade total: \(\text{Sharpe} = \frac{\bar{R}_p - R_f}{\sigma_p}\).</li>
      <li><strong>Sortino Ratio:</strong> Penaliza apenas o risco prejudicial (retornos abaixo da meta ou negativos): \(\text{Sortino} = \frac{\bar{R}_p - R_f}{\sigma_{down}}\). Ideal para estratégias de ações com assimetria positiva.</li>
      <li><strong>Maximum Drawdown (MDD):</strong> A maior queda percentual entre o topo histórico e o fundo subsequente: \(MDD = \min_t \left(\frac{NAV_t - \max_{\tau \le t}(NAV_\tau)}{\max_{\tau \le t}(NAV_\tau)}\right)\).</li>
    </ul>

    <h2>2.4 Script de Nivelamento em Python: Scorecard B3</h2>
    <p>Copie e execute o bloco abaixo para gerar um scorecard institucional com dados reais da B3:</p>

    <pre><code>import numpy as np
import pandas as pd
import yfinance as yf

# 1. Download de cotações B3 ajustadas por proventos
tickers = ['ITUB4.SA', 'VALE3.SA', 'PETR4.SA', 'WEGE3.SA', '^BVSP']
data = yf.download(tickers, start='2021-01-01', end='2026-01-01', progress=False)
prices = data['Adj Close'].dropna()
returns = prices.pct_change().dropna()

# 2. Scorecard Institucional de Risco
def calcular_scorecard(series, rf_anual=0.105):
    rf_diario = (1 + rf_anual) ** (1 / 252) - 1
    retorno_anual = (1 + series.mean()) ** 252 - 1
    vol_anual = series.std() * np.sqrt(252)
    sharpe = (retorno_anual - rf_anual) / vol_anual if vol_anual > 0 else 0
    
    ret_excesso = series - rf_diario
    downside = ret_excesso[ret_excesso < 0].std() * np.sqrt(252)
    sortino = (retorno_anual - rf_anual) / downside if downside > 0 else 0
    
    cum_ret = (1 + series).cumprod()
    mdd = ((cum_ret - cum_ret.cummax()) / cum_ret.cummax()).min()
    
    return pd.Series({
        'Retorno Anual': f"{retorno_anual * 100:.2f}%",
        'Vol Anual': f"{vol_anual * 100:.2f}%",
        'Sharpe': f"{sharpe:.2f}",
        'Sortino': f"{sortino:.2f}",
        'Max Drawdown': f"{mdd * 100:.2f}%"
    })

print(returns.apply(calcular_scorecard).to_string())
</code></pre>

    <div class="page-break"></div>

    <!-- ================= PÁGINA 7-8: TESTE DIAGNÓSTICO ================= -->
    <h1><span class="section-num">3.</span> Teste Diagnóstico de Nivelamento</h1>
    <p>Responda às 10 questões a seguir sem consultar o gabarito para avaliar sua prontidão conceitual e prática.</p>

    <div class="question-box">
      <div class="question-title">Questão 1 • Matemática de Retornos</div>
      <div>Ao montar uma carteira quantitativa com 40% em PETR4 e 60% em VALE3, qual metodologia matemática deve ser utilizada para calcular o retorno total diário do portfólio?</div>
      <div class="question-options">
        A) A média aritmética ponderada dos log-retornos dos ativos.<br>
        <strong>B) A média aritmética ponderada dos retornos simples dos ativos.</strong><br>
        C) A raiz quadrada do produto dos retornos simples.<br>
        D) O logaritmo da soma dos preços de fechamento dividido pelo volume.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 2 • Vieses de Backtest e Microestrutura</div>
      <div>Um analista cria um modelo multifatorial que utiliza a divulgação do balanço do 4º trimestre das empresas brasileiras (com data de referência em 31/12) para comprar ações no primeiro pregão de janeiro. Qual erro metodológico fatal foi cometido?</div>
      <div class="question-options">
        A) Viés de Sobrevivência (*Survivorship Bias*).<br>
        <strong>B) Viés de Antecipação (*Look-Ahead Bias*), pois os balanços reais do 4T só são protocolados na CVM em março ou abril.</strong><br>
        C) Erro de Especificação de Volatilidade por utilizar a raiz de 365 dias.<br>
        D) Erro de Curvatura de Juros por desconsiderar o cupom limpo.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 3 • Manipulação de Séries em Python / Pandas</div>
      <div>Dado um DataFrame <code>df</code> indexado por datas com os preços diários de uma ação na coluna <code>'close'</code>, qual comando em Pandas calcula corretamente os retornos diários simples preservando o alinhamento temporal?</div>
      <div class="question-options">
        A) <code>df['close'].diff() / df['close']</code><br>
        B) <code>np.log(df['close']) - np.log(df['close'].shift(-1))</code><br>
        <strong>C) <code>df['close'].pct_change().dropna()</code></strong><br>
        D) <code>df['close'].rolling(252).mean()</code>
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 4 • Estatística de Séries Temporais e Anualização</div>
      <div>Se uma ação da B3 apresenta uma volatilidade diária de 2,0% em um mercado com 252 dias úteis, qual é a estimativa correta da sua volatilidade anualizada sob a premissa de retornos i.i.d.?</div>
      <div class="question-options">
        A) \(2,0\% \times 252 = 504,0\%\)<br>
        <strong>B) \(2,0\% \times \sqrt{252} \approx 31,75\%\)</strong><br>
        C) \(2,0\% / \sqrt{252} \approx 0,126\%\)<br>
        D) \((1 + 0,02)^{252} - 1 \approx 145,2\%\)
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 5 • Métricas de Risco Assimétrico</div>
      <div>Por que gestores sistemáticos institucionais frequentemente preferem o <strong>Sortino Ratio</strong> em relação ao <strong>Sharpe Ratio</strong> para estratégias de ações com assimetria positiva?</div>
      <div class="question-options">
        A) O Sortino ignora o CDI e utiliza o dólar como referência.<br>
        <strong>B) O Sharpe Ratio penaliza ganhos expressivos para cima (*upside volatility*) da mesma forma que penaliza perdas severas, enquanto o Sortino foca exclusivamente no desvio para baixo (*downside deviation*).</strong><br>
        C) O Sortino Ratio não depende do número de observações da amostra.<br>
        D) O Sharpe Ratio só pode ser calculado para carteiras com mais de 50 ativos.
      </div>
    </div>

    <div class="page-break"></div>

    <div class="question-box">
      <div class="question-title">Questão 6 • Validação de Modelos em Séries Temporais</div>
      <div>Por que a aplicação direta do algoritmo de <em>K-Fold Cross-Validation</em> padrão do Scikit-Learn é inadequada e gera resultados ilusórios em séries financeiras?</div>
      <div class="question-options">
        <strong>A) Porque o K-Fold tradicional embaralha os dados ou treina com dados do futuro para prever o passado, causando vazamento de informação temporal (*data leakage*).</strong><br>
        B) Porque o K-Fold só funciona com variáveis categóricas binárias.<br>
        C) Porque o número de folds precisa ser exatamente igual ao número de ativos da carteira.<br>
        D) Porque o K-Fold dobra os custos operacionais do backtest.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 7 • Factor Investing</div>
      <div>Qual é a diferença fundamental entre uma estratégia de <strong>Cross-Sectional Momentum</strong> e uma estratégia de <strong>Time-Series Momentum (Trend Following)</strong>?</div>
      <div class="question-options">
        A) Cross-Sectional compra ações no Brasil e Time-Series compra apenas índices nos EUA.<br>
        <strong>B) Cross-Sectional compara ativos entre si no mesmo instante (comprando os melhores e vendendo os piores do universo relativo), enquanto Time-Series avalia o ativo contra o seu próprio histórico passado em termos absolutos.</strong><br>
        C) Cross-Sectional utiliza apenas médias móveis simples e Time-Series utiliza regressão linear múltipla.<br>
        D) Não há diferença; ambos os termos são sinônimos na literatura de Fama-French.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 8 • Atritos de Mercado e Execução Real</div>
      <div>Ao realizar o backtest de uma carteira de <em>Small Caps</em> na B3 com patrimônio de R$ 50 milhões, qual variável é determinante para evitar que o modelo compre papéis ilíquidos cuja execução real destruiria o alfa?</div>
      <div class="question-options">
        A) O Índice de Preços ao Consumidor Amplo (IPCA).<br>
        <strong>B) A restrição de participação máxima sobre o Volume Financeiro Médio Diário (ADTV) e modelagem de slippage.</strong><br>
        C) O número de seguidores do perfil da empresa nas redes sociais.<br>
        D) O valor contábil do patrimônio líquido dividido pelo número de cotistas.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 9 • Otimização de Portfólios de Markowitz</div>
      <div>Qual é o principal problema prático da Otimização de Média-Variância clássica de Markowitz quando aplicada diretamente em uma matriz de covariância amostral com dezenas de ações da B3?</div>
      <div class="question-options">
        A) O algoritmo não consegue calcular retornos positivos.<br>
        <strong>B) O algoritmo de Markowitz é um "maximizador de erros de estimativa", alocando pesos extremos e irrealistas em ativos com ruído estatístico, problema resolvido com técnicas de encolhimento como *Ledoit-Wolf Shrinkage*.</strong><br>
        C) Markowitz exige que todos os retornos sejam obrigatoriamente negativos.<br>
        D) O método de Markowitz não permite a inclusão de ações do setor elétrico.
      </div>
    </div>

    <div class="question-box">
      <div class="question-title">Questão 10 • Machine Learning Não-Supervisionado em Alocação</div>
      <div>Qual inovação a metodologia de <strong>Hierarchical Risk Parity (HRP)</strong>, desenvolvida por Marcos López de Prado, trouxe para a alocação quantitativa institucional?</div>
      <div class="question-options">
        <strong>A) Utiliza clusterização hierárquica (aprendizado não-supervisionado) na matriz de correlação, dispensando a necessidade de inversão da matriz de covariância e eliminando a instabilidade numérica de Markowitz.</strong><br>
        B) Automatiza a compra de opções binárias sem risco de perda.<br>
        C) Substitui o código Python por contratos inteligentes em blockchain.<br>
        D) Garante retorno garantido acima de 30% ao ano em qualquer cenário macro.
      </div>
    </div>

    <div class="page-break"></div>

    <!-- ================= PÁGINA 9-10: GABARITO & DIAGNÓSTICO ================= -->
    <h1><span class="section-num">4.</span> Gabarito Oficial Comentado</h1>
    
    <div class="answer-box">
      <div class="answer-title">Questão 1 • Resposta Correta: B</div>
      <div class="answer-desc">A agregação transversal de ativos na carteira obedece à linearidade dos retornos simples: \(R_p = \sum w_i R_i\). Somar log-retornos ponderados de múltiplos ativos gera distorções matemáticas graves.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 2 • Resposta Correta: B</div>
      <div class="answer-desc">Na B3, as companhias têm até 90 dias após o fim do ano fiscal para publicar o balanço do 4T. Utilizar dados de 31/12 em 02/01 é viés de antecipação (*look-ahead bias*), invalidando o backtest.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 3 • Resposta Correta: C</div>
      <div class="answer-desc">O método <code>.pct_change()</code> é a forma vetorizada e auditada nativa do Pandas para calcular \(\frac{P_t - P_{t-1}}{P_{t-1}}\).</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 4 • Resposta Correta: B</div>
      <div class="answer-desc">Sob a premissa de retornos i.i.d., a volatilidade escala com a raiz quadrada do tempo: \(\sigma_{anual} = 2,0\% \times \sqrt{252} \approx 31,75\%\).</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 5 • Resposta Correta: B</div>
      <div class="answer-desc">O Sharpe Ratio penaliza a volatilidade total (inclusive ganhos expressivos para cima). O Sortino isola apenas o *downside deviation*, premiando estratégias com assimetria positiva.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 6 • Resposta Correta: A</div>
      <div class="answer-desc">Séries temporais possuem ordem cronológica e autocorrelação. O K-Fold padrão mistura dados futuros no treino, criando vazamento temporal (*data leakage*). Usa-se *Purged Walk-Forward*.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 7 • Resposta Correta: B</div>
      <div class="answer-desc">Cross-sectional compara ativos entre si (compra os 10% melhores e vende os 10% piores). Time-series avalia a tendência do ativo em relação ao seu próprio histórico passado.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 8 • Resposta Correta: B</div>
      <div class="answer-desc">Em gestão institucional, o impacto de mercado (*slippage*) destrói estratégias com papéis ilíquidos. É obrigatório impor filtros sobre o ADTV (ex: máx. 10% do volume diário).</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 9 • Resposta Correta: B</div>
      <div class="answer-desc">A inversão da matriz amostral amplifica erros estatísticos. Técnicas de regularização como *Ledoit-Wolf Shrinkage* estabilizam os pesos e garantem aplicabilidade prática.</div>
    </div>

    <div class="answer-box">
      <div class="answer-title">Questão 10 • Resposta Correta: A</div>
      <div class="answer-desc">O algoritmo HRP utiliza aprendizado não-supervisionado para clusterizar a matriz de correlação e alocar risco recursivamente sem inverter matrizes de covariância.</div>
    </div>

    <h2>Régua de Nivelamento & Plano de Estudos</h2>
    <table style="width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 8.8pt;">
      <thead>
        <tr style="background: var(--primary-navy); color: white;">
          <th style="padding: 8px; text-align: left; width: 25%;">Acertos</th>
          <th style="padding: 8px; text-align: left; width: 35%;">Diagnóstico Institucional</th>
          <th style="padding: 8px; text-align: left; width: 40%;">Seu Foco Recomendado no Curso</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background: #F8FAFC; border-bottom: 1px solid #E2E8F0;">
          <td style="padding: 8px; font-weight: 700; color: #DC2626;">0 a 4 Acertos</td>
          <td style="padding: 8px;"><strong>Nível 1: Fundamentos / Em Transição</strong><br>Boa vontade analítica, mas vícios comuns de Data Science tradicional ou Excel.</td>
          <td style="padding: 8px;">Os <strong>Módulos 1 e 2</strong> serão decisivos para blindar sua infraestrutura de dados contra vieses temporais e dominar métricas de cauda.</td>
        </tr>
        <tr style="background: #FFFFFF; border-bottom: 1px solid #E2E8F0;">
          <td style="padding: 8px; font-weight: 700; color: #D97706;">5 a 7 Acertos</td>
          <td style="padding: 8px;"><strong>Nível 2: Analista Intermediário</strong><br>Boa base de Python e estatística básica, mas com lacunas em atritos reais e fatores.</td>
          <td style="padding: 8px;">Os <strong>Módulos 3 e 4</strong> levarão seus backtests para a régua de auditoria de gestoras buy-side (ADTV, slippage e factor ranking).</td>
        </tr>
        <tr style="background: #F0FDF4;">
          <td style="padding: 8px; font-weight: 700; color: #16A34A;">8 a 10 Acertos</td>
          <td style="padding: 8px;"><strong>Nível 3: Quant Desk Ready</strong><br>Excelente maturidade técnica e intuição apurada de microestrutura e risco.</td>
          <td style="padding: 8px;">Os <strong>Módulos 4, 5 e 6</strong> permitirão a você dominar técnicas avançadas como Ledoit-Wolf, HRP e montar estratégias completas prontas para produção.</td>
        </tr>
      </tbody>
    </table>

    <div class="callout callout-info" style="margin-top: 18px;">
      <div class="callout-title">🔒 Condição Exclusiva da Lista de Espera VIP</div>
      Ao preencher a landing page oficial, você já assegurou seu lugar prioritário para a 1ª Turma do <strong>Curso de Análise Quantitativa Aplicada</strong> com <strong>20% de desconto exclusivo</strong> e acesso direto às sessões de mentoria de código com o Dr. Lucca Simeoni Pavan.
    </div>

  </div>

</body>
</html>
"""

def main():
    print("=" * 60)
    print("🚀 Gerador de Kit de Nivelamento, Ementa & Teste Diagnóstico")
    print("=" * 60)
    
    html_prod = ROOT_DIR / "products" / "kit_nivelamento_e_ementa_analise_quantitativa.html"
    html_down = ROOT_DIR / "landing_pages" / "downloads" / "kit_nivelamento_e_ementa_analise_quantitativa.html"
    
    html_prod.write_text(KIT_HTML_TEMPLATE, encoding="utf-8")
    html_down.write_text(KIT_HTML_TEMPLATE, encoding="utf-8")
    print("✅ HTMLs gravados com sucesso em products/ e landing_pages/downloads/")
    
    pdf_prod = ROOT_DIR / "products" / "Kit_Nivelamento_e_Ementa_Analise_Quantitativa.pdf"
    pdf_down = ROOT_DIR / "landing_pages" / "downloads" / "Kit_Nivelamento_e_Ementa_Analise_Quantitativa.pdf"
    
    print(f"⏳ Convertendo HTML para PDF de alta resolução...")
    success = convert_html_to_pdf(str(html_prod), str(pdf_prod))
    
    if success and pdf_prod.exists():
        size_kb = pdf_prod.stat().st_size / 1024
        print(f"✅ PDF gerado com sucesso em products! Tamanho: {size_kb:.1f} KB")
        shutil.copy2(str(pdf_prod), str(pdf_down))
        print(f"✅ PDF copiado para landing_pages/downloads/Kit_Nivelamento_e_Ementa_Analise_Quantitativa.pdf")
    else:
        print("❌ Falha na conversão para PDF.")

if __name__ == "__main__":
    main()
