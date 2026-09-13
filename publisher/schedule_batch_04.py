"""
Script para agendar 5 novos posts no Buffer
Temas: Investimento Sistemático & Factor Investing Aplicado ao Brasil (B3)
Datas: 19/09 a 23/09/2026 às 15:00 UTC (12:00 BRT)
"""
import sys
import os
import json
import requests
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = Path(r"c:\Users\CLIENTE\linkedin_money")
sys.path.append(str(ROOT_DIR))
from config import BUFFER_CONFIG

token = BUFFER_CONFIG.get("access_token")
channel_id = BUFFER_CONFIG.get("profile_id")
graphql_url = "https://api.buffer.com/graphql"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

POSTS = [
    {
        "dueAt": "2026-09-19T15:00:00.000Z",
        "title": "Post 1 - Stock Picking vs Factor Investing na B3",
        "text": """A maioria dos investidores na bolsa brasileira passa horas tentando adivinhar qual será a próxima "ação da vez".

O problema dessa abordagem discricionária no Brasil é matemático: o Ibovespa é um dos índices mais concentrados do mundo. Commodities e grandes bancos frequentemente representam mais de 45% do volume e da ponderação.

Tentar antecipar a commodity da semana ou o humor político em Brasília não é estratégia de investimento; é aposta de curtíssimo prazo contra o ruído estocástico.

Nas gestoras sistemáticas e mesas quants institucionais, a abordagem é diametralmente oposta: nós não compramos histórias, compramos prêmios de risco sistemáticos (Factor Investing).

Em vez de apostar em teses narrativas, decompomos o universo da B3 em dimensões estatisticamente persistentes:
▪ Fator Valor: Ativos com múltiplos descontados (P/L, EV/EBITDA, Book-to-Market) que remuneram o investidor pelo risco de valor relativo.
▪ Fator Momentum: Ações que superaram o mercado nos últimos 12 meses tendem a continuar performando no médio prazo por inércia informacional.
▪ Fator Qualidade: Empresas com alto retorno sobre o capital investido (ROE, ROIC) e baixa alavancagem financeira.
▪ Fator Baixa Volatilidade: A anomalia empírica de que ativos de menor risco oscilam menos nas quedas e geram Sharpe superior no longo prazo.

Ao combinar esses fatores de forma ortogonalizada e neutralizada setorialmente, você elimina o risco idiossincrático de uma empresa específica e constrói uma carteira que extrai retorno robusto em qualquer ciclo macroeconômico.

Esse é o pilar central do investimento sistemático: transformar a tomada de decisão em um processo auditável, reproduzível e desprovido de viés emocional.

Você já opera ou estuda estratégias de Factor Investing na B3? Qual prêmio de risco tem sido mais desafiador de modelar no mercado local?

Para aprofundar os fundamentos da modelagem sistemática, ter acesso aos motores em Python e se preparar para o nosso próximo curso de Análise Quantitativa Aplicada:
👉 https://warrenjax.gumroad.com/l/fsrcmj

---
Lucca Simeoni Pavan, Ph.D.
Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação

#QuantFinance #FactorInvesting #InvestimentoSistematico #MercadoFinanceiro #Python"""
    },
    {
        "dueAt": "2026-09-20T15:00:00.000Z",
        "title": "Post 2 - Momentum na B3: Cross-Sectional vs Time-Series",
        "text": """"Compre na alta e venda na baixa" soa como um conselho absurdo para quem aprendeu análise fundamentalista clássica.

No entanto, no universo de Finanças Quantitativas, o Fator Momentum é uma das anomalias empíricas mais documentadas e robustas da história dos mercados globais e da B3.

O grande problema é que muitos analistas confundem duas abordagens completamente diferentes de Momentum:

1. Time-Series Momentum (Trend Following):
Avalia o comportamento do ativo contra o seu próprio histórico temporal. Se o retorno dos últimos 12 meses for positivo, a estratégia assume posição comprada; se negativo, vende a descoberto ou fica em caixa.
👉 É o coração dos fundos CTA (Commodity Trading Advisors), operando futuros de DI, Dólar e Commodities na B3 com foco em controle de risco e metas de volatilidade.

2. Cross-Sectional Momentum (Relative Momentum):
Compara os ativos entre si no mesmo corte transversal de tempo. Ranqueia todas as ações negociadas na bolsa e compra o decil superior dos melhores desempenhos, vendendo ou subponderando o decil inferior.
👉 É o coração das estratégias de Long-Short de Ações e Smart Beta sistemático.

O segredo institucional na B3: a defasagem operacional 12-2.
Quando modelamos Momentum relativo no Brasil, é mandatório desconsiderar o último mês na janela de apuração (olhando o retorno entre t-12 e t-2 meses).

Por que isso é necessário?
Porque no curtíssimo prazo (1 mês), o mercado brasileiro apresenta forte efeito de reversão à média provocado por atritos de liquidez e rebalanceamentos institucionais. Quem tenta comprar o vencedor do último mês na B3 acaba pagando o spread para o formador de mercado.

A diferença entre um modelo de academia e um modelo institucional de buy-side está justamente no domínio desses detalhes de microestrutura.

Você utiliza defasagens de tempo para neutralizar ruídos de curto prazo nos seus modelos?

Para auditar seus backtests, entender a modelagem vetorial de Momentum e acessar os códigos em Python prontos para a B3:
👉 https://warrenjax.gumroad.com/l/fsrcmj

---
Lucca Simeoni Pavan, Ph.D.
Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação

#QuantFinance #FactorInvesting #Momentum #BolsaDeValores #DataScience #Python"""
    },
    {
        "dueAt": "2026-09-21T15:00:00.000Z",
        "title": "Post 3 - O Factor Zoo e a Mineração de Dados na B3",
        "text": """A literatura acadêmica internacional já publicou mais de 400 "fatores de investimento" diferentes afirmando ter encontrado uma nova fonte de retorno extraordinário no mercado de ações.

Os pesquisadores de ponta apelidaram esse fenômeno de "Factor Zoo" (O Zoológico de Fatores).

A realidade crua? Quando aplicados à bolsa brasileira, mais de 90% desses supostos fatores desaparecem ou quebram em produção.

Por que isso acontece na B3 com tanta frequência?

1. Restrição de Universo e Liquidez:
Nos EUA, você pode testar hipóteses em mais de 3.000 ações negociadas com altíssima liquidez. No Brasil, o universo investível institucional raramente ultrapassa 100 ativos (o índice IBrX-100). Com menos ativos, o risco de sobreajuste estatístico (overfitting) e mineração de dados é exponencialmente maior.

2. Redundância e Colinearidade:
Muitos "fatores inovadores" nada mais são do que o velho Fator Valor ou Fator Tamanho fantasiado com outro nome. Se você cria uma métrica baseada em fluxo de caixa livre e não a controla formalmente por P/L ou EV/EBITDA, você não descobriu um novo prêmio de risco — você apenas reinventou a roda.

Como quants institucionais resolvem isso na prática?
▪ Exigência de t-stat mínimo de 3.0 (em vez do ingênuo t=2.0 de 95% de confiança de livros acadêmicos).
▪ Ortogonalização via Teorema de Frisch-Waugh-Lovell (FWL): purgamos o sinal de qualquer correlação prévia com os fatores de mercado, tamanho e valuation antes de aceitá-lo como um fator autônomo.
▪ Validação fora da amostra (Out-of-Sample) e análise de decaimento de alfa.

Em Finanças Quantitativas, o papel do pesquisador sênior não é encontrar mais fatores; é descartar com rigor cirúrgico os sinais que são apenas ruído disfarçado de oportunidade.

Como você valida se as variáveis do seu modelo têm significância econômica real ou são fruto de data snooping?

Para dominar os testes estatísticos de purificação de fatores e os frameworks de validação institucional:
👉 https://warrenjax.gumroad.com/l/fsrcmj

---
Lucca Simeoni Pavan, Ph.D.
Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação

#QuantFinance #FactorInvesting #Econometria #Estatistica #HedgeFunds #Python"""
    },
    {
        "dueAt": "2026-09-22T15:00:00.000Z",
        "title": "Post 4 - Backtesting Realista na B3: Triângulo das Bermudas",
        "text": """Existe um abismo intransponível entre o backtest que gera aplausos em redes sociais e o modelo que sobrevive à execução real em uma mesa de operações institucional.

Costumo dizer que quase todo modelo quantitativo que quebra ao vivo foi tragado pelo "Triângulo das Bermudas do Backtesting na B3":

1. O Viés de Antecipação Contábil (Look-Ahead Leakage):
O erro número um de quem programa fatores fundamentalistas em Python: usar a data de referência contábil (ex: 31/12) para comprar a ação no primeiro pregão de janeiro.
Na vida real, a Demonstração Financeira Padronizada (DFP) do 4º trimestre só é protocolada na CVM em março ou abril. O backtest que utiliza 31/12 está negociando com dados do futuro — uma performance que nunca existiu. É mandatório aplicar o lag operacional Point-in-Time.

2. A Ilusão da Liquidez e o Slippage Quadrático:
Projetar um retorno espetacular comprando uma carteira de Small Caps com R$ 50 milhões de patrimônio sem restringir o Volume Financeiro Médio Diário (ADTV) é ilusão matemática. Se a sua ordem representa 25% do volume médio do papel, o impacto de mercado (slippage) vai consumir 100% do seu alfa teórico.

3. O Tratamento de Proventos e Desdobramentos:
Calcular retornos em séries não ajustadas ou usar bases que tratam dividendos e juros sobre capital próprio de maneira ingênua distorce a volatilidade e gera falsos sinais de arbitragem.

Nas principais gestoras quantitativas, um modelo só recebe alocação de capital após passar por uma bateria impiedosa de auditoria contra esses vieses.

Disciplina metodológica e ceticismo científico são os verdadeiros ativos de um Quant Researcher.

Você já teve a experiência de colocar um modelo para rodar na prática e perceber que os custos de execução comeram a maior parte do resultado teórico?

Para auditar seus pipelines contra as 10 principais armadilhas metodológicas e utilizar nossos códigos de backtesting vetorizado em Python:
👉 https://warrenjax.gumroad.com/l/fsrcmj

---
Lucca Simeoni Pavan, Ph.D.
Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação

#QuantFinance #Backtesting #Python #EngenhariaDeDados #MercadoFinanceiro #Risco"""
    },
    {
        "dueAt": "2026-09-23T15:00:00.000Z",
        "title": "Post 5 - Além de Markowitz: Ledoit-Wolf e HRP na B3",
        "text": """A teoria clássica de Otimização de Portfólios de Markowitz (1952) é linda na lousa da universidade e um perigo nas mesas de alocação de recursos da vida real.

O Prêmio Nobel de Economia de Markowitz baseia-se na inversão matemática da matriz de covariância dos retornos dos ativos.

No entanto, no mercado financeiro brasileiro — onde choques fiscais, oscilações de juros da Selic e volatilidade de commodities alteram correlações da noite para o dia —, a Otimização de Média-Variância atua como um verdadeiro "maximizador de erros de estimativa":
- Aloca pesos desproporcionais e extremos em ativos com ruído estatístico favorável na amostra;
- Gera curvas de capital hiper-sensíveis que exigem giro excessivo de carteira (turnover proibitivo);
- Falha drasticamente durante crises de liquidez, exatamente quando a diversificação é mais necessária.

Como a moderna gestão sistemática resolve essa fragilidade?

Através de duas abordagens quantitativas institucionais:

1. Encolhimento Analítico de Covariância (Ledoit-Wolf Shrinkage):
Em vez de confiar cegamente na matriz amostral ruidosa, encolhemos estatisticamente a matriz de covariância em direção a uma estrutura teórica bem-comportada (como correlação constante). Isso estabiliza a inversão matricial e blinda os pesos contra overfitting.

2. Hierarchical Risk Parity (HRP):
Metodologia pioneira desenvolvida por Marcos López de Prado que une Aprendizado de Máquina Não-Supervisionado com Teoria de Grafos. O HRP agrupa os ativos em uma árvore hierárquica (dendrograma) a partir da matriz de correlação e distribui o risco recursivamente — eliminando por completo a necessidade de inverter matrizes de covariância.

O resultado? Uma alocação muito mais estável, robusta em momentos de estresse de mercado e com menor necessidade de rebalanceamento forçado.

Em finanças institucionais, a matemática sofisticada não serve para prometer lucros mágicos, mas para blindar o portfólio contra a incerteza estrutural do mundo real.

Você ainda utiliza a fronteira eficiente tradicional ou já migrou para técnicas de alocação robusta como Ledoit-Wolf e HRP?

Para dominar esses algoritmos de alocação e rodar os scripts completos de engenharia de risco em Python:
👉 https://warrenjax.gumroad.com/l/fsrcmj

---
Lucca Simeoni Pavan, Ph.D.
Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação

#QuantFinance #AssetAllocation #MachineLearning #Markowitz #Python #RiskManagement"""
    }
]

