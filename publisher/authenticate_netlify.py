"""
Autenticador OAuth Oficial do Netlify
Troca o authorization code pelo token de acesso definitivo e salva em .env
"""
import os
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

import requests
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

env_file = ROOT_DIR / ".env"
load_dotenv(dotenv_path=env_file)

CLIENT_ID = os.getenv("NETLIFY_CLIENT_ID", "f3NXDvxyNmlGYsI3rJcnWL1_Jk7yZkVADUyuYS5LwAc")
CLIENT_SECRET = os.getenv("NETLIFY_CLIENT_SECRET", "7NAEIuw21Wu7_BiHoNpfF9Nak0r7o7-GUy7vX4MwWjI")
REDIRECT_URI = os.getenv("NETLIFY_REDIRECT_URI", "urn:ietf:wg:oauth:2.0:oob")

AUTH_URL = f"https://app.netlify.com/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}"


def exchange_code(code: str):
    """Troca o code pelo access token e salva em .env."""
    code = code.strip()
    print(f"🔄 Conectando com a API do Netlify para trocar o código de autorização...")
    
    response = requests.post(
        "https://api.netlify.com/oauth/token",
        data={
            "grant_type": "authorization_code",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code,
            "redirect_uri": REDIRECT_URI,
        },
        timeout=30,
    )
    
    if response.status_code == 200:
        data = response.json()
        token = data.get("access_token")
        print("✅ Autenticação realizada com sucesso!")
        
        # Salva no .env
        content = env_file.read_text(encoding="utf-8")
        lines = content.splitlines()
        new_lines = []
        found = False
        for line in lines:
            if line.strip().startswith("NETLIFY_AUTH_TOKEN="):
                new_lines.append(f"NETLIFY_AUTH_TOKEN={token}")
                found = True
            else:
                new_lines.append(line)
        if not found:
            new_lines.append(f"NETLIFY_AUTH_TOKEN={token}")
        env_file.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
        print("💾 Token de acesso salvo com sucesso no arquivo .env!")
        return token
    else:
        print(f"❌ Erro na autenticação ({response.status_code}): {response.text}")
        return None


if __name__ == "__main__":
    if len(sys.argv) > 1:
        code_input = sys.argv[1]
        exchange_code(code_input)
    else:
        print("=" * 65)
        print("🔐 AUTENTICAÇÃO OAUTH DO NETLIFY")
        print("=" * 65)
        print("\n1. Abra o link abaixo no seu navegador:")
        print(AUTH_URL)
        print("\n2. Clique em 'Authorize'. O Netlify exibirá um código de autorização na tela.")
        print("3. Copie o código e execute:")
        print("   python publisher/authenticate_netlify.py SEU_CODIGO_AQUI")
        print("=" * 65)
