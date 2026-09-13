import requests
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import BUFFER_CONFIG

token = BUFFER_CONFIG.get("access_token")
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

post_ids = [
    "6aa5c31deba7bc5677856c91" # Post 1 do Lote 04
]

for pid in post_ids:
    q = f"""
    query {{
      post(input: {{ id: "{pid}" }}) {{
        id
        status
        dueAt
        text
      }}
    }}
    """
    r = requests.post(
        "https://api.buffer.com/graphql",
        headers=headers,
        json={"query": q},
        timeout=20
    )
    print(json.dumps(r.json(), indent=2))


