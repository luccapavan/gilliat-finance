# Slippage Não-Linear: Por que 90% dos Backtests Morrem na B3

- **Pilar:** microestrutura
- **Horário Sugerido:** Quarta-feira (09:00)

---

A maioria dos pesquisadores iniciantes assume uma taxa fixa de corretagem e 5 bps de slippage no backtest.
Depois, quando o fundo entra em produção, a performance real descola 800 bps da curva simulada.

A razão tem nome e teoria: Microestrutura de Mercado e Impacto Não-Linear de Preço.

Na bolsa brasileira (B3), a liquidez é concentrada em pouquíssimas empresas (as blue chips do índice).
Quando a sua estratégia quantitativa emite uma ordem de compra para uma Mid Cap ou Small Cap:

1. Custo Permanente vs Custo Temporário (Modelo de Almgren-Chriss):
- O impacto temporário decorre do consumo das ordens do book (bid-ask spread e profundidade imediata).
- O impacto permanente ocorre porque a sua própria agressão informa o mercado sobre fluxo comprador, movendo o ponto médio de equilíbrio contra a sua carteira.

2. A Lei da Raiz Quadrada do Impacto de Mercado:
O impacto no preço não cresce de forma linear. Ele escala proporcionalmente à raiz quadrada da fração do volume médio diário (ADV) que você tenta negociar:
Impacto ≈ Y * σ * sqrt(Q / ADV)
Onde σ é a volatilidade diária, Q é o tamanho da sua ordem e ADV é o volume médio diário.

O que isso significa na prática?
- Se você testar uma estratégia com capital simulado de R$ 100.000, o modelo parece uma mina de ouro.
- Com R$ 10 milhões sob gestão, o custo de impacto de mercado consome integralmente o alfa antes que a posição seja montada.

Em modelagem institucional, um bom Quant Researcher não testa apenas retornos: ele modela a Curva de Capacidade da Estratégia (Capacity Frontier).

Antes de se entusiasmar com um Sharpe de 2.5 no backtest, pergunte-se:
"Quantos dias de volume médio diário eu preciso para desmontar essa carteira sem movimentar o mercado?"

Como você modela fricções de microestrutura nos seus testes de backtest?

#Microestrutura #TradingQuantitativo #Execucao #MercadoFinanceiro #FinancasQuantitativas
