"""
Agendamento Oficial do Lote 03 (Quant Investing) no Buffer
Cadência: 1 post por dia às 12:00 BRT (15:00 UTC) durante 10 dias
Data de Início: 09/09/2026 (Quarta-feira)
Data Final:     18/09/2026 (Sexta-feira)
"""
import sys
import os
import re
import json
import time
from datetime import datetime, timedelta
from pathlib import Path

# Configura UTF-8 no terminal Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from config import BUFFER_CONFIG
from publisher.buffer_publisher import schedule_via_buffer

FORBIDDEN_TERMS = ["Constância", "Constancia", "Maza", "JFK"]
REQUIRED_TITLE = "Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação"
EDUZZ_LINK = "https://chk.eduzz.com/7sfhtm2a"

def extract_portuguese_content(post_md_path: Path) -> str:
    raw = post_md_path.read_text(encoding="utf-8")
    m = re.search(r"## 🇧🇷 Versão em Português:\s*\n\n(.*?)(?=\n---\s*\n## 🇺🇸|\Z)", raw, re.DOTALL)
    if not m:
        raise ValueError(f"Não foi possível extrair a versão em português de {post_md_path}")
    return m.group(1).strip()

def build_schedule_dates(start_date: datetime, count: int = 10):
    """
    Gera timestamps UTC para 12:00 BRT (15:00:00.000Z) para 'count' dias consecutivos.
    """
    slots = []
    for day_offset in range(count):
        current_day = start_date + timedelta(days=day_offset)
        utc_str = f"{current_day.strftime('%Y-%m-%d')}T15:00:00.000Z"
        brt_label = f"{current_day.strftime('%d/%m/%Y')} às 12:00 BRT"
        slots.append((current_day, utc_str, brt_label))
    return slots

def main():
    print("=================================================================")
    print("🚀 INICIANDO AGENDAMENTO DO LOTE 03 NO BUFFER (LINKEDIN)")
    print("=================================================================\n")
    
    posts_dir = ROOT_DIR / "posts" / "batch_03"
    
    # 1. Carrega e valida os 10 posts
    posts_data = []
    print("[1/3] Validando conteúdo e compliance dos 10 posts...")
    for i in range(1, 11):
        file_path = posts_dir / f"post_{i:02d}.md"
        if not file_path.exists():
            print(f"❌ Arquivo não encontrado: {file_path}")
            return
            
        pt_text = extract_portuguese_content(file_path)
        
        # Compliance check
        for term in FORBIDDEN_TERMS:
            if term.lower() in pt_text.lower():
                raise ValueError(f"❌ Violação de compliance no Post {i}: termo proibido '{term}' detectado!")
                
        # Link check nos posts de conversão
        if i in [2, 4, 10] and EDUZZ_LINK not in pt_text:
            raise ValueError(f"❌ Post {i} deveria conter o link da Eduzz ({EDUZZ_LINK})!")
            
        posts_data.append({
            "idx": i,
            "file": str(file_path.name),
            "text": pt_text
        })
        print(f"  ✓ Post {i:02d} validado com sucesso ({len(pt_text)} caracteres).")
        
    print("\nTodos os 10 posts passaram nas validações de compliance e integridade!\n")
    
    # 2. Define o cronograma
    # Início: 09/09/2026 (amanhã) às 12:00 BRT
    start_date = datetime(2026, 9, 9)
    slots = build_schedule_dates(start_date, len(posts_data))
    
    print("[2/3] Cronograma de Publicação planejado:")
    for post, (_, utc_str, brt_label) in zip(posts_data, slots):
        print(f"  - Post {post['idx']:02d}: {brt_label} (UTC: {utc_str})")
        
    print("\n[3/3] Enviando para a API do Buffer...")
    scheduled_results = []
    
    for post, (curr_day, utc_str, brt_label) in zip(posts_data, slots):
        print(f"\n-> Agendando Post [{post['idx']:02d}] para {brt_label}...")
        res = schedule_via_buffer(
            text=post["text"],
            mode="customScheduled",
            save_to_draft=False,
            due_at=utc_str
        )
        
        if res.get("success"):
            post_id = res.get("post_id")
            status = res.get("status")
            print(f"   ✅ SUCESSO! Post ID: {post_id} | Status: {status}")
            scheduled_results.append({
                "post_idx": post["idx"],
                "file": post["file"],
                "buffer_post_id": post_id,
                "due_at_utc": utc_str,
                "scheduled_brt": brt_label,
                "status": status,
                "first_line": post["text"].splitlines()[0][:70]
            })
        else:
            print(f"   ❌ ERRO ao agendar Post {post['idx']:02d}: {res.get('error', res)}")
            scheduled_results.append({
                "post_idx": post["idx"],
                "file": post["file"],
                "error": res.get("error", res),
                "scheduled_brt": brt_label
            })
            
        time.sleep(1.5)  # Respeita rate limit da API
        
    # 3. Salva relatório do agendamento
    report_path = ROOT_DIR / "publisher" / "batch_03_schedule_report.json"
    report_path.write_text(json.dumps(scheduled_results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nRelatório de agendamento salvo em: {report_path}")
    
    success_count = sum(1 for r in scheduled_results if "buffer_post_id" in r)
    print("=================================================================")
    print(f"🎯 RESULTADO FINAL: {success_count}/{len(posts_data)} posts agendados com sucesso no Buffer!")
    print("=================================================================")

if __name__ == "__main__":
    main()
