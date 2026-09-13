"""
Script de Upload de Imagens e Agendamento Completo dos 4 Carrosséis no Buffer Instagram (@pavan_lucca)
Faz upload das 16 lâminas em alta definição para obter URLs públicas permanentes
e agenda cada carrossel com suas 4 lâminas no canal do Instagram via Buffer GraphQL API.
"""
import os
import sys
import json
import time
import requests
from datetime import datetime, timedelta
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import BUFFER_CONFIG

GRAPHQL_URL = "https://api.buffer.com/graphql"
INSTA_CHANNEL_ID = "6aa208b4cd8b9c702c3e33cc"  # @pavan_lucca
LINKEDIN_CHANNEL_ID = "6a9cc410cd8b9c702c14b842"  # Lucca Simeoni Pavan, Ph.D.

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "carousels" / "output"
DATA_FILE = BASE_DIR / "carousels" / "posts_data.json"

def upload_image_to_catbox(file_path: Path) -> str:
    """Faz upload de uma lâmina PNG para o Catbox e retorna a URL direta."""
    url = "https://catbox.moe/user/api.php"
    for attempt in range(3):
        try:
            with open(file_path, "rb") as f:
                r = requests.post(url, data={"reqtype": "fileupload"}, files={"fileToUpload": f}, timeout=30)
            if r.status_code == 200 and r.text.startswith("http"):
                return r.text.strip()
            print(f"Tentativa {attempt+1} falhou para {file_path.name}: {r.text}")
        except Exception as e:
            print(f"Erro na tentativa {attempt+1} para {file_path.name}: {e}")
        time.sleep(2)
    raise RuntimeError(f"Não foi possível fazer upload de {file_path}")

