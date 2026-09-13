"""
Gerador de Lote 2 Bilíngue (Português & English)
Conteúdos de Alta Densidade Técnica e Rigor Metodológico
Autor: Lucca Simeoni Pavan, Ph.D.
"""
import os
import json
from pathlib import Path

BATCH_02_POSTS = [
    {
        "id": "post_01_fwl_ortogonalizacao",
        "pillar": "tecnico_avancado",
        "title_pt": "O Teorema de Frisch-Waugh-Lovell (FWL) e a Ortogonalização de Fatores em Python",
        "title_en": "The Frisch-Waugh-Lovell (FWL) Theorem & Factor Orthogonalization in Python",
        "suggested_day": "Segunda-feira / Monday (08:30)",
        "content_pt": """Se você calcula o alfa de um fator sem neutralizar a exposição a fatores concorrentes, há 90% de chance de estar comemorando uma ilusão estatística.

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

#QuantFinance #Econometria #FactorInvesting #Python #AlgebraMatricial""",
        "content_en": """If you compute a factor's alpha without neutralizing its exposure to existing benchmark factors, there is a 90% chance you are celebrating a statistical illusion.

In theoretical econometrics, the Frisch-Waugh-Lovell (FWL) Theorem is one of the most elegant results in matrix projection algebra.

In quantitative asset management, however, it is the daily operational tool to answer a crucial question:
"Does my signal have genuine orthogonal alpha, or is it merely disguised beta to well-known factors?"

Suppose you want to test whether a Quality metric (e.g., high ROIC) generates genuine abnormal returns.
Since high-ROIC firms often exhibit lower debt and higher P/E multiples, how do you isolate pure Quality without suffering from omitted variable bias?

The institutional FWL pipeline in practice:

1. Project the candidate factor (ROIC) onto control factors (Size, Market, Value) via cross-sectional regression:
   ROIC = Xβ + ε

2. The residual vector ε is, by matrix construction, strictly orthogonal to the subspace spanned by control factors (X'ε = 0).

3. By ranking equities based on residual ε rather than raw ROIC, you construct a factor portfolio with EXACTLY zero beta exposure to Market, Size, and Value.

In Python, this is computed vectorially via the Annihilation / Residual Maker matrix (or QR decomposition):
M = I - X @ np.linalg.pinv(X.T @ X) @ X.T
orthogonal_factor = M @ raw_factor

When you run this rigorous test, you quickly discover that many acclaimed signals in the "Factor Zoo" collapse to t-stats < 1.0 once properly orthogonalized.

Do you orthogonalize your features against style benchmarks prior to portfolio construction, or do you feed raw features directly into a linear/regularized model?

#QuantFinance #FactorInvesting #Python #Econometrics #PortfolioManagement"""
    },
    {
        "id": "post_02_matriz_covariancia_ledoit_wolf",
        "pillar": "tecnico_avancado",
        "title_pt": "Por que a Matriz de Covariância Amostral é o Calcanhar de Aquiles de Markowitz",
        "title_en": "Why the Sample Covariance Matrix is the Achilles Heel of Mean-Variance Optimization",
        "suggested_day": "Terça-feira / Tuesday (08:30)",
        "content_pt": """A otimização de média-variância de Harry Markowitz é matematicamente elegante.
Na prática de mercado, no entanto, ela costuma ser chamada de "máquina de maximização de erros".

O culpado raramente é a formulação quadrática. O verdadeiro problema é a Matriz de Covariância Amostral.

Quando você otimiza uma carteira com N = 100 ativos usando uma janela histórica de T = 252 dias:
1. O número de parâmetros a estimar é N(N+1)/2 = 5.050 covariâncias.
2. A razão N/T ≈ 0.40 significa que a matriz está severamente mal-condicionada.
3. Os menores autovalores — que contêm puro ruído amostral — viram os maiores pesos ao inverter a matriz (Σ⁻¹).

Soluções institucionais com rigor estatístico:
1. Encolhimento de Ledoit-Wolf (Shrinkage): combina a matriz amostral com um alvo estruturado analiticamente sob norma de Frobenius.
2. Hierarchical Risk Parity (HRP de López de Prado): usa teoria dos grafos e clustering hierárquico, dispensando qualquer inversão matricial.

Em Python com scikit-learn:
from sklearn.covariance import LedoitWolf
cov_clean = LedoitWolf().fit(returns).covariance_

Qual método de regularização de matriz de risco você tem utilizado em produção?

#AssetManagement #Risco #OtimizacaoDePortfolio #MachineLearning #Estatistica""",
        "content_en": """Harry Markowitz’s Mean-Variance optimization is mathematically elegant.
In institutional production, however, practitioners often call it an "error-maximization engine."

The flaw rarely lies in the quadratic objective function itself. The real culprit is the Sample Covariance Matrix.

When optimizing a universe of N = 100 assets over T = 252 trading days:
1. You must estimate N(N+1)/2 = 5,050 independent covariance parameters.
2. The ratio N/T ≈ 0.40 indicates severe matrix ill-conditioning.
3. Inverting the matrix (Σ⁻¹) inverts the eigenvalues: the smallest eigenvalues—which represent pure sampling noise—become the largest drivers of portfolio weights!

How institutional quants solve this:
1. Ledoit-Wolf Shrinkage: analytically blends the noisy sample matrix with a structured target (e.g., constant correlation or identity) under Frobenius norm loss.
2. Hierarchical Risk Parity (HRP by Marcos López de Prado): uses graph theory and tree clustering, completely eliminating the need for matrix inversion.

In Python via scikit-learn:
from sklearn.covariance import LedoitWolf
cov_clean = LedoitWolf().fit(returns).covariance_

Which covariance regularization technique do you currently deploy in production?

#QuantFinance #RiskManagement #PortfolioOptimization #MachineLearning #Python"""
    },
    {
        "id": "post_03_microestrutura_slippage_almgren",
        "pillar": "microestrutura",
        "title_pt": "Slippage Não-Linear: Por que 90% dos Backtests Morrem na Produção",
        "title_en": "Non-Linear Slippage: Why 90% of Backtests Die in Production",
        "suggested_day": "Quarta-feira / Wednesday (09:00)",
        "content_pt": """A maioria dos pesquisadores iniciantes assume taxa fixa de corretagem e 5 bps de slippage.
Quando o fundo entra em produção, a performance real descola 800 bps da curva simulada.

A razão tem nome: Microestrutura de Mercado e Impacto Não-Linear de Preço.

1. Modelo de Almgren-Chriss (Impacto Temporário vs Permanente):
O impacto temporário decorre do consumo imediato do book. O permanente ocorre porque a sua própria agressão move o preço de equilíbrio do mercado contra a carteira.

2. A Lei da Raiz Quadrada do Impacto de Mercado:
O impacto de preço escala proporcionalmente à raiz quadrada do volume negociado em relação ao volume médio diário (ADV):
Impacto ≈ Y * σ * sqrt(Q / ADV)

Com R$ 100 mil simulados, a estratégia parece incrível. Com R$ 10 milhões sob gestão, o custo de impacto consome 100% do alfa.

Como você modela fricções de microestrutura nos seus backtests?

#Microestrutura #TradingQuantitativo #Execucao #MercadoFinanceiro #FinancasQuantitativas""",
        "content_en": """Most junior researchers assume flat brokerage fees and 5 bps of fixed slippage.
Once capital is deployed, live performance deteriorates by 800 bps against the simulated curve.

The explanation: Market Microstructure & Non-Linear Market Impact.

1. The Almgren-Chriss Framework (Temporary vs Permanent Impact):
Temporary impact reflects instantaneous order-book liquidity consumption. Permanent impact reflects information leakage: your own execution moves the equilibrium price against you.

2. The Square-Root Law of Price Impact:
Price impact scales with the square root of order size relative to Average Daily Volume (ADV):
Impact ≈ Y * σ * sqrt(Q / ADV)

With $50,000 simulated capital, the strategy looks like pure gold. With $20 million AUM, market impact absorbs 100% of the alpha before positions are even filled.

In institutional research, you must model the Strategy Capacity Frontier.

How do you account for non-linear execution frictions in your backtests?

#Microstructure #QuantFinance #AlgorithmicTrading #Execution #AssetManagement"""
    },
    {
        "id": "post_04_takehome_desafio_quant",
        "pillar": "carreira_senior",
        "title_pt": "A Anatomia de um Desafio Técnico de 48 Horas para Vaga Quant",
        "title_en": "The Anatomy of a 48-Hour Quant Take-Home Challenge",
        "suggested_day": "Quinta-feira / Thursday (09:00)",
        "content_pt": """Você passou na primeira triagem e recebeu: "Segue o dataset com 10 anos de retornos. Você tem 48 horas para nos entregar uma estratégia multifator."

O que a maioria dos candidatos entrega?
- Notebook monolítico de 3.000 linhas.
- Modelos complexos de deep learning ou XGBoost ajustados sem validação temporal estrita.
- Conclusão com Sharpe de 3.8 (descartado na hora por overfitting óbvio).

O que um candidato sênior entrega para ser contratado?
1. Hipótese Econômica a Priori: 3 ou 4 fatores com respaldo teórico claro.
2. Higienização Point-in-Time: marcas temporais com defasagem real de balanços.
3. Código Modular e Testável: classes organizadas e testes unitários em pytest.
4. Decomposição de Risco: correlações com benchmarks, Turnover e Max Drawdown em períodos de estresse.

No mercado financeiro quantitativo, maturidade metodológica vale dez vezes mais do que complexidade algorítmica cega.

#CarreiraQuant #DataScience #ProcessoSeletivo #MercadoFinanceiro #Python""",
        "content_en": """You passed initial screening and received: "Here is a 10-year market dataset. You have 48 hours to deliver a systematic multifactor strategy."

What do most candidates submit?
- A 3,000-line monolithic Jupyter notebook.
- Complex XGBoost or LSTM models fit without strict temporal purging.
- An in-sample Sharpe ratio of 3.8 (instantly discarded by PMs for obvious overfitting).

What do senior candidates submit to secure the offer?
1. An A Priori Economic Hypothesis: 3 to 4 factors with sound theoretical grounding.
2. Point-in-Time Data Engineering: explicit handling of earnings filing publication lags.
3. Modular, Production-Grade Code: structured classes with unit tests in `pytest`.
4. Comprehensive Risk Attribution: benchmark correlation, turnover decay, and regime drawdowns during historical crises.

In quantitative finance, methodological rigor is worth ten times blind algorithmic complexity.

#QuantCareers #DataScience #HedgeFunds #FinTech #Python"""
    },
    {
        "id": "post_05_conversao_playbook_metodologia",
        "pillar": "conversao_autoridade",
        "title_pt": "O Maior Perigo em Finanças Quantitativas é o Ajuste sem Tese Econômica",
        "title_en": "The Greatest Danger in Quantitative Finance is Fitting Without Economic Rationale",
        "suggested_day": "Sexta-feira / Friday (11:30)",
        "content_pt": """Se você colocar um algoritmo de machine learning para rodar sobre um banco de 5.000 métricas financeiras, ele SEMPRE vai encontrar uma combinação que bateu o mercado no passado.
Mas isso não é ciência. É apenas mineração de dados (data snooping).

Depois de anos atuando na gestão quantitativa de recursos — da pesquisa acadêmica no doutorado até a liderança de modelagem sistemática e alocação de portfólios no mercado financeiro —, condensei os pilares que realmente funcionam no mundo real em um material único:

📘 "The Quant Transition Playbook" — Da Academia & Data Science para o Mercado Financeiro Quantitativo (Edição Bilíngue PT/EN).

O que está incluso:
1. Livro Digital em PDF com diagramação executiva completa (versões em Português e Inglês).
2. Protocolos anti-vieses (Look-ahead, Survivorship e validação Purged K-Fold com Embargo).
3. Templates de Código em Python:
   - `backtest_multifactor.py`: seleção multifator (Value + Momentum) com Z-Scores e turnover real.
   - `risk_performance_metrics.py`: motor estatístico de métricas institucionais (Sharpe, Sortino, Calmar, Drawdown e CVaR).

🔗 Acesse o Playbook e os scripts com entrega imediata:
https://warrenjax.gumroad.com/l/fsrcmj

#FinancasQuantitativas #FactorInvesting #DataScience #Econometria #Python #Carreira""",
        "content_en": """If you unleash a machine learning algorithm on a dataset of 5,000 financial metrics, it will ALWAYS find an empirical combination that beat the market in the past.
That is not scientific research. It is pure data snooping.

After years working in systematic asset management—from academic doctoral research to leading quantitative modeling and multi-asset allocation—I synthesized the institutional frameworks that actually survive out-of-sample in a comprehensive blueprint:

📘 "The Quant Transition Playbook" — From Academia & Data Science to Systematic Asset Management (Bilingual PT/EN Edition).

What is included:
1. High-Resolution Executive PDF Book (Both English and Portuguese editions).
2. Institutional Anti-Bias Protocols (Look-ahead, Survivorship & Purged K-Fold with Embargo).
3. Production Python Code Templates:
   - `backtest_multifactor.py`: Vectorized multifactor engine (Value + Momentum) with cross-sectional Z-scores and turnover costs.
   - `risk_performance_metrics.py`: Institutional engine for Sharpe, Sortino, Calmar, Drawdowns, and Coherent CVaR (Expected Shortfall).

🔗 Instant access to the Playbook and Python repository:
https://warrenjax.gumroad.com/l/fsrcmj

#QuantFinance #FactorInvesting #HedgeFunds #DataScience #Python #FinTech"""
    }
]

