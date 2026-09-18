# Grade Curricular e Conteúdo Programático dos Cursos

**Instrutor:** Lucca Simeoni Pavan, Ph.D.  
*Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação • Doutor em Economia*

---

# CURSO 1: Análise Quantitativa Aplicada
### *Modelagem Sistemática, Factor Investing e Gestão de Risco em Python*

* **Objetivo Geral:** Capacitar analistas, economistas e cientistas de dados a estruturarem pipelines quantitativos completos, desde a coleta e tratamento de dados da B3 até o backtesting sem vieses e a alocação robusta de portfólios sistemáticos.
* **Carga Horária Estimada:** 30 horas (Aulas ao vivo/gravadas + Projetos Práticos de Programação).
* **Stack Tecnológica:** Python (Pandas, NumPy, Statsmodels, Scipy, Matplotlib/Seaborn, yfinance, python-bcb).

---

### Módulo 1: Infraestrutura de Dados e Engenharia Financeira em Python
* **Aula 1.1:** Arquitetura do pipeline quant: estruturas de dados para séries temporais financeiras (DataFrames multidimensionais, multi-index e painéis).
* **Aula 1.2:** Conexão com fontes institucionais: APIs do Banco Central do Brasil (SGS), CVM (informes diários de fundos) e cotações de mercado.
* **Aula 1.3:** Tratamento crítico de dados da B3: ajuste ex-dividendos, bonificações, agrupamentos, splits e padronização de datas úteis (calendário ANBIMA).
* **Aula 1.4:** O perigo invisível: como identificar e neutralizar o viés de sobrevivência (*survivorship bias*) e o viés de antecipação (*look-ahead bias*).
* **Laboratório Prático:** Construção de uma base de dados limpa com os últimos 10 anos de negociação das ações do IBrX-100.

---

### Módulo 2: Estatística de Retornos e Métricas Institucionais de Risco
* **Aula 2.1:** Retornos simples vs. log-retornos: propriedades matemáticas e quando utilizar cada um na modelagem.
* **Aula 2.2:** Distribuições empíricas de ativos financeiros: não-normalidade, caudas pesadas (*fat tails*), assimetria (*skewness*) e curtose excessiva.
* **Aula 2.3:** Métricas de performance além do Sharpe: Ratio de Sortino, Ratio de Calmar e Information Ratio.
* **Aula 2.4:** Dinâmica de rebaixamento: cálculo analítico do *Maximum Drawdown* (MDD), duração de drawdown e tempo de recuperação.
* **Aula 2.5:** Modelos de Risco de Cauda: Value at Risk (VaR Histórico e Paramétrico) e Conditional VaR (Expected Shortfall / CVaR).
* **Laboratório Prático:** Desenvolvimento de um módulo automatizado que recebe qualquer série de preços e cospe um *Risk Tear Sheet* institucional.

---

### Módulo 3: Factor Investing e Modelagem Multifatorial no Brasil
* **Aula 3.1:** A evolução das teorias de apreçamento: do CAPM aos modelos multifatoriais de Fama-French e Carhart.
* **Aula 3.2:** Fator de Momentum na B3: diferenças teóricas e práticas entre *Cross-Sectional Momentum* (vencedores vs. perdedores) e *Time-Series Momentum* (seguimento de tendência).
* **Aula 3.3:** Fatores Fundamentistas: Valor (P/L, EV/EBITDA, Book-to-Market) e Qualidade (ROE, ROIC, Margem Líquida, Dívida Líquida/EBITDA).
* **Aula 3.4:** Fatores de Risco: Baixa Volatilidade (*Low Vol*) e Tamanho (*Size / Small Caps*).
* **Aula 3.5:** O problema do *Factor Zoo*: testes de significância t-stat, correção de Bonferroni e validação fora da amostra (*Out-of-Sample*).
* **Laboratório Prático:** Criação de um ranking multifatorial com scores padronizados (Z-Score) para seleção sistemática de carteiras na bolsa brasileira.

---

