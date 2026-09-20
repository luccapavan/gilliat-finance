# Post 06: O seu Sharpe Ratio é falso: Conheça o Deflated Sharpe Ratio (DSR) / Your Sharpe Ratio is a Lie: The Deflated Sharpe Ratio
**Pilar:** Estatística / Rigor  
**Horário Recomendado:** 12:00 BRT / 15:00 UTC  
**Chamada:** Educativo / Autoridade  

---

## 🇧🇷 Versão em Português:

Você rodou 5.000 variações de parâmetros em um backtest e encontrou uma com Sharpe Ratio de 2.1.
Comemora, coloca em produção e... o fundo começa a sangrar dinheiro imediatamente.

O que aconteceu? Você foi vítima do Problema dos Testes Múltiplos (Multiple Testing Problem) e do viés de seleção.

Se você testar 5.000 estratégias com dados aleatórios (ruído puro), o Teorema do Limite Central garante que várias apresentarão Sharpe elevado por pura sorte estatística.

O Sharpe Ratio clássico assume que a estratégia testada foi a ÚNICA hipótese avaliada. Ele é completamente cego ao número de testes fracassados que você descartou antes de encontrar o resultado "ótimo".

Para solucionar isso, Marcos López de Prado e David Bailey desenvolveram o Deflated Sharpe Ratio (DSR):

O DSR ajusta o Sharpe Ratio observado considerando:
1. O número total de estratégias ou parâmetros testados na pesquisa (N);
2. A assimetria (skewness) e a curtose (kurtosis) da distribuição dos retornos;
3. A variância dos desempenhos entre todas as estratégias testadas;
4. O tamanho da série temporal histórica.

Ele calcula a probabilidade estatística de que o Sharpe observado seja fruto de verdadeira habilidade (alfa) e não de pura mineração de dados.

Se o DSR for inferior a 0.95, seu modelo deve ser descartado, não importa quão bonito seja o gráfico.

Quantos testes de backtest você geralmente roda antes de escolher seu modelo final? Você controla esse viés?

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

#QuantFinance #Estatistica #DataScience #Python #InvestimentoSistematico

---

## 🇺🇸 Versão em Inglês (English):

You backtest 5,000 parameter combinations across a strategy space and isolate one configuration delivering an impressive 2.1 Sharpe Ratio.
You deploy capital into live production... and the strategy begins bleeding money immediately.

What happened? You fell into the Multiple Testing Problem and selection bias.

If you generate 5,000 random white-noise time series, standard statistical distribution guarantees that extreme outlier paths will produce high Sharpe ratios purely by stochastic chance.

The canonical Sharpe Ratio operates under a critical assumption: that the reported model was the ONLY hypothesis ever tested. It is mathematically blind to the thousands of discarded iterations left on your hard drive.

To correct this vulnerability, Marcos López de Prado and David Bailey developed the Deflated Sharpe Ratio (DSR):

The DSR discounts the observed Sharpe Ratio by explicitly adjusting for:
1. The total number of independent trials and strategy parameter variations evaluated (N);
2. The non-normality of returns (skewness and kurtosis);
3. The cross-sectional variance of Sharpe ratios across all tested iterations;
4. The historical sample track record length.

The DSR computes the rigorous probability that an observed Sharpe represents genuine predictive skill rather than a data-mined artifact.

If the DSR fails to exceed 0.95, the strategy must be discarded—regardless of how seductive its backtested cumulative equity curve appears.

How many parameter sweeps do you run before selecting a production model? Do you formally control for multiple testing?

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

#QuantitativeFinance #DataScience #Statistics #HedgeFunds #Python #RiskManagement
