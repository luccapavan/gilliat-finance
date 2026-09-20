# Slippage Não-Linear: Por que 90% dos Backtests Morrem na Produção

- **Pilar:** microestrutura
- **Horário Sugerido:** Quarta-feira / Wednesday (09:00 BRT / 13:00 UTC)
- **Idioma:** Português

---

A maioria dos pesquisadores iniciantes assume taxa fixa de corretagem e 5 bps de slippage.
Quando o fundo entra em produção, a performance real descola 800 bps da curva simulada.

A razão tem nome: Microestrutura de Mercado e Impacto Não-Linear de Preço.

1. Modelo de Almgren-Chriss (Impacto Temporário vs Permanente):
O impacto temporário decorre do consumo imediato do book. O permanente ocorre porque a sua própria agressão move o preço de equilíbrio do mercado contra a carteira.

2. A Lei da Raiz Quadrada do Impacto de Mercado:
O impacto de preço escala proporcionalmente à raiz quadrada do volume negociado em relação ao volume médio diário (ADV):
Impacto ≈ Y * σ * sqrt(Q / ADV)

Em economias emergentes como o Brasil (B3), onde a liquidez fora do índice principal é estreita e os spreads são amplos, operar 10% a 20% do volume diário consome 100% do alfa teórico.
Com R$ 100 mil simulados, a estratégia parece incrível. Com R$ 10 milhões sob gestão, o custo de impacto destrói a estratégia.

Como você modela fricções de microestrutura nos seus backtests?

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
