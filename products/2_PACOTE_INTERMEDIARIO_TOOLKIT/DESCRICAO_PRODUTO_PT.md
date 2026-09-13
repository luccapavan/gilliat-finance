# The Institutional Quant Toolkit & Playbook (Edição Intermediária)
**Descrição Comercial & Copy de Vendas**  
**Autor:** Lucca Simeoni Pavan, Ph.D. | *Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação*

---

## 🏷️ Dados do Produto
* **Nome do Produto:** The Institutional Quant Toolkit & Playbook: Edição Intermediária (Toolkit com Motores Python)
* **Subtítulo / Tagline:** O dossiê metodológico completo de 13 páginas + checklists anti-vieses + 4 motores vetorizados em Python prontos para rodar em produção.
* **Preço Sugerido:** R$ 47,00 a R$ 97,00 (PIX ou Cartão em até 12x)
* **Formato de Entrega:** Arquivo compactado `2_PACOTE_INTERMEDIARIO_TOOLKIT.zip` (1.46 MB)

---

## ⚡ Descrição Curta (Para Vitrines, Checkout e Redes Sociais)
> Teoria sem código executável não se sustenta em mesas proprietárias e fundos sistemáticos. O **The Institutional Quant Toolkit & Playbook (Edição Intermediária)** entrega o pacote de trabalho prático definitivo: você recebe os 4 documentos essenciais em PDF (Dossiê de 13 páginas e Checklists de Auditoria em Português e Inglês) **MAIS 4 motores em Python 100% vetorizados e documentados** (Backtest Multifator com lag 12-2, Suíte de Risco com CVaR 95%, Ortogonalização FWL e Covariância Robusta de Ledoit-Wolf). Economize semanas de desenvolvimento com código limpo de nível institucional.

---

## 📄 Descrição Completa (Para Página de Vendas / Gumroad / Eduzz)

### A Ponte Entre a Metodologia Institucional e o Código de Produção
No mercado financeiro quantitativo, saber como a teoria funciona é apenas 20% da equação. Os outros 80% residem na capacidade de transformar governança em código de alta performance que não quebre sob atrito real de mercado.

A maioria dos analistas que tenta programar suas próprias estratégias cai em armadilhas de desenvolvimento:
* Códigos lentos cheios de loops iterativos (`for`) que demoram horas para simular um universo modesto de ações;
* Padronizações incorretas de indicadores que contaminam o corte temporal com dados passados ou futuros;
* Ignorância do risco de cauda e otimizações ingênuas de carteira baseadas na matriz amostral de Markowitz que geram carteiras extremas e inviáveis.

A **Edição Intermediária** foi projetada para solucionar esse problema: ela entrega os 4 motores em Python fundamentais para qualquer mesa de ações quantitativas, programados com vetorização pura em NumPy e Pandas, testados e comentados linha a linha.

---

### 📦 O Que Você Irá Receber (`2_PACOTE_INTERMEDIARIO_TOOLKIT.zip`):

#### 1. Dossiês Metodológicos & Checklists em PDF (PT & EN):
* `The_Quant_Transition_Playbook_PT.pdf` (Dossiê conceitual de 13 páginas em português)
* `The_Quant_Transition_Playbook_EN.pdf` (Dossiê conceitual de 13 páginas em inglês)
* `Quant_Anti_Bias_Checklist_PT.pdf` (Checklist de bolso anti-vieses de 2 páginas em português)
* `Quant_Anti_Bias_Checklist_EN.pdf` (Checklist de bolso anti-vieses de 2 páginas em inglês)

#### 2. Os 4 Motores de Produção em Python (`code/`):
* **Engine 1: Backtest Multifatorial Vetorizado (`backtest_multifactor.py`)**
  * Simula uma carteira quantitativa com fatores de Value (Earnings Yield) e Momentum (12-2).
  * Código 100% vetorizado (livre de loops `for`), garantindo velocidade profissional.
  * Normalização transversal (*Cross-Sectional Z-Score*) recalculada a cada corte temporal.
  * Lag estrito de 21 dias para eliminar ruídos de microestrutura e reversão de curto prazo.
  * Dedução realista de custos de corretagem, emolumentos e atrito de giro (*turnover*).
* **Engine 2: Métricas de Risco de Cauda & Performance (`risk_performance_metrics.py`)**
  * Cálculo institucional de **CVaR 95% (Conditional VaR / Expected Shortfall)**, além de VaR paramétrico e histórico.
  * Métricas completas de comitê de investimento: Sharpe Anualizado ponderado pela taxa livre de risco/CDI, Índice de Sortino (*downside deviation*), Drawdown Máximo, Duração de Drawdown e Índice de Calmar.
* **Engine 3: Ortogonalização de Fatores FWL (`factor_orthogonalization_fwl.py`)**
  * Implementação algorítmica do Teorema de Frisch-Waugh-Lovell via projeção matricial QR/OLS.
  * Purifica sinais de investimento: expurga a correlação espúria com betas redundantes de mercado e gera o resíduo puro de alpha com teste t e significância estatística.
* **Engine 4: Covariância Robusta com Encolhimento de Ledoit-Wolf (`ledoit_wolf_covariance.py`)**
  * Elimina a instabilidade numérica da matriz de covariância amostral tradicional.
  * Calcula analiticamente a intensidade ótima de encolhimento (*shrinkage*) em direção a um alvo estruturado, gerando carteiras de variância mínima e tangência matematicamente estáveis.
* **Guia de Execução & Dependências:**
  * `requirements.txt` (NumPy, SciPy, Pandas) e `README_TOOLKIT.md` com explicações de execução e interpretação de saídas.

---

### 🎯 Para Quem é Este Pacote:
* **Candidatos a Vagas Quant:** Tenha uma base de código profissional para apresentar em desafios técnicos (Take-Home tests) e entrevistas de contratação.
* **Analistas & Gestores de Investimento:** Automatize e profissionalize processos de seleção de ativos sistemáticos com padrões de governança institucional.
* **Cientistas de Dados & Programadores:** Economize meses de pesquisa e tentativa-e-erro com algoritmos prontos que já resolvem os maiores desafios de microestrutura financeira.

---

### 👤 Sobre o Autor
**Lucca Simeoni Pavan, Ph.D.**  
Doutor em Economia pela PUCRS com período sanduíche na University of Illinois Urbana-Champaign. Ex-Head de Estratégias Quant e Gerente de Produtos e Alocação no mercado financeiro brasileiro. Liderou a modelagem de estratégias sistemáticas, criação de produtos de investimento e gestão quantitativa de risco.
