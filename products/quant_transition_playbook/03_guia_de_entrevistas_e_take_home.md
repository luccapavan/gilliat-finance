# Módulo 3: Guia Prático de Entrevistas & Portfólio GitHub

## 1. Como Gestores Avaliam seu Portfólio no GitHub

Em processos seletivos para vagas de Quant Researcher ou Data Scientist de Asset, gestores recebem centenas de links de GitHub. O que te separa de 95% dos concorrentes?

### ❌ O que NÃO colocar no seu GitHub:
* O clássico projeto de prever ações da Apple com LSTM/GRU sem custos de transação.
* Classificador do Titanic ou Iris dataset.
* Notebooks gigantes sem modularização, funções soltas e variáveis globais.

### ✅ O que ENCANTA um avaliador técnico:
1. **Pipeline de Dados Modular:** Código limpo com classes/funções bem definidas (`etl.py`, `factors.py`, `backtest.py`).
2. **Tratamento Explícito de Fricções:** Código que aplica spread, taxa de corretagem e custo de empréstimo.
3. **Métricas Completas de Risco:** Não apenas Sharpe Ratio, mas *Maximum Drawdown duration*, *Sortino*, *Calmar*, *Turnover* e *Information Ratio*.
4. **Testes Unitários:** Ter testes em `pytest` garantindo que o backtest não executa ordens no mesmo instante do sinal.

---

## 2. As Perguntas Clássicas em Entrevistas

### Pergunta 1 (Econometria / Estatística):
> *"O que acontece com os estimadores de MQO se a série temporal for não-estacionária com raiz unitária? Como diagnosticar e corrigir?"*
* **Resposta esperada:** Os estimadores podem gerar regressão espúria (R² elevado e t-estatísticas infladas sem relação econômica real). Diagnóstico: Teste Augmented Dickey-Fuller (ADF) ou Phillips-Perron. Correção: Diferenciação da série ou verificação de cointegração via procedimento de Engle-Granger / Johansen.

### Pergunta 2 (Factor Investing):
> *"Como você constrói um fator de Momentum cruzado (cross-sectional) e por que costumamos excluir o mês mais recente (t-12 até t-2)?"*
* **Resposta esperada:** O Momentum tradicional (Jegadeesh & Titman) ranqueia as ações pelo retorno acumulado de 12 meses, excluindo o mês imediatamente anterior ($t-1$). O motivo da exclusão é neutralizar o efeito de reversão à média de curto prazo (*short-term reversal*) provocado por pressões temporárias de liquidez e microestrutura.

### Pergunta 3 (Gestão de Risco):
> *"Qual a diferença conceitual e matemática entre VaR (Value at Risk) e CVaR (Conditional VaR / Expected Shortfall)?"*
* **Resposta esperada:** O VaR informa a perda máxima esperada para um determinado nível de confiança (ex: 95%), mas não diz nada sobre a gravidade da perda caso esse limiar seja ultrapassado. O CVaR calcula o valor esperado da perda *condicional* a estar na cauda além do VaR. O CVaR é uma medida de risco coerente (atende à subaditividade), enquanto o VaR não é.
