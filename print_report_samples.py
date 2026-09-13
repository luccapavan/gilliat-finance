import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('final_report_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

target_cats = [
    'influencia_titans', 'influencia_headhunters', 'influencia_media_podcasts',
    'influencia_academicos', 'compradores_playbook_transicao',
    'compradores_toolkit_econometria', 'assinantes_factor_newsletter',
    'assessoria_agro_commodities'
]

for cat in target_cats:
    items = data.get(cat, [])
    print(f"\n### {cat} (Total: {len(items)})")
    for it in items[:10]:
        email = f" - Email: {it['email']}" if it['email'] else ""
        print(f"* **{it['name']}**: {it['pos']} na *{it['comp']}*{email}")

