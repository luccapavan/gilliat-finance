# Slippage Não-Linear: Por que 90% dos Backtests Morrem na Produção

- **Pilar:** microestrutura
- **Horário Sugerido:** Quarta-feira / Wednesday (09:00)
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

Com R$ 100 mil simulados, a estratégia parece incrível. Com R$ 10 milhões sob gestão, o custo de impacto consome 100% do alfa.

Como você modela fricções de microestrutura nos seus backtests?

#Microestrutura #TradingQuantitativo #Execucao #MercadoFinanceiro #FinancasQuantitativas
