import csv
import json
import unicodedata
from collections import Counter, defaultdict

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

print(f"Total connections processed: {len(connections)}")

# Master Categories
groups = {
    # 1. QUANT INFLUENCE & PARTNERSHIPS
    "1_quant_global_titans": [],
    "1_quant_media_podcasts": [],
    "1_quant_headhunters": [],
    "1_academics_professors": [],

    # 2. QUANT PRODUCTS (BUYERS)
    "2_product_quant_transition": [],    # Students, interns, trainees, junior analysts, career changers
    "2_product_econometrics_toolkit": [],# Practicing quants, risk analysts, data scientists, ML engineers
    "2_product_factor_newsletter": [],   # Buyside PMs, hedge fund analysts, CIOs, buy-side research

    # 3. WEALTH ADVISORY (CLIENT PROSPECTS)
    "3_wealth_agro_commodities": [],     # Agro owners, farm managers, grain/trading execs, coop leaders
    "3_wealth_business_owners": [],      # CEOs, Founders, Partners of real economy businesses
    "3_wealth_corporate_c_level": [],    # C-Level, VPs, Directors of medium/large non-finance corporations
    "3_wealth_doctors_lawyers": [],      # Doctors, law firm partners, clinics, specialized liberal pros
    "3_wealth_investors_hnw": [],        # Self-declared investors, family office members, HNW individuals

    # 4. FINANCIAL ECOSYSTEM & INDUSTRY PEERS (NETWORKING / B2B)
    "4_ecosystem_jfk": [],               # JFK colleagues
    "4_ecosystem_advisors_bankers": [],  # Other AAIs, Bankers, Wealth advisors (peers/potential distributors)
    "4_ecosystem_finance_corporate": [], # Other finance pros (compliance, operations, backoffice, credit analysts)

    # 5. OTHERS
    "5_others": []
}

# Known global quant names
global_titans_patterns = [
    'lopez de prado', 'david blitz', 'harald lohre', 'guido baltussen', 'sebastien page',
    'caio natividade', 'paulo gala', 'alexandre schwartzman', 'saeed amen', 'sofien kaabar',
    'jonathan kinlay', 'gianni pola', 'vincent zoonekynd', 'kathryn kaminski',
    'neil constable', 'ian baker', 'carlos takahashi', 'giuliano de marchi', 'daniel darahem',
    'solange srour', 'thomas wu', 'fernando ferreira', 'matthias uhl', 'aleksandr treskov',
    'gino cenedese', 'juan torres', 'rishi kohli', 'brian mangwiro', 'marcello estevao',
    'andreas steiner', 'quentin gallea', 'marcos carreira'
]

agro_keywords = [
    'agro', 'agricola', 'graos', 'fazenda', 'sementes', 'adubos', 'fertilizante',
    'cooperativa', 'slc maquinas', 'bunge', 'cotrijal', 'usina', 'cana', 'biofuel',
    'agronegocio', 'moinho iguacu', 'dreymoor', 'quadra commodities', 'tks agrologistica',
    'onebeef', 'corteva', 'komatsu', 'veterinaria', 'pecuaria', 'soja', 'milho', 'trigo',
    'rural', 'agribrasil', 'cafe', 'algodao', 'citros', 'laranja', 'frigorifico', 'minerva foods',
    'agromano', 'terramagna', 'copersucar', 'louis dreyfus', 'timbro trading'
]

