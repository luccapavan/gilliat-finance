"""
Gerador de Mensagens e Fila de Abordagem para Assessoria de Investimentos
Processa os leads qualificados do final_report_data.json e gera o CSV e o Dashboard HTML.
"""

import json
import csv
import re
import unicodedata
from pathlib import Path
from outreach.templates import TEMPLATES, clean_company_name

def clean_first_name(raw_name):
    """
    Higieniza o nome para saudações naturais (ex: 'Olá Carlos', 'Olá Sofia')
    Remove títulos honoríficos, apelidos, certificações e emojis.
    """
    if not raw_name:
        return "Amigo(a)"

    name = raw_name.strip()
    
    # Remove aspas e parênteses
    name = re.sub(r'[\"\'\(\)\[\]]', ' ', name)
    
    # Remove certificações e sufixos pós-vírgula/hífen
    for sep in [',', ' - ', ' – ', ' | ']:
        if sep in name:
            name = name.split(sep)[0].strip()

    # Remove títulos iniciais comuns
    prefixes = ['dr.', 'dra.', 'prof.', 'profa.', 'professora', 'professor', 'eng.', 'ca ', 'sr.', 'sra.']
    for p in prefixes:
        if name.lower().startswith(p):
            name = name[len(p):].strip()

    # Remove caracteres especiais e emojis iniciais
    name = re.sub(r'^[^\w]+', '', name)

    parts = name.split()
    if not parts:
        return "Amigo(a)"

    first = parts[0].capitalize()
    
    # Se primeiro nome for inicial única tipo 'M.' ou 'J.', pega o segundo se existir
    if len(first) <= 2 and len(parts) > 1:
        first = parts[1].capitalize()

    # Se for nome composto comum no Brasil (João Pedro, Ana Paula, etc.)
    if len(parts) > 1 and first.lower() in ['joao', 'joão', 'ana', 'maria', 'pedro', 'luiz', 'luis']:
        second = parts[1].capitalize()
        # Não junta se o segundo for preposição
        if second.lower() not in ['de', 'da', 'do', 'dos', 'das', 'e']:
            return f"{first} {second}"

    return first

def build_outreach_database():
    base_dir = Path(__file__).resolve().parent.parent
    data_file = base_dir / "final_report_data.json"
    
    if not data_file.exists():
        raise FileNotFoundError(f"Arquivo {data_file} não encontrado. Execute generate_final_report_data.py primeiro.")

    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    category_mapping = {
        "assessoria_agro_commodities": "agro",
        "assessoria_empresarios_founders": "founders",
        "assessoria_executivos_clevel": "clevel",
        "assessoria_medicos_advogados": "doctors_lawyers",
        "assessoria_investidores_hnw": "investors_hnw"
    }

    queue = []
    item_id = 1

    for cat_key, template_key in category_mapping.items():
        leads = data.get(cat_key, [])
        tmpl_data = TEMPLATES[template_key]
        tag = tmpl_data["tag"]
        msg_variants = tmpl_data["messages"]

        for idx, lead in enumerate(leads):
            full_name = lead["name"]
            first_name = clean_first_name(full_name)
            company_raw = lead["comp"]
            company_clean = clean_company_name(company_raw)
            pos = lead["pos"]
            url = lead["url"]
            email = lead.get("email", "")

            # Alterna as variantes de copy para garantir diversidade no envio
            var_idx = idx % len(msg_variants)
            msg_tuple = msg_variants[var_idx]

            msg1 = msg_tuple[0].format(
                first_name=first_name,
                company_clean=company_clean if company_clean else "sua empresa",
                position=pos
            )
            msg2 = msg_tuple[1].format(
                first_name=first_name,
                company_clean=company_clean if company_clean else "sua empresa"
            )

            queue.append({
                "id": item_id,
                "name": full_name,
                "first_name": first_name,
                "company": company_raw,
                "company_clean": company_clean,
                "position": pos,
                "url": url,
                "email": email,
                "segment_key": template_key,
                "segment_label": tag,
                "message_1": msg1,
                "message_2_followup": msg2,
                "status": "Pendente"
            })
            item_id += 1

    return queue

