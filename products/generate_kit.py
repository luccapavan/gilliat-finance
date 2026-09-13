import os
import sys
import subprocess
from pathlib import Path

ROOT_DIR = Path(rc:\Users\CLIENTE\linkedin_money)
PRODUCTS_DIR = ROOT_DIR / products
DOWNLOADS_DIR = ROOT_DIR / landing_pages / downloads

sys.path.append(str(ROOT_DIR))
from pdf_engine.builder import convert_html_to_pdf

MD_CONTENT = "# KIT INSTITUCIONAL DE ENTRADA: EMENTA, GUIA TÉCNICO E TESTE DE NIVELAMENTO
### *Curso de Análise Quantitativa Aplicada: Modelagem Sistemática, Factor Investing e Gestão de Risco em Python*

**Autor e Instrutor:** Lucca Simeoni Pavan, Ph.D.  
*Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação • Doutor em Economia (UFPR)*  
**Material Exclusivo para Inscritos na Lista de Espera VIP**

---

## 🧭 Bem-vindo ao Seu Ponto de Partida Quant

Este kit foi elaborado para ser um divisor de águas na sua jornada rumo ao mercado financeiro quantitativo institucional. Ele está estruturado em três partes complementares:

1. **Parte 1: Ementa Oficial e Estrutura do Curso:** O currículo completo e detalhado de 30 horas de imersão prática para você conhecer exatamente as habilidades e modelos que construirá do zero.
2. **Parte 2: Guia de Nivelamento Técnico:** As fundações matemáticas, estatísticas e computacionais indispensáveis (com script Python pronto para rodar com ativos da B3).
3. **Parte 3: Teste Diagnóstico de Nivelamento (Autoavaliação):** 10 questões práticas baseadas em desafios reais de buy-side, acompanhadas de gabarito comentado e régua de pontuação para diagnosticar o seu nível de prontidão quant.

---

# PARTE 1: EMENTA OFICIAL DO CURSO

* **Nome do Curso:** Análise Quantitativa Aplicada: Modelagem Sistemática, Factor Investing e Gestão de Risco em Python
* **Carga Horária:** 30 horas (Aulas ao vivo/gravadas + Laboratórios Práticos de Código).
* **Stack Tecnológica:** Python 3.10+, Pandas, NumPy, Statsmodels, SciPy, Matplotlib, Seaborn, yfinance, python-bcb.
* **Objetivo Geral:** Capacitar analistas, economistas e cientistas de dados a estruturarem pipelines quantitativos completos, desde a coleta e tratamento de dados da B3 até o backtesting sem vieses e a alocação robusta de portfólios sistemáticos nos mesmos moldes adotados pelas principais gestoras do mercado.

---

### Módulo 1: Infraestrutura de Dados e Engenharia Financeira em Python
* **Aula 1.1:** Arquitetura do pipeline quant: estruturas de dados multidimensionais para séries temporais financeiras (DataFrames multi-index e painéis).
* **Aula 1.2:** Conexão com fontes públicas e institucionais: APIs do Banco Central do Brasil (SGS), CVM (informes diários de fundos) e cotações de mercado.
* **Aula 1.3:** Tratamento crítico de dados da B3: ajuste ex-dividendos, bonificações, desdobramentos (splits) e padronização por dias úteis (calendário ANBIMA).
* **Aula 1.4:** O perigo invisível: como identificar e neutralizar o viés de sobrevivência (*survivorship bias*) e o viés de antecipação (*look-ahead bias*).
* **Laboratório Prático:** Construção de uma base de dados limpa com os últimos 10 anos de negociação das ações do IBrX-100.

---

### Módulo 2: Estatística de Retornos e Métricas Institucionais de Risco
* **Aula 2.1:** Retornos simples vs. log-retornos: propriedades matemáticas e quando utilizar cada um na modelagem.
* **Aula 2.2:** Distribuições empíricas de ativos financeiros: não-normalidade, caudas pesadas (*fat tails*), assimetria (*skewness*) e curtose excessiva.
* **Aula 2.3:** Métricas de performance além do Sharpe: Ratio de Sortino, Ratio de Calmar e Information Ratio.
* **Aula 2.4:** Dinâmica de rebaixamento: cálculo analítico do *Maximum Drawdown* (MDD), duração de drawdown e tempo de recuperação.
* **Aula 2.5:** Modelos de Risco de Cauda: Value at Risk (VaR Histórico e Paramétrico) e Conditional VaR (Expected Shortfall / CVaR).
* **Laboratório Prático:** Desenvolvimento de um módulo automatizado que recebe séries de preços e gera um *Risk Tear Sheet* institucional.