for c in connections:
    first_name = c['First Name'].strip()
    last_name = c['Last Name'].strip()
    name = f"{first_name} {last_name}".strip()
    pos = c['Position'].strip()
    comp = c['Company'].strip()
    url = c['URL'].strip()
    email = c.get('Email Address', '').strip()
    date_conn = c.get('Connected On', '').strip()
    item = {
        "name": name, "pos": pos, "comp": comp, "url": url, "email": email, "date": date_conn
    }

    n_name = normalize(name)
    n_pos = normalize(pos)
    n_comp = normalize(comp)
    n_all = f"{n_name} {n_pos} {n_comp}"

    if not pos and not comp:
        groups["5_others"].append(item)
        continue

    # JFK Peers
    if 'jfk investimentos' in n_comp or 'jfk corretora' in n_comp or 'jfk' in n_comp:
        groups["4_ecosystem_jfk"].append(item)
        continue

    # Global Quant Titans & Top Influencers
    if any(p in n_name for p in global_titans_patterns):
        groups["1_quant_global_titans"].append(item)
        continue

    # Headhunters & Recruiters
    if any(k in n_all for k in ['recruiter', 'headhunter', 'talent acquisition', 'selby jennings', 'phaidon', 'gethyr', 'robert half', 'fox human capital', 'roy talman', 'ackermann']):
        groups["1_quant_headhunters"].append(item)
        continue

    # Media, Podcasters, Journalists, Creators
    if any(k in n_all for k in ['podcast', 'blushing quants', 'host', 'editor', 'jornalista', 'globo', 'jota', 'analise macro', 'suno']):
        if 'análise macro' in n_comp or 'blushing quants' in n_comp or 'podcast' in n_all or 'jornalista' in n_pos or 'editor' in n_pos or 'suno' in n_comp:
            groups["1_quant_media_podcasts"].append(item)
            continue

    # Agro & Commodities (Wealth Prospect #1)
    if any(k in n_all for k in agro_keywords):
        if any(k in n_pos for k in ['ceo', 'founder', 'proprietario', 'diretor', 'gerente', 'head', 'superintendente', 'agricultor', 'general manager', 'board member', 'trading', 'socio', 'comercial', 'controller', 'agronomo']):
            groups["3_wealth_agro_commodities"].append(item)
            continue

    # Other Wealth: Business Owners & Founders (Economy Real)
    if any(k in n_pos for k in ['ceo', 'founder', 'fundador', 'proprietario', 'proprietaria', 'socio proprietario', 'managing partner', 'presidente', 'diretor geral', 'chief executive officer', 'cofundador', 'co-founder', 'owner', 'empresario', 'empresaria']):
        if not any(k in n_comp for k in ['capital', 'asset', 'investimentos', 'quant', 'wealth', 'family office', 'fundo', 'securities']):
            groups["3_wealth_business_owners"].append(item)
            continue

    # Other Wealth: Corporate C-Level & Directors (Real Economy)
    if any(k in n_pos for k in ['cfo', 'coo', 'cto', 'diretor', 'director', 'superintendente', 'general manager', 'vice president', 'vp', 'head']) and not any(k in n_comp for k in ['asset', 'gestora', 'capital', 'investimentos', 'quant', 'corretora', 'family office', 'securities']):
        groups["3_wealth_corporate_c_level"].append(item)
        continue

    # Wealth: Doctors, Dentists, Lawyers, Clinics
    if any(k in n_all for k in ['medico', 'medica', 'advogado', 'advogada', 'cirurgiao', 'advocacia', 'procurador', 'juiz', 'psicolog', 'clinica', 'odontopay', 'dentista', 'hospital']):
        if not any(k in n_pos for k in ['estagiari', 'intern']):
            groups["3_wealth_doctors_lawyers"].append(item)
            continue

    # Wealth: Self-directed Investors & HNW
    if any(k in n_pos for k in ['investidor', 'day trader', 'high net worth', 'investor']) and not any(k in n_comp for k in ['asset', 'capital']):
        groups["3_wealth_investors_hnw"].append(item)
        continue

    # Advisory Peers (XP, BTG, Santander, Bradesco Private, etc.)
    if any(k in n_pos for k in ['assessor de investimento', 'agente autonomo', 'aai', 'investment advisor', 'private banker', 'wealth management', 'banker', 'consultor financeiro', 'consultor de investimento', 'consultora de investimento']):
        groups["4_ecosystem_advisors_bankers"].append(item)
        continue

    # Academics & Researchers (Universities)
    if any(k in n_pos for k in ['professor', 'docente', 'postdoctoral', 'adjunct professor', 'assistant professor', 'associate professor', 'dean', 'pro-rector', 'chair in finance', 'pesquisador', 'researcher', 'fellow', 'lecturer']) and not any(k in n_pos for k in ['quant', 'data scientist']):
        groups["1_academics_professors"].append(item)
        continue

    # Quant Transition Playbook (Students, Interns, Trainees, Junior Transitioners)
    if (any(k in n_pos for k in ['intern', 'estagiari', 'trainee', 'student', 'bolsist', 'iniciacao cientifica', 'aluno', 'graduate research assistant', 'research assistant', 'junior analyst', 'analista junior', 'analista jr', 'junior associate', 'working student', 'assistente'])
        or any(k in n_comp for k in ['liga de mercado', 'finance league', 'universidade', 'university', 'insper', 'fgv', 'mackenzie', 'ufrgs', 'ufpr', 'ufpe', 'usp', 'unicamp', 'puc']) and any(k in n_pos for k in ['membro', 'assistente', 'bolsista', 'estudante', 'student', 'vice president', 'presidente'])):
        groups["2_product_quant_transition"].append(item)
        continue

    # Quant Buyside Newsletter / High-end Institutional Quant
    if any(k in n_pos for k in ['portfolio manager', 'gestor', 'head of research', 'chief investment officer', 'cio', 'asset allocation', 'estrategista', 'chief economist', 'economista-chefe', 'head of quantitative', 'managing director', 'co-cio', 'head of macro', 'superintendente de gestao', 'head of credit', 'head of equity', 'head of fixed income', 'head of systemic']) and any(k in n_comp for k in ['capital', 'asset', 'investimentos', 'bank', 'banco', 'robeco', 'fidelity', 'goldman', 'spx', 'kinea', 'itau', 'santander', 'btg', 'bradesco', 'vontobel', 'quoniam', 'kapitalo', 'mag', 'somma', 'man ahl', 'blackrock', 'jpmorgan', 'ubs', 'barclays', 'citi', 'bnp', 'daycoval', 'legacy', 'occam', 'genoa', 'verde', 'perfin', 'kadima', 'clube do valor', 'tenax', 'artesanal', 'bloxs', 'solis', 'altside', 'oby', 'prinz', 'galapagos', 'adam', 'turim', 'bahia asset']):
        groups["2_product_factor_newsletter"].append(item)
        continue

    # Quant Practitioners Toolkit (Quants, Risk Analysts, Data Scientists, AI/ML Engineers)
    if any(k in n_all for k in ['quant', 'data scientist', 'cientista de dados', 'machine learning', 'mlops', 'ai engineer', 'data engineer', 'engenheiro de software', 'software engineer', 'data analyst', 'analista de dados', 'analista quantitativo', 'quantitative researcher', 'quant researcher', 'quantitative analyst', 'quant analyst', 'risk analyst', 'analista de risco', 'modelagem', 'pricing', 'trading strategist', 'algorithmic trader', 'systematic trader', 'econometrista', 'macro research', 'equity research']):
        groups["2_product_econometrics_toolkit"].append(item)
        continue

    # Other Finance Corporate
    if any(k in n_comp for k in ['banco', 'bank', 'investimentos', 'asset', 'capital', 'corretora', 'seguros', 'previdencia', 'b3', 'anbima', 'cvm', 'bacen', 'banco central']):
        groups["4_ecosystem_finance_corporate"].append(item)
        continue

    # Remaining
    groups["5_others"].append(item)

print("\n================== CONTAGEM COMPLETA ==================")
for k, v in groups.items():
    print(f"{k}: {len(v)}")

with open('classified_connections.json', 'w', encoding='utf-8') as f:
    json.dump(groups, f, indent=2, ensure_ascii=False)

print("\nArquivo classified_connections.json gerado com sucesso!")
