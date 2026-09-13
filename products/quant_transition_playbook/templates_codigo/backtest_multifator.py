"""
Template de Código: Backtest de Estratégia Multifatorial (Value + Momentum)
Parte integrante de: The Quant Transition Playbook (por Lucca Simeoni Pavan, Ph.D.)
"""

import numpy as np
import pandas as pd

def compute_z_score(df: pd.DataFrame) -> pd.DataFrame:
    """Padroniza os fatores em cada período de corte transversal (Cross-Sectional Z-Score)."""
    return df.sub(df.mean(axis=1), axis=0).div(df.std(axis=1), axis=0)

def simulate_multifactor_strategy(
    prices: pd.DataFrame,
    pe_ratios: pd.DataFrame,
    rebalance_freq: str = "M",
    top_n: int = 5,
    transaction_cost: float = 0.0015
) -> pd.DataFrame:
    """
    Executa um backtest vetorial de carteira multifator (Value + Momentum).
    
    Parâmetros:
    - prices: DataFrame de preços diários ajustados (ações nas colunas, datas no índice)
    - pe_ratios: DataFrame de múltiplos Preço/Lucro
    - rebalance_freq: Frequência de rebalanceamento ('M' = mensal)
    - top_n: Quantidade de ativos no quintil superior
    - transaction_cost: Custo por operação (15 bps por padrão)
    """
    returns = prices.pct_change()
    
    # 1. Fator Momentum: Retorno de 12 meses excluindo o mês mais recente (t-12 até t-2)
    momentum_factor = prices.shift(21) / prices.shift(252) - 1
    
    # 2. Fator Value: Inverso do P/L (Earnings Yield: E/P)
    value_factor = 1.0 / pe_ratios.replace(0, np.nan)
    
    # Padronização por Z-Score
    z_mom = compute_z_score(momentum_factor)
    z_val = compute_z_score(value_factor)
    
    # Score Composto: 50% Momentum + 50% Value
    composite_score = 0.5 * z_mom + 0.5 * z_val
    
    # Identificação das datas de rebalanceamento
    rebalance_dates = prices.resample(rebalance_freq).last().index
    
    portfolio_weights = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)
    
    # Definição de pesos a cada data de rebalanceamento
    for date in rebalance_dates:
        if date in composite_score.index:
            scores_on_date = composite_score.loc[date].dropna()
            if len(scores_on_date) >= top_n:
                # Seleciona as top_n melhores empresas
                selected_assets = scores_on_date.nlargest(top_n).index
                # Peso igual (Equal Weighted)
                portfolio_weights.loc[date, selected_assets] = 1.0 / top_n
                
    # Propaga os pesos até o próximo rebalanceamento
    portfolio_weights = portfolio_weights.replace(0.0, np.nan).ffill().fillna(0.0)
    
    # IMPORTANTE: Aplicar shift(1) para evitar Look-Ahead Bias (decisão ontem, execução hoje)
    exec_weights = portfolio_weights.shift(1).fillna(0.0)
    
    # Cálculo do retorno bruto diário da carteira
    gross_strategy_returns = (exec_weights * returns).sum(axis=1)
    
    # Cálculo de turnover e dedução de custos de transação
    weight_changes = exec_weights.diff().abs().sum(axis=1)
    costs = weight_changes * transaction_cost
    net_strategy_returns = gross_strategy_returns - costs
    
    # Curva de patrimônio acumulado
    cumulative_returns = (1 + net_strategy_returns).cumprod()
    
    results = pd.DataFrame({
        "gross_returns": gross_strategy_returns,
        "costs": costs,
        "net_returns": net_strategy_returns,
        "cumulative": cumulative_returns
    })
    
    return results

if __name__ == "__main__":
    print("Demonstração do motor de backtest multifator.")
    np.random.seed(42)
    dates = pd.date_range("2020-01-01", "2023-12-31", freq="B")
    assets = ["VALE3", "PETR4", "ITUB4", "BBDC4", "WEGE3", "RENT3", "PRIO3", "BBAS3", "GGBR4", "EQTL3"]
    
    # Geração de dados de simulação
    mock_returns = np.random.normal(0.0005, 0.018, size=(len(dates), len(assets)))
    mock_prices = pd.DataFrame(100 * (1 + mock_returns).cumprod(axis=0), index=dates, columns=assets)
    mock_pe = pd.DataFrame(np.random.uniform(5, 25, size=(len(dates), len(assets))), index=dates, columns=assets)
    
    backtest = simulate_multifactor_strategy(mock_prices, mock_pe)
    print(f"Retorno acumulado líquido final: {backtest['cumulative'].iloc[-1]:.2%}")
