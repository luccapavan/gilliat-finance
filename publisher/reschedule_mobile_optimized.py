"""
Atualiza o Buffer com as lâminas dos 4 carrosséis com tipografia otimizada para celular.
1. Faz upload das 16 novas lâminas para o Catbox.
2. Remove os agendamentos anteriores.
3. Agenda os 4 posts com as novas imagens de alta legibilidade no Buffer.
"""
import os
import sys
import json
import time
import requests
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import BUFFER_CONFIG

GRAPHQL_URL = "https://api.buffer.com/graphql"
INSTA_CHANNEL_ID = "6aa208b4cd8b9c702c3e33cc"

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "carousels" / "output"
DATA_FILE = BASE_DIR / "carousels" / "posts_data.json"
URLS_FILE = BASE_DIR / "carousels" / "uploaded_image_urls.json"

OLD_POST_IDS = [
    "6aa2aa1798d1587af5240539",
    "6aa2aa1998d1587af52405b1",
    "6aa2aa1bdf56ba8a23997df0",
    "6aa2aa1d78a1026cf22b881e"
]

def upload_image(file_path: Path) -> str:
    url = "https://catbox.moe/user/api.php"
    for attempt in range(3):
        try:
            with open(file_path, "rb") as f:
                r = requests.post(url, data={"reqtype": "fileupload"}, files={"fileToUpload": f}, timeout=30)
            if r.status_code == 200 and r.text.startswith("http"):
                return r.text.strip()
        except Exception as e:
            print(f"Tentativa {attempt+1} falhou para {file_path.name}: {e}")
        time.sleep(2)
    raise RuntimeError(f"Falha ao enviar {file_path}")

def upload_all_mobile_images() -> dict:
    print("Iniciando upload das 16 lâminas com tipografia otimizada para mobile...")
    mapping = {}
    for post_idx in range(1, 5):
        post_key = f"post_{post_idx:02d}"
        post_dir = OUTPUT_DIR / post_key
        mapping[post_key] = []
        print(f"\nUpload {post_key}...")
        for slide_idx in range(1, 5):
            slide_file = post_dir / f"slide_{slide_idx:02d}.png"
            print(f"  Enviando {slide_file.name}...", end=" ", flush=True)
            img_url = upload_image(slide_file)
            print(f"OK -> {img_url}")
            mapping[post_key].append(img_url)
            time.sleep(0.4)

    with open(URLS_FILE, "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2)
    return mapping

def delete_old_posts():
    token = BUFFER_CONFIG.get("access_token")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    print("\nRemovendo agendamentos anteriores do Buffer...")
    for p_id in OLD_POST_IDS:
        q = f'mutation {{ deletePost(input: {{ id: "{p_id}" }}) {{ ... on DeletePostSuccess {{ id }} }} }}'
        requests.post(GRAPHQL_URL, headers=headers, json={"query": q}, timeout=15)
        print(f"  Post {p_id} removido.")

def schedule_posts(urls_map):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        posts_data = json.load(f)
        
    schedule_dates = [
        "2026-09-11T15:00:00.000Z",
        "2026-09-14T15:00:00.000Z",
        "2026-09-16T15:00:00.000Z",
        "2026-09-18T15:00:00.000Z",
    ]
    
    token = BUFFER_CONFIG.get("access_token")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    mutation = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        ... on PostActionSuccess {
          post {
            id
            status
            dueAt
          }
        }
        ... on LimitReachedError { message }
        ... on UnauthorizedError { message }
        ... on InvalidInputError { message }
        ... on UnexpectedError { message }
      }
    }
    """
    
    results = []
    print("\n=== AGENDANDO OS CARROSSÉIS OTIMIZADOS PARA MOBILE NO BUFFER ===")
    for i, post in enumerate(posts_data.get("posts", [])):
        post_id = post.get("id")
        category = post.get("category_name")
        caption = post.get("caption")
        due_at = schedule_dates[i]
        image_urls = urls_map.get(post_id, [])
        
        assets = [{"image": {"url": u}} for u in image_urls]
        input_payload = {
            "channelId": INSTA_CHANNEL_ID,
            "text": caption,
            "mode": "customScheduled",
            "schedulingType": "automatic",
            "needsApproval": False,
            "saveToDraft": False,
            "dueAt": due_at,
            "assets": assets,
            "metadata": {
                "instagram": {
                    "type": "post",
                    "shouldShareToFeed": True
                }
            }
        }
        
        print(f"\nAgendando {category} ({post_id}) para {due_at}...")
        resp = requests.post(GRAPHQL_URL, headers=headers, json={"query": mutation, "variables": {"input": input_payload}}, timeout=30)
        result = resp.json().get("data", {}).get("createPost", {})
        
        if "post" in result and result["post"]:
            p_res = {
                "success": True,
                "post_id": result["post"].get("id"),
                "status": result["post"].get("status"),
                "dueAt": result["post"].get("dueAt"),
                "category": category,
                "post_id_ref": post_id
            }
            print(f"  [OK] Sucesso! Buffer Post ID: {p_res['post_id']}")
            results.append(p_res)
        else:
            print(f"  [ERRO]: {result}")
            results.append({"success": False, "post_id_ref": post_id, "error": str(result)})
            
    with open(BASE_DIR / "publisher" / "instagram_carousels_scheduled_official.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
        
    return results

def main():
    urls_map = upload_all_mobile_images()
    delete_old_posts()
    schedule_posts(urls_map)
    print("\nAgendamento com imagens otimizadas para mobile concluído!")

if __name__ == "__main__":
    main()
