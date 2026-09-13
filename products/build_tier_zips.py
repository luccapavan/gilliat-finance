"""
Construtor dos 3 Pacotes ZIP para a Escada de Produtos:
Tier 1: PDFs Only (Playbook PT/EN + Checklist PT/EN)
Tier 2: Toolkit Quant Padrão (PDFs + 4 Motores Quant em Python)
Tier 3: Plus / All-in-One (Tier 2 + Econometrics Toolkit)
"""
import zipfile
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PRODUCTS_DIR = ROOT_DIR / "products"
CODE_DIR = PRODUCTS_DIR / "quant_transition_playbook" / "templates_codigo"
ECONOMY_DIR = PRODUCTS_DIR / "econometrics_toolkit"

PDF_FILES = [
    ("The_Quant_Transition_Playbook_PT.pdf", PRODUCTS_DIR / "The_Quant_Transition_Playbook_PT.pdf"),
    ("The_Quant_Transition_Playbook_EN.pdf", PRODUCTS_DIR / "The_Quant_Transition_Playbook_EN.pdf"),
    ("Quant_Anti_Bias_Checklist_PT.pdf", PRODUCTS_DIR / "Quant_Anti_Bias_Checklist_PT.pdf"),
    ("Quant_Anti_Bias_Checklist_EN.pdf", PRODUCTS_DIR / "Quant_Anti_Bias_Checklist_EN.pdf"),
]

QUANT_CODE_FILES = [
    ("code/backtest_multifactor.py", CODE_DIR / "backtest_multifator.py"),
    ("code/risk_performance_metrics.py", CODE_DIR / "metricas_risco_performance.py"),
    ("code/factor_orthogonalization_fwl.py", CODE_DIR / "factor_orthogonalization_fwl.py"),
    ("code/ledoit_wolf_covariance.py", CODE_DIR / "ledoit_wolf_covariance.py"),
    ("code/requirements.txt", CODE_DIR / "requirements.txt"),
    ("code/README_TOOLKIT.md", CODE_DIR / "README_TOOLKIT.md"),
]

ECONOMETRIC_FILES = [
    ("econometrics_toolkit/modelos_series_temporais.py", ECONOMY_DIR / "modelos_series_temporais.py"),
    ("econometrics_toolkit/analise_estilo_sharpe.py", ECONOMY_DIR / "analise_estilo_sharpe.py"),
    ("econometrics_toolkit/README.md", ECONOMY_DIR / "README.md"),
    ("econometrics_toolkit/README_EN.md", ECONOMY_DIR / "README_EN.md"),
]

def build_tier_1():
    zip_path = PRODUCTS_DIR / "quant_transition_playbook_tier1_pdfs.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for arcname, filepath in PDF_FILES:
            if filepath.exists():
                z.write(filepath, arcname)
    print(f"[OK] Tier 1 ZIP criado: {zip_path.name} ({zip_path.stat().st_size / 1024:.1f} KB)")
    return zip_path

def build_tier_2():
    zip_path = PRODUCTS_DIR / "quant_transition_playbook_tier2_toolkit.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        # PDFs
        for arcname, filepath in PDF_FILES:
            if filepath.exists():
                z.write(filepath, arcname)
        # Quant Engines
        for arcname, filepath in QUANT_CODE_FILES:
            if filepath.exists():
                z.write(filepath, arcname)
    print(f"[OK] Tier 2 ZIP criado: {zip_path.name} ({zip_path.stat().st_size / 1024:.1f} KB)")
    
    # Atualiza também quant_transition_playbook_v1.zip para manter retrocompatibilidade
    v1_path = PRODUCTS_DIR / "quant_transition_playbook_v1.zip"
    import shutil
    shutil.copy2(zip_path, v1_path)
    print(f"[OK] Atualizado quant_transition_playbook_v1.zip ({v1_path.stat().st_size / 1024:.1f} KB)")
    return zip_path

def build_tier_3():
    zip_path = PRODUCTS_DIR / "quant_transition_playbook_tier3_plus.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        # PDFs
        for arcname, filepath in PDF_FILES:
            if filepath.exists():
                z.write(filepath, arcname)
        # Quant Engines
        for arcname, filepath in QUANT_CODE_FILES:
            if filepath.exists():
                z.write(filepath, arcname)
        # Econometric Toolkit
        for arcname, filepath in ECONOMETRIC_FILES:
            if filepath.exists():
                z.write(filepath, arcname)
    print(f"[OK] Tier 3 ZIP criado: {zip_path.name} ({zip_path.stat().st_size / 1024:.1f} KB)")
    return zip_path

if __name__ == "__main__":
    print("Iniciando build dos 3 tiers ZIP...")
    build_tier_1()
    build_tier_2()
    build_tier_3()
    print("Build concluído com sucesso!")
