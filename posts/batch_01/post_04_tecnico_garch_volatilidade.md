# Por que assumir volatilidade constante é um tiro no pé

- **Pilar:** tecnico
- **Horário Sugerido:** Terça-feira (08:30)

---

Um dos fatos estilizados mais conhecidos em finanças empíricas é o agrupamento de volatilidade (volatility clustering): grandes choques tendem a ser seguidos por grandes choques, e períodos de calmaria tendem a persistir.

Ainda assim, vejo analistas calculando desvio padrão simples dos últimos 30 dias para estimar o risco futuro de um ativo.

O problema dessa abordagem ingênua:
1. Ela atribui o mesmo peso para o retorno de hoje e o retorno de 29 dias atrás.
2. Ela ignora que a volatilidade possui memória e dinâmica autorregressiva.
3. Em eventos de estresse de mercado, o VaR (Value at Risk) calculado de forma estática subestima o risco justamente quando você mais precisa de proteção.

É aqui que a família de modelos ARCH/GARCH entra em cena.
Ao modelar a variância condicional como dependente dos erros passados e da própria variância defasada, conseguimos capturar a assimetria e o retorno rápido ao equilíbrio médio.

Em Python, com poucas linhas usando a biblioteca `arch`, é possível estimar modelos GARCH(1,1) ou EGARCH (que captura o 'efeito alavancagem' — quedas de preço geram mais volatilidade que altas).

Você já utiliza volatilidade condicional na modelagem de risco da sua carteira ou ainda usa desvio padrão rolante?

Para aprender a implementar modelos avançados de risco e volatilidade e baixar a Ementa Oficial do curso com o Kit de Nivelamento em Python:
👉 https://curso-quant-research.netlify.app/

#Risco #Econometria #GARCH #Python #MercadoFinanceiro
