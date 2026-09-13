# Como Publicar a Landing Page no Netlify em Menos de 1 Minuto

A pasta `landing_pages/` está 100% autossuficiente e configurada para o Netlify, com redirecionamentos automáticos (`_redirects`) e downloads dos materiais em PDF.

---

### Opção 1: Método Mais Rápido (Netlify Drop - Sem Código nem Git)

1. Acesse: **[https://app.netlify.com/drop](https://app.netlify.com/drop)** (faça login ou crie sua conta gratuita).
2. Abra a pasta do projeto no Windows Explorer:
   `c:\Users\CLIENTE\gilliat-finance\landing_pages`
3. **Arraste e solte a pasta `landing_pages`** diretamente na área pontilhada da tela do Netlify.
4. O Netlify publicará o site instantaneamente e gerará uma URL (ex: `https://heuristic-darwin-123456.netlify.app`).
5. No painel do Netlify, clique em **Site configuration** > **Change site name** e renomeie para:
   👉 `analise-quantitativa` (ficando `https://analise-quantitativa.netlify.app`).

---

### Opção 2: Se o nome do seu site no Netlify for diferente

Se o Netlify gerar uma URL diferente (ex: `https://quant-pavan.netlify.app` ou seu domínio próprio):
1. Abra o arquivo `.env` na raiz do projeto e altere a linha:
   ```bash
   QUANT_COURSE_LP_URL=https://seu-link-real.netlify.app
   ```
2. Execute o script de sincronização instantânea no terminal:
   ```bash
   python publisher/sync_lp_url.py
   ```
   *Em 5 segundos, todos os posts agendados no Buffer serão atualizados automaticamente via API oficial com a nova URL!*
