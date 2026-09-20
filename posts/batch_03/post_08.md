# Post 08: Por que o VaR 95% quebra fundos e como o CVaR protege seu capital em crises / Why 95% VaR Blows Up Funds: The Case for CVaR
**Pilar:** Gestão de Risco  
**Horário Recomendado:** 12:00 BRT / 15:00 UTC  
**Chamada:** Técnico / Fórmulas  

---

## 🇧🇷 Versão em Português:

Se a gestão de risco da sua carteira ainda toma decisões baseada apenas no VaR a 95%, você está dirigindo a 180 km/h olhando apenas para o velocímetro — completamente cego para o abismo à frente.

O Value at Risk (VaR) de 1 dia a 95% nos diz apenas o seguinte:
"Com 95% de confiança, nossa perda máxima diária não ultrapassará X."

Mas o que acontece nos outros 5% dos dias — que é exatamente quando fundos quebram, o mercado entra em pânico e a liquidez evapora?
O VaR tradicional é completamente mudo sobre isso. Para ele, tanto faz se a perda no percentil de cauda for de 3% ou de 50%.

Além disso, o VaR viola um axioma matemático fundamental de medidas de risco coerentes: a subaditividade.
Sob distribuições com caudas pesadas (típicas de mercados financeiros), o VaR de uma carteira combinada pode ser MAIOR do que a soma dos VaRs dos ativos individuais — punindo a diversificação!

Por isso, mesas quantitativas institucionais utilizam o CVaR (Conditional Value at Risk / Expected Shortfall):

CVaR_95 = E[R | R <= VaR_95]

O CVaR calcula o valor esperado da perda condicionado a estarmos dentro da pior cauda de 5%.
Ele é matematicamente coerente, subaditivo e penaliza diretamente estratégias que geram "alfa falso" vendendo risco de cauda oculta.

Qual métrica de risco de cauda tem o poder de veto na mesa da sua instituição?

---

🎓 **Curso de Análise Quantitativa Aplicada (Turma Fundadora):**
Baixe a Ementa Oficial de 30h e o Kit de Nivelamento gratuito em Python:
👉 https://curso-quant-research.netlify.app/

📘 **The Quant Transition Playbook:**
Acesse o guia prático de carreira no buy-side e os motores vetoriais de backtesting em Python:
👉 https://warrenjax.gumroad.com/l/fsrcmj

---
Lucca Simeoni Pavan, Ph.D.  
Ex-Head de Estratégias Quant & Gerente de Alocação de Recursos • Doutor em Economia

#GestaoDeRisco #CVaR #QuantFinance #Python #Econometria #RiscoDeCauda

---

## 🇺🇸 Versão em Inglês (English):

If your portfolio risk management framework still makes leverage decisions based exclusively on 95% Value-at-Risk (VaR), you are driving at 120 mph staring solely at the speedometer—completely blind to the cliff ahead.

A 95% 1-day VaR reveals only the boundary threshold:
"With 95% confidence, daily losses will not exceed X."

It is mathematically blind to the shape, severity, and magnitude of losses BEYOND that boundary.
Whether the tail loss is 5% or 50%, the classical VaR metric remains identically oblivious.

Furthermore, VaR is not a mathematically coherent risk measure: it routinely violates the subadditivity axiom under skewed, fat-tailed distributions (the VaR of a diversified portfolio can exceed the sum of standalone component VaRs, penalizing diversification).

That is why institutional desks evaluate tail risk via Conditional Value at Risk (CVaR / Expected Shortfall):

CVaR_95 = E[R | R <= VaR_95]

CVaR computes the expected average loss strictly within the worst 5% tail.
It is strictly subadditive, convex, and directly penalizes strategies that harvest synthetic yield by selling unhedged tail risk.

Managing dynamic leverage with VaR alone is like trusting an airbag that only deploys after a minor fender-bender but disables itself in a head-on collision.

Which tail risk metric holds sovereign veto power on your desk?

---

🎓 **Free 30-Hour Course Syllabus & Python Leveling Kit:**
Download the institutional curriculum and diagnostic test:
👉 https://curso-quant-research.netlify.app/

📘 **The Quant Transition Playbook & Vectorized Python Engines:**
Fast-track your buy-side quant career with institutional templates:
👉 https://warrenjax.gumroad.com/l/fsrcmj

---
Lucca Simeoni Pavan, Ph.D.  
Former Head of Quantitative Strategies & Portfolio Allocation Manager • Ph.D. in Economics

#RiskManagement #CVaR #QuantitativeFinance #Econometrics #Python #TailRisk