---

### Módulo 3: Factor Investing e Modelagem Multifatorial no Brasil
* **Aula 3.1:** A evolução das teorias de apreçamento: do CAPM aos modelos multifatoriais de Fama-French e Carhart.
* **Aula 3.2:** Fator de Momentum na B3: diferenças teóricas e empíricas entre *Cross-Sectional Momentum* (vencedores vs. perdedores) e *Time-Series Momentum* (seguimento de tendência).
* **Aula 3.3:** Fatores Fundamentistas: Valor (P/L, EV/EBITDA, Book-to-Market) e Qualidade (ROE, ROIC, Margem Líquida, Dívida Líquida/EBITDA).
* **Aula 3.4:** Fatores de Risco: Baixa Volatilidade (*Low Vol*) e Tamanho (*Size / Small Caps*).
* **Aula 3.5:** O problema do *Factor Zoo*: testes de significância t-stat, correção de Bonferroni e validação fora da amostra (*Out-of-Sample*).
* **Laboratório Prático:** Criação de um ranking multifatorial com scores padronizados (Z-Score) para seleção sistemática de carteiras na bolsa brasileira.

---

### Módulo 4: Framework de Backtesting Institucional Realista
* **Aula 4.1:** Arquiteturas de Backtest: Vectorizado (rápido para prototipagem) vs. Orientado a Eventos (preciso para execução).
* **Aula 4.2:** Modelagem de atritos de mercado: custos de corretagem, emolumentos B3, taxa de liquidação e imposto sobre proventos.
* **Aula 4.3:** Modelagem de *Slippage* e Impacto de Mercado: restrições de liquidez com base no volume financeiro médio diário (ADTV).
* **Aula 4.4:** Rebalanceamento periódico: frequências ótimas (semanal, mensal, trimestral), bandas de tolerância (*turnover*) e custos de rotação.
* **Aula 4.5:** Walk-Forward Analysis e Validação Cruzada Purificada (Purged Cross-Validation para séries temporais).
* **Laboratório Prático:** Execução do backtest de 5 anos de uma carteira de Fatores na B3 com relatório completo de custos e curva de capital auditável.

---

### Módulo 5: Otimização de Portfólios e Alocação de Risco
* **Aula 5.1:** Otimização de Média-Variância de Markowitz: limites práticos e a extrema sensibilidade a erros de estimativa.
* **Aula 5.2:** Regularização de matrizes de covariância: método Ledoit-Wolf Shrinkage e filtragem de ruído por Random Matrix Theory (RMT).
* **Aula 5.3:** Paridade de Risco (*Risk Parity*) e Contribuição Marginal de Risco: garantindo que ativos mais voláteis não dominem o portfólio.
* **Aula 5.4:** *Hierarchical Risk Parity* (HRP): como usar aprendizado não-supervisionado (clusterização hierárquica) para alocar sem necessidade de inversão de matriz.
* **Laboratório Prático:** Comparação empírica de performance: Carteira 1/N vs. Média-Variância vs. HRP com ativos brasileiros e globais.

---

### Módulo 6: Projeto Final e Produção Quant
* **Aula 6.1:** Estruturação de projetos em Python: boas práticas de código, modularização e reprodutibilidade.
* **Aula 6.2:** Geração de relatórios executivos em HTML/PDF com gráficos interativos.
* **Projeto Final de Conclusão:** Desenvolvimento de uma estratégia quantitativa proprietária completa (extração -> cálculo de fatores -> backtest com atritos -> otimização de pesos -> relatório final de risco).

---

# PARTE 2: GUIA DE NIVELAMENTO TÉCNICO

## 1. A Matemática dos Retornos Financeiros

Um dos equívocos mais recorrentes de analistas e cientistas de dados ao migrarem para finanças é a confusão entre retornos simples e logarítmicos.

### 1.1 Retorno Simples (Aritmético)
Mede a variação percentual do preço entre dois instantes:
R_t = \frac{P_t - P_{t-1}}{P_{t-1}} = \frac{P_t}{P_{t-1}} - 1

