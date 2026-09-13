"""
Agendamento dos 2 Posts Virais em Inglês no Buffer
Horário Estratégico Internacional: 13:00 UTC
- 09:00 AM New York (EDT - Abertura de Wall Street)
- 14:00 London (BST - Pico pós-almoço The City)
- 15:00 Frankfurt/Zurich (CEST)
- 10:00 BRT
"""
import sys
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from publisher.buffer_publisher import schedule_via_buffer

p1_path = ROOT_DIR / "posts" / "viral_en_01_lstm_github.md"
p2_path = ROOT_DIR / "posts" / "viral_en_02_phd_transition.md"

def extract_body(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    # Pega o conteúdo após o segundo '---'
    parts = raw.split("---", 2)
    if len(parts) >= 3:
        return parts[2].strip()
    return raw.strip()

text_p1 = extract_body(p1_path)
text_p2 = extract_body(p2_path)

# Datas estratégicas às 13:00 UTC (09:00 AM NY / 14:00 London)
# Post 1 (LSTM): Sábado 19/09/2026 às 13:00 UTC
# Post 2 (PhD): Segunda-feira 21/09/2026 às 13:00 UTC (Segunda é o dia de maior engajamento profissional)
date_p1 = "2026-09-19T13:00:00.000Z"
date_p2 = "2026-09-21T13:00:00.000Z"

print("=========================================================")
print("AGENDANDO POSTS VIRAIS EM INGLÊS NO BUFFER")
print("Horário: 13:00 UTC (09:00 AM New York / 14:00 London)")
print("=========================================================\n")

print("-> Agendando Post 01 (LSTM no GitHub)...")
res1 = schedule_via_buffer(text=text_p1, due_at=date_p1)
if res1.get("success"):
    print(f"   [OK] Post 01 agendado com sucesso! ID: {res1.get('post_id')} para {date_p1}")
else:
    print(f"   [!] Erro no Post 01: {res1}")

print("\n-> Agendando Post 02 (Transição do Doutorado)...")
res2 = schedule_via_buffer(text=text_p2, due_at=date_p2)
if res2.get("success"):
    print(f"   [OK] Post 02 agendado com sucesso! ID: {res2.get('post_id')} para {date_p2}")
else:
    print(f"   [!] Erro no Post 02: {res2}")

print("\nConcluído!")