mutation = """
mutation CreatePost($input: CreatePostInput!) {
  createPost(input: $input) {
    ... on PostActionSuccess {
      post {
        id
        status
        dueAt
      }
    }
    ... on LimitReachedError {
      message
    }
    ... on UnauthorizedError {
      message
    }
    ... on InvalidInputError {
      message
    }
    ... on UnexpectedError {
      message
    }
  }
}
"""

print(f"🚀 Iniciando agendamento de {len(POSTS)} posts no Buffer...")
print(f"Canal Alvo: {channel_id}")
print("=" * 60)

for idx, post in enumerate(POSTS, 1):
    payload = {
        "channelId": channel_id,
        "text": post["text"],
        "mode": "customScheduled",
        "dueAt": post["dueAt"],
        "schedulingType": "automatic",
        "needsApproval": False,
        "saveToDraft": False
    }
    
    res = requests.post(
        graphql_url,
        headers=headers,
        json={"query": mutation, "variables": {"input": payload}},
        timeout=20
    )
    
    res_json = res.json()
    post_info = res_json.get("data", {}).get("createPost", {})
    created_post = post_info.get("post")
    
    if created_post:
        print(f"✅ [{idx}/5] {post['title']}")
        print(f"   ID: {created_post.get('id')} | Data: {created_post.get('dueAt')} | Status: {created_post.get('status')}")
    else:
        print(f"❌ [{idx}/5] Erro ao agendar {post['title']}: {json.dumps(res_json, indent=2)}")

print("=" * 60)
print("🎉 Concluído!")
