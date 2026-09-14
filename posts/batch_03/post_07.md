# Post 07: A Mecânica do Fator Momentum: Por que pular o mês mais recente (t-1) é obrigatório
**Pilar:** Fatores / Modelagem  
**Horário Recomendado:** 12:00 BRT  
**Chamada:** Educativo / Fórmulas  

---

## 🇧🇷 Versão em Português:

O erro mais comum que vejo quem está começando em Factor Investing cometer no Python:

Calcular o fator Momentum pegando o retorno dos últimos 12 meses direto até ontem:
`prices / prices.shift(252) - 1`

Se você faz isso no seu código de backtest, você está sabotando o próprio sinal sem saber.

Nas mesas quantitativas institucionais, o Momentum clássico de 12 meses SEMPRE exclui o mês imediatamente anterior (janela t-12 a t-2):
`momentum_factor = prices.shift(21) / prices.shift(252) - 1`

Por que essa exclusão de 21 dias úteis (1 mês) é regra obrigatória de sobrevivência?

Por causa do Efeito de Reversão de Curto Prazo (Short-Term Reversal):
1. Em horizontes semanais e intradiários, os preços são dominados por choques de liquidez de microestrutura e rebalanceamentos pontuais de grandes fundos, gerando forte reversão à média;
2. Se você inclui os últimos 20 dias no cálculo do Momentum, o efeito de reversão de curto prazo contamina e neutraliza a persistência de médio prazo;
3. Ao aplicar o lag de 21 dias, você purifica o vetor, capturando a verdadeira continuidade informacional institucional.

Pequenos detalhes econométricos de duas linhas no código são a diferença exata entre uma estratégia lucrativa e um modelo que sangra dinheiro por ruído.

Você aplica o lag de reversão de curto prazo nos seus fatores em Python?

No "The Institutional Quant Toolkit & Playbook", o script em Python do backtest multifator já vem com o lag 12-2, Z-Score transversal e turnover vetorizados:
👉 https://curso-quant-research.netlify.app/

---
Lucca Simeoni Pavan, Ph.D.
Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação

---

## 🇺🇸 Versão em Inglês (English):

The Momentum anomaly (Jegadeesh & Titman, 1993) represents one of the most robust, cross-asset phenomena in financial history.

Yet when junior quants code Momentum in Python, they routinely make a glaring econometric blunder:
Calculating 12-month trailing returns straight up to yesterday (`prices / prices.shift(252) - 1`).

On institutional systematic desks, canonical 12-month equity momentum strictly skips the most recent month (window t-12 to t-2):
`momentum_factor = prices.shift(21) / prices.shift(252) - 1`

Why is skipping the last 21 trading days non-negotiable?

Because of the Short-Term Reversal Anomaly:
1. Over 1-to-4-week horizons, order flow is dominated by market-maker inventory rebalancing and institutional liquidity shocks, inducing mean reversion;
2. Including the last 20 days pollutes your intermediate-term trend signal with high-frequency noise;
3. Lagging the calculation window by 21 days isolates clean, persistent institutional information diffusion.

Disciplined econometric formulation in Python code is what separates institutional alpha from amateur curve-fitting.

Do your factor engines account for the 1-month short-term reversal lag?

---
Lucca Simeoni Pavan, Ph.D.
Former Head of Quantitative Strategies & Product/Allocation Manager
