"""
Sincronização dos Posts Agendados no Buffer com o Link do Gumroad:
https://warrenjax.gumroad.com/l/fsrcmj
Substitui qualquer menção a Eduzz e garante que todos os posts agendados
tenham chamada institucional com link direto para o Gumroad.
"""
import re
import sys
from pathlib import Path
import requests

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))
from config import BUFFER_CONFIG

token = BUFFER_CONFIG.get("access_token")
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
graphql_url = "https://api.buffer.com/graphql"

# Mapeamento dos 8 posts agendados: (número_do_post, post_id, due_at)
posts_schedule = [
    (3, "6aa0955c3bd0dd9ef31e2b70", "2026-09-11T15:00:00.000Z"),
    (4, "6aa0955f3bd0dd9ef31e2bb6", "2026-09-12T15:00:00.000Z"),
    (5, "6aa095635bcf98109f5d7f74", "2026-09-13T15:00:00.000Z"),
    (6, "6aa095663c5ae934d51d6906", "2026-09-14T15:00:00.000Z"),
    (7, "6aa09569493bbf8c2823d145", "2026-09-15T15:00:00.000Z"),
    (8, "6aa0956c3bd0dd9ef31e2c60", "2026-09-16T15:00:00.000Z"),
    (9, "6aa0956f5bcf98109f5d8004", "2026-09-17T15:00:00.000Z"),
    (10, "6aa095713bd0dd9ef31e2c88", "2026-09-18T15:00:00.000Z"),
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

def sync_all():
    print("=========================================================")
    print("ATUALIZANDO POSTS NO BUFFER COM O LINK DO GUMROAD")
    print("Link: https://warrenjax.gumroad.com/l/fsrcmj")
    print("=========================================================\n")
    
    success_count = 0
    for num, post_id, due_at in posts_schedule:
        pt_text = extract_pt_text(num)
        has_gumroad = "https://warrenjax.gumroad.com/l/fsrcmj" in pt_text
        print(f"-> Sincronizando Post [{num:02d}] (ID: {post_id} | Data: {due_at[:10]})...")
        print(f"   Contém link do Gumroad: {has_gumroad}")
        
        payload = {
            "input": {
                "id": post_id,
                "text": pt_text,
                "dueAt": due_at,
                "mode": "customScheduled"
            }
        }
        
        r = requests.post(graphql_url, json={"query": mutation_edit, "variables": payload}, headers=headers, timeout=25)
        data = r.json()
        post_res = data.get("data", {}).get("editPost", {}).get("post")
        if post_res:
            success_count += 1
            print(f"   [OK] Post {num:02d} atualizado com sucesso! Status: {post_res.get('status')}")
            # Conferir últimas 3 linhas
            last_lines = [l for l in post_res.get('text', '').splitlines() if l.strip()][-3:]
            print(f"        Final: {' | '.join(last_lines)}")
        else:
            print(f"   [!] Erro na resposta: {data}")
            
    print(f"\n=========================================================")
    print(f"Sincronização concluída: {success_count}/{len(posts_schedule)} posts atualizados!")
    print("=========================================================")

if __name__ == "__main__":
    sync_all()
