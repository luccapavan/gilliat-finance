"""
Ajuste de Horários dos Posts no Buffer para 12:00 e 18:30 (Horário de Brasília)
Passa o texto obrigatório junto com dueAt.
"""
import os
import sys
import json
import requests
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import BUFFER_CONFIG

load_dotenv()
token = BUFFER_CONFIG.get("access_token")
graphql_url = "https://api.buffer.com/graphql"
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

# Carrega os textos oficiais dos posts
with open("posts/batch_01/index.json", "r", encoding="utf-8") as f:
    batch_posts = {p["id"]: p["content"] for p in json.load(f)}

# Mapeamento dos posts ativos para os novos horários
# 12:00 BRT = 15:00 UTC
# 18:30 BRT = 21:30 UTC
schedule_plan = [
    # 1. Hoje domingo (06/09) às 18:30 BRT (Volatilidade / GARCH)
    ("6a9cc6e5fba008bcd5560b5d", "post_04_tecnico_garch_volatilidade", "2026-09-06T21:30:00.000Z", "Hoje (Domingo 06/09) às 18:30 BRT"),
    
    # 2. Segunda-feira (07/09) às 12:00 BRT (Por que LSTM falha)
    ("6a9cc6e785ccb3a22c0e7cc1", "post_02_carreira_lstm_vs_quants", "2026-09-07T15:00:00.000Z", "Segunda-feira (07/09) às 12:00 BRT"),
    
    # 3. Segunda-feira (07/09) às 18:30 BRT (Factor Zoo)
    ("6a9cc6e935b71c36e4739310", "post_05_tecnico_factor_zoo", "2026-09-07T21:30:00.000Z", "Segunda-feira (07/09) às 18:30 BRT"),
    
    # 4. Terça-feira (08/09) às 12:00 BRT (Conversão / Playbook Gumroad)
    ("6a9ccfc3534afc9129e98f84", "post_03_conversao_playbook", "2026-09-08T15:00:00.000Z", "Terça-feira (08/09) às 12:00 BRT"),
]

mutation_edit = """
mutation EditPost($input: EditPostInput!) {
  editPost(input: $input) {
    ... on PostActionSuccess {
      post {
        id
        status
        dueAt
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

print("\n--- Atualizando Horários dos Posts Ativos no Buffer ---")
for post_id, post_key, due_at_utc, label_brt in schedule_plan:
    text_content = batch_posts.get(post_key)
    payload = {
        "input": {
            "id": post_id,
            "text": text_content,
            "dueAt": due_at_utc,
            "mode": "customScheduled"
        }
    }
    try:
        r = requests.post(graphql_url, headers=headers, json={"query": mutation_edit, "variables": payload}, timeout=15)
        res_json = r.json()
        post_data = res_json.get("data", {}).get("editPost", {}).get("post", {})
        if post_data:
            print(f"[OK] Post {post_id} ajustado com sucesso para: {label_brt}")
            print(f"     Status: {post_data.get('status')} | UTC: {post_data.get('dueAt')}")
        else:
            print(f"[!] Erro ao atualizar post {post_id}: {res_json}")
    except Exception as e:
        print(f"[!] Falha na requisição para {post_id}: {e}")

print("\nTodos os horários foram atualizados para 12:00 e 18:30 de Brasília!")
