# Os 3 erros que destroem backtests no mercado real

- **Pilar:** tecnico
- **Horário Sugerido:** Segunda-feira (08:30)

---

O backtest mais bonito que você já viu em Python provavelmente vai quebrar no primeiro mês de execução real.

Quando converso com cientistas de dados ou pesquisadores que estão começando em modelagem financeira quantitativa, vejo quase sempre os mesmos três vieses ocultos:

1. Look-Ahead Bias (Viés de Antecipação):
Usar variáveis que só estavam disponíveis no fechamento do pregão (ou dias depois) para tomar decisões na abertura. Parece óbvio, mas calcular métricas usando balanços trimestrais antes da data oficial de divulgação pela CVM é o erro número um.

2. Survivorship Bias (Viés de Sobrevivência):
Fazer backtest em um universo de ações com as empresas que compõem o índice hoje. Você exclui automaticamente as empresas que quebraram, foram liquidadas ou deslistadas ao longo do período, inflando artificialmente o retorno histórico da sua estratégia.

3. Custos de Transação e Market Impact Desconsiderados:
Uma estratégia com giro de carteira semanal (high turnover) que gera 25% ao ano na planilha pode virar negativa quando você aplica corretagem, emolumentos B3, aluguel de ações (no caso de ponta vendida) e o slippage de execução.

Modelar mercado não é prever o próximo candle com uma rede neural profunda. É ter disciplina estatística para garantir que o seu sinal sobrevive fora da amostra e aos custos do mundo real.

Qual viés já te deu mais dor de cabeça em projetos de modelagem?

#QuantFinance #DataScience #Python #InvestimentoSistematico #FinancasQuantitativas
