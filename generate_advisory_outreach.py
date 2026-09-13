"""
Script Principal de Geração de Fila de Abordagem para Assessoria de Investimentos
Execução:
    python generate_advisory_outreach.py
"""

import sys
from pathlib import Path
from outreach.generator import build_outreach_database, export_csv, export_dashboard_html

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("=" * 65)
    print("🚀 INICIANDO GERADOR DE MENSAGENS PARA ASSESSORIA DE INVESTIMENTOS")
    print("=" * 65)

    base_dir = Path(__file__).resolve().parent
    csv_out = base_dir / "outreach_advisory_queue.csv"
    html_out = base_dir / "outreach_dashboard.html"

    queue = build_outreach_database()

    print(f"\n✅ Total de leads qualificados processados: {len(queue)}")
    
    # Contagem por nicho
    counts = {}
    for item in queue:
        lbl = item["segment_label"]
        counts[lbl] = counts.get(lbl, 0) + 1

    print("\n📊 Distribuição por Cluster:")
    for lbl, cnt in counts.items():
        print(f"  • {lbl.ljust(35)}: {cnt} leads")

    # Exportar CSV
    export_csv(queue, csv_out)
    print(f"\n📁 Fila salva em formato CSV (pronto para Excel/Waalaxy/Expandi):")
    print(f"   -> {csv_out.name}")

    # Exportar Dashboard HTML
    export_dashboard_html(queue, html_out)
    print(f"\n🌐 Dashboard Interativo com Copiar em 1 Clique gerado:")
    print(f"   -> {html_out.name}")

    print("\n" + "=" * 65)
    print("💡 COMO UTILIZAR NO DIA A DIA:")
    print(" 1. Dobre o clique no arquivo 'outreach_dashboard.html' no seu navegador.")
    print(" 2. Escolha o cluster desejado (ex: Agro, Founders ou C-Level).")
    print(" 3. Clique em 'Copiar', depois em 'Abrir LinkedIn' e cole no chat.")
    print(" 4. Meta recomendada: 15 a 20 mensagens por dia (leva ~10 minutos).")
    print("=" * 65)

if __name__ == "__main__":
    main()
