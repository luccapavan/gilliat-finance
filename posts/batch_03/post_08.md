# Post 08: Por que o VaR 95% quebra fundos e como o CVaR protege seu capital em crises
**Pilar:** Gestão de Risco  
**Horário Recomendado:** 12:00 BRT  
**Chamada:** Técnico / Fórmulas  

---

## 🇧🇷 Versão em Português:

Se a gestão de risco da sua carteira ainda toma decisões baseada apenas no VaR a 95%, você está dirigindo a 180 km/h olhando apenas para o velocímetro — completamente cego para o abismo à frente.

O Value at Risk (VaR 95%) é uma das métricas mais populares do mercado. E também foi o responsável direto por algumas das quebras financeiras mais espetaculares de fundos de investimento.

Qual é a fraqueza fatal que quase ninguém te conta sobre o VaR?

O VaR 95% informa apenas a perda mínima no limiar de corte: "Com 95% de certeza, você não perderá mais do que X".
Mas ele é matematicamente CEGO sobre o que acontece no dia em que você cruza essa linha.
Se a perda na cauda for de 6% ou de 60%, para a fórmula do VaR é rigorosamente a mesma coisa.

Além disso, o VaR viola um axioma matemático fundamental: ele NÃO é uma medida coerente de risco, pois falha na subaditividade (o VaR de uma carteira pode ser maior do que a soma dos riscos individuais em distribuições com cauda pesada).

É por isso que nas mesas quantitativas institucionais, a métrica soberana com poder de veto é o Conditional Value at Risk (CVaR / Expected Shortfall):
CVaR_95 = E[R | R <= VaR_95]

O CVaR calcula a média das perdas condicionadas aos 5% piores cenários históricos e estressados. Ele é matematicamente coerente e penaliza severamente estratégias que colhem retornos aparentes vendendo risco de cauda escondido.

No comitê de risco da sua instituição, qual métrica tem o poder de veto final?

No "The Institutional Quant Toolkit & Playbook", disponibilizo o motor em Python para cálculo vetorizado de CVaR 95%, VaR e métricas de cauda institucionais:
👉 https://warrenjax.gumroad.com/l/fsrcmj

---
Lucca Simeoni Pavan, Ph.D.
Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação

---

## 🇺🇸 Versão em Inglês (English):

For decades, 95% Value at Risk (VaR) was the ubiquitous benchmark across global risk committees and banking regulators.

It was also directly implicated in several of the most catastrophic blowups in hedge fund history.

What is the fatal flaw of standard VaR?
A 95% 1-day VaR tells you only the boundary threshold: "With 95% confidence, your loss will not exceed X".
It is mathematically blind to the shape and severity of the tail BEYOND that boundary.
Whether the tail loss is 5% or 50%, the VaR calculation remains identically oblivious.

Furthermore, VaR is not a mathematically coherent risk measure: it routinely violates the subadditivity axiom under skewed distributions (the VaR of a combined portfolio can exceed the sum of standalone component VaRs).

That is why institutional desks evaluate risk via Conditional Value at Risk (CVaR / Expected Shortfall):

CVaR_95 = E[R | R <= VaR_95]

CVaR computes the expected average loss strictly within the worst 5% percentile tail. It is mathematically subadditive and directly penalizes strategies that harvest synthetic yield by selling unhedged tail risk.

Managing dynamic leverage with VaR alone is like driving a racecar monitoring the speedometer while ignoring the cliff ahead.

Which tail risk metric holds sovereign veto power on your desk?

---
Lucca Simeoni Pavan, Ph.D.
Former Head of Quantitative Strategies & Product/Allocation Manager
