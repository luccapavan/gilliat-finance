"""
Gerador de Lâminas de Carrossel para Instagram (1080x1350 px)
Utiliza Playwright e o motor headless do Chrome para renderização em Retina Display (2x).
"""
import os
import sys
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pdf_engine.builder import find_browser_binary

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "posts_data.json"
CSS_FILE = BASE_DIR / "styles.css"
OUTPUT_DIR = BASE_DIR / "output"

def generate_slide_html(post_data: dict, slide_data: dict, css_content: str) -> str:
    slide_type = slide_data.get("type")
    theme_class = post_data.get("theme_class", "agro")
    category = post_data.get("category_name", "Assessoria")
    slide_num = slide_data.get("slide_num", "01/04")
    swipe_text = slide_data.get("swipe_text", "Arraste 👉")
    
    # Common header and footer
    header_html = f"""
    <div class="card-header">
      <div class="category-pill {theme_class}">{category}</div>
      <div class="slide-number">{slide_num}</div>
    </div>
    """
    
    footer_html = f"""
    <div class="card-footer">
      <div class="author-brand">
        <div class="author-avatar-ph">LP</div>
        <div class="author-details">
          <div class="author-name">Lucca Simeoni Pavan, Ph.D.</div>
          <div class="author-title">Assessoria de Investimentos • Alocação & Risco</div>
        </div>
      </div>
      <div class="swipe-indicator {theme_class}">{swipe_text}</div>
    </div>
    """
    
    content_html = ""
    glow_class = f"glow-orb-{theme_class}"
    
    if slide_type == "cover":
        headline = slide_data.get("headline", "")
        subheadline = slide_data.get("subheadline", "")
        badge_icon = slide_data.get("badge_icon", "✨")
        badge_text = slide_data.get("badge_text", "")
        
        content_html = f"""
        <div class="card-content">
          <h1 class="cover-headline">{headline}</h1>
          <p class="cover-subheadline">{subheadline}</p>
          <div class="cover-badge-box">
            <span class="cover-badge-icon">{badge_icon}</span>
            <span class="cover-badge-text">{badge_text}</span>
          </div>
        </div>
        """
        
    elif slide_type == "problem":
        title = slide_data.get("title", "")
        cards = slide_data.get("cards", [])
        impact_text = slide_data.get("impact_text", "")
        
        cards_html = ""
        for c in cards:
            cards_html += f"""
            <div class="problem-card">
              <div class="problem-card-title">⚠️ {c.get('title', '')}</div>
              <div class="problem-card-desc">{c.get('desc', '')}</div>
            </div>
            """
            
        impact_html = f'<div class="impact-badge"><p>{impact_text}</p></div>' if impact_text else ''
        
        content_html = f"""
        <div class="card-content">
          <h2 class="section-title">{title}</h2>
          <div class="problem-grid">
            {cards_html}
          </div>
          {impact_html}
        </div>
        """
        
    elif slide_type == "solution":
        title = slide_data.get("title", "")
        pillars = slide_data.get("pillars", [])
        
        pillars_html = ""
        for idx, p in enumerate(pillars, 1):
            pillars_html += f"""
            <div class="pillar-card {theme_class}">
              <div class="pillar-number {theme_class}">0{idx}</div>
              <div class="pillar-info">
                <h3>{p.get('title', '')}</h3>
                <p>{p.get('desc', '')}</p>
              </div>
            </div>
            """
            
        content_html = f"""
        <div class="card-content">
          <h2 class="section-title">{title}</h2>
          <div class="pillars-container">
            {pillars_html}
          </div>
        </div>
        """
        
    elif slide_type == "comparison_table":
        title = slide_data.get("title", "")
        comparisons = slide_data.get("comparisons", [])
        
        comps_html = ""
        for item in comparisons:
            comps_html += f"""
            <div class="comparison-card">
              <div class="comparison-card-topic">{item.get('topic', '')}</div>
              <div class="comparison-row">
                <div class="comparison-box-traditional">
                  <div class="tag-small">❌ Banco Tradicional</div>
                  <p>{item.get('traditional', '')}</p>
                </div>
                <div class="comparison-box-advisory">
                  <div class="tag-small">✅ Assessoria Consultiva</div>
                  <p>{item.get('advisory', '')}</p>
                </div>
              </div>
            </div>
            """
            
        content_html = f"""
        <div class="card-content">
          <h2 class="section-title">{title}</h2>
          <div class="comparison-container">
            {comps_html}
          </div>
        </div>
        """
        
    elif slide_type == "cta":
        quote = slide_data.get("quote", "")
        cta_icon = slide_data.get("cta_icon", "📲")
        cta_title = slide_data.get("cta_title", "")
        cta_subtitle = slide_data.get("cta_subtitle", "")
        
        content_html = f"""
        <div class="card-content">
          <div class="cta-quote-box">
            <div class="cta-quote-text">{quote}</div>
          </div>
          <div class="cta-action-card">
            <div class="cta-action-icon">{cta_icon}</div>
            <div class="cta-action-details">
              <div class="cta-action-title">{cta_title}</div>
              <div class="cta-action-subtitle">{cta_subtitle}</div>
            </div>
          </div>
        </div>
        """
        
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <style>
    {css_content}
  </style>
</head>
<body>
  <div class="glow-orb {glow_class}"></div>
  {header_html}
  {content_html}
  {footer_html}
</body>
</html>
"""
    return html

def render_all_cards():
    print("Iniciando geração de cards de carrossel em alta resolução...")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    with open(CSS_FILE, "r", encoding="utf-8") as f:
        css_content = f.read()
        
    browser_bin = find_browser_binary()
    print(f"Navegador detectado: {browser_bin}")
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    generated_images = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=browser_bin, headless=True)
        # 1080x1350 viewport com scale factor 2 para ultra-nitidez Retina
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
        
        for post in data.get("posts", []):
            post_id = post.get("id")
            post_dir = OUTPUT_DIR / post_id
            post_dir.mkdir(parents=True, exist_ok=True)
            print(f"\nRenderizando carrossel: {post.get('category_name')} ({post_id})")
            
            for idx, slide in enumerate(post.get("slides", []), 1):
                slide_html = generate_slide_html(post, slide, css_content)
                html_path = post_dir / f"slide_{idx:02d}.html"
                png_path = post_dir / f"slide_{idx:02d}.png"
                
                with open(html_path, "w", encoding="utf-8") as hf:
                    hf.write(slide_html)
                    
                page.goto(html_path.resolve().as_uri())
                page.wait_for_load_state("networkidle")
                page.screenshot(path=str(png_path), type="png")
                
                print(f"  [OK] Lâmina {idx:02d} gerada: {png_path.name}")
                generated_images.append(str(png_path))
                
        browser.close()
        
    print(f"\nSucesso total: {len(generated_images)} lâminas geradas com sucesso!")
    return generated_images

if __name__ == "__main__":
    render_all_cards()
