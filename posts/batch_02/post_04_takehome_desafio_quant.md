# A Anatomia de um Desafio Técnico de 48 Horas para Vaga Quant

- **Pilar:** carreira_senior
- **Horário Sugerido:** Quinta-feira (09:00)

---

Você passou na primeira triagem de currículo e recebeu por e-mail:
"Segue o dataset com 10 anos de retornos e balanços. Você tem 48 horas para nos entregar um relatório e o repositório com uma estratégia multifator."

O que a maioria dos candidatos entrega?
- Um Jupyter Notebook de 3.000 linhas com gráficos coloridos do Seaborn.
- Três modelos do XGBoost ajustados sem cross-validation temporal.
- Conclusão: "Meu modelo prevê o mercado com 72% de acerto e Sharpe de 3.8."

O que acontece com essa entrega? É descartada nos primeiros 5 minutos de análise do comitê.

Por quê? Porque quem trabalha com capital real sabe que Sharpe 3.8 em renda variável acionária não existe fora da amostra. O avaliador sabe na hora que houve overfitting ou look-ahead bias.

O que um candidato sênior realmente entrega para garantir a vaga?

1. Formulação de Hipótese Econômica a Priori:
Em vez de minerar 200 variáveis aleatórias, escolhe 3 ou 4 fatores com respaldo teórico claro (ex: Momentum residual, Eficiência de Capital e Baixa Volatilidade idiossincrática).

2. Higienização e Tratamento Point-in-Time:
Deixa explícito no código o atraso temporal de divulgação de balanços (defasagem de 45 dias) e o tratamento de splits/grupamentos e dividendos.

3. Código Modular e Testável:
Estruturado em módulos Python com classes (`UniverseSelector`, `SignalGenerator`, `PortfolioOptimizer`, `ExecutionSimulator`), com testes unitários em `pytest` garantindo que o sinal em t só executa em t+1.

4. Decomposição Detalhada de Risco:
O relatório final não exibe apenas retorno: exibe correlação com o CDI e Ibov, Turnover médio mensal, Max Drawdown por subperíodos de crise (ex: 2020, 2022) e análise de sensibilidade a custos.

No mercado financeiro quantitativo, maturidade metodológica vale dez vezes mais do que complexidade algorítmica cega.

No Módulo 5 do nosso curso, abrimos a rubrica exata e o repositório modelo para aprovação em desafios de 48h. Baixe a Ementa Oficial e o Kit de Nivelamento gratuito:
👉 https://curso-quant-research.netlify.app/

Você já participou de um processo seletivo com teste prático take-home? O que achou mais desafiador?

#CarreiraQuant #DataScience #ProcessoSeletivo #MercadoFinanceiro #Python
