"""
Gerador de Lotes de Postagens para o LinkedIn
"""
import os
import json
from pathlib import Path

POSTS_DATA = [
    {
        "id": "post_01_erros_backtest",
        "pillar": "tecnico",
        "title": "Os 3 erros que destroem backtests no mercado real",
        "suggested_day": "Segunda-feira (08:30)",
        "content": """O backtest mais bonito que você já viu em Python provavelmente vai quebrar no primeiro mês de execução real.

Quando converso com cientistas de dados ou pesquisadores que estão começando em modelagem financeira quantitativa, vejo quase sempre os mesmos três vieses ocultos:

1. Look-Ahead Bias (Viés de Antecipação):
Usar variáveis que só estavam disponíveis no fechamento do pregão (ou dias depois) para tomar decisões na abertura. Parece óbvio, mas calcular métricas usando balanços trimestrais antes da data oficial de divulgação pela CVM é o erro número um.

2. Survivorship Bias (Viés de Sobrevivência):
Fazer backtest em um universo de ações com as empresas que compõem o índice hoje. Você exclui automaticamente as empresas que quebraram, foram liquidadas ou deslistadas ao longo do período, inflando artificialmente o retorno histórico da sua estratégia.

3. Custos de Transação e Market Impact Desconsiderados:
Uma estratégia com giro de carteira semanal (high turnover) que gera 25% ao ano na planilha pode virar negativa quando você aplica corretagem, emolumentos B3, aluguel de ações (no caso de ponta vendida) e o slippage de execução.

Modelar mercado não é prever o próximo candle com uma rede neural profunda. É ter disciplina estatística para garantir que o seu sinal sobrevive fora da amostra e aos custos do mundo real.

Qual viés já te deu mais dor de cabeça em projetos de modelagem?

#QuantFinance #DataScience #Python #InvestimentoSistematico #FinancasQuantitativas"""
    },
    {
        "id": "post_02_carreira_lstm_vs_quants",
        "pillar": "carreira",
        "title": "Por que prever ações com LSTM costuma falhar em entrevistas quant",
        "suggested_day": "Quarta-feira (09:00)",
        "content": """Se você colocar no seu GitHub um projeto intitulado "Prevendo o preço de PETR4 com LSTM e Redes Neurais", a chance de um gestor quant descartar o currículo é alta.

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

#CarreiraQuant #MachineLearning #CienciadeDados #DataScience #Financas"""
    },
    {
        "id": "post_03_conversao_playbook",
        "pillar": "conversao",
        "title": "O mapa prático de transição da Academia/Data Science para o Mercado Quant",
        "suggested_day": "Sexta-feira (11:30)",
        "content": """Quando concluí meu Doutorado em Economia e ingressei na gestão quantitativa de recursos, percebi uma lacuna brutal:

A faculdade te ensina a teoria econométrica pura. Os cursos de data science ensinam a ajustar modelos no Scikit-Learn.
Mas praticamente NINGUÉM ensina como uma gestora de fundos quantitativos realmente opera no dia a dia.

Questões como:
- Como estruturar um pipeline de Factor Investing (Momentum, Value, Quality, Low Vol) sem vieses temporais?
- Como codificar um backtester vetorial confiável em Python?
- O que realmente cai nas provas técnicas e entrevistas de contratação para vagas de Quant?

Nos últimos meses, organizei toda essa vivência empírica, erros comuns e boas práticas de modelagem em um material único:

📘 "The Quant Transition Playbook" — O Guia Prático para Ingressar no Mercado Financeiro Quantitativo.

O material inclui o passo a passo metodológico mais 3 repositórios com código em Python prontos para estudo:
1. Pipeline de extração e tratamento de dados de mercado da B3.
2. Modelo multifator completo de seleção de ativos e rebalanceamento.
3. Motor de análise de risco e performance (Sharpe, Sortino, Drawdown, VaR).

Se você quer acelerar sua transição para a Faria Lima ou mesas de operações com base sólida e código real:

🔗 Link com todos os detalhes e templates: https://warrenjax.gumroad.com/l/fsrcmj

#QuantFinance #Carreira #Econometria #Python #AssetManagement"""
    },
    {
        "id": "post_04_tecnico_garch_volatilidade",
        "pillar": "tecnico",
        "title": "Por que assumir volatilidade constante é um tiro no pé",
        "suggested_day": "Terça-feira (08:30)",
        "content": """Um dos fatos estilizados mais conhecidos em finanças empíricas é o agrupamento de volatilidade (volatility clustering): grandes choques tendem a ser seguidos por grandes choques, e períodos de calmaria tendem a persistir.

Ainda assim, vejo analistas calculando desvio padrão simples dos últimos 30 dias para estimar o risco futuro de um ativo.

O problema dessa abordagem ingênua:
1. Ela atribui o mesmo peso para o retorno de hoje e o retorno de 29 dias atrás.
2. Ela ignora que a volatilidade possui memória e dinâmica autorregressiva.
3. Em eventos de estresse de mercado, o VaR (Value at Risk) calculado de forma estática subestima o risco justamente quando você mais precisa de proteção.

É aqui que a família de modelos ARCH/GARCH entra em cena.
Ao modelar a variância condicional como dependente dos erros passados e da própria variância defasada, conseguimos capturar a assimetria e o retorno rápido ao equilíbrio médio.

Em Python, com poucas linhas usando a biblioteca `arch`, é possível estimar modelos GARCH(1,1) ou EGARCH (que captura o 'efeito alavancagem' — quedas de preço geram mais volatilidade que altas).

Você já utiliza volatilidade condicional na modelagem de risco da sua carteira ou ainda usa desvio padrão rolante?

#Risco #Econometria #GARCH #Python #MercadoFinanceiro"""
    },
    {
        "id": "post_05_tecnico_factor_zoo",
        "pillar": "tecnico",
        "title": "O 'Factor Zoo': Por que mais de 400 fatores de mercado são pura ilusão estatística",
        "suggested_day": "Quinta-feira (09:00)",
        "content": """Na literatura acadêmica de finanças, estima-se que existam mais de 400 'fatores de risco' publicados com suposto prêmio de retorno acima do mercado.

O professor John Cochrane chamou isso de "Factor Zoo" (o zoológico de fatores).

Mas por que a grande maioria desses fatores simplesmente desaparece quando tentamos explorá-los em uma carteira real?

Três motivos estatísticos e práticos explicam:

1. Data Snooping e p-hacking:
Se você testar 100 indicadores diferentes com nível de significância de 5%, por pura probabilidade estocástica cerca de 5 deles vão parecer estatisticamente significantes, sem que exista qualquer fundamento econômico real por trás.

2. Falta de robustez fora da amostra:
Um fator só é confiável se funcionar em diferentes períodos temporais, diferentes geografias e através de diferentes métricas (ex: Value medido por P/L, EV/EBITDA e P/VP).

3. Custos de implementação:
Muitos fatores mostram 'alfa' teórico porque estão concentrados em ações de microcaps ilíquidas, onde o custo de montagem da posição consome 100% do retorno excedente.

Em factor investing profissional, menos é mais: concentre-se nos pilares comprovados (Value, Momentum, Quality, Low Volatility e Size) com tese econômica clara e disciplina de execução.

Qual o seu fator favorito na bolsa brasileira?

#FactorInvesting #Quant #Investimentos #MercadoDeCapitais #Economia"""
    }
]

def generate_batch():
    batch_dir = Path("posts/batch_01")
    batch_dir.mkdir(parents=True, exist_ok=True)
    
    index_file = batch_dir / "index.json"
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(POSTS_DATA, f, ensure_ascii=False, indent=2)
        
    for post in POSTS_DATA:
        post_path = batch_dir / f"{post['id']}.md"
        with open(post_path, "w", encoding="utf-8") as f:
            f.write(f"# {post['title']}\n\n")
            f.write(f"- **Pilar:** {post['pillar']}\n")
            f.write(f"- **Horário Sugerido:** {post['suggested_day']}\n\n")
            f.write("---\n\n")
            f.write(post['content'])
            f.write("\n")
            
    print(f"Sucesso! {len(POSTS_DATA)} posts gerados em {batch_dir}")

if __name__ == "__main__":
    generate_batch()
