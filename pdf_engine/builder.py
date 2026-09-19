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
    html_path = Path(html_file).resolve()
    pdf_abs = Path(output_pdf).resolve()
    
    pdf_abs.parent.mkdir(parents=True, exist_ok=True)
    
    # Root directory of the repository
    repo_root = Path(__file__).resolve().parent.parent
    theme_uri = (repo_root / "pdf_engine" / "theme.css").resolve().as_uri()
    mathjax_uri = (repo_root / "pdf_engine" / "mathjax" / "tex-svg.js").resolve().as_uri()
    
    content = html_path.read_text(encoding="utf-8")
    
    # Normalize paths so MathJax and CSS always load regardless of directory depth
    needs_mathjax = "MathJax" in content or "tex-svg.js" in content or "$$" in content
    
    target_to_print = html_path.as_uri()
    temp_rendered_file = None
    
    if needs_mathjax:
        # Replace relative links with guaranteed absolute file URIs
        import re
        content_fixed = re.sub(r'href=[\'"][^\'"]*theme\.css[\'"]', f'href="{theme_uri}"', content)
        content_fixed = re.sub(r'src=[\'"][^\'"]*tex-svg\.js[\'"]', f'src="{mathjax_uri}"', content_fixed)
        
        temp_input = html_path.parent / f"_temp_mathjax_input_{html_path.stem}.html"
        temp_input.write_text(content_fixed, encoding="utf-8")
        
        # Step 1: Pre-render DOM with MathJax vector SVGs
        cmd_dump = [
            browser_bin,
            "--headless=new",
            "--disable-gpu",
            "--allow-file-access-from-files",
            "--disable-web-security",
            "--virtual-time-budget=12000",
            "--dump-dom",
            temp_input.resolve().as_uri()
        ]
        res_dump = subprocess.run(cmd_dump, capture_output=True, text=True, encoding="utf-8", errors="ignore")
        
        if "<mjx-container" in res_dump.stdout:
            temp_rendered_file = html_path.parent / f"_temp_mathjax_rendered_{html_path.stem}.html"
            temp_rendered_file.write_text(res_dump.stdout, encoding="utf-8")
            target_to_print = temp_rendered_file.resolve().as_uri()
        else:
            target_to_print = temp_input.resolve().as_uri()
            
        try:
            temp_input.unlink(missing_ok=True)
        except Exception:
            pass
            
    cmd = [
        browser_bin,
        "--headless=new",
        "--disable-gpu",
        "--allow-file-access-from-files",
        "--disable-web-security",
        "--virtual-time-budget=6000",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_abs}",
        "--no-pdf-header-footer",
        target_to_print
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if temp_rendered_file:
        try:
            temp_rendered_file.unlink(missing_ok=True)
        except Exception:
            pass
            
    if result.returncode == 0 and pdf_abs.exists():
        return True
    else:
        print(f"Erro ao gerar PDF: {result.stderr}")
        return False

if __name__ == "__main__":
    print(f"Motor de PDF detectado: {find_browser_binary()}")

