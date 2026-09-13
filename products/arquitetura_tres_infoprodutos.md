# Arquitetura dos 3 Pacotes ZIP (Tiers de Produto)

**Autor:** Lucca Simeoni Pavan, Ph.D.  
*Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação*

---

## 🎯 Estratégia de Empacotamento em 3 Níveis

Para atender a diferentes perfis de clientes e poder de compra (desde estudantes e pesquisadores até profissionais que buscam repositórios prontos para produção), o produto foi dividido em **3 pacotes ZIP independentes**:

```
products/
├── quant_transition_playbook_tier1_pdfs.zip      (1.45 MB) -> Versão Entrada (Apenas PDFs)
├── quant_transition_playbook_tier2_toolkit.zip   (1.46 MB) -> Versão Intermediária (ZIP Atual com 4 Motores)
└── quant_transition_playbook_tier3_plus.zip      (1.47 MB) -> Versão Plus (Completa com Econometrics Toolkit)
```

---

## 🪜 Tabela Comparativa dos 3 Tiers

| Característica / Entregável | Tier 1 (Mais Barato / PDFs) | Tier 2 (Intermediário / Toolkit) | Tier 3 (Versão Plus / All-in-One) |
| :--- | :---: | :---: | :---: |
| **Arquivo ZIP Entregue** | `quant_transition_playbook_tier1_pdfs.zip` | `quant_transition_playbook_tier2_toolkit.zip` | `quant_transition_playbook_tier3_plus.zip` |
| **Preço Sugerido (BRL)** | **R$ 5,99 a R$ 19,90** | **R$ 47,00 a R$ 97,00** | **R$ 97,00 a R$ 147,00** |
| **Preço Sugerido (USD)** | **$5.99** | **$19.00** | **$27.00 - $37.00** |
| **Playbook PT (13 pág.)** | ✅ | ✅ | ✅ |
| **Playbook EN (13 pág.)** | ✅ | ✅ | ✅ |
| **Checklist Anti-Bias PT** | ✅ | ✅ | ✅ |
| **Checklist Anti-Bias EN** | ✅ | ✅ | ✅ |
| **Engine Backtest Multifator** | ❌ | ✅ | ✅ |
| **Engine Risco & CVaR 95%** | ❌ | ✅ | ✅ |
| **Engine Ortogonalização FWL**| ❌ | ✅ | ✅ |
| **Engine Covariância Ledoit-Wolf**| ❌ | ✅ | ✅ |
| **Econometria: RBSA Estilo Sharpe**| ❌ | ❌ | ✅ |
| **Econometria: Séries Temporais / VAR**| ❌ | ❌ | ✅ |

---

## 📦 Conteúdo Interno de Cada Arquivo ZIP

### 1. Tier 1: `quant_transition_playbook_tier1_pdfs.zip` (Mais Barata)
* **Objetivo:** Para quem quer dominar os conceitos, a metodologia institucional e os protocolos anti-vieses sem precisar de código-fonte em Python imediato.
* **Conteúdo:**
  - `The_Quant_Transition_Playbook_PT.pdf` (Dossiê conceitual de 13 páginas em português)
  - `The_Quant_Transition_Playbook_EN.pdf` (Dossiê conceitual de 13 páginas em inglês)
  - `Quant_Anti_Bias_Checklist_PT.pdf` (Checklist executivo de 2 páginas em português)
  - `Quant_Anti_Bias_Checklist_EN.pdf` (Checklist executivo de 2 páginas em inglês)

---

### 2. Tier 2: `quant_transition_playbook_tier2_toolkit.zip` (Intermediária / ZIP Atual)
* **Objetivo:** O pacote de trabalho completo para quem vai codificar estratégias sistemáticas de ações e submeter testes em processos seletivos.
* **Conteúdo:**
  - *Todos os 4 PDFs do Tier 1*
  - 📁 `code/`
    - `backtest_multifactor.py` (Engine completa com lag 12-2, z-score transversal e turnover)
    - `risk_performance_metrics.py` (Métricas de cauda CVaR 95%, VaR, Sortino e Sharpe)
    - `factor_orthogonalization_fwl.py` (Decomposição matricial FWL para purificar alpha)
    - `ledoit_wolf_covariance.py` (Encolhimento analítico de covariância vs erro de Markowitz)
    - `requirements.txt` (Dependências testadas)
    - `README_TOOLKIT.md` (Manual completo de execução de cada script)

*(Nota: O arquivo `quant_transition_playbook_v1.zip` é mantido idêntico a este para total compatibilidade com os links já gerados).*

---

### 3. Tier 3: `quant_transition_playbook_tier3_plus.zip` (Versão Plus)
* **Objetivo:** O toolkit mais abrangente, unindo a esteira de Factor Investing e a suíte completa de Econometria Financeira Avançada para modelagem macro, análise de fundos de terceiros e séries multivariadas.
* **Conteúdo:**
  - *Todos os 4 PDFs do Tier 1*
  - *Todos os 4 Motores Quant em Python do Tier 2*
  - 📁 `econometrics_toolkit/`
    - `analise_estilo_sharpe.py` (Returns-Based Style Analysis - RBSA de William Sharpe via otimização quadrática restrita no scipy)
    - `modelos_series_temporais.py` (Vetor Autorregressivo VAR multivariado, critérios AIC/BIC e matriz residual)
    - `README.md` (Documentação teórica e prática em português)
    - `README_EN.md` (Documentação teórica e prática em inglês)

---

## ⚡ Estrutura de Upsell & Order Bump Recomendada

No checkout da Eduzz ou do Gumroad:
1. **Comprador escolhe o Tier 1 (PDFs por R$ 5,99 ou R$ 9,90):**
   - **Order Bump 1:** *"Adicionar os 4 Motores em Python prontos para rodar por apenas +R$ 67,00?"* -> Entrega o **Tier 2**.
   - **Order Bump 2 (Upsell):** *"Levar a suíte completa com os módulos de Econometria Financeira (VAR + Análise de Estilo de Sharpe) por apenas +R$ 87,00?"* -> Entrega o **Tier 3 Plus**.