* **Propriedade fundamental:** Retornos simples se somam **entre ativos no espaço (cross-section)**. Se uma carteira aloca pesos $, o retorno total do portfólio no dia é exatamente a média ponderada:
R_{p, t} = \sum_{i=1}^N w_i R_{i, t}

### 1.2 Retorno Logarítmico (Composto Continuamente)
Definido como a diferença do logaritmo natural dos preços:
r_t = \ln\left(\frac{P_t}{P_{t-1}}\right) = \ln(P_t) - \ln(P_{t-1})

* **Propriedade fundamental:** Retornos logarítmicos se somam **ao longo do tempo (série temporal)**. O retorno composto de um período de $ dias é simplesmente a soma direta dos log-retornos diários:
r_{total} = \sum_{t=1}^{T} r_t

> **Regra de Ouro:**  
> • Use **retornos simples** para calcular o valor patrimonial de portfólios e métricas de atribuição de performance.  
> • Use **log-retornos** para estimação de modelos estatísticos, distribuições, volatilidade e testes econométricos.

---

## 2. Convenção de Anualização no Brasil (252 Dias Úteis)

O mercado financeiro brasileiro adota a convenção de **252 dias úteis** por ano (calendário ANBIMA):

* **Retorno Anualizado:**
\bar{R}_{anual} = (1 + \bar{R}_{diário})^{252} - 1

* **Volatilidade Anualizada (Raiz do Tempo):**
\sigma_{anual} = \sigma_{diária} \times \sqrt{252}

---

## 3. Métricas Institucionais de Performance e Risco

1. **Sharpe Ratio:**
   \text{Sharpe} = \frac{\bar{R}_p - R_f}{\sigma_p}
   Onde $ é a taxa livre de risco anualizada (geralmente o CDI no Brasil).

2. **Sortino Ratio (Penalização Apenas do Downside):**
   \text{Sortino} = \frac{\bar{R}_p - R_f}{\sigma_{down}}
   \sigma_{down} = \sqrt{\frac{1}{T} \sum_{t=1}^T \min(0, R_{p,t} - R_{f,t})^2 \times 252}

3. **Maximum Drawdown (MDD):**
   DD_t = \frac{\text{NAV}_t - \max_{\tau \le t}(\text{NAV}_\tau)}{\max_{\tau \le t}(\text{NAV}_\tau)}, \quad MDD = \min_t(DD_t)

---

## 4. Script Python de Nivelamento: Análise de Ativos da B3

Execute o código abaixo no seu ambiente Python (VS Code ou Jupyter) para calcular o scorecard quantitativo dos principais papéis da B3:

`python
import numpy as np
import pandas as pd
import yfinance as yf

# 1. Definição do Universo de Ações
tickers = ['ITUB4.SA', 'VALE3.SA', 'PETR4.SA', 'WEGE3.SA', '^BVSP']
start_date = '2021-01-01'
end_date = '2026-01-01'

print(📥 Baixando cotações históricas da B3...)
data = yf.download(tickers, start=start_date, end=end_date, progress=False)

# 2. Utilização de Preços Ajustados por Proventos ('Adj Close')
prices = data['Adj Close'].dropna()

# 3. Retornos Diários Simples
returns = prices.pct_change().dropna()

# 4. Função de Cálculo de Métricas Institucionais
def calcular_scorecard(series, rf_anual=0.105):
    rf_diario = (1 + rf_anual) ** (1 / 252) - 1
    retorno_anual = (1 + series.mean()) ** 252 - 1
    vol_anual = series.std() * np.sqrt(252)
    
    # Sharpe Ratio
    sharpe = (retorno_anual - rf_anual) / vol_anual if vol_anual > 0 else 0
    
    # Sortino Ratio
    ret_excesso = series - rf_diario
    downside = ret_excesso[ret_excesso < 0].std() * np.sqrt(252)
    sortino = (retorno_anual - rf_anual) / downside if downside > 0 else 0
    
    # Maximum Drawdown (MDD)
    cum_returns = (1 + series).cumprod()
    peak = cum_returns.cummax()
    drawdown = (cum_returns - peak) / peak
    mdd = drawdown.min()
    
    return pd.Series({
        'Retorno Anualizado': f{retorno_anual * 100:.2f}%,
        'Volatilidade Anual': f{vol_anual * 100:.2f}%,
        'Sharpe Ratio': f{sharpe:.2f},
        'Sortino Ratio': f{sortino:.2f},
        'Max Drawdown': f{mdd * 100:.2f}%
    })

scorecard = returns.apply(calcular_scorecard)
print(\\n + = * 65)
print(📊 SCORECARD QUANTITATIVO INSTITUCIONAL)
print(= * 65)
print(scorecard.to_string())

# 5. Matriz de Correlação
print(\\n🔗 Matriz de Correlação Linear:)
print(np.round(returns.corr(), 2).to_string())
`

