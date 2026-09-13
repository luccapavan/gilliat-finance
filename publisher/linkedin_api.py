import os
import sys
import requests
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import LINKEDIN_CONFIG

def publish_to_linkedin(text: str) -> dict:
    """
    Publica um post em texto no LinkedIn utilizando a API v2 oficial.
    Requer token de acesso com permissão 'w_member_social'.
    """
    access_token = LINKEDIN_CONFIG.get("access_token")
    author_urn = LINKEDIN_CONFIG.get("author_urn")
    
    if not access_token or not author_urn:
        return {
            "success": False,
            "error": "Credenciais do LinkedIn não configuradas em config.py ou variáveis de ambiente."
        }
    
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    
    payload = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code in [200, 201]:
            return {"success": True, "data": response.json()}
        else:
            return {"success": False, "status_code": response.status_code, "response": response.text}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    test_text = "Teste de postagem automatizada via API oficial do LinkedIn."
    print(publish_to_linkedin(test_text))
