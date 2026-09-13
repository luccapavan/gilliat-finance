"""
Atualização dos Posts de Conversão no Buffer para o Novo Toolkit & Playbook
Posts a atualizar:
- Post 02 (10/09/2026 às 12:00 BRT): ID 6aa09559493bbf8c2823d0b0
- Post 04 (12/09/2026 às 12:00 BRT): ID 6aa0955f3bd0dd9ef31e2bb6
- Post 10 (18/09/2026 às 12:00 BRT): ID 6aa095713bd0dd9ef31e2c88
"""
import sys
import re
import json
import requests
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from config import BUFFER_CONFIG

token = BUFFER_CONFIG.get("access_token")
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
graphql_url = "https://api.buffer.com/graphql"

posts_to_update = [
    (2, "6aa09559493bbf8c2823d0b0", "2026-09-10T15:00:00.000Z"),
    (5, "6aa095635bcf98109f5d7f74", "2026-09-13T15:00:00.000Z"),
    (7, "6aa09569493bbf8c2823d145", "2026-09-15T15:00:00.000Z"),
    (8, "6aa0956c3bd0dd9ef31e2c60", "2026-09-16T15:00:00.000Z"),
]

mutation_edit = """
mutation EditPost($input: EditPostInput!) {
  editPost(input: $input) {
    ... on PostActionSuccess {
      post {
        id
        status
        dueAt
        text
      }
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

def extract_pt_text(post_num: int) -> str:
    path = ROOT_DIR / "posts" / "batch_03" / f"post_{post_num:02d}.md"
    raw = path.read_text(encoding="utf-8")
    m = re.search(r"## 🇧🇷 Versão em Português:\s*\n\n(.*?)(?=\n---\s*\n## 🇺🇸|\Z)", raw, re.DOTALL)
    if not m:
        raise ValueError(f"Não encontrou texto PT no post {post_num}")
    return m.group(1).strip()

print("=========================================================")
print("ATUALIZANDO POSTS NO BUFFER PARA O NOVO TOOLKIT & PLAYBOOK")
print("=========================================================\n")

for num, post_id, due_at in posts_to_update:
    pt_text = extract_pt_text(num)
    print(f"-> Atualizando Post [{num:02d}] (ID: {post_id})...")
    payload = {
        "input": {
            "id": post_id,
            "text": pt_text,
            "dueAt": due_at,
            "mode": "customScheduled"
        }
    }
    r = requests.post(graphql_url, json={"query": mutation_edit, "variables": payload}, headers=headers, timeout=20)
    data = r.json()
    post_res = data.get("data", {}).get("editPost", {}).get("post")
    if post_res:
        print(f"   [OK] Post {num:02d} atualizado com sucesso! DueAt: {post_res.get('dueAt')}")
        print(f"        Prévia: {post_res.get('text')[:80]}...")
    else:
        print(f"   [!] Erro na resposta: {data}")

print("\nConcluído com sucesso!")
