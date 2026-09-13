# Guia de Nivelamento Técnico: Python e Matemática Financeira para Análise Quantitativa

**Material Exclusivo para Inscritos na Lista de Espera VIP**  
**Autor:** Lucca Simeoni Pavan, Ph.D.  
*Ex-Head de Estratégias Quant & Gerente de Produtos e Alocação*

---

## 🎯 Objetivo Deste Guia
Seja muito bem-vindo! Este material foi estruturado para garantir que você inicie o **Curso de Análise Quantitativa Aplicada** com as fundações certas. 

Aqui você vai dominar os conceitos matemáticos, estatísticos e de manipulação de dados em Python que separam amadores que usam planilhas manuais dos profissionais que atuam no mercado financeiro institucional.

---

## 1. Configuração do Ambiente de Trabalho

Para trabalhar como um analista quantitativo sério, recomendamos a seguinte pilha de ferramentas:
1. **Python 3.10 ou 3.11:** Versões mais estáveis para bibliotecas científicas.
2. **VS Code com extensão Jupyter:** Ideal para prototipagem rápida e desenvolvimento modular.
3. **Ambiente Virtual Dedicado:**
   ```bash
   python -m venv venv_quant
   # No Windows (PowerShell):
   .\venv_quant\Scripts\Activate.ps1
   ```
4. **Instalação dos pacotes essenciais:**
   ```bash
   pip install numpy pandas matplotlib seaborn scipy statsmodels yfinance
   ```

---

## 2. A Matemática dos Retornos Financeiros

Um dos erros mais comuns de quem migra de ciência de dados geral para finanças quantitativas é calcular e agregar retornos de forma equivocada.

### 2.1 Retorno Simples (Aritmético)
Representa o ganho percentual entre o instante $t-1$ e $t$:
$$R_t = \frac{P_t - P_{t-1}}{P_{t-1}} = \frac{P_t}{P_{t-1}} - 1$$

* **Propriedade fundamental:** Retornos simples se somam **entre ativos no espaço** (cross-section). Se você tem uma carteira com 50% no ativo A e 50% no ativo B, o retorno da carteira é a média ponderada dos retornos simples:
$$R_{p, t} = w_A R_{A, t} + w_B R_{B, t}$$

### 2.2 Retorno Logarítmico (Composto Continuamente)
Definido como a variação do logaritmo natural dos preços:
$$r_t = \ln\left(\frac{P_t}{P_{t-1}}\right) = \ln(P_t) - \ln(P_{t-1})$$

* **Propriedade fundamental:** Retornos logarítmicos se somam **ao longo do tempo** (série temporal). O retorno composto de 1 ano é simplesmente a soma dos retornos diários em log:
$$r_{total} = \sum_{t=1}^{T} r_t$$

> **Regra de Ouro do Quant:**  
> • Use **retornos simples** quando for calcular o valor monetário ou a agregação de uma carteira de múltiplos ativos.  
> • Use **log-retornos** quando estiver modelando séries temporais, distribuições estatísticas, volatilidade e testes econométricos.

---

## 3. Métricas Essenciais de Desempenho e Risco

### 3.1 Anualização de Métricas (Convenção Brasil: 252 dias úteis)
No Brasil, ativos de mercado de capitais e juros operam sob a base de 252 dias úteis:
* **Retorno Médio Anualizado:**
$$\bar{R}_{anual} = (1 + \bar{R}_{diário})^{252} - 1 \quad \text{ou} \quad \bar{r}_{anual} = \bar{r}_{diário} \times 252$$
* **Volatilidade Anualizada (Desvio-Padrão):**
$$\sigma_{anual} = \sigma_{diária} \times \sqrt{252}$$

### 3.2 Sharpe Ratio
Mede o retorno excedente por unidade de volatilidade total:
$$\text{Sharpe} = \frac{\bar{R}_p - R_f}{\sigma_p}$$
*(Onde $R_f$ é o ativo livre de risco, geralmente o CDI anualizado no Brasil).*

### 3.3 Sortino Ratio (Foco no Risco Ruim)
A volatilidade comum penaliza oscilações para cima da mesma forma que para baixo. O Sortino avalia apenas o desvio-padrão dos retornos negativos (*Downside Deviation*):
$$\text{Sortino} = \frac{\bar{R}_p - R_f}{\sigma_{down}}$$
$$\sigma_{down} = \sqrt{\frac{1}{N} \sum_{t=1}^{N} \min(0, R_t - R_f)^2}$$