### Módulo 4: Framework de Backtesting Institucional Realista
* **Aula 4.1:** Arquiteturas de Backtest: Vectorizado (rápido para prototipagem) vs. Orientado a Eventos (preciso para execução).
* **Aula 4.2:** Modelagem de atritos de mercado: custos de corretagem, emolumentos B3, taxa de liquidação e imposto sobre proventos.
* **Aula 4.3:** Modelagem de *Slippage* e Impacto de Mercado: restrições de liquidez com base no volume financeiro médio diário (ADTV).
* **Aula 4.4:** Rebalanceamento periódico: frequências ótimas (semanal, mensal, trimestral), bandas de tolerância (*turnover*) e custos de rotação.
* **Aula 4.5:** Walk-Forward Analysis e Validação Cruzada Purificada (Purged Cross-Validation para séries temporais).
* **Laboratório Prático:** Execução do backtest de 5 anos de uma carteira de Fatores na B3 com relatório completo de custos e curva de capital auditável.

---

### Módulo 5: Otimização de Portfólios e Alocação de Risco
* **Aula 5.1:** Otimização de Média-Variância de Markowitz: limites práticos e a extrema sensibilidade a erros de estimativa.
* **Aula 5.2:** Regularização de matrizes de covariância: método Ledoit-Wolf Shrinkage e filtragem de ruído por Random Matrix Theory (RMT).
* **Aula 5.3:** Paridade de Risco (*Risk Parity*) e Contribuição Marginal de Risco: garantindo que ativos mais voláteis não dominem o portfólio.
* **Aula 5.4:** *Hierarchical Risk Parity* (HRP): como usar aprendizado não-supervisionado (clusterização hierárquica) para alocar sem necessidade de inversão de matriz.
* **Laboratório Prático:** Comparação empírica de performance: Carteira 1/N vs. Média-Variância vs. HRP com ativos brasileiros e globais.

---

### Módulo 6: Projeto Final e Produção Quant
* **Aula 6.1:** Estruturação de projetos em Python: boas práticas de código, modularização e reprodutibilidade.
* **Aula 6.2:** Geração de relatórios executivos em HTML/PDF com gráficos interativos.
* **Projeto Final de Conclusão:** Desenvolvimento de uma estratégia quantitativa proprietária completa (extração -> cálculo de fatores -> backtest com atritos -> otimização de pesos -> relatório final de risco).

---
---

# CURSO 2: Análise Econômica e de Investimentos para Assessores
### *Macro Advisory, Leitura de Mercados e Asset Allocation Estratégico*

* **Objetivo Geral:** Capacitar assessores de investimentos (AAIs), consultores CVM, bankers e planejadores financeiros a dominarem a macroeconomia prática, traduzindo dados e movimentos de juros em estratégias de alocação de ativos e conversas comerciais de alta autoridade com clientes qualificados.
* **Carga Horária Estimada:** 24 horas (Aulas ao vivo/gravadas + Estudos de Caso de Reunião com Clientes).
* **Ferramentas Utilizadas:** Plataformas de mercado, planilhas gerenciais de alocação, relatórios do Banco Central, curvas de DI e frameworks de recomendação.

---

### Módulo 1: Decodificando a Macroeconomia Brasileira Sem Ruídos
* **Aula 1.1:** O funcionamento da política monetária: o Comitê de Política Monetária (Copom), o regime de metas de inflação e o mecanismo de transmissão da Selic.
* **Aula 1.2:** Como ler o Boletim Focus como um profissional: mediana vs. média, expectativas ancoradas, horizonte relevante e quando o consenso está errado.
* **Aula 1.3:** Inflação na veia: componentes do IPCA (preços livres vs. administrados, inflação de serviços, núcleos e inércia inflacionária).
* **Aula 1.4:** Política Fiscal e Risco Soberano: dívida/PIB, superávit primário, arcabouço fiscal e como o humor do investidor institucional reage às contas públicas.
* **Estudo de Caso Prático:** Análise em tempo real de uma Ata do Copom: o que sublinhar e como formular um resumo executivo de 5 linhas para a sua base de clientes.

---

