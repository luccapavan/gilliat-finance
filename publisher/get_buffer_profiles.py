"""
Script Auxiliar: Obter Canais Conectados no Buffer via GraphQL API Oficial
"""
import sys
import os
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import BUFFER_CONFIG

def get_buffer_channels(token: str = None):
    access_token = token or BUFFER_CONFIG.get("access_token")
    if not access_token:
        print("\n[!] Token não encontrado em .env nem informado por argumento.")
        return

    graphql_url = "https://api.buffer.com/graphql"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # 1. Buscar a organização da conta
    query_account = """
    query {
      account {
        id
        email
        organizations {
          id
          name
        }
      }
    }
    """
    
    try:
        resp = requests.post(graphql_url, headers=headers, json={"query": query_account}, timeout=15)
        if resp.status_code != 200:
            print(f"Erro na autenticação ({resp.status_code}): {resp.text}")
            return
            
        data = resp.json().get("data", {}).get("account", {})
        orgs = data.get("organizations", [])
        if not orgs:
            print("Nenhuma organização encontrada para este usuário.")
            return
            
        org_id = orgs[0]["id"]
        
        # 2. Buscar os canais da organização
        query_channels = f"""
        query {{
          channels(input: {{ organizationId: "{org_id}" }}) {{
            id
            name
            service
          }}
        }}
        """
        
        resp_channels = requests.post(graphql_url, headers=headers, json={"query": query_channels}, timeout=15)
        channels_data = resp_channels.json().get("data", {}).get("channels", [])
        
        if not channels_data:
            print("\n[!] Nenhum canal/rede conectado ainda na sua conta do Buffer.")
            print("Por favor, acesse https://publish.buffer.com e conecte seu canal do LinkedIn.")
            return
            
        print("\n=== Canais Conectados no seu Buffer ===")
        for ch in channels_data:
            print(f"Rede / Serviço : {ch.get('service', '').capitalize()}")
            print(f"Nome da Conta  : {ch.get('name')}")
            print(f"Channel ID     : {ch.get('id')}")
            print("-" * 40)
            
        return channels_data
        
    except Exception as e:
        print(f"Erro ao consultar Buffer GraphQL API: {e}")

if __name__ == "__main__":
    cli_token = sys.argv[1] if len(sys.argv) > 1 else None
    get_buffer_channels(cli_token)