### 3.4 Maximum Drawdown (MDD)
Mede a perda máxima desde o pico mais alto até o vale subsequente:
$$DD_t = \frac{P_t - \max_{\tau \le t} (P_\tau)}{\max_{\tau \le t} (P_\tau)}$$
$$MDD = \min_t (DD_t)$$

---

## 4. Código Prático: Seu Primeiro Script de Análise Quantitativa

Copie e execute o código abaixo no seu VS Code ou Jupyter Notebook. Ele baixa ações da B3, higieniza a base, calcula métricas de risco e exporta uma análise comparativa:

```python
import numpy as np
import pandas as pd
import yfinance as yf

# 1. Definição do Universo de Ativos (Tickers B3 com sufixo .SA)
tickers = ['ITUB4.SA', 'VALE3.SA', 'PETR4.SA', 'WEGE3.SA', '^BVSP']
start_date = '2021-01-01'
end_date = '2026-01-01'

print("📥 Baixando cotações históricas da B3...")
data = yf.download(tickers, start=start_date, end=end_date, progress=False)

# 2. Utilizar 'Adj Close' (Preço ajustado por dividendos e desdobramentos)
prices = data['Adj Close'].dropna()

# 3. Cálculo dos Retornos Diários Simples
returns = prices.pct_change().dropna()

# 4. Cálculo das Métricas Anualizadas (252 dias úteis)
def calcular_metricas(ret_series, rf_anual=0.105):
    rf_diario = (1 + rf_anual) ** (1 / 252) - 1
    retorno_anual = (1 + ret_series.mean()) ** 252 - 1
    vol_anual = ret_series.std() * np.sqrt(252)
    
    # Sharpe Ratio
    sharpe = (retorno_anual - rf_anual) / vol_anual if vol_anual > 0 else 0
    
    # Sortino Ratio
    ret_excesso = ret_series - rf_diario
    downside = ret_excesso[ret_excesso < 0].std() * np.sqrt(252)
    sortino = (retorno_anual - rf_anual) / downside if downside > 0 else 0
    
    # Maximum Drawdown (MDD)
    cum_returns = (1 + ret_series).cumprod()
    peak = cum_returns.cummax()
    drawdown = (cum_returns - peak) / peak
    mdd = drawdown.min()
    
    return pd.Series({
        'Retorno Anualizado': f"{retorno_anual * 100:.2f}%",
        'Volatilidade Anual': f"{vol_anual * 100:.2f}%",
        'Sharpe Ratio': f"{sharpe:.2f}",
        'Sortino Ratio': f"{sortino:.2f}",
        'Max Drawdown': f"{mdd * 100:.2f}%"
    })

tabela_metricas = returns.apply(calcular_metricas)

print("\n" + "=" * 65)
print("📊 SCORECARD INSTITUCIONAL DE DESEMPENHO E RISCO")
print("=" * 65)
print(tabela_metricas.to_string())

# 5. Matriz de Correlação entre os Ativos
corr_matrix = returns.corr()
print("\n🔗 Matriz de Correlação entre Ativos:")
print(np.round(corr_matrix, 2).to_string())
```

---

## 5. Mini-Desafio de Nivelamento
Antes de iniciar a 1ª aula do curso, tente realizar este exercício prático:
1. Adicione mais dois ativos da B3 de setores diferentes (ex: `RENT3.SA` e `RADL3.SA`).
2. Crie uma carteira hipotética igualmente ponderada ($w_i = \frac{1}{N}$).
3. Calcule o Sharpe e o Maximum Drawdown dessa carteira combinada e compare com o Ibovespa (`^BVSP`).
4. *Pergunta reflexiva:* A volatilidade da carteira foi menor do que a média das volatilidades individuais dos ativos? Por que isso acontece matematicamente?

---

> 💡 **Parabéns por dar o primeiro passo!** Guarde este material com carinho. Durante o curso, nós vamos expandir este ferramental para a criação de fatores sistemáticos avançados, backtests com fricções reais de mercado e algoritmos de paridade de risco.
