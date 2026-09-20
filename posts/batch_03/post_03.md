# Post 03: A Lei da Raiz Quadrada e o Impacto de Microestrutura / The Square-Root Law & Non-Linear Slippage in Emerging Markets
**Pilar:** Microestrutura / Execução  
**Horário Recomendado:** 12:00 BRT / 15:00 UTC  
**Chamada:** Educativo / Reflexão  

---

## 🇧🇷 Versão em Português:

Um backtest sem custos realistas de microestrutura não é uma estratégia de investimento. É uma obra de ficção.

Com frequência vejo algoritmos projetados na B3 assumindo execução instantânea a preço de fechamento ou spread fixo de 2 centavos.

No mercado real, especialmente no Brasil onde a liquidez é concentrada em poucos ativos, o atrito operacional obedece à Lei da Raiz Quadrada do Impacto de Mercado:

Impacto ≈ Y * Vol_Diária * sqrt(Q / ADV)

O que essa fórmula nos ensina?
1. O custo de impacto cresce de forma côncava com o volume relativo da ordem (Q / ADV);
2. Não adianta seu backtest ter Sharpe 2.0 se ele gira 80% da carteira por semana em papéis com ADV de R$ 2 milhões;
3. O próprio ato de comprar empurra o preço de equilíbrio para cima (impacto permanente), devorando o alfa antes que ele chegue ao cotista.

Isso define a Fronteira de Capacidade da Estratégia: o teto de patrimônio (AUM) que o modelo suporta antes de começar a perder dinheiro por atrito de livro.

Antes de celebrar a rentabilidade acumulada de um backtest, responda a uma pergunta:
Seu modelo sobrevive a 15 bps de custo fixo mais 20 bps de slippage não-linear?

---

🎓 **Curso de Análise Quantitativa Aplicada (Turma Fundadora):**
Baixe a Ementa Oficial e o Kit de Nivelamento gratuito em Python:
👉 https://curso-quant-research.netlify.app/

📘 **The Quant Transition Playbook:**
Acesse o guia prático de carreira no buy-side e os motores vetoriais de backtesting em Python:
👉 https://warrenjax.gumroad.com/l/fsrcmj

---
Lucca Simeoni Pavan, Ph.D.  
Ex-Head de Estratégias Quant & Gerente de Alocação de Recursos • Doutor em Economia

#Microestrutura #TradingQuantitativo #Execucao #MercadoFinanceiro #FinancasQuantitativas

---

## 🇺🇸 Versão em Inglês (English):

A backtest devoid of realistic market microstructure friction is not an investment strategy. It is financial fiction.

Too often, quantitative algorithms are designed assuming instantaneous fills at the mid-price or flat penny spreads.

In production markets, transaction impact is strictly governed by the Square-Root Law of Market Impact:

Impact ≈ Y * Daily_Volatility * sqrt(Q / ADV)

What does this equation tell us?
1. Execution impact scales concavely with the order's participation rate relative to Average Daily Volume (Q / ADV);
2. A 2.0 Sharpe ratio is meaningless if the model demands 80% weekly portfolio turnover in mid-cap names;
3. The very act of executing your order moves the equilibrium order book price against you (permanent market impact), wiping out alpha.

In emerging economies—such as Brazil (B3)—these frictions are amplified.
Liquidity is heavily concentrated in a handful of commodity and banking mega-caps. In mid and small-cap equities, order books are shallow and short-borrow fees are steep.
Executing an order exceeding 10% to 15% of ADV triggers severe non-linear slippage that completely devours theoretical factor returns.

This defines the Strategy Capacity Frontier: the strict AUM ceiling beyond which execution frictions destroy 100% of paper alpha.

Before celebrating a stellar backtest cumulative curve, ask yourself:
Does your algorithm survive realistic non-linear execution frictions in emerging market regimes?

---

🎓 **Free Course Syllabus & Python Leveling Kit:**
Download the institutional curriculum and diagnostic test:
👉 https://curso-quant-research.netlify.app/

📘 **The Quant Transition Playbook & Vectorized Python Engines:**
Fast-track your buy-side quant career with institutional templates:
👉 https://warrenjax.gumroad.com/l/fsrcmj

---
Lucca Simeoni Pavan, Ph.D.  
Former Head of Quantitative Strategies & Portfolio Allocation Manager • Ph.D. in Economics

#Microstructure #QuantFinance #AlgorithmicTrading #Execution #EmergingMarkets #Python
