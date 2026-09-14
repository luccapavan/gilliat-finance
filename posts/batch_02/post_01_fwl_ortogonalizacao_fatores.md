# O Teorema de Frisch-Waugh-Lovell (FWL) e a Ortogonalização de Fatores em Python

- **Pilar:** tecnico_avancado
- **Horário Sugerido:** Segunda-feira (08:30)

---

Se você calcula o alfa de um fator sem neutralizar a exposição a fatores concorrentes, há 90% de chance de estar comemorando uma ilusão estatística.

Em econometria teórica, o Teorema de Frisch-Waugh-Lovell (FWL) é uma das pérolas da álgebra matricial de projeções.

Mas em gestão quantitativa profissional, ele é a ferramenta diária para responder à pergunta:
"O meu fator tem alfa residual próprio ou é apenas um beta disfarçado de outro fator conhecido?"

Suponha que você queira testar se um sinal de Qualidade (ex: ROIC elevado) gera retornos anômalos.
Se empresas com alto ROIC também tendem a ter baixo endividamento e múltiplos P/L mais altos, como isolar o efeito puro de Qualidade sem sofrer viés de variável omitida?

A aplicação do FWL na prática:

1. Você projeta o fator de interesse (ROIC) sobre os fatores de controle (Tamanho, Mercado, Valor) via regressão transversal:
   ROIC = Xβ + ε

2. O resíduo ε desta regressão é, por definição matricial, perfeitamente ortogonal ao subespaço gerado pelos fatores de controle (X'ε = 0).

3. Ao ranquear as ações pelo resíduo ε em vez do valor bruto de ROIC, você constrói uma carteira que tem exposição EXATA a zero beta em relação a Mercado, Tamanho e Valor.

Em Python, isso é resolvido de forma vetorial limpa com decomposição QR ou projeção matricial de Annihilation:
M = I - X @ inv(X'X) @ X'
fator_ortogonal = M @ fator_bruto

Quando você roda esse teste, descobre que muitos fatores aclamados no "Factor Zoo" simplesmente colapsam para t-stat < 1.0 quando ortogonalizados contra os pilares clássicos.

Você costuma rodar ortogonalização prévia nos seus sinais ou joga todas as features diretamente num regressor linear/lasso?

Para aprender o Teorema FWL na prática, baixar a Ementa Oficial do curso e receber os scripts em Python com dados da B3:
👉 https://curso-quant-research.netlify.app/

#QuantFinance #Econometria #FactorInvesting #Python #AlgebraMatricial
