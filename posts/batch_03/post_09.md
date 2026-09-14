# Post 09: Loops 'for' em Python: O teste silencioso que reprova candidatos em vagas Quant
**Pilar:** Engenharia / Código  
**Horário Recomendado:** 12:00 BRT  
**Chamada:** Educativo / Código  

---

## 🇧🇷 Versão em Português:

Quando avalio códigos em desafios técnicos para contratação de quants, a primeira busca que faço no repositório é simples:

Quantas vezes a palavra `for` aparece em iterações de séries temporais de preços?

Se o candidato escreveu:
`for i in range(len(df)):`
`    if df['pe'].iloc[i] < 10 and df['mom'].iloc[i] > 0:`
`        portfolio.append(...)`

A avaliação técnica encerra ali.

Por que as mesas são tão intransigentes com isso?
1. Performance Computacional: Em Python, loops interpretados linha por linha são 50 a 100 vezes mais lentos que operações matriciais vetorizadas em C/Fortran pelo NumPy e Polars;
2. Risco Operacional de Vazamento: Loops manuais são o terreno fértil ideal para Look-Ahead Bias acidental ao referenciar índices incorretos (`i` vs `i-1`);
3. Escalabilidade de Pesquisa: Um backtest que leva 40 minutos em loops manuais roda em 2 segundos quando devidamente vetorizado com Z-Scores transversais (`df.sub(mean, axis=0).div(std, axis=0)`).

No buy-side, velocidade de computação vetorial não é estética; é a diferença entre testar 10 hipóteses por dia ou testar 10.000.

Domine operações matriciais e broadcasting em NumPy/pandas. É o pré-requisito silencioso de qualquer processo seletivo institucional.

No "The Institutional Quant Toolkit & Playbook", todos os 4 motores em Python foram escritos com vetorização pura (zero loops lentos), prontos para produção e processos seletivos:
👉 https://curso-quant-research.netlify.app/

---
Lucca Simeoni Pavan, Ph.D.
Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação

---

## 🇺🇸 Versão em Inglês (English):

When reviewing technical code submissions for quantitative research positions, my initial repository search is straightforward:

How many times does the keyword `for` appear iterating over daily financial time series?

If an applicant writes:
`for i in range(len(df)):`
`    if df['pe'].iloc[i] < 10 and df['mom'].iloc[i] > 0:`
`        portfolio.append(...)`

The technical evaluation effectively ends right there.

Why are quantitative desks so uncompromising on this?
1. Execution Latency: In Python, line-by-line interpreted procedural loops run 50x to 100x slower than vectorized C/Fortran matrix operations powered by NumPy and Polars;
2. Look-Ahead Vulnerability: Manual row indexing is the single most common source of accidental temporal leakage (`i` vs `i-1`);
3. Research Velocity: A multi-asset backtest taking 40 minutes under procedural loops executes in under 2 seconds when cleanly vectorized with cross-sectional Z-scores (`df.sub(mean, axis=0).div(std, axis=0)`).

On systematic desks, vectorized matrix operations are not a stylistic preference; they determine whether your team tests 10 hypotheses a week or 10,000.

Master broadcasting and matrix algebra in NumPy and pandas. It is the silent prerequisite of buy-side recruiting.

---
Lucca Simeoni Pavan, Ph.D.
Former Head of Quantitative Strategies & Product/Allocation Manager
