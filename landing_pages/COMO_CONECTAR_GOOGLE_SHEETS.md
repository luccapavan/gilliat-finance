# Como Conectar as Landing Pages ao seu Google Sheets (Passo a Passo)

Este guia mostra como conectar os formulários das landing pages diretamente a uma planilha do seu Google Drive em **menos de 3 minutos**, de forma 100% gratuita e sem precisar de servidor.

---

### Passo 1: Criar a Planilha no Google Drive
1. Acesse **[sheets.new](https://sheets.new)** no seu navegador (isso abrirá uma nova planilha do Google).
2. Dê um nome para a planilha no topo esquerdo, por exemplo: `Leads Cursos LinkedIn`.
3. Não precisa digitar nada nas células; o script cria o cabeçalho formatado automaticamente!

---

### Passo 2: Adicionar o Código do Apps Script
1. No menu superior da planilha, clique em: **Extensões** > **Apps Script**.
2. Uma nova aba será aberta com um editor de código.
3. Apague qualquer texto que estiver lá (como `function myFunction() { ... }`).
4. Abra o arquivo **`landing_pages/google_sheets_code.js`** do seu projeto, copie todo o conteúdo e cole dentro do editor do Google.
5. Clique no ícone de **Salvar** (o disquete) ou pressione `Ctrl + S`.

---

### Passo 3: Publicar o Webhook (Implantar)
1. No canto superior direito da tela do Apps Script, clique no botão azul **Implantar** (Deploy) e selecione **Nova implantação**.
2. Na janela que abrir, clique na **engrenagem** ao lado de "Selecionar tipo" e escolha **App da Web**.
3. Preencha as configurações exatamente assim:
   * **Descrição:** `Captura de Leads Landing Pages`
   * **Executar como:** `Eu (seu e-mail)`
   * **Quem pode acessar:** `Qualquer pessoa` *(MUITO IMPORTANTE: se deixar restrito, o formulário da página não conseguirá enviar).*
4. Clique no botão azul **Implantar**.
5. Se o Google solicitar "Autorizar acesso", clique na sua conta, depois em *Avançado* e em *Acessar (não seguro)* para permitir.
6. Copie a **URL do App da Web** que será exibida (ela termina com `/exec`).  
   Exemplo: `https://script.google.com/macros/s/AKfycbx.../exec`

---

### Passo 4: Colar a URL nas Landing Pages
Abra os arquivos das landing pages e substitua a variável `GOOGLE_SHEETS_WEBHOOK_URL` pela sua URL copiada:

1. No arquivo `landing_pages/analise_quantitativa.html`:
   Procure por:
   ```javascript
   const GOOGLE_SHEETS_WEBHOOK_URL = ""; // Cole sua URL aqui
   ```
   E substitua por:
   ```javascript
   const GOOGLE_SHEETS_WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbx.../exec";
   ```

2. Faça o mesmo no arquivo `landing_pages/macro_assessores.html`.

---

### ✅ Pronto! O que acontece agora:
* Toda vez que alguém no LinkedIn preencher qualquer uma das landing pages (seja no celular ou no computador), uma **nova linha aparece em tempo real** no seu Google Sheets.
* Os campos registrados serão:
  1. **Data e Hora** (Horário de Brasília)
  2. **Curso de Interesse** (Análise Quantitativa ou Assessores)
  3. **Nome do Aluno**
  4. **E-mail**
  5. **WhatsApp**
  6. **Atuação / Cargo**
  7. **Nível em Python ou Perfil de Custódia**
  8. **Melhor Horário Escolhido**
  9. **Desconto (20% OFF Garantido)**
  10. **Status do Lead**
