"""
Módulo de Agendamento Oficial para Instagram via Buffer GraphQL API
Suporta publicação em fila (addToQueue), agendamento com data/hora (customScheduled)
ou salvamento direto em rascunhos (Drafts) na conta @pavan_lucca.
"""
import os
import sys
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import BUFFER_CONFIG

GRAPHQL_URL = "https://api.buffer.com/graphql"
DEFAULT_INSTAGRAM_CHANNEL_ID = "6aa208b4cd8b9c702c3e33cc"  # @pavan_lucca

def get_instagram_channel_id(token: str = None) -> str:
    """Busca dinamicamente o canal do Instagram associado à conta do Buffer."""
    access_token = token or BUFFER_CONFIG.get("access_token")
    if not access_token:
        return DEFAULT_INSTAGRAM_CHANNEL_ID
        
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    query = """
    query {
      account {
        organizations {
          id
        }
      }
    }
    """
    try:
        r = requests.post(GRAPHQL_URL, headers=headers, json={"query": query}, timeout=15)
        orgs = r.json().get("data", {}).get("account", {}).get("organizations", [])
        if not orgs:
            return DEFAULT_INSTAGRAM_CHANNEL_ID
        org_id = orgs[0]["id"]
        
        query_channels = f"""
        query {{
          channels(input: {{ organizationId: "{org_id}" }}) {{
            id
            service
            name
          }}
        }}
        """
        r_chan = requests.post(GRAPHQL_URL, headers=headers, json={"query": query_channels}, timeout=15)
        channels = r_chan.json().get("data", {}).get("channels", [])
        for ch in channels:
            if ch.get("service") == "instagram":
                return ch.get("id")
    except Exception as e:
        print(f"[!] Erro ao resolver canal dinamicamente: {e}")
        
    return DEFAULT_INSTAGRAM_CHANNEL_ID

def schedule_instagram_post(
    text: str,
    channel_id: str = None,
    mode: str = "addToQueue",
    save_to_draft: bool = True,
    due_at: str = None,
    image_urls: list = None
) -> dict:
    """
    Cria ou agenda um post no Instagram via Buffer.
    
    Parâmetros:
    - text: Legenda completa com quebras de linha e hashtags
    - channel_id: ID do canal do Instagram no Buffer
    - mode: 'addToQueue', 'customScheduled', 'shareNow'
    - save_to_draft: se True, salva como rascunho (recomendado para carrosséis)
    - due_at: String ISO UTC (ex: '2026-09-15T15:00:00.000Z')
    - image_urls: Lista de URLs públicas das imagens (se houver)
    """
    access_token = BUFFER_CONFIG.get("access_token")
    target_channel_id = channel_id or get_instagram_channel_id(access_token)
    
    if not access_token or not target_channel_id:
        return {"success": False, "error": "Credenciais do Buffer não encontradas."}
        
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
        ... on LimitReachedError {
          message
        }
        ... on UnauthorizedError {
          message
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
    
    actual_mode = "customScheduled" if due_at else mode
    
    input_payload = {
        "channelId": target_channel_id,
        "text": text,
        "mode": actual_mode,
        "schedulingType": "automatic",
        "needsApproval": False,
        "saveToDraft": save_to_draft,
        "metadata": {
            "instagram": {
                "type": "post",
                "shouldShareToFeed": True
            }
        }
    }
    
    if due_at:
        input_payload["dueAt"] = due_at
        
    if image_urls and len(image_urls) > 0:
        assets = []
        for url in image_urls:
            assets.append({
                "image": {
                    "url": url
                }
            })
        input_payload["assets"] = assets
        
    try:
        response = requests.post(
            GRAPHQL_URL,
            headers=headers,
            json={"query": mutation, "variables": {"input": input_payload}},
            timeout=25
        )
        
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
                "dueAt": result["post"].get("dueAt"),
                "saveToDraft": save_to_draft,
                "channel_id": target_channel_id
            }
        elif "message" in result:
            return {"success": False, "error": result["message"]}
        else:
            return {"success": False, "response": result}
            
    except Exception as e:
        return {"success": False, "error": str(e)}

def schedule_carousel_campaign(as_draft: bool = True, start_days_from_now: int = 1, interval_days: int = 2):
    """
    Agenda a sequência completa dos 4 posts de assessoria no Instagram.
    """
    posts_file = Path(__file__).resolve().parent.parent / "carousels" / "posts_data.json"
    with open(posts_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    posts = data.get("posts", [])
    print(f"\n=== Agendando Campanha de Carrosséis no Buffer Instagram (@pavan_lucca) ===")
    print(f"Total de posts: {len(posts)}")
    print(f"Modo: {'Rascunho (Draft)' if as_draft else 'Fila Agendada (Scheduled)'}")
    print("-" * 65)
    
    results = []
    base_date = datetime.utcnow() + timedelta(days=start_days_from_now)
    # Define horário de publicação padrão: 15:00 UTC (12:00 Horário de Brasília)
    base_date = base_date.replace(hour=15, minute=0, second=0, microsecond=0)
    
    for i, post in enumerate(posts):
        post_id = post.get("id")
        category = post.get("category_name")
        caption = post.get("caption")
        
        post_due_at = None
        if not as_draft:
            scheduled_time = base_date + timedelta(days=i * interval_days)
            post_due_at = scheduled_time.strftime("%Y-%m-%dT%H:%M:%00.000Z")
            
        print(f"\nAgendando Post {i+1}/4: {category} ({post_id})...")
        res = schedule_instagram_post(
            text=caption,
            mode="customScheduled" if post_due_at else "addToQueue",
            save_to_draft=as_draft,
            due_at=post_due_at
        )
        
        res["post_id_ref"] = post_id
        res["category"] = category
        if post_due_at:
            res["scheduled_utc"] = post_due_at
            
        results.append(res)
        
        if res.get("success"):
            print(f"  [OK] Sucesso! Buffer Post ID: {res.get('post_id')} (Status: {res.get('status')})")
            if post_due_at:
                print(f"       Data/Hora programada: {post_due_at} UTC (12:00 BRT)")
        else:
            print(f"  [ERRO] Falha ao agendar: {res.get('error') or res.get('errors')}")
            
    report_file = Path(__file__).resolve().parent / "instagram_campaign_schedule_report.json"
    with open(report_file, "w", encoding="utf-8") as rf:
        json.dump(results, rf, indent=2, ensure_ascii=False)
        
    print(f"\nRelatório de agendamento salvo em: {report_file}")
    return results

if __name__ == "__main__":
    as_draft = True
    if len(sys.argv) > 1 and sys.argv[1].lower() in ["--live", "--queue", "--publish"]:
        as_draft = False
        
    schedule_carousel_campaign(as_draft=as_draft)
