# The Quant Transition Playbook
## Da Academia & Ciência de Dados para o Mercado Financeiro Quantitativo

**Autor:** Lucca Simeoni Pavan, Ph.D.  
*Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação | Doutor em Economia*

---

## 🎯 Objetivo Deste Guia
O objetivo deste playbook é fechar o abismo existente entre o ensino formal (mestrados, doutorados em Economia/Estatística ou bootcamps de Data Science) e a prática diária de uma gestora de recursos sistemática (*asset management* / *hedge fund*).

Aqui você não encontrará teorias abstratas desconectadas do mercado nem promessas vazias de ganhos rápidos. Este material foi desenhado para quem busca:
1. Entender a estrutura real da indústria de gestão quantitativa de recursos;
2. Dominar as boas práticas de modelagem e evitar os vícios que desclassificam candidatos;
3. Construir um portfólio no GitHub que chame a atenção de gestores e heads de risco;
4. Se preparar para os desafios técnicos (*take-home tests*) e entrevistas com gestores.

---

## 📑 Estrutura dos Módulos

* **Módulo 1:** [O Ecossistema Quant e os Modelos de Negócio](01_ecossistema_e_tipos_de_fundos.md)
  * As diferenças práticas entre fundos de Fatores, Arbitragem Estatística, Trend Following e Risk Parity.
  * O papel do Quant Researcher, Quant Developer e Gestor de Risco.
* **Módulo 2:** [Armadilhas Críticas de Modelagem e Backtesting](02_armadilhas_criticas_de_modelagem.md)
  * Os 4 vieses que invalidam um backtest: Look-ahead, Survivorship, Microestrutura e Overfitting.
  * Como estruturar uma validação cruzada para séries temporais financeiras (Purged K-Fold).
* **Módulo 3:** [Guia Prático de Entrevistas & Portfólio GitHub](03_guia_de_entrevistas_e_take_home.md)
  * Perguntas clássicas de probabilidade e econometria em entrevistas de Faria Lima.
  * Como estruturar um teste *take-home* de 48 horas.
* **Módulo 4:** [Templates de Código em Python](templates_codigo/)
  * `backtest_multifator.py`: Pipeline completo de seleção multifatorial e rebalanceamento.
  * `metricas_risco_performance.py`: Motor estatístico de métricas de risco e retornos ajustados.
