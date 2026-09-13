"""
Script de Deploy e Gerenciamento do Netlify para o Gilliat Finance
Publica as Landing Pages via Netlify REST API ou prepara o pacote zip para o Netlify Drop.

Uso:
    python publisher/deploy_netlify.py
    python publisher/deploy_netlify.py --site-name analise-quantitativa
    python publisher/deploy_netlify.py --sync  (Deploy + Sincronização automática com Buffer)
"""

import os
import sys
import json
import zipfile
import subprocess
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

import requests
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

# Carrega .env
env_file = ROOT_DIR / ".env"
load_dotenv(dotenv_path=env_file)

NETLIFY_TOKEN = os.getenv("NETLIFY_AUTH_TOKEN", "").strip()
NETLIFY_SITE_ID = os.getenv("NETLIFY_SITE_ID", "").strip()
LP_DIR = ROOT_DIR / "landing_pages"
ZIP_FILE = ROOT_DIR / "landing_pages.zip"


def create_zip_package():
    """Gera o arquivo zip com toda a estrutura necessária para o Netlify."""
    print("📦 Compactando landing_pages para deploy...")
    with zipfile.ZipFile(ZIP_FILE, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(LP_DIR):
            if "__pycache__" in root or ".git" in root:
                continue
            for file in files:
                # Ignora arquivos temporários locais
                if file.endswith((".pyc", ".tmp", ".log")):
                    continue
                full_path = Path(root) / file
                rel_path = full_path.relative_to(LP_DIR)
                zipf.write(full_path, rel_path)
    size_kb = ZIP_FILE.stat().st_size / 1024
    print(f"✅ Pacote gerado com sucesso: {ZIP_FILE.name} ({size_kb:.1f} KB)")
    return ZIP_FILE


def update_env_variable(key: str, value: str):
    """Atualiza ou insere uma variável no arquivo .env."""
    if not env_file.exists():
        env_file.write_text(f"{key}={value}\n", encoding="utf-8")
        return

    content = env_file.read_text(encoding="utf-8")
    lines = content.splitlines()
    found = False
    new_lines = []

    for line in lines:
        if line.strip().startswith(f"{key}="):
            new_lines.append(f"{key}={value}")
            found = True
        else:
            new_lines.append(line)

    if not found:
        new_lines.append(f"{key}={value}")

    env_file.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    print(f"📝 Variável {key} atualizada no arquivo .env")


def deploy_via_api():
    """Realiza o upload direto para a API oficial do Netlify usando zip deploy."""
    headers = {
        "Authorization": f"Bearer {NETLIFY_TOKEN}",
        "Content-Type": "application/zip",
    }

    with open(ZIP_FILE, "rb") as f:
        zip_data = f.read()

    if NETLIFY_SITE_ID:
        print(f"🚀 Enviando nova versão para o site existente (ID: {NETLIFY_SITE_ID})...")
        url = f"https://api.netlify.com/api/v1/sites/{NETLIFY_SITE_ID}/deploys"
        response = requests.post(url, headers=headers, data=zip_data, timeout=60)
    else:
        print("🚀 Criando novo site e publicando no Netlify...")
        url = "https://api.netlify.com/api/v1/sites"
        response = requests.post(url, headers=headers, data=zip_data, timeout=60)

    if response.status_code in (200, 201):
        data = response.json()
        site_id = data.get("site_id") or data.get("id")
        deploy_url = data.get("ssl_url") or data.get("url")
        print("\n🎉 Deploy realizado com sucesso no Netlify!")
        print(f"🌐 URL no ar: {deploy_url}")
        print(f"🔑 Site ID: {site_id}")

        if site_id and site_id != NETLIFY_SITE_ID:
            update_env_variable("NETLIFY_SITE_ID", site_id)

        update_env_variable("QUANT_COURSE_LP_URL", deploy_url)

        if "--sync" in sys.argv:
            print("\n🔄 Sincronizando posts agendados do Buffer com a nova URL...")
            sync_script = ROOT_DIR / "publisher" / "sync_lp_url.py"
            subprocess.run([sys.executable, str(sync_script), deploy_url], check=False)

        return deploy_url
    else:
        print(f"❌ Erro no deploy da API do Netlify ({response.status_code}):")
        try:
            print(response.json())
        except Exception:
            print(response.text)
        return None


def show_manual_instructions():
    """Exibe instruções práticas quando não há token configurado."""
    print("\n" + "=" * 65)
    print("🌐 COMO CONCLUIR O DEPLOY NO NETLIFY")
    print("=" * 65)
    print("\nOpção A: Netlify Drop (Mais rápida - Sem necessidade de token):")
    print("  1. Acesse: https://app.netlify.com/drop")
    print(f"  2. Arraste e solte o arquivo '{ZIP_FILE.name}' ou a pasta 'landing_pages'.")
    print("  3. Em 5 segundos seu site estará no ar com HTTPS gratuito!")
    print("  4. No painel, vá em 'Site configuration' > 'Change site name' para customizar o subdomínio.")
    print("\nOpção B: Deploy Automático Contínuo via GitHub:")
    print("  1. Acesse: https://app.netlify.com")
    print("  2. Clique em 'Add new site' > 'Import an existing project' > 'GitHub'.")
    print("  3. Selecione o repositório 'luccapavan/gilliat-finance'.")
    print("  4. O arquivo 'netlify.toml' que já criamos configurará tudo automaticamente!")
    print("  5. Cada 'git push' atualizará o site em produção.")
    print("\nOpção C: Deploy 100% via Terminal (REST API):")
    print("  1. Obtenha um token em: https://app.netlify.com/user/applications#personal-access-tokens")
    print("  2. Adicione no arquivo .env:")
    print("     NETLIFY_AUTH_TOKEN=seu_token_aqui")
    print("  3. Rode novamente: python publisher/deploy_netlify.py --sync")
    print("=" * 65 + "\n")


def main():
    create_zip_package()

    if NETLIFY_TOKEN:
        deploy_via_api()
    else:
        show_manual_instructions()


if __name__ == "__main__":
    main()
