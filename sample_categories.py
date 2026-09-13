import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('classified_connections.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for cat, items in data.items():
    print(f"\n==================== {cat.upper()} (Total: {len(items)}) ====================")
    for it in items[:10]:
        email_str = f" [{it['email']}]" if it['email'] else ""
        print(f" • {it['name']} - {it['pos']} @ {it['comp']}{email_str}")