---

# PARTE 3: TESTE DIAGNÓSTICO DE NIVELAMENTO
### *Autoavaliação de Prontidão Quant (10 Questões)*

Responda às 10 questões a seguir sem consultar o gabarito. Ao final, confira suas respostas explicadas e descubra em qual nível de maturidade você se encontra.

---

### Questão 1 (Matemática de Retornos)
Ao montar uma estratégia quantitativa que aloca 40% em PETR4 e 60% em VALE3, qual metodologia matemática deve ser utilizada para calcular o retorno total diário da carteira?
* A) A média aritmética ponderada dos log-retornos dos ativos.
* B) A média aritmética ponderada dos retornos simples dos ativos.
* C) A raiz quadrada do produto dos retornos simples.
* D) O logaritmo da soma dos preços de fechamento dividido pelo volume.

---

### Questão 2 (Vieses de Backtest e Microestrutura)
Um analista cria um modelo multifatorial que utiliza a divulgação do balanço do 4º trimestre das empresas brasileiras (com data de referência em 31/12) para comprar ações no primeiro pregão de janeiro. Qual erro metodológico fatal foi cometido?
* A) Viés de Sobrevivência (*Survivorship Bias*).
* B) Viés de Antecipação (*Look-Ahead Bias*), pois os balanços reais do 4T só são protocolados na CVM em março ou abril.
* C) Erro de Especificação de Volatilidade por utilizar a raiz quadrada de 365 dias.
* D) Erro de Curvatura de Juros por desconsiderar o cupom limpo.

---

### Questão 3 (Manipulação de Séries em Python/Pandas)
Dado um DataFrame df indexado por datas com os preços diários de uma ação na coluna 'close', qual comando em Pandas calcula corretamente os retornos diários simples preservando o alinhamento temporal?
* A) df['close'].diff() / df['close']
* B) 
p.log(df['close']) - np.log(df['close'].shift(-1))
* C) df['close'].pct_change().dropna()
* D) df['close'].rolling(252).mean()

---

### Questão 4 (Estatística e Anualização)
Se uma ação da B3 apresenta uma volatilidade diária de 2,0% em um mercado com 252 dias úteis, qual é a estimativa correta da sua volatilidade anualizada sob a premissa de retornos i.i.d.?
* A) ,0\% \times 252 = 504,0\%$
* B) ,0\% \times \sqrt{252} \approx 31,75\%$
* C) ,0\% / \sqrt{252} \approx 0,126\%$
* D) ^{252} - 1 \approx 145,2\%$

---

### Questão 5 (Métricas de Risco Assimétrico)
Por que gestores sistemáticos institucionais frequentemente preferem o **Sortino Ratio** em relação ao **Sharpe Ratio** para estratégias de ações com assimetria positiva?
* A) O Sortino ignora o CDI e utiliza o dólar como referência.
* B) O Sharpe Ratio penaliza ganhos expressivos para cima (*upside volatility*) da mesma forma que penaliza perdas severas, enquanto o Sortino foca exclusivamente no desvio para baixo (*downside deviation*).
* C) O Sortino Ratio não depende do número de observações da amostra.
* D) O Sharpe Ratio só pode ser calculado para carteiras com mais de 50 ativos.

---

### Questão 6 (Validação de Modelos em Séries Temporais)
Por que a aplicação direta do algoritmo de *K-Fold Cross-Validation* padrão do Scikit-Learn é inadequada e gera resultados ilusórios em séries financeiras?
* A) Porque o K-Fold tradicional embaralha os dados ou treina com dados do futuro para prever o passado, causando vazamento de informação temporal (*data leakage*).
* B) Porque o K-Fold só funciona com variáveis categóricas binárias.
* C) Porque o número de folds precisa ser exatamente igual ao número de ativos da carteira.
* D) Porque o K-Fold dobra os custos operacionais do backtest.

