# Módulo 2: Armadilhas Críticas de Modelagem e Backtesting

Em finanças quantitativas, a frase de Ronald Coase é uma verdade diária: *"Se você torturar os dados por tempo suficiente, eles confessarão qualquer coisa"*. A maioria dos modelos falha porque o pesquisador se enganou durante o processo de teste.

---

## 1. Look-Ahead Bias (Viés de Olhar à Frente)

Ocorre quando dados do futuro vazam para o instante da decisão no passado.
* **Exemplo Clássico em Factor Investing:** Usar a divulgação de resultados de uma empresa no mesmo dia de encerramento do trimestre contábil (31/03). Na vida real, o balanço é entregue à CVM 30 a 45 dias depois.
* **Como evitar:**
  * Utilize marcas temporais rígidas de *divulgação do dado* (`publication_date`) e não apenas do *período de competência* (`reference_date`).
  * No cálculo de retornos, a decisão no tempo $t$ (ex: fechamento de hoje) só pode ser executada no preço de abertura do tempo $t+1$ (`shift(1)` obrigatório).

---

## 2. Survivorship Bias (Viés de Sobrevivência)

Ocorre quando o universo histórico de ações inclui apenas as empresas ativas na data presente.
* **Impacto:** Se você testar uma estratégia de 2010 a 2024 usando a composição atual do Ibovespa ou apenas ações negociadas hoje, você removeu todas as empresas que faliram, foram liquidadas ou tiveram quedas de 95% e saíram do índice. O retorno aparente do backtest será artificialmente inflado em dezenas de pontos percentuais.
* **Como evitar:**
  * Utilizar bases de dados *point-in-time*, que contêm os preços históricos mesmo de ativos cancelados pela CVM.

---

## 3. Custos de Transação e Impacto de Mercado

Um backtest "sem atrito" é apenas uma peça de ficção. Na vida real, cada operação gera custos:
1. **Corretagem e Emolumentos:** Taxas cobradas pela bolsa (B3) e intermediários.
2. **Bid-Ask Spread (Spread de Compra e Venda):** Em ações de média/baixa liquidez, a diferença entre o melhor comprador e vendedor corrói o alfa.
3. **Custo de Aluguel de Ações (Short Fee):** Em estratégias *long-short*, a ponta vendida exige pagamento de taxa de empréstimo (BTC) ao doador.
4. **Market Impact (Impacto de Mercado):** Ordens institucionais de milhões de reais movimentam o preço contra a própria execução.

---

## 4. Validação Cruzada: Por que o K-Fold Padrão é Inválido?

Em Machine Learning tradicional, divide-se o dataset aleatoriamente em $K$ partes (K-Fold Cross Validation). **Em séries temporais financeiras, isso é estritamente proibido**, pois causa vazamento de informação do futuro para o passado.

### O Protocolo Correto: Purged K-Fold com Embargo
1. **Purging (Expurgo):** Remove períodos de treino cujos rótulos de retorno se sobrepõem à janela de teste.
2. **Embargo:** Adiciona uma janela de espera imediatamente após o conjunto de teste para garantir que a autocorrelação residual da série não contamine a amostra de treino subsequente.
