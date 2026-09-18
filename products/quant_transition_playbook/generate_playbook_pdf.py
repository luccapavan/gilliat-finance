"""
Compilador Expandido do Playbook para PDF (Edição Completa de ~15 Páginas)
The Quant Transition Playbook - Edição Completa & Institucional
Autor: Lucca Simeoni Pavan, Ph.D.
"""
import os
import sys
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from pdf_engine.builder import convert_html_to_pdf

PLAYBOOK_HTML_PT_FULL = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>The Quant Transition Playbook - Lucca Simeoni Pavan, Ph.D.</title>
  <link rel="stylesheet" href="../../pdf_engine/theme.css">
  <style>
    .section-num { color: var(--accent-cyan); font-weight: 700; margin-right: 6px; }
    .toc-item { display: flex; justify-content: space-between; border-bottom: 1px dotted var(--border-light); padding: 5px 0; margin-bottom: 3px; font-size: 9.5pt; }
    .toc-page { font-family: 'JetBrains Mono', monospace; font-weight: 600; color: var(--accent-blue); }
    .formula-box {
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      border-left: 4px solid var(--primary-navy);
      padding: 12px 18px;
      margin: 14px 0;
      border-radius: 4px;
      text-align: center;
    }
    mjx-container[jax="SVG"] {
      font-size: 110% !important;
    }
    mjx-container[jax="SVG"][display="true"] {
      margin: 6px 0 !important;
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

  <!-- ================= CAPA EXECUTIVA (PÁGINA 1) ================= -->
  <div class="cover-page">
    <div class="cover-header">
      <span class="cover-badge">MANUAL METODOLÓGICO & MODELAGEM QUANTITATIVA</span>
      <div class="cover-title">THE QUANT TRANSITION<br>PLAYBOOK</div>
      <div class="cover-subtitle">Da Academia & Ciência de Dados para a Indústria de Gestão Sistemática de Recursos</div>
      <div class="cover-accent-line"></div>
    </div>

    <div style="margin: 20px 0;">
      <div style="font-family: 'JetBrains Mono', monospace; font-size: 8.5pt; color: #94A3B8; line-height: 2.0;">
        <div>▪ Módulo 1: Taxonomia do Mercado Quant Global & Estratégias Sistemáticas</div>
        <div>▪ Módulo 2: Engenharia de Fatores, Ortogonalização FWL & Neutralização</div>
        <div>▪ Módulo 3: Protocolo Institucional Anti-Vieses & Validação Purged K-Fold</div>
        <div>▪ Módulo 4: Otimização de Portfólio, Shrinkage de Ledoit-Wolf & Risco de Cauda</div>
        <div>▪ Módulo 5: Blueprint de Contratação, Testes Take-Home 48h & Engenharia de GitHub</div>
        <div>▪ Módulo 6: Especificação e Guia de Execução dos Motores em Python</div>
      </div>
    </div>

    <div class="cover-footer">
      <p class="author-name">Lucca Simeoni Pavan, Ph.D.</p>
      <p class="author-title">Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação</p>
      <p class="author-desc">Doutor em Economia • Especialista em Factor Investing, Séries Temporais, Alocação & Risco</p>
    </div>
  </div>

  <!-- ================= PÁGINA 2: SUMÁRIO & CARTA DO AUTOR ================= -->
  <div class="content-wrapper">
    <h1>Sumário & Apresentação da Obra</h1>
    
    <p>O mercado de finanças quantitativas (<em>Quantitative Finance</em>) representa a fronteira intelectual do mercado de capitais moderno. Durante décadas, as principais decisões de alocação de ativos foram dominadas por teses discricionárias, reuniões de comitê e intuições de gestores. No entanto, o crescimento exponencial no volume de dados, a microestrutura eletrônica de negociação e os avanços em econometria empírica consolidaram a gestão sistemática como o padrão de excelência institucional.</p>

    <p>Este manual foi concebido para fechar uma lacuna crítica: a distância entre o rigor teórico dos programas de pós-graduação (Mestrados e Doutorados em Economia, Estatística, Física ou Engenharia) e as exigências operacionais diárias de uma mesa quantitativa institucional. Aqui você não encontrará jargões superficiais de redes sociais, mas sim os fundamentos metodológicos, fórmulas, armadilhas reais e códigos funcionais necessários para atuar no mercado de alta performance.</p>

    <h2>Índice Geral do Playbook</h2>
    <div style="margin: 15px 0;">
      <div class="toc-item"><span><strong>Módulo 1:</strong> A Taxonomia do Mercado Quant & Estrutura de Negócios</span><span class="toc-page">Pág. 3</span></div>
      <div class="toc-item"><span><strong>Módulo 2:</strong> Engenharia de Fatores & Factor Investing de Ponta</span><span class="toc-page">Pág. 5</span></div>
      <div class="toc-item"><span><strong>Módulo 3:</strong> Protocolo Institucional Anti-Vieses de Backtesting</span><span class="toc-page">Pág. 7</span></div>
      <div class="toc-item"><span><strong>Módulo 4:</strong> Otimização de Carteiras & Gestão de Risco de Cauda</span><span class="toc-page">Pág. 10</span></div>
      <div class="toc-item"><span><strong>Módulo 5:</strong> Blueprint de Contratação, Take-Home Tests & GitHub</span><span class="toc-page">Pág. 12</span></div>
      <div class="toc-item"><span><strong>Módulo 6:</strong> Manual dos Motores em Python & Considerações Finais</span><span class="toc-page">Pág. 13</span></div>
    </div>

    <div class="callout callout-info">
      <div class="callout-title">💡 Como Utilizar Este Material</div>
      Recomenda-se a leitura sequencial. Ao avançar pelos capítulos teóricos de engenharia de fatores e controle de risco, abra simultaneamente os scripts em Python que acompanham o pacote (<code>backtest_multifactor.py</code> e <code>risk_performance_metrics.py</code>) para verificar como cada conceito matemático se traduz em código vetorizado pronto para produção.
    </div>

    <div class="page-break"></div>

    <!-- ================= PÁGINA 3-4: MÓDULO 1 ================= -->
    <h1><span class="section-num">1.</span> A Taxonomia do Mercado Quant & Negócios</h1>
    
    <p>Ao ingressar na indústria de gestão sistemática, o pesquisador se depara com uma pluralidade de mandatos, horizontes temporais e classes de ativos. Compreender a taxonomia dos fundos é essencial para direcionar sua pesquisa ao modelo de negócios adequado.</p>

    <h2>1.1 As Quatro Grandes Famílias Sistemáticas</h2>

    <h3>1. Factor Investing & Smart Beta (Ações / Long-Only & Long/Short)</h3>
    <p>A premissa fundamental do investimento em fatores é que retornos excedentes a longo prazo não decorrem de sorte ou "escolha de ações", mas sim da exposição disciplinada a prêmios de risco sistemáticos amplamente documentados na literatura empírica (Fama-French, Carhart, Asness). A frequência de giro de carteira é de baixa a média (rebalanceamentos mensais ou trimestrais), exigindo foco em métricas fundamentais, governança de dados point-in-time e controle estrito de turnover.</p>

    <h3>2. Arbitragem Estatística (StatArb & Pairs Trading)</h3>
    <p>Estratégias baseadas na identificação de distorções temporárias de preço entre ativos economicamente relacionados (ações de um mesmo setor, contratos futuros de diferentes vencimentos ou ADRs versus ativos locais). Utilizam ferramentas como testes de cointegração de Engle-Granger e Johansen, Filtros de Kalman para estimar coeficientes variantes no tempo e modelos de microestrutura para explorar reversão à média (<em>mean reversion</em>). O horizonte varia de intradiário a alguns dias.</p>

    <h3>3. Trend-Following & CTAs (Commodity Trading Advisors)</h3>
    <p>Operam posições direcionais compradas ou vendidas em dezenas de mercados futuros globais (taxas de juros, moedas, índices e commodities). A tese econômica baseia-se na existência de tendências de preços prolongadas provocadas por fluxos institucionais de proteção (<em>hedging</em>) e reações atrasadas de investidores discricionários. O gerenciamento de risco é orientado pelo controle dinâmico de volatilidade (<em>volatility targeting</em>).</p>

    <h3>4. Paridade de Risco (Risk Parity & All-Weather)</h3>
    <p>Popularizada por Ray Dalio e Edward Qian, a paridade de risco equaliza a contribuição de risco marginal de cada classe de ativos (ações, títulos públicos nominais, títulos indexados à inflação e commodities) em vez de alocar capital monetário igualitariamente. Emprega alavancagem em classes de menor volatilidade para alcançar o perfil desejado de retorno com proteção assimétrica contra diferentes regimes macroeconômicos.</p>

    <div class="page-break"></div>

    <h2>1.2 A Divisão do Trabalho Técnico na Gestora</h2>
    <table>
      <thead>
        <tr>
          <th>Papel Técnico</th>
          <th>Responsabilidades Primárias</th>
          <th>Stack Tecnológico Típico</th>
          <th>Métrica de Sucesso</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Quant Researcher</strong></td>
          <td>Formulação de hipóteses econômicas, teste e ortogonalização de fatores, higienização point-in-time e validação out-of-sample.</td>
          <td>Python (pandas, numpy, statsmodels, scikit-learn), R, SQL, Polars.</td>
          <td>Information Ratio (IR), consistência de Sharpe e t-stats de alfa residual.</td>
        </tr>
        <tr>
          <td><strong>Quant Developer</strong></td>
          <td>Engenharia de pipelines de dados, otimização de motores de backtesting orientados a eventos e conectividade de baixa latência com corretoras.</td>
          <td>C++, Rust, Python avançado, Cython, Kafka, Docker, Kubernetes.</td>
          <td>Latência de processamento, uptime de infraestrutura e fidelidade de slippage.</td>
        </tr>
        <tr>
          <td><strong>Risk / Portfolio Manager</strong></td>
          <td>Dimensionamento de posições, testes de estresse histórico e macroeconômico, cálculo de métricas de cauda (VaR/CVaR) e monitoramento de limites.</td>
          <td>Python, SQL, R, otimizadores quadráticos e cônicos (CVXPY, MOSEK).</td>
          <td>Controle de Maximum Drawdown, aderência a limites regulatórios e beta residual.</td>
        </tr>
      </tbody>
    </table>

    <h2>1.3 O Stack Tecnológico Institucional</h2>
    <p>Existe uma convenção bem estabelecida na indústria: <strong>Python para Pesquisa, C++/Rust para Execução</strong>. No ecossistema de pesquisa, o domínio de bibliotecas vetoriais (NumPy, pandas e Polars) é inegociável. Candidatos que escrevem loops <code>for</code> manuais para iterar sobre preços diários são desqualificados instantaneamente. O mercado exige código vetorizado que explore operações matriciais em memória.</p>

    <div class="page-break"></div>

    <!-- ================= PÁGINA 5-7: MÓDULO 2 ================= -->
    <h1><span class="section-num">2.</span> Engenharia de Fatores & Factor Investing</h1>

    <p>A construção de carteiras quantitativas de ações baseia-se na identificação de atributos mensuráveis que explicam o corte transversal dos retornos esperados. O desafio de um Quant Researcher sênior não é encontrar dados; é transformar sinais brutos barulhentos em fatores ortogonais robustos.</p>

    <h2>2.1 Os Cinco Fatores Fundamentais</h2>
    <ul>
      <li><strong>Momentum (Mom):</strong> A tendência documentada de ativos com performance superior nos últimos 3 a 12 meses continuarem superando os pares. A formulação padrão (Jegadeesh & Titman) ranqueia ativos pela rentabilidade acumulada de 12 meses excluindo o mês imediatamente anterior (\(t-12\) a \(t-2\)), eliminando o ruído de reversão à média de curto prazo.</li>
      <li><strong>Value (Val):</strong> A preferência por empresas com preços deprimidos em relação aos fundamentos contábeis. Métricas clássicas: Earnings Yield (\(E/P\)), Book-to-Market (\(B/M\)) e Enterprise Value sobre EBITDA (\(EV/EBITDA\)).</li>
      <li><strong>Quality (Qual):</strong> Empresas com alta rentabilidade sobre o capital investido, fluxos de caixa operacionais consistentes e baixo endividamento. Indicadores: ROIC, ROE, Margem Operacional e Z-Score de Altman.</li>
      <li><strong>Low Volatility (LowVol):</strong> A chamada "anomalia de baixa volatilidade", que desafia o CAPM tradicional: ações com menor variância histórica ou menor beta frequentemente entregam retornos ajustados ao risco superiores a ações ultra voláteis.</li>
      <li><strong>Size (Tamanho):</strong> O prêmio histórico de pequenas empresas (Small Caps) sobre grandes conglomerados (Large Caps), compensando menor liquidez e maior sensibilidade a ciclos econômicos.</li>
    </ul>

    <h2>2.2 O Processo Matemático de Padronização</h2>
    <p>Como variáveis contábeis e de preço possuem ordens de magnitude díspares (por exemplo, um múltiplo P/L varia de 5 a 30, enquanto o Momentum varia de -50% a +80%), é obrigatório padronizar as features a cada corte transversal (<em>cross-section</em>):</p>

    <div class="formula-box">
      $$Z_{i,t} = \frac{X_{i,t} - \mu_t(X)}{\sigma_t(X)}$$
    </div>

    <p><strong>Winsorização:</strong> Antes da padronização, valores extremos que distorcem a média devem ser limitados (geralmente nos percentis 1% e 99% ou a \(\pm 3\sigma\)), evitando que uma única empresa anômala domine os pesos da carteira.</p>

    <div class="page-break"></div>

    <h2>2.3 Ortogonalização via Teorema de Frisch-Waugh-Lovell (FWL)</h2>
    <p>Um dos maiores perigos na pesquisa empírica é o chamado "Factor Zoo": publicar sinais que aparentam gerar alfa, mas que na realidade são meras combinações lineares de fatores já conhecidos. Para validar se um novo sinal possui mérito independente, aplica-se o <strong>Teorema de Frisch-Waugh-Lovell</strong>.</p>

    <p>Considere o modelo de precificação onde desejamos estimar o efeito do fator \(F_1\) sobre os retornos \(Y\), controlando por uma matriz de fatores existentes \(X\):</p>

    <div class="formula-box">
      $$Y = X\beta + F_1\gamma + \varepsilon$$
    </div>

    <p>O Teorema FWL estabelece que a estimativa MQO de \(\gamma\) é matematicamente idêntica à obtida por este procedimento em 2 etapas:</p>
    <ol>
      <li>Regrida \(F_1\) sobre \(X\) e obtenha os resíduos \(\tilde{F}_1 = M_X F_1\), onde \(M_X\) é a matriz de aniquilação (projeção ortogonal);</li>
      <li>Regrida \(Y\) sobre os resíduos \(\tilde{F}_1\). O coeficiente obtido é rigorosamente o mesmo \(\gamma\).</li>
    </ol>

    <div class="formula-box">
      $$\tilde{F}_1 = M_X F_1 = \left(I - X(X'X)^{-1}X'\right)F_1 \quad \implies \quad \hat{\gamma} = \left(\tilde{F}_1'\tilde{F}_1\right)^{-1}\tilde{F}_1' Y$$
    </div>

    <div class="callout callout-warning">
      <div class="callout-title">⚠️ Aplicação Institucional do FWL</div>
      Ao projetar seu sinal de interesse sobre os fatores de mercado e tamanho antes de ranquear a carteira, você garante que a estratégia operará com <strong>Beta rigorosamente neutro</strong> em relação aos pilares concorrentes.
    </div>

    <h2>2.4 Neutralização de Portfólio</h2>
    <p>Uma carteira quantitativa com verdadeiro valor agregado não deve ser uma "aposta direcional de mercado disfarçada". Aplica-se:</p>
    <ul>
      <li><strong>Dollar Neutrality:</strong> O valor financeiro da ponta comprada iguala exatamente a ponta vendida (\(\sum w_i^{\text{long}} = \sum |w_i^{\text{short}}| = 1\)).</li>
      <li><strong>Sector Neutrality:</strong> A exposição líquida em cada setor econômico (ex: Financeiro, Petróleo, Varejo) é restrita a zero, forçando o modelo a extrair alfa puro intra-setorial em vez de fazer timing macroeconômico setorial.</li>
    </ul>

    <div class="page-break"></div>

    <!-- ================= PÁGINA 8-10: MÓDULO 3 ================= -->
    <h1><span class="section-num">3.</span> O Protocolo Institucional Anti-Vieses</h1>

    <p>Nas palavras do pesquisador Marcos López de Prado, a maioria das descobertas financeiras publicadas em backtests são falsas. Nesta seção, detalhamos os quatro vieses sistemáticos que destroem estratégias ao entrarem em ambiente de negociação real.</p>

    <h2>3.1 Os Quatro Vieses que Invalidam um Backtest</h2>

    <h3>1. Look-Ahead Bias (Viés de Olhar à Frente)</h3>
    <p>Ocorre quando dados indisponíveis no momento da decisão histórica vazam para a lógica do algoritmo. Exemplo: utilizar dados de balanço patrimonial referente ao 4º trimestre (fechado em 31/12) nos primeiros dias de janeiro. Na prática brasileira, a demonstração contábil oficial só é protocolada na CVM 60 a 90 dias após o fechamento do exercício social. Decisões tomadas antes do timestamp efetivo de publicação são fictícias.</p>

    <h3>2. Survivorship Bias (Viés de Sobrevivência)</h3>
    <p>Ocorre quando a base histórica de ativos inclui unicamente empresas negociadas hoje. As centenas de empresas que enfrentaram liquidação, recuperação judicial ou cancelamento de registro na B3 ao longo dos últimos 15 anos são apagadas da amostra. Testar uma estratégia sem esses ativos infla artificialmente os retornos em até 600 bps anuais.</p>

    <h3>3. Overfitting & Data Snooping (p-hacking)</h3>
    <p>Com poder computacional moderno, testar 10.000 combinações de médias móveis ou hiperparâmetros garante que, pelo menos por acaso estatístico, dezenas de combinações parecerão excepcionais na amostra histórica. Esse fenômeno é governado pela distribuição do máximo de variáveis aleatórias (Teorema de Valores Extremos). Quando a estratégia entra em produção, a correlação espúria quebra imediatamente.</p>

    <h3>4. Negligência de Fricções de Microestrutura</h3>
    <p>Um backtest que ignora spread bid-ask dinâmico, taxas de empréstimo de ações (BTC/short fees) e o impacto não-linear de mercado é puramente teórico. Na B3, ordens de magnitude institucional em papéis de menor liquidez distorcem o livro de ofertas.</p>

    <div class="page-break"></div>

    <h2>3.2 Modelo de Impacto de Mercado de Almgren-Chriss</h2>
    <p>Em gestão profissional, o custo de execução é decomposto segundo a formulação de Almgren e Chriss (2000):</p>

    <div class="formula-box">
      $$\text{Custo Total} = \text{Spread Bid-Ask} + \eta \left(\frac{Q}{\tau}\right)^\alpha + \gamma Q$$
    </div>

    <p>Onde o primeiro termo representa o custo imediato de cruzar o spread; o segundo termo representa o <strong>Impacto Temporário</strong> (consumo passageiro da liquidez do livro); e o terceiro termo representa o <strong>Impacto Permanente</strong> (informação introduzida no mercado pela agressão da sua ordem, movendo o preço de equilíbrio definitivamente).</p>

    <h2>3.3 A Lei da Raiz Quadrada</h2>
    <p>Pesquisas empíricas globais (Barra, Bloomberg, AQR) confirmam que o impacto de mercado escala de forma côncava com a raiz quadrada do volume relativo da ordem:</p>

    <div class="formula-box">
      $$\text{Impacto} \approx Y \cdot \sigma_{\text{diária}} \cdot \sqrt{\frac{Q}{\text{ADV}}}$$
    </div>

    <p>Onde \(Q\) é a quantidade executada, \(\text{ADV}\) é o Volume Médio Diário e \(Y \approx 0.5 - 0.7\) é uma constante empírica. Essa relação impõe o que chamamos de <strong>Fronteira de Capacidade da Estratégia</strong>: o patrimônio líquido máximo que o modelo pode absorver antes que o custo de mercado devore 100% do alfa.</p>

    <div class="page-break"></div>

    <h2>3.4 Validação Cruzada Purged K-Fold com Embargo</h2>
    <p>O método tradicional de K-Fold aleatório é estritamente proibido em séries temporais financeiras. Como retornos de ativos apresentam autocorrelação e variáveis de fatores utilizam janelas móveis de cálculo (overlapping), pontos de teste vazam informação diretamente para os pontos de treino.</p>

    <div class="callout callout-danger">
      <div class="callout-title">📌 O Protocolo Purged K-Fold (López de Prado)</div>
      1. <strong>Expurgo (Purging):</strong> Elimina do conjunto de treino todas as observações cujas janelas temporais de cálculo de retorno se sobreponham ao início do conjunto de teste.<br>
      2. <strong>Embargo (Quarentena):</strong> Adiciona um período de espera imediatamente após o final do bloco de teste (geralmente 1 a 3 meses) antes de iniciar novo bloco de treino, neutralizando efeitos de memória autorregressiva residual.
    </div>

    <h2>3.5 O Deflated Sharpe Ratio (DSR)</h2>
    <p>Para corrigir a inflação do Sharpe Ratio resultante de múltiplos testes de hipóteses sobre os mesmos dados históricos, aplica-se o <em>Deflated Sharpe Ratio</em>:</p>

    <div class="formula-box">
      $$\text{DSR} \equiv \text{PSR}\left(\text{SR}^*\right) = \Phi\left[ \frac{\left(\widehat{\text{SR}} - \text{SR}^*\right)\sqrt{T-1}}{\sqrt{1 - \hat{\gamma}_3 \widehat{\text{SR}} + \frac{\hat{\gamma}_4 - 1}{4}\widehat{\text{SR}}^2}} \right]$$
    </div>

    <p>Onde \(\widehat{\text{SR}}\) é o Sharpe observado, \(\text{SR}^*\) é o benchmark ajustado pelo número de tentativas \(N\), \(\Phi\) é a função de distribuição acumulada normal padrão, e \(\hat{\gamma}_3\) e \(\hat{\gamma}_4\) são a assimetria e curtose dos retornos.</p>

    <div class="page-break"></div>

    <!-- ================= PÁGINA 11-12: MÓDULO 4 ================= -->
    <h1><span class="section-num">4.</span> Otimização de Carteiras & Gestão de Risco</h1>

    <p>A determinação dos pesos finais dos ativos em uma carteira multifator representa a etapa de síntese entre os sinais de alfa e as restrições de capital. A abordagem ingênua de média-variância frequentemente colapsa na prática.</p>

    <h2>4.1 A Falha de Markowitz & Matrizes Mal-Condicionadas</h2>
    <p>A otimização de média-variância busca minimizar a variância da carteira \(w' \Sigma w\). A solução analítica do portfólio de variância mínima exige a inversão da matriz de covariância (\(\Sigma^{-1}\)):</p>

    <div class="formula-box">
      $$\min_{w} w' \Sigma w \quad \text{sujeito a} \quad w'\mathbf{1} = 1 \quad \implies \quad w^* = \frac{\Sigma^{-1}\mathbf{1}}{\mathbf{1}'\Sigma^{-1}\mathbf{1}}$$
    </div>

    <p>No entanto, para \(N = 100\) ativos e \(T = 252\) dias de histórico, a razão \(N/T \approx 0.40\) introduz imenso erro amostral. Pela teoria das matrizes aleatórias (Marchenko-Pastur), os menores autovalores amostrais são artificialmente rebaixados pelo ruído. Ao inverter \(\Sigma\), esses autovalores invertidos viram gigantescos, atribuindo pesos extremos e instáveis justamente aos ativos cujas variâncias foram subestimadas pelo acaso.</p>

    <h2>4.2 Encolhimento de Ledoit-Wolf (Linear Shrinkage)</h2>
    <p>Olivier Ledoit e Michael Wolf desenvolveram uma solução matematicamente rigorosa: em vez de confiar na matriz amostral pura \(S\), encolhe-se a matriz em direção a uma matriz estruturada alvo \(F\) (como correlações constantes ou modelo de fator único):</p>

    <div class="formula-box">
      $$\Sigma_{\text{LW}} = \alpha^* F + (1 - \alpha^*) S$$
    </div>

    <p>O parâmetro de encolhimento \(\alpha^* \in [0, 1]\) é calculado analiticamente para minimizar a perda quadrática esperada sob a norma de Frobenius, restaurando o condicionamento e reduzindo drasticamente a volatilidade fora da amostra.</p>

    <div class="page-break"></div>

    <h2>4.3 Métricas Coerentes de Risco de Cauda</h2>
    <p>Gestores de risco institucionais avaliam estratégias através de métricas de preservação de capital que superam as limitações do índice de Sharpe simples:</p>

    <table>
      <thead>
        <tr>
          <th>Métrica de Risco</th>
          <th>Formulação Conceitual</th>
          <th>Interpretação Prática</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Sortino Ratio</strong></td>
          <td>$$\text{Sortino} = \frac{\mathbb{E}[R_p - R_f]}{\sqrt{\frac{1}{T}\sum_{t=1}^T \min(0, R_{p,t} - R_f)^2}}$$</td>
          <td>Não penaliza a volatilidade positiva (retornos acima da taxa livre de risco).</td>
        </tr>
        <tr>
          <td><strong>Calmar Ratio</strong></td>
          <td>$$\text{Calmar} = \frac{\text{CAGR}}{|\text{Max Drawdown}|}$$</td>
          <td>Mede a taxa de retorno anualizada em relação à pior queda histórica acumulada.</td>
        </tr>
        <tr>
          <td><strong>Value at Risk (VaR 95%)</strong></td>
          <td>$$\text{VaR}_{95\%} = \mu - 1.645 \cdot \sigma$$</td>
          <td>Perda máxima esperada para 95% dos dias sob condições normais de mercado.</td>
        </tr>
        <tr>
          <td><strong>Conditional VaR (CVaR 95%)</strong></td>
          <td>$$\text{CVaR}_{95\%} = \mathbb{E}\left[R \mid R \le \text{VaR}_{95\%}\right]$$</td>
          <td>Média das perdas nos 5% piores cenários. Medida estatisticamente <em>coerente</em> de risco.</td>
        </tr>
      </tbody>
    </table>

    <div class="page-break"></div>

    <!-- ================= PÁGINA 13-14: MÓDULO 5 ================= -->
    <h1><span class="section-num">5.</span> O Blueprint de Contratação & Take-Home Tests</h1>

    <p>Processos seletivos para vagas de Quant Researcher ou Engenheiro de Dados em gestoras de recursos envolvem a resolução de desafios técnicos práticos para casa (<em>take-home challenges</em>) com prazos de 48 a 72 horas. Esta seção detalha como estruturar uma entrega de nível sênior.</p>

    <h2>5.1 Estrutura de Pastas do Repositório Modelo</h2>
    <p>Um candidato que envia um arquivo <code>.zip</code> com um único notebook monolítico é descartado. A entrega esperada segue a arquitetura de software profissional:</p>

    <pre><code>quant_project/
├── data/                  # Scripts de ETL e caching point-in-time
│   ├── fetcher.py         # Ingestão de dados com tratamento de splits/dividendos
│   └── universe.py        # Filtro de liquidez mínima (ex: R$ 5M/dia)
├── src/
│   ├── factors.py         # Cálculo de fatores e Z-Scores transversais
│   ├── orthogonalize.py   # Projeção matricial FWL para neutralização
│   ├── optimizer.py       # Alocador de pesos (Ledoit-Wolf / Risk Parity)
│   └── backtest.py        # Motor de simulação vetorial com custos
├── tests/
│   ├── test_lookahead.py  # Teste unitário em pytest garantindo shift(1)
│   └── test_shapes.py     # Verificação de alinhamento matricial
├── notebooks/
│   └── research_walkthrough.ipynb # Visualização executiva dos resultados
├── README.md              # Racional econômico, hipóteses e conclusões
└── requirements.txt       # Dependências com versões congeladas</code></pre>

    <h2>5.2 As Perguntas Frequentes em Sabatinas Técnicas</h2>
    <div class="callout callout-info">
      <div class="callout-title">Q1: "Por que não aplicar PCA diretamente em retornos para gerar fatores?"</div>
      <strong>Resposta Modelo:</strong> O PCA é uma técnica puramente estatística e não supervisionada. O primeiro componente principal captura o fator de mercado comum, mas os componentes subsequentes sofrem com instabilidade temporal e falta de interpretabilidade econômica. Fatores fundamentais baseados em premissas econômicas prévias oferecem maior persistência out-of-sample.
    </div>

    <div class="callout callout-warning">
      <div class="callout-title">Q2: "Como você trataria quebras estruturais em séries financeiras?"</div>
      <strong>Resposta Modelo:</strong> Séries financeiras não são ergódicas. Aplica-se testes de quebra estrutural (Chow, Bai-Perron) e janelas móveis com decaimento exponencial de pesos (<em>exponential weighting</em>), calibrando a meia-vida do sinal para absorver transições de regime de taxa de juros e volatilidade.
    </div>

    <div class="page-break"></div>

    <!-- ================= PÁGINA 15: MÓDULO 6 ================= -->
    <h1><span class="section-num">6.</span> Manual de Execução dos Scripts em Python</h1>

    <p>Como parte integrante deste Playbook, disponibilizamos dois módulos em Python projetados com arquitetura modular, comentários didáticos e total ausência de look-ahead bias:</p>

    <h2>6.1 `backtest_multifactor.py`</h2>
    <p>Implementa um pipeline de ponta a ponta para carteiras de ações:</p>
    <ul>
      <li><strong>Cálculo do Momentum 12-2:</strong> <code>prices.shift(21) / prices.shift(252) - 1</code>.</li>
      <li><strong>Cálculo de Múltiplo de Valor:</strong> Inverso do Preço/Lucro (<code>Earnings Yield = 1.0 / PE</code>).</li>
      <li><strong>Padronização Matricial:</strong> Z-Score de corte transversal período a período.</li>
      <li><strong>Neutralização de Look-Ahead:</strong> <code>execution_weights = portfolio_weights.shift(1).fillna(0.0)</code>.</li>
      <li><strong>Dedução Dinâmica de Custos:</strong> Cálculo do turnover diário multiplicado pela taxa de atrito operacional.</li>
    </ul>

    <h2>6.2 `risk_performance_metrics.py`</h2>
    <p>Calcula o sumário executivo institucional de performance e cauda:</p>
    <ul>
      <li>CAGR (Taxa Geométrica de Crescimento Anual);</li>
      <li>Volatilidade Anualizada corrigida por \(\sqrt{252}\);</li>
      <li>Índices de Sharpe, Sortino e Calmar;</li>
      <li>Maximum Drawdown e duração de recuperação do topo histórico;</li>
      <li>VaR Paramétrico, VaR Histórico e Conditional VaR (Expected Shortfall) a 95% de confiança.</li>
    </ul>

    <h2>Considerações Finais</h2>
    <p>A transição da teoria acadêmica para a gestão sistemática de recursos não exige o abandono do rigor científico; pelo contrário, exige a elevação desse rigor a um nível em que hipóteses imperfeitas são punidas com perda financeira real. O pesquisador que alia disciplina estatística, domínio de microestrutura e qualidade de engenharia de software posiciona-se na vanguarda do mercado de capitais global.</p>

    <div style="margin-top: 50px; border-top: 2px solid var(--primary-navy); padding-top: 20px; font-size: 9pt; color: var(--text-muted); text-align: center;">
      <strong>The Quant Transition Playbook</strong> • Elaborado por Lucca Simeoni Pavan, Ph.D.<br>
      Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação • Todos os direitos reservados.
    </div>
  </div>

</body>
</html>
"""

def build_full_playbook_pdf_pt():
    html_path = Path("products/quant_transition_playbook/playbook_render_pt_full.html")
    pdf_path = Path("products/The_Quant_Transition_Playbook.pdf")
    
    html_path.parent.mkdir(parents=True, exist_ok=True)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(PLAYBOOK_HTML_PT_FULL)
        
    print("Compilando Playbook COMPLETO em Português (~15 páginas com fórmulas em LaTeX/MathJax)...")
    success = convert_html_to_pdf(str(html_path), str(pdf_path))
    
    if success:
        size_kb = pdf_path.stat().st_size / 1024
        print(f"[OK] PDF em Português gerado com sucesso!")
        print(f"Arquivo: {pdf_path.resolve()} ({size_kb:.1f} KB)")
        return str(pdf_path)
    else:
        print("[!] Erro ao gerar o PDF em Português.")
        return None

if __name__ == "__main__":
    build_full_playbook_pdf_pt()
