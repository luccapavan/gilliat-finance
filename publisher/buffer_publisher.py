"""
Módulo de Agendamento Seguro via Buffer GraphQL API Oficial
"""
import os
import sys
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import BUFFER_CONFIG

GRAPHQL_URL = "https://api.buffer.com/graphql"

def schedule_via_buffer(text: str, mode: str = "addToQueue", save_to_draft: bool = False, due_at: str = None) -> dict:
    """
    Agenda ou publica um post através do Buffer utilizando a API GraphQL oficial.
    
    Parâmetros:
    - text: Texto da postagem formatado para o LinkedIn.
    - mode: 'addToQueue', 'shareNow', 'customScheduled'
    - save_to_draft: se True, salva na aba de rascunhos do Buffer.
    - due_at: Timestamp ISO 8601 UTC (ex: '2026-09-07T15:00:00.000Z' para 12:00 BRT)
    """
    access_token = BUFFER_CONFIG.get("access_token")
    channel_id = BUFFER_CONFIG.get("profile_id")
    
    if not access_token or not channel_id:
        return {
            "success": False,
            "error": "Credenciais do Buffer não encontradas nas variáveis de ambiente (.env)."
        }
        
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
        "channelId": channel_id,
        "text": text,
        "mode": actual_mode,
        "schedulingType": "automatic",
        "needsApproval": False,
        "saveToDraft": save_to_draft
    }
    
    if due_at:
        input_payload["dueAt"] = due_at
        
    variables = {
        "input": input_payload
    }
    
    try:
        response = requests.post(GRAPHQL_URL, headers=headers, json={"query": mutation, "variables": variables}, timeout=20)
        
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
                "mode": mode
            }
        elif "message" in result:
            return {"success": False, "error": result["message"]}
        else:
            return {"success": False, "response": result}
            
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    test_text = "Teste de postagem via Buffer API."
    print("Módulo pronto para agendamento.")