def generate_batch_02_bilingual():
    batch_dir = Path("posts/batch_02")
    batch_dir.mkdir(parents=True, exist_ok=True)
    
    index_file = batch_dir / "index.json"
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(BATCH_02_POSTS, f, ensure_ascii=False, indent=2)
        
    for post in BATCH_02_POSTS:
        # Arquivo em Português
        pt_path = batch_dir / f"{post['id']}_pt.md"
        with open(pt_path, "w", encoding="utf-8") as f:
            f.write(f"# {post['title_pt']}\n\n")
            f.write(f"- **Pilar:** {post['pillar']}\n")
            f.write(f"- **Horário Sugerido:** {post['suggested_day']}\n")
            f.write(f"- **Idioma:** Português\n\n---\n\n")
            f.write(post['content_pt'])
            f.write("\n")
            
        # Arquivo em Inglês
        en_path = batch_dir / f"{post['id']}_en.md"
        with open(en_path, "w", encoding="utf-8") as f:
            f.write(f"# {post['title_en']}\n\n")
            f.write(f"- **Pillar:** {post['pillar']}\n")
            f.write(f"- **Suggested Time:** {post['suggested_day']}\n")
            f.write(f"- **Language:** English\n\n---\n\n")
            f.write(post['content_en'])
            f.write("\n")
            
    print(f"[OK] {len(BATCH_02_POSTS)*2} arquivos de posts gerados com sucesso (PT e EN) em {batch_dir}")

if __name__ == "__main__":
    generate_batch_02_bilingual()