### Módulo 2: O Coração do Mercado: A Curva de Juros (DI Futuro)
* **Aula 2.1:** A estrutura a termo da taxa de juros (ETTF): vértices curtos, intermediários e longos no mercado futuro da B3.
* **Aula 2.2:** O que mexe na inclinação da curva: achatamento (*flattening*), empinamento (*steepening*), prêmios de liquidez e prêmios fiscais.
* **Aula 2.3:** Marcação a Mercado desmistificada: por que títulos prefixados e indexados à inflação (Tesouro IPCA+) oscilam violentamente e como transformar isso em oportunidade.
* **Aula 2.4:** Inflação Implícita (*Breakeven Inflation*): como calcular a expectativa de inflação embutida nas NTN-Bs e decidir entre papel pós, pré ou IPCA+.
* **Aula 2.5:** O mercado de Crédito Privado: spreads de debêntures incentivadas, CRIs e CRAs; duration e risco de crédito vs. risco soberano.
* **Estudo de Caso Prático:** Como proteger e reestruturar a carteira de renda fixa de um cliente antes de uma virada de ciclo de juros.

---

### Módulo 3: O Tabuleiro Internacional (Macro Global & Offshore)
* **Aula 3.1:** O banco central do mundo: Federal Reserve (Fed), a taxa Fed Funds e o ciclo de liquidez internacional.
* **Aula 3.2:** *Treasuries* americanas: por que o rendimento do título de 10 anos dos EUA dita o ritmo dos mercados globais e emergentes.
* **Aula 3.3:** O Índice Dólar (DXY) e o Câmbio no Brasil: diferenciais de juros (carry trade), termos de troca, risco-país (CDS) e volatilidade cambial.
* **Aula 3.4:** Ciclos de Commodities e a Economia Chinesa: minério de ferro, petróleo e agronegócio; como o comércio global afeta as empresas brasileiras.
* **Estudo de Caso Prático:** Como estruturar e justificar uma alocação internacional defensiva para um cliente conservador avesso a risco cambial.

---

### Módulo 4: Engenharia de Asset Allocation para Clientes Qualificados
* **Aula 4.1:** Fundamentos de Alocação de Ativos: classes de ativos, correlações dinâmicas e o mito da diversificação ingênua.
* **Aula 4.2:** O Portfólio para Todos os Cenários (*All-Weather Portfolio* adaptado à realidade de juros altos do Brasil).
* **Aula 4.3:** Matriz de Decisão Tática: alocação por quadrante econômico (Crescimento Acelerado / Desaceleração / Inflação Alta / Desinflação).
* **Aula 4.4:** Estruturação de carteiras por objetivos de vida: caixa de liquidez imediata, preservação de capital com ganho real e motor de valorização.
* **Aula 4.5:** Rebalanceamento Disciplinado: quando realizar lucros, quando rebalancear por bandas e como evitar que o cliente venda no fundo.
* **Estudo de Caso Prático:** Montagem completa de uma carteira de alocação macro de R$ 5 milhões para uma família empresária.

---

### Módulo 5: Storytelling Econômico e Comunicação Comercial de Alto Nível
* **Aula 5.1:** Do economês à narrativa convincente: como explicar conceitos complexos sem soar arrogante nem simplista demais.
* **Aula 5.2:** O Roteiro da Reunião de Alocação (20 a 30 minutos):
  1. Leitura de Cenário em 5 minutos;
  2. Diagnóstico das vulnerabilidades da carteira atual do cliente;
  3. A tese macroestratégica proposta;
  4. O plano de ação e cronograma de aportes.
* **Aula 5.3:** Protocolo de Crise e Volatilidade: scripts exatos de comunicação proativa em dias de estresse agudo de mercado (eleições, eventos fiscais, quedas globais).
* **Aula 5.4:** Como abordar empresários, founders e profissionais liberais com teses macro que geram novos aportes.
* **Simulação Prática:** Roleplay de reunião de revisão de carteira com objeções reais de clientes receosos.

---

### Módulo 6: Workshop de Alocação e Mentoria de Casos Reais
* **Aula 6.1:** Análise e consultoria ao vivo de carteiras reais trazidas pelos alunos (com dados anonimizados).
* **Aula 6.2:** Montagem do próprio *Macro Scorecard Mensal* do assessor para envio exclusivo à sua base de relacionamento.
* **Projeto de Conclusão:** Elaboração de uma Proposta de Alocação Macroeconômica completa com tese de investimento pronta para apresentação a um cliente qualificado.
