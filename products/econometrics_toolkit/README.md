# Applied Financial Econometrics Toolkit (Python)
**Biblioteca de Modelos Econométricos & Análise Quantitativa para Finanças**  
*Desenvolvido por Lucca Simeoni Pavan, Ph.D.*

---

## 🎯 O que é este Toolkit?
O **Applied Financial Econometrics Toolkit** é um conjunto de módulos prontos para produção e pesquisa acadêmica, projetado para poupar semanas de desenvolvimento em tarefas essenciais de econometria financeira e gestão quantitativa de portfólios.

Cada script segue os padrões rigorosos de literatura empírica e vem totalmente documentado com formulação matemática e exemplos práticos reproduzíveis.

---

## 📦 Conteúdo dos Módulos

### 1. `modelos_series_temporais.py`
* **Testes de Estacionariedade:** Augmented Dickey-Fuller (ADF) e KPSS com interpretação automática.
* **Modelos Vetoriais Autorregressivos (VAR):** Seleção de defasagem ótima via critérios de informação (AIC, BIC, HQIC).
* **Funções de Impulso-Resposta (IRF) & Decomposição da Variância do Erro de Previsão (FEVD):** Medição do impacto dinâmico de choques entre variáveis macro e financeiras.

### 2. `analise_estilo_sharpe.py`
* **Returns-Based Style Analysis (RBSA):** Algoritmo de William Sharpe para descobrir a exposição real de fundos de investimento a múltiplos fatores ou classes de ativos sem precisar da carteira de ativos aberta.
* **Otimização Quadrática Restrita:** Resolução via `scipy.optimize` garantindo $\sum w_i = 1$ e $w_i \ge 0$ (ou relaxamento para fundos alavancados).
* **Cálculo de R² de Estilo e Tracking Error.**
