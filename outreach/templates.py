"""
Templates de Copys Consultivas para Prospecção de Assessoria de Investimentos (Wealth Management)
Persona: Lucca Simeoni Pavan, Ph.D. em Economia (UFPR), especialista em modelagem quantitativa e alocação de portfólios.
"""

def clean_company_name(comp):
    if not comp:
        return "sua empresa"
    # Remove common corporate suffixes for natural reading
    for suffix in [
        ' ltda.', ' ltda', ' s.a.', ' s/a', ' sa', ' inc.', ' inc', ' corp',
        ' brasil', ' gmbh', ' pvt ltd', ' s.p.a', ' srl', ' cia'
    ]:
        if comp.lower().endswith(suffix):
            comp = comp[:-len(suffix)].strip()
    return comp.strip()

TEMPLATES = {
    "agro": {
        "tag": "🌾 Agronegócio & Tradings",
        "pain_points": ["volatilidade de insumos", "gestão de caixa pós-safra", "isenção em CRAs/LCAs", "hedge de commodities e câmbio"],
        "messages": [
            (
                "Olá {first_name}, tudo bem?\n\n"
                "Acompanho de perto a atuação da {company_clean} no agro. Aqui na mesa, desenvolvemos uma análise quantitativa focada exatamente no ciclo produtivo do agronegócio: como rentabilizar a sobra de caixa da safra e proteger margens de insumos/câmbio sem imobilizar a liquidez do giro.\n\n"
                "Como economista com doutorado pela UFPR e atuação em alocação patrimonial, estruturamos soluções com títulos incentivados (CRAs/LCIs com isenção) e operações de hedge sob medida para produtores e líderes do setor.\n\n"
                "Gostaria de compartilhar um diagnóstico comparativo rápido sobre rentabilidade real para a cadeia do agro. Vale um papo rápido de 10 minutos na próxima semana?",
                # Follow up
                "Olá {first_name}, tudo bem? Imagino a correria por aí. Só passando para saber se conseguiu dar uma olhada na mensagem anterior sobre as alternativas de otimização de caixa e proteção cambial para a {company_clean}. Se fizer sentido, podemos marcar uma breve conversa quando for mais conveniente."
            ),
            (
                "Olá {first_name}, tudo bem?\n\n"
                "Tenho conversado com diretores e produtores da cadeia do agronegócio sobre um desafio frequente: a alta volatilidade dos preços de commodities e a ineficiência de manter liquidez parada em bancos comerciais com tributação desfavorável.\n\n"
                "Utilizo modelagem quantitativa para desenhar estruturas de carteira que protegem o patrimônio da família e o caixa operacional da {company_clean}, combinando CRAs de primeira linha com estratégias de hedge cambial sem taxa de bancão.\n\n"
                "Teria 15 minutos na terça ou quinta para um alinhamento inicial sem compromisso?",
                # Follow up
                "Oi {first_name}, tudo certo? Sei que a rotina no agro é dinâmica. Caso tenha interesse em avaliar como blindar e rentabilizar o caixa da {company_clean} para o próximo ciclo, fico à total disposição para trocarmos uma ideia rápida."
            )
        ]
    },

    "founders": {
        "tag": "🚀 Founders & Empresários",
        "pain_points": ["caixa PJ em bancão", "custo de oportunidade", "planejamento tributário PF/PJ", "diversificação fora do próprio negócio"],
        "messages": [
            (
                "Olá {first_name}, tudo bem?\n\n"
                "Parabéns pela condução da {company_clean}. Tenho conversado com vários fundadores sobre uma dor clássica: o caixa da empresa muitas vezes fica acomodado em CDBs de bancão com 'come-cotas' e taxas ocultas, perdendo rentabilidade real todos os meses.\n\n"
                "Com base na minha experiência como Doutor em Economia e ex-Head de Estratégias Quantitativas, desenvolvemos uma matriz de otimização de liquidez corporativa que aumenta o retorno do caixa PJ (D+0/D+1) e alinha o fluxo de dividendos para a gestão patrimonial pessoal dos sócios.\n\n"
                "Se fizer sentido, adoraria lhe apresentar um raio-X rápido de como otimizar o rendimento do caixa da {company_clean}. Teria 15 minutos nesta semana?",
                # Follow up
                "Olá {first_name}, tudo bem? Imagino que a rotina à frente da {company_clean} seja intensa. Se quiser apenas dar uma olhada no resumo em PDF com a nossa metodologia de otimização de caixa PJ versus CDI tradicional, posso te enviar direto por aqui!"
            ),
            (
                "Olá {first_name}, tudo bem?\n\n"
                "Acompanho o ecossistema e admiro a trajetória da {company_clean}. Em momentos de juros elevados, muitos empresários focam 100% na operação e acabam deixando o patrimônio financeiro e a reserva de oportunidade da empresa com gestão passiva em instituições tradicionais.\n\n"
                "Nós ajudamos fundadores a construir uma tese de alocação de alta precisão técnica — separando com clareza o risco operacional da empresa da preservação e multiplicação do patrimônio pessoal dos sócios.\n\n"
                "Vale tomarmos um café virtual de 10 minutos na quinta-feira para nos conhecermos?",
                # Follow up
                "Oi {first_name}, tudo ótimo? Passando apenas para manter o contato. Se em algum momento fizer sentido revisar a alocação patrimonial ou a eficiência de tesouraria da {company_clean}, será um prazer colaborar."
            )
        ]
    },

    "clevel": {
        "tag": "🏢 Executivos C-Level & Diretores",
        "pain_points": ["falta de tempo", "imposto de renda alto", "concentração em bônus/stock options", "previdência privada ineficiente"],
        "messages": [
            (
                "Olá {first_name}, tudo bem?\n\n"
                "Vejo sua liderança na {company_clean} e sei como o tempo para cuidar das finanças pessoais costuma ser escasso nessa rotina. O padrão mais comum que encontro em executivos é a carteira concentrada em poucos ativos ou alocada em fundos caros de private banking que cobram taxas abusivas para entregar pouco acima do CDI.\n\n"
                "Sou Doutor em Economia pela UFPR e atuo com gestão patrimonial e alocação sistemática independente, ajudando diretores a blindar o patrimônio, otimizar previdência fechada e estruturar alocações globais (offshore).\n\n"
                "Teria disponibilidade para uma conversa breve de 15 minutos na próxima semana?",
                # Follow up
                "Olá {first_name}, tudo certo? Imagino que a agenda corporativa na {company_clean} esteja corrida. Só reforçando que fico à disposição caso queira um diagnóstico independente e sem custos da sua estrutura atual de investimentos."
            ),
            (
                "Olá {first_name}, tudo bem?\n\n"
                "Parabéns pelo trabalho à frente da diretoria da {company_clean}. Muitos executivos seniores com quem converso buscam hoje uma gestão de investimentos técnica, fundamentada em dados e livre de conflitos de interesse de grandes bancos.\n\n"
                "Nosso foco é desenhar portfólios sob medida com governança institucional, combinando ativos isentos de IR, diversificação internacional e gestão ativa de risco para garantir independência financeira no longo prazo.\n\n"
                "Se tiver 15 minutos livres na quarta ou quinta, será um prazer trocar ideias.",
                # Follow up
                "Oi {first_name}, espero que esteja tudo bem. Passando apenas para não deixar a conversa se perder. Se quiser bater um papo rápido sobre estratégias de alocação para executivos C-level, é só me avisar."
            )
        ]
    },

    "doctors_lawyers": {
        "tag": "⚖️ Médicos, Cirurgiões & Advogados",
        "pain_points": ["alta geração de caixa", "pouco tempo para gerir", "tributação na PF", "preservação de capital"],
        "messages": [
            (
                "Olá {first_name}, tudo bem?\n\n"
                "Sei o quanto a rotina em {company_clean} exige dedicação integral. Profissionais liberais de excelência costumam ter uma capacidade formidável de geração de caixa, mas raramente têm tempo para monitorar o mercado e auditar as taxas que os bancos tradicionais cobram.\n\n"
                "Como economista com doutorado e especialista em alocação de portfólios, ajudo profissionais com alta receita a estruturar carteiras focadas em blindagem patrimonial, eficiência fiscal (isenção de IR) e renda passiva previsível de longo prazo.\n\n"
                "Gostaria de lhe apresentar um panorama sobre alocação inteligente para profissionais liberais. Teria 15 minutos nesta semana para um café virtual?",
                # Follow up
                "Olá {first_name}, tudo bem? Imagino que a rotina esteja intensa. Se fizer sentido em algum momento analisar como rentabilizar sua geração de caixa com total independência e assessoria dedicada, estou à disposição!"
            )
        ]
    },

    "investors_hnw": {
        "tag": "💎 Investidores Qualificados & HNW",
        "pain_points": ["acesso a produtos institucionais", "alocação quantitativa", "pesquisa macro independente", "gestão de risco profissional"],
        "messages": [
            (
                "Olá {first_name}, tudo bem?\n\n"
                "Notei seu perfil como investidor ativo e com visão estratégica de mercado. Minha trajetória é dedicada à econometria e estratégias quantitativas de investimento (Doutor em Economia pela UFPR e ex-Head de Estratégias Quant).\n\n"
                "Atuo auxiliando investidores qualificados a implementar alocações sistemáticas baseadas em fatores macro e microeconômicos, com acesso a ativos institucionais, operações estruturadas e controle rigoroso de drawdown.\n\n"
                "Seria um prazer trocar insights sobre o cenário atual de juros e oportunidades assimétricas. Vale um papo de 15 minutos na próxima semana?",
                # Follow up
                "Olá {first_name}, tudo bem? Caso tenha interesse em acompanhar nossas análises sistemáticas de mercado ou trocar visões sobre teses de alocação para 2026/2027, sigo à disposição por aqui."
            )
        ]
    }
}
