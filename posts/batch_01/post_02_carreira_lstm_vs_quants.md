# Por que prever ações com LSTM costuma falhar em entrevistas quant

- **Pilar:** carreira
- **Horário Sugerido:** Quarta-feira (09:00)

---

Se você colocar no seu GitHub um projeto intitulado "Prevendo o preço de PETR4 com LSTM e Redes Neurais", a chance de um gestor quant descartar o currículo é alta.

Por que isso acontece se deep learning é tão avançado em visão computacional e NLP?

A razão é simples: relação sinal-ruído (Signal-to-Noise Ratio).

Séries temporais financeiras são caracterizadas por:
- Não-estacionariedade severa (regimes econômicos mudam constantemente).
- Baixíssima razão sinal-ruído (a maior parte da variação diária é puro ruído estocástico).
- Reflexividade: o mercado reage às estratégias dos próprios participantes.

Quando você aplica um modelo com centenas de milhares de parâmetros em preços de fechamento, a rede neural simplesmente decora o ruído passado (overfitting extremo). O modelo parece perfeito no gráfico de treino, mas falha miseravelmente fora da amostra.

O que os gestores e heads de modelagem realmente querem ver no seu portfólio?
1. Engenharia de features rigorosa (fatores de risco baseados em fundamentos econômicos e microestrutura).
2. Protocolo de validação cruzada específico para séries financeiras (Purged Group TimeSeries Split para evitar vazamento temporal).
3. Gestão de risco explícita: métricas de Maximum Drawdown, controle de volatilidade e custos de turnover.

No mercado financeiro quantitativo, o domínio do problema econômico e da estatística clássica sempre vem antes da complexidade do algoritmo.

Você já tentou rodar modelos complexos em séries financeiras? Como foi a experiência fora da amostra?

#CarreiraQuant #MachineLearning #CienciadeDados #DataScience #Financas