def upload_all_carousel_images() -> dict:
    """Faz upload de todas as 16 lâminas e mapeia as URLs por post."""
    urls_file = BASE_DIR / "carousels" / "uploaded_image_urls.json"
    if urls_file.exists():
        with open(urls_file, "r", encoding="utf-8") as f:
            existing = json.load(f)
            if len(existing) == 4 and all(len(v) == 4 for v in existing.values()):
                print("URLs de imagens já existentes e completas.")
                return existing

    print("Iniciando upload das 16 lâminas de carrossel para geração de URLs públicas...")
    mapping = {}
    for post_idx in range(1, 5):
        post_key = f"post_{post_idx:02d}"
        post_dir = OUTPUT_DIR / post_key
        mapping[post_key] = []
        print(f"\nFazendo upload das lâminas de {post_key}...")
        for slide_idx in range(1, 5):
            slide_file = post_dir / f"slide_{slide_idx:02d}.png"
            if not slide_file.exists():
                raise FileNotFoundError(f"Arquivo não encontrado: {slide_file}")
            print(f"  Enviando {slide_file.name}...", end=" ", flush=True)
            img_url = upload_image_to_catbox(slide_file)
            print(f"OK -> {img_url}")
            mapping[post_key].append(img_url)
            time.sleep(0.5)

    with open(urls_file, "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2)
    print(f"\nTodas as URLs salvas com sucesso em: {urls_file}")
    return mapping

def schedule_post_on_buffer(channel_id: str, text: str, image_urls: list, due_at: str, is_insta: bool = True) -> dict:
    access_token = BUFFER_CONFIG.get("access_token")
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
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
    
    assets = [{"image": {"url": u}} for u in image_urls]
    
    input_payload = {
        "channelId": channel_id,
        "text": text,
        "mode": "customScheduled",
        "schedulingType": "automatic",
        "needsApproval": False,
        "saveToDraft": False,
        "dueAt": due_at,
        "assets": assets
    }
    
    if is_insta:
        input_payload["metadata"] = {
            "instagram": {
                "type": "carousel" if len(image_urls) > 1 else "post",
                "shouldShareToFeed": True
            }
        }
        
    response = requests.post(GRAPHQL_URL, headers=headers, json={"query": mutation, "variables": {"input": input_payload}}, timeout=30)
    
    if response.status_code != 200:
        return {"success": False, "status_code": response.status_code, "error": response.text}
        
    res_json = response.json()
    if "errors" in res_json:
        return {"success": False, "errors": res_json["errors"]}
        
    result = res_json.get("data", {}).get("createPost", {})
    if "post" in result and result["post"]:
        return {
            "success": True,
            "post_id": result["post"].get("id"),
            "status": result["post"].get("status"),
            "dueAt": result["post"].get("dueAt")
        }
    elif "message" in result:
        # Se type: "carousel" não for aceito diretamente, tenta com type: "post"
        if is_insta and "carousel" in str(result):
            input_payload["metadata"]["instagram"]["type"] = "post"
            retry_resp = requests.post(GRAPHQL_URL, headers=headers, json={"query": mutation, "variables": {"input": input_payload}}, timeout=30)
            retry_res = retry_resp.json().get("data", {}).get("createPost", {})
            if "post" in retry_res and retry_res["post"]:
                return {
                    "success": True,
                    "post_id": retry_res["post"].get("id"),
                    "status": retry_res["post"].get("status"),
                    "dueAt": retry_res["post"].get("dueAt")
                }
        return {"success": False, "error": result["message"]}
    else:
        return {"success": False, "response": result}

def run_schedule():
    # 1. Obter URLs públicas das lâminas
    images_mapping = upload_all_carousel_images()
    
    # 2. Carregar dados dos posts
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        posts_data = json.load(f)
        
    posts = posts_data.get("posts", [])
    
    # 3. Definir cronograma de publicação estratégica:
    # Post 1: Sexta-feira 11/09/2026 às 12:00 BRT (15:00 UTC)
    # Post 2: Segunda-feira 14/09/2026 às 12:00 BRT (15:00 UTC)
    # Post 3: Quarta-feira 16/09/2026 às 12:00 BRT (15:00 UTC)
    # Post 4: Sexta-feira 18/09/2026 às 12:00 BRT (15:00 UTC)
    schedule_dates = [
        "2026-09-11T15:00:00.000Z",
        "2026-09-14T15:00:00.000Z",
        "2026-09-16T15:00:00.000Z",
        "2026-09-18T15:00:00.000Z",
    ]
    
    print("\n=== AGENDANDO OS 4 CARROSSÉIS NO BUFFER INSTAGRAM (@pavan_lucca) ===")
    results = []
    
    for i, post in enumerate(posts):
        post_id = post.get("id")
        category = post.get("category_name")
        caption = post.get("caption")
        due_at = schedule_dates[i]
        image_urls = images_mapping.get(post_id, [])
        
        print(f"\nAgendando {category} ({post_id}) para {due_at} (12:00 BRT)...")
        print(f"  Anexando {len(image_urls)} lâminas do carrossel...")
        
        res = schedule_post_on_buffer(
            channel_id=INSTA_CHANNEL_ID,
            text=caption,
            image_urls=image_urls,
            due_at=due_at,
            is_insta=True
        )
        
        res["post_id_ref"] = post_id
        res["category"] = category
        res["scheduled_dueAt"] = due_at
        res["channel"] = "Instagram (@pavan_lucca)"
        results.append(res)
        
        if res.get("success"):
            print(f"  [SUCESSO] Post agendado com ID: {res.get('post_id')} (Status: {res.get('status')})")
        else:
            print(f"  [FALHA]: {res.get('error') or res.get('errors')}")
            
    # Salvar relatório oficial
    report_file = BASE_DIR / "publisher" / "instagram_carousels_scheduled_official.json"
    with open(report_file, "w", encoding="utf-8") as rf:
        json.dump(results, rf, indent=2, ensure_ascii=False)
        
    print(f"\nRelatório oficial gravado em: {report_file}")
    return results

if __name__ == "__main__":
    run_schedule()
