/**
 * SCRIPT DE CAPTURA AUTOMÁTICA DE LEADS PARA O GOOGLE SHEETS
 * 
 * Como usar:
 * 1. Abra o Google Sheets (sheets.new) e crie uma planilha vazia chamada "Leads Cursos LinkedIn".
 * 2. No menu superior, clique em: Extensões > Apps Script.
 * 3. Apague tudo o que estiver no editor e cole este código completo.
 * 4. Clique em "Salvar" (ícone de disquete).
 * 5. Clique em "Implantar" (botão azul no canto superior direito) > "Nova implantação".
 * 6. Na engrenagem ao lado de 'Selecionar tipo', escolha: "App da Web".
 * 7. Configure:
 *    - Descrição: "Captura de Leads Landing Pages"
 *    - Executar como: "Eu" (seu e-mail)
 *    - Quem pode acessar: "Qualquer pessoa" (MUITO IMPORTANTE!)
 * 8. Clique em "Implantar" e autorize as permissões de acesso.
 * 9. Copie a "URL do App da Web" gerada (termina em /exec) e cole no seu HTML!
 */

function doPost(e) {
  var lock = LockService.getScriptLock();
  // Espera até 30 segundos para evitar concorrência se vários leads entrarem juntos
  lock.waitLock(30000);

  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getActiveSheet();
    
    // Converte os dados recebidos da Landing Page
    var data = {};
    if (e && e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (err) {
        data = e.parameter;
      }
    } else if (e && e.parameter) {
      data = e.parameter;
    }

    // Se a planilha estiver vazia, cria automaticamente o cabeçalho formatado
    if (sheet.getLastRow() === 0) {
      var headers = [
        "Data e Hora", 
        "Curso de Interesse", 
        "Nome do Aluno", 
        "E-mail", 
        "WhatsApp", 
        "Atuação / Cargo", 
        "Detalhe (Nível Python / Custódia)", 
        "Melhor Horário Escolhido", 
        "Desconto",
        "Status"
      ];
      sheet.appendRow(headers);

      // Estilização do cabeçalho
      var headerRange = sheet.getRange(1, 1, 1, headers.length);
      headerRange.setFontWeight("bold");
      headerRange.setBackground("#0f172a");
      headerRange.setFontColor("#f8fafc");
      headerRange.setHorizontalAlignment("center");
      sheet.setFrozenRows(1);
    }

    // Prepara a nova linha com a data atual no horário de Brasília
    var dataHora = Utilities.formatDate(new Date(), "America/Sao_Paulo", "dd/MM/yyyy HH:mm:ss");
    var detalhe = data.python_level || data.aum || "Não informado";

    var newRow = [
      dataHora,
      data.course || "Não especificado",
      data.name || "",
      data.email || "",
      data.phone || "",
      data.role || "",
      detalhe,
      data.availability || "Não informado",
      "20% OFF Garantido",
      "Lead Qualificado (Lista VIP)"
    ];

    sheet.appendRow(newRow);

    // Ajusta o alinhamento
    sheet.autoResizeColumns(1, 10);

    return ContentService.createTextOutput(JSON.stringify({ 
      status: "success", 
      message: "Lead registrado com sucesso na planilha!" 
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ 
      status: "error", 
      message: error.toString() 
    })).setMimeType(ContentService.MimeType.JSON);

  } finally {
    lock.releaseLock();
  }
}

// Suporte para teste rápido via navegador (GET)
function doGet(e) {
  return ContentService.createTextOutput(JSON.stringify({
    status: "online",
    message: "O Webhook do Google Sheets para as Landing Pages está ativo e funcionando perfeitamente!"
  })).setMimeType(ContentService.MimeType.JSON);
}
