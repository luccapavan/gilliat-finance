"""
Gerador Institucional de PDFs em Alta Resolução
Utiliza o motor headless do Chrome / Edge para renderização CSS Paged Media.
"""
import os
import sys
import subprocess
from pathlib import Path

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]

def find_browser_binary() -> str:
    for p in CHROME_PATHS:
        if os.path.exists(p):
            return p
    raise FileNotFoundError("Nenhum binário do Chrome ou Edge foi encontrado nos caminhos padrão.")

def convert_html_to_pdf(html_file: str, output_pdf: str) -> bool:
    browser_bin = find_browser_binary()
    html_abs = Path(html_file).resolve().as_uri()
    pdf_abs = Path(output_pdf).resolve()
    
    pdf_abs.parent.mkdir(parents=True, exist_ok=True)
    
    cmd = [
        browser_bin,
        "--headless=new",
        "--disable-gpu",
        "--allow-file-access-from-files",
        "--enable-local-file-accesses",
        "--virtual-time-budget=6000",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_abs}",
        "--no-pdf-header-footer",
        html_abs
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0 and pdf_abs.exists():
        return True
    else:
        print(f"Erro ao gerar PDF: {result.stderr}")
        return False

if __name__ == "__main__":
    print(f"Motor de PDF detectado: {find_browser_binary()}")
