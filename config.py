"""
Configurações do Ecossistema LinkedIn & Infoprodutos
Carrega variáveis seguras de ambiente a partir de .env
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega arquivo .env seguro localizado na raiz do projeto
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# Dados da Persona do Criador
AUTHOR_INFO = {
    "name": "Lucca Simeoni Pavan, Ph.D.",
    "role_pt": "Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação",
    "role_en": "Former Head of Quantitative Strategies & Asset Allocation Manager",
    "background_pt": "Doutor em Economia com ampla vivência em modelagem quantitativa, Factor Investing e alocação de portfólios no mercado financeiro",
    "background_en": "Ph.D. in Economics, specialized in Time Series Econometrics, Systematic Factor Investing, Risk & Portfolio Allocation",
    "tone": "Técnico, sóbrio, analítico, baseado em dados empíricos e código reproduzível (PT e EN)",
    "bilingual": True
}

# Configurações de API carregadas estritamente de variáveis de ambiente
LINKEDIN_CONFIG = {
    "client_id": os.getenv("LINKEDIN_CLIENT_ID", ""),
    "client_secret": os.getenv("LINKEDIN_CLIENT_SECRET", ""),
    "access_token": os.getenv("LINKEDIN_ACCESS_TOKEN", ""),
    "author_urn": os.getenv("LINKEDIN_AUTHOR_URN", ""),
}

BUFFER_CONFIG = {
    "access_token": os.getenv("BUFFER_ACCESS_TOKEN", ""),
    "profile_id": os.getenv("BUFFER_PROFILE_ID", ""),
}

PRODUCT_LINKS = {
    "playbook": os.getenv("PLAYBOOK_GUMROAD_URL", "https://warrenjax.gumroad.com/l/fsrcmj"),
    "newsletter": os.getenv("NEWSLETTER_URL", "https://factormacro.substack.com"),
    "toolkit": os.getenv("TOOLKIT_GUMROAD_URL", "https://gumroad.com/l/econometrics-python-toolkit"),
    "quant_course_lp": os.getenv("QUANT_COURSE_LP_URL", "https://curso-quant-research.netlify.app"),
}
