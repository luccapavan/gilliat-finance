import os, sys, requests, json
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = Path(r"c:\Users\CLIENTE\linkedin_money")
sys.path.append(str(ROOT_DIR))
from config import BUFFER_CONFIG

token = BUFFER_CONFIG.get("access_token")
channel_id = "6a9cc410cd8b9c702c14b842"
org_id = "6a9cc3eb79abd3cf24e8d5d5"
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

query = f"""
query {{
  posts(input: {{ organizationId: "{org_id}", filter: {{ channelIds: ["{channel_id}"] }} }}) {{
    total
    edges {{
      node {{
        id
        status
        dueAt
        text
      }}
    }}
  }}
}}
"""

r = requests.post(
    "https://api.buffer.com/graphql",
    headers=headers,
    json={"query": query},
    timeout=20
)

data = r.json()
edges = data.get("data", {}).get("posts", {}).get("edges", [])
print(f"Total posts no canal: {len(edges)}")
for e in sorted(edges, key=lambda x: str(x['node'].get('dueAt'))):
    n = e["node"]
    text_preview = n.get("text", "")[:60].replace("\n", " ")
    print(f"DueAt: {n.get('dueAt')} | Status: {n.get('status')} | ID: {n.get('id')} | Text: {text_preview}...")
