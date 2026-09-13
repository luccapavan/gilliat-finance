# Módulo 1: O Ecossistema Quant e os Modelos de Negócio

## 1. O Mapa das Estratégias Quantitativas

Diferente do mercado tradicional discricionário, onde decisões são tomadas com base em reuniões de comitê e teses qualitativas, a indústria quantitativa opera orientada por dados empíricos e algoritmos sistemáticos. As principais vertentes são:

### 1.1 Factor Investing / Smart Beta
* **Tese:** Retornos excedentes de longo prazo são gerados pela exposição a fatores de risco sistemáticos compensados pelo mercado (Momentum, Value, Quality, Low Volatility, Size).
* **Frequência:** Baixa a média (rebalanceamentos mensais ou trimestrais).
* **Skills centrais:** Econometria de corte transversal (cross-sectional), análise contábil e de múltiplos, álgebra matricial e otimização de portfólio restrita.

### 1.2 Arbitragem Estatística (StatArb) & Pairs Trading
* **Tese:** Ativos economicamente relacionados possuem equilíbrio histórico de preços; desvios desse equilíbrio temporário abrem oportunidades de reversão à média (*mean reversion*).
* **Frequência:** Média a alta (intradiária ou poucos dias).
* **Skills centrais:** Testes de cointegração (Engle-Granger, Johansen), modelos de espaço de estados (Filtro de Kalman) e microestrutura de mercado.

### 1.3 Trend-Following / CTAs (Commodity Trading Advisors)
* **Tese:** Mercados globais (taxas de juros, moedas, commodities, índices) passam por tendências persistentes de preço impulsionadas por fluxos e comportamento institucional.
* **Frequência:** Média a longo prazo.
* **Skills centrais:** Análise de séries temporais não-lineares, gestão de alavancagem dinâmica e controle de *drawdown*.

---

## 2. As Funções em uma Gestora Quant

1. **Quant Researcher (Pesquisador Quantitativo):**
   * Responsável por formular hipóteses econômicas, testar bases de dados, modelar fatores e validar se o "alfa" é estatisticamente robusto fora da amostra.
   * *Background comum:* Doutorado/Mestrado em Economia, Finanças, Física, Estatística ou Matemática.
2. **Quant Developer (Engenheiro de Software Quant):**
   * Responsável pela infraestrutura: pipelines de ingestão de dados de alta velocidade, motores de backtesting de baixa latência e execução algorítmica de ordens (APIs de corretoras e bolsas).
   * *Background comum:* Ciência da Computação, Engenharia de Software. Linguagens: Python, C++, Rust, SQL.
3. **Risk Manager (Gestor de Risco Quantitativo):**
   * Avalia continuamente os limites de estresse da carteira: testes de estresse histórico, cálculo de VaR/CVaR, risco de liquidez e controle de correlações setoriais.
