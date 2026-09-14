# Post 03: A Lei da Raiz Quadrada e o Cemitério de Estratégias Quant na B3
**Pilar:** Microestrutura / Execução  
**Horário Recomendado:** 12:00 BRT  
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

No "The Institutional Quant Toolkit & Playbook", disponibilizo o Checklist Anti-Vieses com os 10 testes de auditoria de microestrutura e motores em Python prontos para produção. Baixe a Ementa Oficial e o Kit de Nivelamento do curso:
👉 https://curso-quant-research.netlify.app/

---
Lucca Simeoni Pavan, Ph.D.
Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação

---

## 🇺🇸 Versão em Inglês (English):

A backtest devoid of realistic market microstructure friction is not an investment strategy. It is financial fiction.

Too often, quantitative algorithms are designed assuming instantaneous fills at the mid-price or fixed penny bid-ask spreads.

In production markets, transaction impact is governed by the Square-Root Law of Market Impact:

Impact ≈ Y * Daily_Volatility * sqrt(Q / ADV)

What does this equation tell us?
1. Execution impact scales concavely with the order's participation rate relative to Average Daily Volume (Q / ADV);
2. A 2.0 Sharpe ratio is meaningless if the model demands 80% weekly portfolio turnover in mid-cap names;
3. The very act of executing your order moves the equilibrium order book price against you (permanent market impact), wiping out alpha.

This dictates the Strategy Capacity Frontier: the strict AUM ceiling beyond which execution frictions erode 100% of theoretical alpha.

Before celebrating a stellar backtest cumulative curve, ask yourself:
Does your algorithm survive 15 bps of brokerage plus 20 bps of nonlinear slippage?

---
Lucca Simeoni Pavan, Ph.D.
Former Head of Quantitative Strategies & Product/Allocation Manager
