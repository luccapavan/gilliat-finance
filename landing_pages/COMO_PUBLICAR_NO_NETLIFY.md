# Como Publicar as Landing Pages no Netlify

A estrutura das Landing Pages está totalmente configurada e compatível com o Netlify, contando com:
* `netlify.toml` na raiz do repositório (direcionamento automático para a pasta `landing_pages`);
* Redirecionamentos oficiais configurados em `_redirects` (`/` -> `analise_quantitativa.html`, `/macro` -> `macro_assessores.html`, `/portal` -> `index.html`, `/kit` e `/ementa` -> PDF do Kit);
* Cabeçalhos de segurança e cache otimizados para PDFs e assets;
* Script de deploy automatizado via Python (`publisher/deploy_netlify.py`).

---

## 🚀 Método 1: Integração Contínua com GitHub (Recomendado)

Como o repositório já está conectado ao GitHub (`luccapavan/gilliat-finance`):
1. Acesse o painel do [Netlify](https://app.netlify.com).
2. Clique em **Add new site** > **Import an existing project** > **GitHub**.
3. Selecione o repositório `luccapavan/gilliat-finance`.
4. As configurações de build serão preenchidas automaticamente pelo `netlify.toml` (`publish = landing_pages`).
5. Clique em **Deploy site**.
6. A cada `git push` no repositório, o Netlify atualizará a Landing Page automaticamente.

---

## ⚡ Método 2: Netlify Drop (Deploy Instantâneo em 10 Segundos - Sem Git)

1. Acesse: **[https://app.netlify.com/drop](https://app.netlify.com/drop)**.
2. Abra a pasta do projeto no Windows Explorer:
   `c:\Users\CLIENTE\gilliat-finance`
3. Arraste e solte o arquivo **`landing_pages.zip`** (ou a pasta **`landing_pages`**) na tela do Netlify.
4. O site estará no ar imediatamente com HTTPS!
5. No painel do Netlify, clique em **Site configuration** > **Change site name** e defina o nome (ex: `analise-quantitativa`).

---

## 💻 Método 3: Deploy Direto via Terminal (Python REST API)

Se você preferir rodar tudo direto pelo terminal:
1. Obtenha um Personal Access Token no Netlify: **User Settings > Applications > Personal Access Tokens**.
2. Adicione no seu arquivo `.env`:
   ```env
   NETLIFY_AUTH_TOKEN=seu_token_aqui
   ```
3. Execute no terminal:
   ```bash
   python publisher/deploy_netlify.py --sync
   ```
   *O script publica o site, captura a URL oficial gerada e já sincroniza todos os posts agendados no Buffer!*

---

## 🔄 Sincronização dos Links no Buffer

Sempre que alterar o domínio ou nome do site no Netlify:
1. Atualize a linha `QUANT_COURSE_LP_URL` no `.env`.
2. Rode no terminal:
   ```bash
   python publisher/sync_lp_url.py
   ```
   *Todos os posts agendados no LinkedIn via Buffer serão atualizados instantaneamente.*