---

### Questão 7 (Factor Investing)
Qual é a diferença fundamental entre uma estratégia de **Cross-Sectional Momentum** e uma estratégia de **Time-Series Momentum (Trend Following)**?
* A) Cross-Sectional compra ações no Brasil e Time-Series compra apenas índices nos EUA.
* B) Cross-Sectional compara ativos entre si no mesmo instante (comprando os melhores e vendendo os piores do universo relativo), enquanto Time-Series avalia o ativo contra o seu próprio histórico passado em termos absolutos.
* C) Cross-Sectional utiliza apenas médias móveis simples e Time-Series utiliza regressão linear múltipla.
* D) Não há diferença; ambos os termos são sinônimos perfeitos na literatura de Fama-French.

---

### Questão 8 (Atritos de Mercado e Execução Real)
Ao realizar o backtest de uma carteira de *Small Caps* na B3 com um patrimônio de R$ 50 milhões, qual variável é determinante para evitar que o modelo compre ativos ilíquidos cuja execução real destruiria o alfa?
* A) O Índice de Preços ao Consumidor Amplo (IPCA).
* B) A restrição de participação máxima sobre o Volume Financeiro Médio Diário (ADTV - *Average Daily Trading Volume*) e modelagem de *slippage*.
* C) O número de seguidores do perfil da empresa nas redes sociais.
* D) O valor contábil do patrimônio líquido dividido pelo número de cotistas.

---

### Questão 9 (Otimização de Portfólios de Markowitz)
Qual é o principal problema prático da Otimização de Média-Variância clássica de Markowitz quando aplicada diretamente em uma matriz de covariância amostral com dezenas de ações da B3?
* A) O algoritmo não consegue calcular retornos positivos.
* B) O algoritmo de Markowitz é um maximizador de erros de estimativa, alocando pesos extremos e irrealistas em ativos com ruído estatístico, problema resolvido com técnicas de encolhimento como *Ledoit-Wolf Shrinkage*.
* C) Markowitz exige que todos os retornos sejam obrigatoriamente negativos.
* D) O método de Markowitz não permite a inclusão de ações do setor elétrico.

---

### Questão 10 (Machine Learning Não-Supervisionado em Alocação)
Qual inovação a metodologia de **Hierarchical Risk Parity (HRP)**, desenvolvida por Marcos López de Prado, trouxe para a alocação quantitativa institucional?
* A) Utiliza clusterização hierárquica (aprendizado não-supervisionado) na matriz de correlação, dispensando a necessidade de inversão da matriz de covariância e eliminando a instabilidade numérica de Markowitz.
* B) Automatiza a compra de opções binárias sem risco de perda.
* C) Substitui o código Python por contratos inteligentes em blockchain.
* D) Garante retorno garantido acima de 30% ao ano em qualquer cenário macro.

---

# GABARITO OFICIAL COMENTADO

* **Questão 1: B**  
  *Comentário:* A agregação transversal (cross-section) de múltiplos ativos obedece estritamente à linearidade dos retornos simples:  = \sum w_i R_i$. Somar log-retornos ponderados de ativos gera distorções matemáticas graves na carteira.
* **Questão 2: B**  
  *Comentário:* Na B3, as companhias têm prazo legal de até 90 dias após o fim do exercício fiscal para publicar o balanço do 4T. Utilizar dados de 31/12 no dia 02/01 é viés de antecipação puro (*look-ahead bias*), inviabilizando qualquer backtest profissional.
* **Questão 3: C**  
  *Comentário:* df['close'].pct_change().dropna() é a forma vetorizada nativa e precisa do Pandas para calcular $\frac{P_t - P_{t-1}}{P_{t-1}}$.
* **Questão 4: B**  
  *Comentário:* Sob a premissa de retornos independentes e identicamente distribuídos, a variância cresce linearmente com o tempo e o desvio-padrão (volatilidade) cresce com a **raiz quadrada do tempo**: $\sigma_{anual} = 2,0\% \times \sqrt{252} \approx 31,75\%$.
