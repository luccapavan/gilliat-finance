"""
Construtor dos 3 Pacotes ZIP para a Escada de Produtos:
Tier 1: PDFs Only (Playbook PT/EN + Checklist PT/EN + README EN/PT)
Tier 2: Toolkit Quant Padrão (PDFs + 4 Motores Quant em Python EN/PT + READMEs)
Tier 3: Plus / All-in-One (Tier 2 + Econometrics Toolkit EN/PT + READMEs)
"""
import zipfile
import shutil
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
    ("code/backtest_multifactor_en.py", CODE_DIR / "backtest_multifactor_en.py"),
    ("code/risk_performance_metrics.py", CODE_DIR / "metricas_risco_performance.py"),
    ("code/risk_performance_metrics_en.py", CODE_DIR / "risk_performance_metrics_en.py"),
    ("code/factor_orthogonalization_fwl.py", CODE_DIR / "factor_orthogonalization_fwl.py"),
    ("code/factor_orthogonalization_fwl_en.py", CODE_DIR / "factor_orthogonalization_fwl_en.py"),
    ("code/ledoit_wolf_covariance.py", CODE_DIR / "ledoit_wolf_covariance.py"),
    ("code/ledoit_wolf_covariance_en.py", CODE_DIR / "ledoit_wolf_covariance_en.py"),
    ("code/requirements.txt", CODE_DIR / "requirements.txt"),
    ("code/README_TOOLKIT.md", CODE_DIR / "README_TOOLKIT.md"),
    ("code/README_TOOLKIT_EN.md", CODE_DIR / "README_TOOLKIT_EN.md"),
]

ECONOMETRIC_FILES = [
    ("econometrics_toolkit/modelos_series_temporais.py", ECONOMY_DIR / "modelos_series_temporais.py"),
    ("econometrics_toolkit/time_series_models.py", ECONOMY_DIR / "time_series_models.py"),
    ("econometrics_toolkit/analise_estilo_sharpe.py", ECONOMY_DIR / "analise_estilo_sharpe.py"),
    ("econometrics_toolkit/sharpe_style_analysis.py", ECONOMY_DIR / "sharpe_style_analysis.py"),
    ("econometrics_toolkit/README.md", ECONOMY_DIR / "README.md"),
    ("econometrics_toolkit/README_EN.md", ECONOMY_DIR / "README_EN.md"),
]

def build_tier_1():
    zip_path = PRODUCTS_DIR / "quant_transition_playbook_tier1_pdfs.zip"
    tier1_dir = PRODUCTS_DIR / "1_PACOTE_BASICO_PDFS"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for arcname, filepath in PDF_FILES:
            if filepath.exists():
                z.write(filepath, arcname)
        if (tier1_dir / "README.txt").exists():
            z.write(tier1_dir / "README.txt", "README.txt")
        if (tier1_dir / "LEIA-ME.txt").exists():
            z.write(tier1_dir / "LEIA-ME.txt", "LEIA-ME.txt")
    print(f"[OK] Tier 1 ZIP criado: {zip_path.name} ({zip_path.stat().st_size / 1024:.1f} KB)")
    return zip_path

def build_tier_2():
    zip_path = PRODUCTS_DIR / "quant_transition_playbook_tier2_toolkit.zip"
    tier2_dir = PRODUCTS_DIR / "2_PACOTE_INTERMEDIARIO_TOOLKIT"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        if (tier2_dir / "README.txt").exists():
            z.write(tier2_dir / "README.txt", "README.txt")
        if (tier2_dir / "LEIA-ME.txt").exists():
            z.write(tier2_dir / "LEIA-ME.txt", "LEIA-ME.txt")
        for arcname, filepath in PDF_FILES:
            if filepath.exists():
                z.write(filepath, arcname)
        for arcname, filepath in QUANT_CODE_FILES:
            if filepath.exists():
                z.write(filepath, arcname)
    print(f"[OK] Tier 2 ZIP criado: {zip_path.name} ({zip_path.stat().st_size / 1024:.1f} KB)")
    
    v1_path = PRODUCTS_DIR / "quant_transition_playbook_v1.zip"
    shutil.copy2(zip_path, v1_path)
    print(f"[OK] Atualizado quant_transition_playbook_v1.zip ({v1_path.stat().st_size / 1024:.1f} KB)")
    return zip_path

def build_tier_3():
    zip_path = PRODUCTS_DIR / "quant_transition_playbook_tier3_plus.zip"
    tier3_dir = PRODUCTS_DIR / "3_PACOTE_PLUS_ECONOMETRIA"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        if (tier3_dir / "README.txt").exists():
            z.write(tier3_dir / "README.txt", "README.txt")
        if (tier3_dir / "LEIA-ME.txt").exists():
            z.write(tier3_dir / "LEIA-ME.txt", "LEIA-ME.txt")
        for arcname, filepath in PDF_FILES:
            if filepath.exists():
                z.write(filepath, arcname)
        for arcname, filepath in QUANT_CODE_FILES:
            if filepath.exists():
                z.write(filepath, arcname)
        for arcname, filepath in ECONOMETRIC_FILES:
            if filepath.exists():
                z.write(filepath, arcname)
    print(f"[OK] Tier 3 ZIP criado: {zip_path.name} ({zip_path.stat().st_size / 1024:.1f} KB)")
    return zip_path

def sync_folders():
    for tier in ["2_PACOTE_INTERMEDIARIO_TOOLKIT", "3_PACOTE_PLUS_ECONOMETRIA"]:
        target_code = PRODUCTS_DIR / tier / "code"
        target_code.mkdir(parents=True, exist_ok=True)
        for _, fpath in QUANT_CODE_FILES:
            if fpath.exists():
                shutil.copy2(fpath, target_code / fpath.name)
    
    target_econ = PRODUCTS_DIR / "3_PACOTE_PLUS_ECONOMETRIA" / "econometrics_toolkit"
    target_econ.mkdir(parents=True, exist_ok=True)
    for _, fpath in ECONOMETRIC_FILES:
        if fpath.exists():
            shutil.copy2(fpath, target_econ / fpath.name)
            
    print("[OK] Pastas fisicas dos Tiers sincronizadas com versoes PT e EN")

if __name__ == "__main__":
    print("Iniciando build dos 3 tiers ZIP bilingues...")
    sync_folders()
    build_tier_1()
    build_tier_2()
    build_tier_3()
    print("Build e sincronizacao concluidos com sucesso!")
