# Post 04: O Desafio de 48 Horas: O que gestores quant procuram em um teste técnico
**Pilar:** Carreira / Bastidores  
**Horário Recomendado:** 12:00 BRT  
**Chamada:** Conversão Playbook  

---

## 🇧🇷 Versão em Português:

Se você se candidatar a uma vaga de Quant Researcher em uma gestora sistemática, dificilmente sua sabatina será sobre conceitos teóricos de livro.

Você receberá um dataset de preços e fundamentos e terá 48 a 72 horas para entregar uma estratégia completa.

O que separa os 5% que são contratados dos 95% que são reprovados de imediato?

1. Eliminação estrita de Look-Ahead Bias: Aplicar shift(1) nos pesos de execução (`exec_weights = weights.shift(1)`). Se você calcular retorno no dia t usando pesos definidos no fechamento do dia t sem lag operacional, é desclassificação sumária.
2. Arquitetura de Software Modular: Quem envia um Jupyter Notebook monolítico de 3.000 linhas é descartado. Gestores esperam módulos limpos (`factors.py`, `optimizer.py`, `backtest.py`), testes unitários em pytest e `requirements.txt` congelado.
3. Tratamento de Sobrevivência e Fricção: Considerar custos de empréstimo (BTC) na ponta vendida e descontar slippage conservador.
4. Racional Econômico: Explicar POR QUE a anomalia existe, quem está do outro lado perdendo dinheiro e qual o risco de cauda do portfólio.

No "The Institutional Quant Toolkit & Playbook", incluí o blueprint exato desse desafio técnico de 48h, a rubrica de avaliação dos gestores e os 4 motores completos em Python para você nunca começar do zero. Acesse a Ementa Oficial e o Kit de Nivelamento do curso:
👉 https://curso-quant-research.netlify.app/

---
Lucca Simeoni Pavan, Ph.D.
Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação

---

## 🇺🇸 Versão em Inglês (English):

When applying for a Quant Researcher or Portfolio Manager seat at a systematic hedge fund, interviewers rarely test you on textbook memorization.

Instead, you receive a historical dataset and a 48-to-72-hour window to submit a production-grade strategy.

What separates the 5% who get hired from the 95% filtered out instantly?

1. Zero Tolerance for Look-Ahead Bias: Enforcing strict lag on execution vectors (`exec_weights = weights.shift(1)`). Using same-day close prices without implementation latency is an immediate rejection.
2. Modular Software Architecture: Submitting a monolithic 3,000-line Jupyter Notebook signals poor engineering hygiene. Desks expect clean modular packages (`factors.py`, `optimizer.py`, `backtest.py`), pytest suites, and deterministic `requirements.txt`.
3. Survivorship & Frictional Realism: Modeling borrow fees on short legs and incorporating non-linear execution slippage.
4. Economic Rationale: Articulating WHY the anomaly persists, who is providing the liquidity on the losing side, and where the strategy breaks down.

In 'The Institutional Quant Toolkit & Playbook', I provide the complete institutional blueprint for this 48h take-home case, the exact grading rubric, and 4 verified production Python engines:
👉 https://chk.eduzz.com/7sfhtm2a

---
Lucca Simeoni Pavan, Ph.D.
Former Head of Quantitative Strategies & Product/Allocation Manager
