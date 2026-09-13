import csv
import json
import unicodedata
from collections import Counter

def normalize(text):
    if not text:
        return ""
    text = unicodedata.normalize('NFKD', str(text))
    text = "".join([c for c in text if not unicodedata.combining(c)])
    return text.lower().strip()

with open('connections.csv', 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

header_idx = -1
for i, l in enumerate(lines):
    if l.startswith('First Name,Last Name'):
        header_idx = i
        break

reader = csv.DictReader(lines[header_idx:])
connections = [r for r in reader if r.get('First Name')]

fin_entity_kws = [
    'capital', 'asset', 'investimentos', 'wealth', 'gestora', 'gestao de recursos',
    'bank', 'banco', 'corretora', 'ctvm', 'dtvm', 'family office', 'hedge fund',
    'fundos', 'securities', 'fundo'
]

agro_kws = [
    'agro', 'agricola', 'graos', 'fazenda', 'sementes', 'adubos', 'fertilizante',
    'cooperativa', 'slc maquinas', 'bunge', 'cotrijal', 'usina', 'cana', 'biofuel',
    'agronegocio', 'moinho iguacu', 'dreymoor', 'quadra commodities', 'tks agrologistica',
    'onebeef', 'corteva', 'komatsu', 'veterinaria', 'pecuaria', 'soja', 'milho', 'trigo',
    'rural', 'agribrasil', 'cafe', 'algodao', 'citros', 'laranja', 'frigorifico', 'minerva foods',
    'agromano', 'terramagna', 'copersucar', 'louis dreyfus', 'timbro trading', 'agrocereais'
]

quant_global_names = [
    'lopez de prado', 'david blitz', 'harald lohre', 'guido baltussen', 'sebastien page',
    'caio natividade', 'paulo gala', 'alexandre schwartzman', 'saeed amen', 'sofien kaabar',
    'jonathan kinlay', 'gianni pola', 'vincent zoonekynd', 'kathryn kaminski',
    'neil constable', 'ian baker', 'carlos takahashi', 'giuliano de marchi', 'daniel darahem',
    'solange srour', 'thomas wu', 'fernando ferreira', 'matthias uhl', 'aleksandr treskov',
    'gino cenedese', 'juan torres', 'rishi kohli', 'brian mangwiro', 'marcello estevao',
    'andreas steiner', 'quentin gallea', 'marcos carreira'
]

res = {
    # 1. Influência e Autoridade Quant
    "influencia_titans": [],
    "influencia_media_podcasts": [],
    "influencia_headhunters": [],
    "influencia_academicos": [],

    # 2. Materiais & Infoprodutos Quant
    "compradores_playbook_transicao": [],
    "compradores_toolkit_econometria": [],
    "assinantes_factor_newsletter": [],

    # 3. Clientes de Assessoria de Investimentos (Prospects Reais)
    "assessoria_agro_commodities": [],
    "assessoria_empresarios_founders": [],
    "assessoria_executivos_clevel": [],
    "assessoria_medicos_advogados": [],
    "assessoria_investidores_hnw": [],

    # 4. Ecossistema de Assessoria e Mercado (Parceiros/Networking)
    "ecossistema_jfk_colegas": [],
    "ecossistema_assessores_outros": [],
    "ecossistema_mercado_financeiro": [],

    # 5. Outros
    "outros": []
}

for c in connections:
    first_name = c['First Name'].strip()
    last_name = c['Last Name'].strip()
    name = f"{first_name} {last_name}".strip()
    pos = c['Position'].strip()
    comp = c['Company'].strip()
    url = c['URL'].strip()
    email = c.get('Email Address', '').strip()
    date_conn = c.get('Connected On', '').strip()
    item = {"name": name, "pos": pos, "comp": comp, "url": url, "email": email, "date": date_conn}

    n_name = normalize(name)
    n_pos = normalize(pos)
    n_comp = normalize(comp)
    n_all = f"{n_name} {n_pos} {n_comp}"

    if not pos and not comp:
        res["outros"].append(item)
        continue

    # JFK Peers
    if 'jfk investimentos' in n_comp or 'jfk corretora' in n_comp:
        res["ecossistema_jfk_colegas"].append(item)
        continue

    # Global Quant Titans
    if any(p in n_name for p in quant_global_names):
        res["influencia_titans"].append(item)
        continue

    # Headhunters
    if any(k in n_all for k in ['recruiter', 'headhunter', 'talent acquisition', 'selby jennings', 'phaidon', 'gethyr', 'robert half', 'fox human capital', 'roy talman', 'ackermann']):
        res["influencia_headhunters"].append(item)
        continue

    # Media, Podcasters, Jornalistas
    if (any(k in n_all for k in ['blushing quants', 'análise macro', 'analise macro', 'suno', 'economies mdpi', 'momentum podcast'])
        or any(k in n_pos for k in ['podcast', 'jornalista', 'editor', 'colunista', 'host', 'comunicacao de investimentos'])):
        res["influencia_media_podcasts"].append(item)
        continue

    # Assessoria: Agro & Commodities (Founders, diretores, proprietários, gerentes)
    if any(k in n_all for k in agro_kws) and not any(k in n_comp for k in ['investo']):
        if any(k in n_pos for k in ['ceo', 'founder', 'proprietario', 'diretor', 'gerente', 'head', 'superintendente', 'agricultor', 'general manager', 'board member', 'socio', 'comercial', 'controller', 'agronomo', 'planejamento', 'suprimentos', 'compras']):
            res["assessoria_agro_commodities"].append(item)
            continue

    # Assessoria: Médicos, Dentistas, Advogados Sócios (não estagiários)
    if any(k in n_all for k in ['medico', 'medica', 'advogado', 'advogada', 'cirurgiao', 'advocacia', 'procurador', 'juiz', 'psicolog', 'clinica', 'odontopay', 'dentista']) and not any(k in n_pos for k in ['estagiari', 'intern', 'recepcionista', 'auxiliar', 'assistente']):
        res["assessoria_medicos_advogados"].append(item)
        continue

    # Assessoria / Wealth: Investidores HNW declarados / Traders autônomos
    if any(k in n_pos for k in ['investidor', 'day trader', 'high net worth', 'investor']) and not any(k in n_comp for k in ['asset', 'capital', 'banco', 'bank', 'investo', 'sulamérica']):
        res["assessoria_investidores_hnw"].append(item)
        continue

    # Outros Assessores / Bankers / Wealth Managers (Networking / Pares)
    if any(k in n_pos for k in ['assessor de investimento', 'agente autonomo', 'aai', 'investment advisor', 'private banker', 'wealth management', 'banker alta renda', 'banker', 'consultor de investimento', 'consultora de investimento', 'consultor financeiro']):
        res["ecossistema_assessores_outros"].append(item)
        continue

    # Academics & Professores (Universidades / Faculdades)
    if any(k in n_pos for k in ['professor', 'docente', 'postdoctoral', 'adjunct professor', 'assistant professor', 'associate professor', 'dean', 'pro-rector', 'chair in finance', 'pesquisador', 'researcher', 'fellow', 'lecturer']) and not any(k in n_pos for k in ['quant', 'data scientist']):
        res["influencia_academicos"].append(item)
        continue

    # Quant Transition Playbook (Estudantes, Estagiários, Trainees, Bolsistas, Membros de Ligas)
    if (any(k in n_pos for k in ['intern', 'estagiari', 'trainee', 'student', 'bolsist', 'iniciacao cientifica', 'aluno', 'graduate research assistant', 'research assistant', 'junior analyst', 'analista junior', 'analista jr', 'junior associate', 'working student', 'assistente'])
        or (any(k in n_comp for k in ['liga de mercado', 'finance league', 'universidade', 'university', 'insper', 'fgv', 'mackenzie', 'ufrgs', 'ufpr', 'ufpe', 'usp', 'unicamp', 'puc']) and any(k in n_pos for k in ['membro', 'assistente', 'bolsista', 'estudante', 'student', 'vice president', 'presidente']))):
        res["compradores_playbook_transicao"].append(item)
        continue

    # Buyside Decision Makers / Factor Newsletter (CIOs, Heads de Gestão, PMs em assets e hedge funds)
    is_fin_comp = any(k in n_comp for k in fin_entity_kws)
    if any(k in n_pos for k in ['portfolio manager', 'gestor', 'head of research', 'chief investment officer', 'cio', 'asset allocation', 'estrategista', 'chief economist', 'economista-chefe', 'head of quantitative', 'managing director', 'co-cio', 'head of macro', 'superintendente de gestao', 'head of credit', 'head of equity', 'head of fixed income', 'head of systematic', 'head of dpm', 'head of unit linked', 'head of emerging markets']):
        res["assinantes_factor_newsletter"].append(item)
        continue
    # If CEO/Founder/Partner of an Asset/Fund/Wealth/Capital firm:
    if any(k in n_pos for k in ['ceo', 'founder', 'fundador', 'partner', 'socio', 'managing partner']) and is_fin_comp:
        res["assinantes_factor_newsletter"].append(item)
        continue

    # Quant Practitioners / Econometrics Toolkit (Quants, Data Scientists, Risk Analysts, AI Engineers, Devs)
    if any(k in n_all for k in ['quant', 'data scientist', 'cientista de dados', 'machine learning', 'mlops', 'ai engineer', 'data engineer', 'engenheiro de software', 'software engineer', 'data analyst', 'analista de dados', 'analista quantitativo', 'quantitative researcher', 'quant researcher', 'quantitative analyst', 'quant analyst', 'risk analyst', 'analista de risco', 'modelagem', 'pricing', 'trading strategist', 'algorithmic trader', 'systematic trader', 'econometrista', 'macro research', 'equity research', 'inteligencia artificial']):
        res["compradores_toolkit_econometria"].append(item)
        continue

    # Assessoria: Business Owners & Founders da Economia Real
    if any(k in n_pos for k in ['ceo', 'founder', 'fundador', 'proprietario', 'proprietaria', 'socio proprietario', 'managing partner', 'presidente', 'diretor geral', 'chief executive officer', 'cofundador', 'co-founder', 'owner', 'empresario', 'empresaria']) and not is_fin_comp:
        res["assessoria_empresarios_founders"].append(item)
        continue

    # Assessoria: C-Level & Diretores da Economia Real
    if any(k in n_pos for k in ['cfo', 'coo', 'cto', 'diretor', 'director', 'superintendente', 'general manager', 'vice president', 'vp', 'head']) and not is_fin_comp:
        res["assessoria_executivos_clevel"].append(item)
        continue

    # Rest of Finance Corporate
    if is_fin_comp:
        res["ecossistema_mercado_financeiro"].append(item)
        continue

    # Remainder
    res["outros"].append(item)

print("\n" + "="*50)
print("RELATÓRIO DE DISTRIBUIÇÃO DAS 2.195 CONEXÕES")
print("="*50)
for k, v in res.items():
    print(f"{k.ljust(35)}: {len(v)}")

with open('final_report_data.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, indent=2, ensure_ascii=False)