* **Questão 5: B**  
  *Comentário:* O Sharpe Ratio penaliza a volatilidade total (inclusive retornos positivos extremos). O Sortino Ratio substitui o denominador pelo *downside deviation*, premiando estratégias que geram assimetria positiva de ganhos.
* **Questão 6: A**  
  *Comentário:* Séries temporais possuem dependência sequencial e autocorrelação. O K-Fold padrão mistura dados futuros no conjunto de treino, criando um modelo com performance excepcional no papel que quebra imediatamente em produção. Em finanças, utiliza-se *Purged Walk-Forward Cross-Validation*.
* **Questão 7: B**  
  *Comentário:* Cross-sectional momentum gera um ranking relativo (compra os 10% melhores e vende os 10% piores do universo). Time-series momentum avalia a tendência própria do ativo ao longo do tempo (positivo compra, negativo vende ou fica em caixa).
* **Questão 8: B**  
  *Comentário:* Em estratégias com capital institucional, o impacto de mercado (*slippage*) pode apagar 100% do retorno teórico. É mandatório aplicar filtros de liquidez (ex: máximo de 10% do ADTV) e custo de execução quadrático ou em raiz de volume.
* **Questão 9: B**  
  *Comentário:* A inversão da matriz de covariância amostral amplifica erros de ruído estatístico. O estimador *Ledoit-Wolf Shrinkage* aproxima a matriz amostral de um alvo estruturado, gerando pesos equilibrados e robustos.
* **Questão 10: A**  
  *Comentário:* O HRP organiza os ativos em uma árvore hierárquica usando aprendizado de máquina não-supervisionado, calculando a paridade de risco recursiva sem inverter matrizes, conferindo estabilidade máxima em períodos de estresse.

---

# RÉGUA DE NIVELAMENTO E PLANO DE ESTUDOS

Conte quantas questões você acertou e localize o seu diagnóstico institucional:

`
┌─────────────────┬────────────────────────────────────────────────────────┐
│  PONTUAÇÃO      │  DIAGNÓSTICO & PLANO DE ACELERAÇÃO NO CURSO            │
├─────────────────┼────────────────────────────────────────────────────────┤
│  0 a 4 Acertos  │  NÍVEL 1: FUNDAMENTOS / TRANSIÇÃO                      │
│                 │  Você tem interesse na área, mas ainda carrega vícios   │
│                 │  de Data Science tradicional ou de finanças em Excel.   │
│                 │  👉 FOCO NO CURSO: Os Módulos 1 e 2 serão transformadores │
│                 │  para construir a infraestrutura correta sem vieses.   │
├─────────────────┼────────────────────────────────────────────────────────┤
│  5 a 7 Acertos  │  NÍVEL 2: ANALISTA INTERMEDIÁRIO                       │
│                 │  Você domina a sintaxe básica de Python e estatística,  │
│                 │  mas ainda precisa dominar atritos e factor modeling.  │
│                 │  👉 FOCO NO CURSO: Os Módulos 3 e 4 levarão o seu       │
│                 │  backtesting para o padrão de exigência de buy-side.   │
├─────────────────┼────────────────────────────────────────────────────────┤
│  8 a 10 Acertos │  NÍVEL 3: QUANT AVANÇADO / DESK READY                  │
│                 │  Excelente maturidade conceitual e técnica!            │
│                 │  Você já entende o jogo institucional.                 │
│                 │  👉 FOCO NO CURSO: Os Módulos 4, 5 e 6 vão consolidar  │
│                 │  sua capacidade de rodar HRP e portfólios proprietários│
│                 │  com nível de Head de Estratégias Sistemáticas.       │
└─────────────────┴────────────────────────────────────────────────────────┘
`

---

> 🔒 **Garantia VIP da Lista de Espera:** Guarde este documento. Os inscritos na lista de espera receberão a oportunidade de ingressar na primeira turma oficial com **20% de desconto exclusivo** e mentoria direta nas sessões práticas de código.
"

# 1. Salva os arquivos Markdown
(PRODUCTS_DIR / kit_nivelamento_e_ementa_analise_quantitativa.md).write_text(MD_CONTENT, encoding=utf-8)
(DOWNLOADS_DIR / kit_nivelamento_e_ementa_analise_quantitativa.md).write_text(MD_CONTENT, encoding=utf-8)
print(✅ Markdown salvo em products/ e landing_pages/downloads/)

