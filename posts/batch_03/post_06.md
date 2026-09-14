# Post 06: O seu Sharpe Ratio é falso: Conheça o Deflated Sharpe Ratio (DSR)
**Pilar:** Estatística / Rigor  
**Horário Recomendado:** 12:00 BRT  
**Chamada:** Educativo / Autoridade  

---

## 🇧🇷 Versão em Português:

Você rodou 5.000 variações de parâmetros em um backtest e encontrou uma com Sharpe Ratio de 2.1.
Você encontrou uma estratégia vencedora ou foi vítima do Teorema de Valores Extremos?

Se você testar 5.000 séries puramente aleatórias geradas por passeios aleatórios (Random Walk), a melhor série terá, com certeza matemática, um Sharpe aparentemente brilhante.

Isso é o que Marcos López de Prado chama de "Selection Bias under Multiple Testing" (viés de seleção sob múltiplos testes).

Para resolver essa armadilha, o buy-side institucional não olha apenas para o Sharpe bruto. Nós calculamos o Deflated Sharpe Ratio (DSR).

O DSR ajusta o Sharpe observado considerando três variáveis críticas:
1. O número total de testes e variações tentadas (N trials);
2. A variância entre as estratégias testadas;
3. A não-normalidade dos retornos (assimetria / skewness e curtose da cauda).

Uma estratégia com Sharpe 1.8 pode ter DSR próximo de zero se foi selecionada entre 10.000 tentativas. Enquanto um Sharpe de 1.1 desenvolvido a partir de uma tese econômica sólida com apenas 3 testes pode ser estatisticamente robusto.

Nunca avalie um algoritmo quantitativo pelo Sharpe Ratio isolado. Pergunte quantas tentativas foram descartadas para chegar até ele.

No "The Institutional Quant Toolkit & Playbook", detalho o protocolo de Purged K-Fold com Embargo e o cálculo do Deflated Sharpe Ratio (DSR):
👉 https://curso-quant-research.netlify.app/

---
Lucca Simeoni Pavan, Ph.D.
Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação

---

## 🇺🇸 Versão em Inglês (English):

You ran 5,000 parameter permutations in a backtest and isolated one configuration delivering a 2.1 Sharpe ratio.
Did you uncover a persistent market anomaly, or were you fooled by Extreme Value Theory?

If you simulate 5,000 purely random Gaussian walks, the maximum observed Sharpe ratio among them is mathematically guaranteed to look stellar.

This is what Marcos López de Prado formalizes as Selection Bias under Multiple Testing (p-hacking).

To neutralize this trap, institutional quantitative desks reject raw Sharpe ratios. We compute the Deflated Sharpe Ratio (DSR).

The DSR mathematically discounts the observed Sharpe by accounting for three parameters:
1. The total number of model trials and variations attempted (N trials);
2. The variance of performance across all tested iterations;
3. Non-normality of asset returns (negative skewness and fat-tailed kurtosis).

A backtest with a 1.8 Sharpe ratio can have a DSR near zero if cherry-picked from 10,000 trials. Conversely, a 1.1 Sharpe developed from solid economic intuition across just 3 trials can be exceptionally robust.

Never evaluate a quantitative algorithm by its isolated Sharpe ratio. Always audit how many rejected iterations were buried in the graveyard to produce it.

---
Lucca Simeoni Pavan, Ph.D.
Former Head of Quantitative Strategies & Product/Allocation Manager
