"""
Consulta Completa de Métricas e Performance dos Posts Publicados no Buffer
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
channel_id = BUFFER_CONFIG.get("profile_id")
graphql_url = "https://api.buffer.com/graphql"
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

query_posts = """
query {
  posts(input: { organizationId: "6a9cc3eb79abd3cf24e8d5d5", filter: { channelIds: ["%s"], status: [sent] } }) {
    edges {
      node {
        id
        status
        sentAt
        dueAt
        text
        externalLink
        metrics {
          name
          value
        }
      }
    }
  }
}
""" % channel_id

r = requests.post(graphql_url, headers=headers, json={"query": query_posts}, timeout=15)
posts = r.json().get("data", {}).get("posts", {}).get("edges", [])

output_data = []
for p in posts:
    node = p.get("node", {})
    output_data.append({
        "id": node.get("id"),
        "status": node.get("status"),
        "sentAt": node.get("sentAt"),
        "dueAt": node.get("dueAt"),
        "title_preview": node.get("text", "").split("\n")[0][:60],
        "metrics": node.get("metrics", []),
        "externalLink": node.get("externalLink")
    })

# Salva em json para leitura limpa
with open("publisher/metrics_report.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Relatório de métricas gerado com {len(output_data)} posts.")