def export_csv(queue, output_path):
    headers = [
        "ID", "Nome Completo", "Primeiro Nome", "Cargo", "Empresa",
        "Segmento", "URL LinkedIn", "Email", "Mensagem 1 (Gancho)",
        "Mensagem 2 (Follow-up)", "Status"
    ]
    with open(output_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for q in queue:
            writer.writerow([
                q["id"], q["name"], q["first_name"], q["position"], q["company"],
                q["segment_label"], q["url"], q["email"], q["message_1"],
                q["message_2_followup"], q["status"]
            ])

def export_dashboard_html(queue, output_path):
    """
    Gera um dashboard moderno, responsivo e interativo para revisão e envio com 1 clique.
    """
    queue_json = json.dumps(queue, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Outreach Wealth & Assessoria — Fila de Abordagem Inteligente</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        .custom-scrollbar::-webkit-scrollbar {{ width: 6px; }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{ background-color: #cbd5e1; border-radius: 4px; }}
    </style>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen font-sans antialiased">

    <!-- Top Navigation -->
    <header class="border-b border-slate-800 bg-slate-950/80 sticky top-0 z-30 backdrop-blur-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex flex-col sm:flex-row justify-between items-center gap-4">
            <div class="flex items-center space-x-3">
                <div class="h-10 w-10 rounded-xl bg-gradient-to-tr from-amber-500 to-indigo-600 flex items-center justify-center font-bold text-white shadow-lg shadow-indigo-500/20">
                    <i class="fa-solid fa-paper-plane"></i>
                </div>
                <div>
                    <h1 class="text-xl font-bold tracking-tight text-white">Outreach Wealth & Assessoria</h1>
                    <p class="text-xs text-slate-400">Persona: Lucca Simeoni Pavan, Ph.D. • JFK Investimentos / XP</p>
                </div>
            </div>
            <div class="flex items-center space-x-3 text-sm">
                <div class="bg-slate-800 px-4 py-1.5 rounded-lg border border-slate-700 flex items-center gap-2">
                    <span class="h-2 w-2 rounded-full bg-emerald-400 animate-pulse"></span>
                    <span class="text-slate-300 font-medium"><span id="total-count">{len(queue)}</span> Leads Qualificados</span>
                </div>
                <button onclick="exportTableToCSV()" class="bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-1.5 rounded-lg font-medium transition shadow-md flex items-center gap-2 text-xs">
                    <i class="fa-solid fa-download"></i> Baixar CSV
                </button>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">

        <!-- Metrics Cards -->
        <div class="grid grid-cols-2 md:grid-cols-5 gap-3">
            <button onclick="setFilter('all')" class="stat-card active bg-slate-800/80 border border-slate-700 p-3 rounded-xl text-left hover:border-indigo-500 transition group focus:outline-none">
                <div class="text-xs text-slate-400 font-medium">Todos os Leads</div>
                <div class="text-2xl font-bold text-white mt-1">{len(queue)}</div>
            </button>
            <button onclick="setFilter('agro')" class="stat-card bg-slate-800/80 border border-slate-700 p-3 rounded-xl text-left hover:border-amber-500 transition group focus:outline-none">
                <div class="text-xs text-amber-400 font-medium">🌾 Agro & Tradings</div>
                <div class="text-2xl font-bold text-white mt-1" id="count-agro">0</div>
            </button>
            <button onclick="setFilter('founders')" class="stat-card bg-slate-800/80 border border-slate-700 p-3 rounded-xl text-left hover:border-emerald-500 transition group focus:outline-none">
                <div class="text-xs text-emerald-400 font-medium">🚀 Founders & CEOs</div>
                <div class="text-2xl font-bold text-white mt-1" id="count-founders">0</div>
            </button>
            <button onclick="setFilter('clevel')" class="stat-card bg-slate-800/80 border border-slate-700 p-3 rounded-xl text-left hover:border-cyan-500 transition group focus:outline-none">
                <div class="text-xs text-cyan-400 font-medium">🏢 C-Level & Diretores</div>
                <div class="text-2xl font-bold text-white mt-1" id="count-clevel">0</div>
            </button>
            <button onclick="setFilter('doctors_lawyers')" class="stat-card bg-slate-800/80 border border-slate-700 p-3 rounded-xl text-left hover:border-purple-500 transition group focus:outline-none">
                <div class="text-xs text-purple-400 font-medium">⚖️ Médicos & Advogados</div>
                <div class="text-2xl font-bold text-white mt-1" id="count-doctors">0</div>
            </button>
        </div>

        <!-- Search & Control Bar -->
        <div class="flex flex-col sm:flex-row gap-4 justify-between items-center bg-slate-950 p-4 rounded-xl border border-slate-800">
            <div class="relative w-full sm:w-96">
                <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-3 text-slate-500 text-sm"></i>
                <input type="text" id="search-input" onkeyup="handleSearch()" placeholder="Buscar por nome, empresa ou cargo..." class="w-full bg-slate-900 border border-slate-800 rounded-lg pl-10 pr-4 py-2 text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition">
            </div>
            <div class="text-xs text-slate-400 flex items-center gap-2">
                <i class="fa-solid fa-lightbulb text-amber-400"></i>
                <span>Recomendação: Envie entre <b>15 a 25 mensagens personalizadas/dia</b> para máxima conversão.</span>
            </div>
        </div>

        <!-- Leads List -->
        <div id="leads-container" class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Cards rendered by JS -->
        </div>

    </main>

    <!-- Toast Notification -->
    <div id="toast" class="fixed bottom-5 right-5 bg-emerald-600 text-white px-5 py-2.5 rounded-xl shadow-2xl font-medium text-sm flex items-center gap-2 transform translate-y-20 opacity-0 transition duration-300 z-50">
        <i class="fa-solid fa-check-circle"></i>
        <span id="toast-msg">Mensagem copiada para a área de transferência!</span>
    </div>

    <script>
        const leadsData = {queue_json};
        let currentFilter = 'all';
        let searchQuery = '';

        // Calculate counts
        document.getElementById('count-agro').innerText = leadsData.filter(l => l.segment_key === 'agro').length;
        document.getElementById('count-founders').innerText = leadsData.filter(l => l.segment_key === 'founders').length;
        document.getElementById('count-clevel').innerText = leadsData.filter(l => l.segment_key === 'clevel').length;
        document.getElementById('count-doctors').innerText = leadsData.filter(l => l.segment_key === 'doctors_lawyers').length;

        function setFilter(filter) {{
            currentFilter = filter;
            renderLeads();
        }}

        function handleSearch() {{
            searchQuery = document.getElementById('search-input').value.toLowerCase();
            renderLeads();
        }}

        function showToast(msg) {{
            const toast = document.getElementById('toast');
            document.getElementById('toast-msg').innerText = msg;
            toast.classList.remove('translate-y-20', 'opacity-0');
            setTimeout(() => {{
                toast.classList.add('translate-y-20', 'opacity-0');
            }}, 2500);
        }}

        function copyToClipboard(elementId, btn) {{
            const text = document.getElementById(elementId).innerText;
            navigator.clipboard.writeText(text).then(() => {{
                const originalHTML = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check"></i> Copiado!';
                btn.classList.remove('bg-indigo-600', 'hover:bg-indigo-500');
                btn.classList.add('bg-emerald-600');
                showToast("Mensagem copiada! Abra o LinkedIn e cole no inbox.");
                setTimeout(() => {{
                    btn.innerHTML = originalHTML;
                    btn.classList.remove('bg-emerald-600');
                    btn.classList.add('bg-indigo-600', 'hover:bg-indigo-500');
                }}, 2000);
            }});
        }}

        function renderLeads() {{
            const container = document.getElementById('leads-container');
            container.innerHTML = '';

            const filtered = leadsData.filter(lead => {{
                const matchesFilter = currentFilter === 'all' || lead.segment_key === currentFilter;
                const matchesSearch = !searchQuery || 
                    lead.name.toLowerCase().includes(searchQuery) ||
                    lead.company.toLowerCase().includes(searchQuery) ||
                    lead.position.toLowerCase().includes(searchQuery);
                return matchesFilter && matchesSearch;
            }});

            if (filtered.length === 0) {{
                container.innerHTML = `
                    <div class="col-span-2 text-center py-16 bg-slate-950 rounded-2xl border border-slate-800">
                        <i class="fa-regular fa-folder-open text-4xl text-slate-600 mb-3"></i>
                        <p class="text-slate-400">Nenhum lead encontrado com os filtros aplicados.</p>
                    </div>
                `;
                return;
            }}

            filtered.forEach(lead => {{
                const card = document.createElement('div');
                card.className = 'bg-slate-950 border border-slate-800 rounded-2xl p-5 hover:border-slate-700 transition flex flex-col justify-between shadow-sm';
                
                let badgeClass = "bg-slate-800 text-slate-300";
                if(lead.segment_key === 'agro') badgeClass = "bg-amber-950/60 text-amber-300 border border-amber-800/60";
                else if(lead.segment_key === 'founders') badgeClass = "bg-emerald-950/60 text-emerald-300 border border-emerald-800/60";
                else if(lead.segment_key === 'clevel') badgeClass = "bg-cyan-950/60 text-cyan-300 border border-cyan-800/60";
                else if(lead.segment_key === 'doctors_lawyers') badgeClass = "bg-purple-950/60 text-purple-300 border border-purple-800/60";

                card.innerHTML = `
                    <div>
                        <!-- Header -->
                        <div class="flex justify-between items-start gap-2 mb-3">
                            <div>
                                <span class="text-[10px] font-semibold uppercase px-2.5 py-1 rounded-full ${{badgeClass}}">${{lead.segment_label}}</span>
                                <h2 class="text-base font-bold text-white mt-2 leading-tight">${{lead.name}}</h2>
                                <p class="text-xs text-slate-400">${{lead.position}} <span class="text-slate-600">•</span> <span class="text-slate-300 font-medium">${{lead.company}}</span></p>
                            </div>
                            <a href="${{lead.url}}" target="_blank" class="text-slate-400 hover:text-indigo-400 text-sm p-2 rounded-lg hover:bg-slate-900 transition flex items-center gap-1.5" title="Abrir perfil no LinkedIn">
                                <i class="fa-brands fa-linkedin text-lg text-sky-400"></i>
                                <span class="text-xs font-medium">Ver</span>
                            </a>
                        </div>

                        <!-- Message 1 Tab -->
                        <div class="mt-3 bg-slate-900/90 rounded-xl p-3.5 border border-slate-800 text-xs text-slate-300 leading-relaxed custom-scrollbar max-h-48 overflow-y-auto whitespace-pre-line font-mono" id="msg1-${{lead.id}}">${{lead.message_1}}</div>
                    </div>

                    <!-- Footer Actions -->
                    <div class="mt-4 pt-3 border-t border-slate-900 flex items-center justify-between gap-2">
                        <button onclick="toggleFollowup(${{lead.id}})" class="text-slate-400 hover:text-slate-200 text-xs flex items-center gap-1">
                            <i class="fa-solid fa-clock-rotate-left"></i> <span id="toggle-lbl-${{lead.id}}">Ver Follow-up</span>
                        </button>
                        <div class="flex items-center gap-2">
                            <a href="${{lead.url}}" target="_blank" class="bg-slate-800 hover:bg-slate-700 text-slate-200 px-3 py-1.5 rounded-lg text-xs font-medium transition flex items-center gap-1.5">
                                <i class="fa-solid fa-arrow-up-right-from-square"></i> Abrir LinkedIn
                            </a>
                            <button onclick="copyToClipboard('msg1-${{lead.id}}', this)" class="bg-indigo-600 hover:bg-indigo-500 text-white px-3 py-1.5 rounded-lg text-xs font-medium transition flex items-center gap-1.5 shadow-sm">
                                <i class="fa-regular fa-copy"></i> Copiar
                            </button>
                        </div>
                    </div>

                    <!-- Hidden Followup Box -->
                    <div id="followup-box-${{lead.id}}" class="hidden mt-3 pt-3 border-t border-slate-800">
                        <div class="text-[11px] text-amber-400 font-semibold mb-1 flex items-center justify-between">
                            <span>Mensagem 2 (Follow-up após 4-5 dias):</span>
                            <button onclick="copyToClipboard('msg2-${{lead.id}}', this)" class="text-slate-400 hover:text-white text-[10px] underline">Copiar Follow-up</button>
                        </div>
                        <div class="bg-slate-900/80 rounded-xl p-3 border border-slate-800 text-xs text-slate-300 whitespace-pre-line font-mono" id="msg2-${{lead.id}}">${{lead.message_2_followup}}</div>
                    </div>
                `;
                container.appendChild(card);
            }});
        }}

        function toggleFollowup(id) {{
            const box = document.getElementById(`followup-box-${{id}}`);
            const lbl = document.getElementById(`toggle-lbl-${{id}}`);
            if (box.classList.contains('hidden')) {{
                box.classList.remove('hidden');
                lbl.innerText = 'Ocultar Follow-up';
            }} else {{
                box.classList.add('hidden');
                lbl.innerText = 'Ver Follow-up';
            }}
        }}

        function exportTableToCSV() {{
            window.location.href = "outreach_advisory_queue.csv";
        }}

        // Initial render
        renderLeads();
    </script>
</body>
</html>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
