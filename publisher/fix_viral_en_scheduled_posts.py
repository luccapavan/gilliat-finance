"""
Correção do texto completo dos 2 Posts Virais em Inglês no Buffer
Post 1 (LSTM): ID 6aa3524b71ba1c02ccef1e6f (2026-09-19T13:00:00.000Z)
Post 2 (PhD):  ID 6aa3524d71ba1c02ccef1ea5 (2026-09-21T13:00:00.000Z)
"""
import sys
from pathlib import Path
import requests

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))
from config import BUFFER_CONFIG

token = BUFFER_CONFIG.get("access_token")
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
graphql_url = "https://api.buffer.com/graphql"

p1_path = ROOT_DIR / "posts" / "viral_en_01_lstm_github.md"
p2_path = ROOT_DIR / "posts" / "viral_en_02_phd_transition.md"

def extract_full_post(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    # Pega tudo após o primeiro '---'
    idx = raw.find("---")
    if idx != -1:
        return raw[idx + 3:].strip()
    return raw.strip()

text_p1 = extract_full_post(p1_path)
text_p2 = extract_full_post(p2_path)

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

updates = [
    ("6aa3524b71ba1c02ccef1e6f", text_p1, "2026-09-19T13:00:00.000Z", "Post 01 (LSTM)"),
    ("6aa3524d71ba1c02ccef1ea5", text_p2, "2026-09-21T13:00:00.000Z", "Post 02 (PhD Transition)")
]

for post_id, text, due_at, label in updates:
    print(f"-> Atualizando {label} (ID: {post_id})...")
    print(f"   Primeiras linhas: {text[:100]}...")
    payload = {
        "input": {
            "id": post_id,
            "text": text,
            "dueAt": due_at,
            "mode": "customScheduled"
        }
    }
    r = requests.post(graphql_url, json={"query": mutation_edit, "variables": payload}, headers=headers, timeout=20)
    data = r.json()
    post_res = data.get("data", {}).get("editPost", {}).get("post")
    if post_res:
        print(f"   [OK] {label} atualizado com sucesso! Tamanho: {len(post_res['text'])} caracteres")
    else:
        print(f"   [!] Erro: {data}")
    print()

print("Concluído!")
