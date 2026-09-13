"""
Sincronizador Oficial da URL da Landing Page nos Posts do Buffer
Atualiza os posts do Lote 04 (Factor Investing & Investimento Sistemático na B3)
para direcionarem para a Landing Page onde o usuário baixa o Kit Gratuito (Ementa + Guia + Teste)
e garante 20% de desconto VIP.

Uso:
    python publisher/sync_lp_url.py [OPCIONAL_NOVA_URL]
Exemplo:
    python publisher/sync_lp_url.py https://meu-site.netlify.app
"""
import sys
import os
import re
import json
import requests
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))
from config import BUFFER_CONFIG, PRODUCT_LINKS

# Pega URL do argumento de linha de comando ou do .env / config.py
lp_url = sys.argv[1] if len(sys.argv) > 1 else PRODUCT_LINKS.get("quant_course_lp", "https://analise-quantitativa.netlify.app")
token = BUFFER_CONFIG.get("access_token")
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
graphql_url = "https://api.buffer.com/graphql"

# Metadados dos 5 posts do Lote 04
POSTS_TO_UPDATE = [
    {
        "id": "6aa5c31deba7bc5677856c91",
        "num": 1,
        "title": "Post 1 - Stock Picking vs Factor Investing na B3",
        "dueAt": "2026-09-19T15:00:00.000Z",
        "mode": "customScheduled"
    },
    {
        "id": "6aa5c31ef7b1958d5cd67540",
        "num": 2,
        "title": "Post 2 - Momentum na B3: Cross-Sectional vs Time-Series",
        "dueAt": "2026-09-20T15:00:00.000Z",
        "mode": "customScheduled"
    },
    {
        "id": "6aa5c31f66679b076f181809",
        "num": 3,
        "title": "Post 3 - O Factor Zoo e a Mineração de Dados na B3",
        "dueAt": "2026-09-21T15:00:00.000Z",
        "mode": "customScheduled"
    },
    {
        "id": "6aa5c32066679b076f181831",
        "num": 4,
        "title": "Post 4 - Backtesting Realista na B3: Triângulo das Bermudas",
        "dueAt": "2026-09-22T15:00:00.000Z",
        "mode": "customScheduled"
    },
    {
        "id": "6aa5c32d7da3ee968d04ec51",
        "num": 5,
        "title": "Post 5 - Além de Markowitz: Ledoit-Wolf e HRP na B3",
        "dueAt": "2026-09-23T15:00:00.000Z",
        "mode": "customScheduled"
    }
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

query_get = """
query GetPost($id: String!) {
  post(input: { id: $id }) {
    id
    text
    dueAt
    status
  }
}
"""

def update_cta_text(old_text: str, new_url: str) -> str:
    # Substitui qualquer link anterior (Gumroad ou antigo) pelo novo link da LP e a chamada com o Kit Gratuito
    pattern = r"(Para [^\n]+:\s*\n👉\s*)https?://[^\s]+"
    
    new_call = (
        "Para se inscrever na lista VIP, baixar gratuitamente o Kit Institucional de Entrada "
        "(Ementa Oficial de 30h + Guia Técnico em Python + Teste Diagnóstico de Nivelamento) "
        "e garantir 20% OFF no lançamento:\n👉 " + new_url
    )
    
    if re.search(pattern, old_text):
        return re.sub(pattern, new_call, old_text)
    else:
        # Fallback caso não dê match exato no regex
        if "https://warrenjax.gumroad.com/l/fsrcmj" in old_text:
            return old_text.replace("https://warrenjax.gumroad.com/l/fsrcmj", new_url)
        return old_text + f"\n\n👉 {new_url}"

def main():
    print("=" * 65)
    print("🚀 SINCRONIZADOR DE LANDING PAGE NO BUFFER (LOTE 04)")
    print(f"🔗 Nova URL Alvo: {lp_url}")
    print("=" * 65 + "\n")

    for p in POSTS_TO_UPDATE:
        pid = p["id"]
        title = p["title"]
        print(f"-> Processando [{title}] (ID: {pid})...")
        
        # 1. Busca texto atual no Buffer via query direta
        q_get = f"""
        query {{
          post(input: {{ id: "{pid}" }}) {{
            id
            text
            dueAt
            status
          }}
        }}
        """
        r_get = requests.post(graphql_url, json={"query": q_get}, headers=headers, timeout=20)
        post_data = r_get.json().get("data", {}).get("post")
        
        if not post_data:
            print(f"   [!] Erro ao buscar post {pid}: {r_get.text}")
            continue
            
        current_text = post_data.get("text", "")
        updated_text = update_cta_text(current_text, lp_url)
        
        # 2. Executa a mutação de edição no Buffer
        edit_payload = {
            "input": {
                "id": pid,
                "text": updated_text,
                "dueAt": p["dueAt"],
                "mode": p["mode"]
            }
        }
        
        r_edit = requests.post(graphql_url, json={"query": mutation_edit, "variables": edit_payload}, headers=headers, timeout=20)
        res_edit = r_edit.json()
        saved_post = res_edit.get("data", {}).get("editPost", {}).get("post")
        
        if saved_post:
            print(f"   ✅ Atualizado com sucesso! Status: {saved_post.get('status')} | Data: {saved_post.get('dueAt')}")
            # Mostra prévia da CTA atualizada
            last_lines = [l for l in saved_post.get("text", "").splitlines() if l.strip()][-4:]
            print("      CTA atualizada:")
            for ll in last_lines:
                print(f"        {ll}")
        else:
            print(f"   ❌ Erro ao editar post: {res_edit}")

    # Atualiza o arquivo local batch_04_factor_investing_brasil.md
    batch_file = ROOT_DIR / "posts" / "batch_04_factor_investing_brasil.md"
    if batch_file.exists():
        content = batch_file.read_text(encoding="utf-8")
        updated_content = re.sub(
            r"👉 https://warrenjax\.gumroad\.com/l/fsrcmj",
            f"👉 {lp_url}",
            content
        )
        updated_content = re.sub(
            r"Para aprofundar os fundamentos da modelagem sistemática, ter acesso aos motores em Python e se preparar para o nosso próximo curso de Análise Quantitativa Aplicada:",
            "Para se inscrever na lista VIP, baixar gratuitamente o Kit Institucional de Entrada (Ementa Oficial de 30h + Guia Técnico em Python + Teste Diagnóstico de Nivelamento) e garantir 20% OFF no lançamento:",
            updated_content
        )
        batch_file.write_text(updated_content, encoding="utf-8")
        print(f"\n✅ Arquivo local posts/batch_04_factor_investing_brasil.md atualizado com a nova URL!")

    print("\n🎉 Todos os posts foram sincronizados com sucesso!")

if __name__ == "__main__":
    main()
