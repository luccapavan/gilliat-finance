"""
Prompts e Estruturas de Conteúdo para o LinkedIn
"""

PILLARS = {
    "tecnico": {
        "name": "Modelagem Quantitativa & Factor Investing",
        "description": "Conteúdo técnico profundo sobre risco, fatores, econometria e machine learning financeiro.",
        "topics": [
            "Os 3 maiores erros de iniciantes ao fazer backtesting de fatores (Look-ahead bias, survivorship bias, custos de transação).",
            "Por que Sharpe Ratio isolado é uma métrica perigosa e como usar Sortino, Calmar e Maximum Drawdown.",
            "Cross-sectional Momentum vs Time-Series Momentum: entendendo a diferença matemática na prática.",
            "Modelos GARCH na prática: por que a volatilidade agrupa em clusters no mercado brasileiro.",
            "Como tratar multicolinearidade em modelos multifatoriais com regularização (Ridge/Lasso) e PCA.",
            "O problema do 'Factor Zoo' e por que a maioria dos fatores publicados não sobrevive fora da amostra."
        ]
    },
    "carreira": {
        "name": "Transição de Carreira: Academia / Data Science -> Mercado Quant",
        "description": "Orientações pragmáticas para quem quer entrar em assets, hedge funds ou bancos.",
        "topics": [
            "O choque de realidade ao sair do doutorado em economia e entrar numa gestora de recursos.",
            "O que os gestores de fundos quantitativos realmente olham no seu GitHub (e o que você deve deletar agora).",
            "Cientistas de dados tradicionais vs Quants: por que prever preços com LSTM quase sempre falha no mercado real.",
            "Como se preparar para um teste técnico de take-home para vaga de analista quant.",
            "A habilidade mais subestimada por quem quer entrar na Faria Lima: higienização de dados de mercado."
        ]
    },
    "conversao": {
        "name": "Geração de Demanda & CTAs dos Produtos",
        "description": "Posts que entregam um checklist ou framework e convidam para os infoprodutos.",
        "topics": [
            "Lançamento / Teaser do 'The Quant Transition Playbook': o guia que eu gostaria de ter tido no início.",
            "Convocação para a Newsletter 'Factor & Macro Intelligence': o scorecard mensal de fatores.",
            "Apresentação do 'Applied Financial Econometrics Toolkit': o repositório de templates em Python."
        ]
    }
}

POST_TEMPLATE_GUIDELINES = """
Regras de Redação para o Perfil:
1. Tom de voz: Sóbrio, direto, acadêmico-pragmático, sem clichês de autoajuda ou jargões vazios de marketing.
2. Gancho inicial: As 2 primeiras linhas devem quebrar um mito comum da área ou fazer uma afirmação contra-intuitiva com base em evidências.
3. Espaçamento: Frases curtas e parágrafos de 1 a 3 linhas para garantir ótima legibilidade no feed do LinkedIn.
4. Código / Matemática: Sempre que relevante, incluir pequenos trechos ilustrativos de lógica em Python ou fórmulas explicadas.
5. Fechamento: Terminar com uma pergunta reflexiva para gerar comentários técnicos OU um CTA elegante para o produto.
6. Hashtags: No máximo 3 a 4 hashtags relevantes (ex: #QuantFinance #DataScience #Python #Econometria).
"""
