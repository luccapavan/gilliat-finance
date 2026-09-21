# Os 3 erros que destroem backtests no mercado real / The 3 Errors That Destroy Backtests

- **Pilar:** Técnico / Microestrutura
- **Horário Sugerido:** Segunda-feira (08:30 BRT / 12:30 UTC)

---

## 🇧🇷 Versão em Português:

O backtest mais bonito que você já viu em Python provavelmente vai quebrar no primeiro mês de execução real.

Quando converso com cientistas de dados e econometristas em transição para o mercado quant, quase sempre vejo os mesmos três vieses ocultos:

1. Look-Ahead Bias (Viés de Antecipação):
Usar variáveis que só estavam disponíveis no fechamento (ou dias depois) para decidir ordens na abertura.
Calcular fatores contábeis antes da divulgação oficial de balanços na CVM/SEC é o erro mais frequente.

2. Survivorship Bias (Viés de Sobrevivência):
Rodar backtest na composição atual do índice.
Você ignora as empresas que quebraram, foram liquidadas ou deslistadas, inflando artificialmente o Sharpe histórico.

3. Atritos de Microestrutura e Custos Reais:
Uma estratégia de alto giro com 25% a.a. na planilha vira negativa ao incluir emolumentos da B3, taxas de aluguel de ações (short borrow) e o slippage quadrático da execução.

Modelar mercado não é prever o próximo candle com deep learning.
É ter disciplina estatística para provar que seu sinal sobrevive fora da amostra e aos custos do mundo real.

Qual desses vieses já te deu mais dor de cabeça em projetos de modelagem?

---

🎓 **Curso de Análise Quantitativa Aplicada (Turma Fundadora):**
Baixe a Ementa Oficial e o Kit de Nivelamento gratuito em Python:
🔗 (Link in first comment)

📘 **The Quant Transition Playbook:**
Acesse o guia prático de carreira no buy-side e os motores vetoriais de backtesting em Python:
🔗 (Link in first comment)

---
Lucca Simeoni Pavan, Ph.D.  
Ex-Head de Estratégias Quant & Gerente de Alocação de Recursos • Doutor em Economia  

#QuantFinance #DataScience #Python #InvestimentoSistematico #FinancasQuantitativas

---

## 🇺🇸 Versão em Inglês (English):

The most elegant backtest you have ever coded in Python will likely blow up in its first month of live production.

When mentoring data scientists and economists transitioning to systematic asset management, I consistently encounter the same three structural flaws:

1. Look-Ahead Bias:
Using market data only available at the closing bell to execute simulated morning open orders.
In accounting factors, using quarterly reporting dates instead of the actual regulatory filing publication timestamp is the #1 silent alpha killer.

2. Survivorship Bias:
Backtesting on today's index constituents.
By filtering out equities that suffered insolvency, distress, or delisting across the sample, you artificially fabricate an unearned Sharpe ratio.

3. Microstructure Frictions & Non-Linear Slippage:
In emerging economies—such as Brazil (B3)—these frictions are amplified.
Wider bid-ask spreads, steep equity borrow rates for short legs, and non-linear market impact turn an apparent 25% paper return deeply negative in live trading.

Quantitative research is not about predicting the next candlestick with a complex neural net.
It is about rigorous statistical hygiene to guarantee that your signal survives out-of-sample regimes and real-world transaction drag.

Which backtesting bias has caused you the most unexpected headaches in live trading?

---

🎓 **Free Course Syllabus & Python Leveling Kit:**
Download the institutional curriculum and diagnostic test:
🔗 (Link in first comment)

📘 **The Quant Transition Playbook & Vectorized Python Engines:**
Fast-track your buy-side quant career with institutional templates:
🔗 (Link in first comment)

---
Lucca Simeoni Pavan, Ph.D.  
Former Head of Quantitative Strategies & Portfolio Allocation Manager • Ph.D. in Economics  

#QuantFinance #DataScience #Python #SystematicTrading #Microstructure
