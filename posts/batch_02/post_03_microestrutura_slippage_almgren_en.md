# Non-Linear Slippage: Why 90% of Backtests Die in Production

- **Pillar:** microestrutura
- **Suggested Time:** Quarta-feira / Wednesday (09:00)
- **Language:** English

---

Most junior researchers assume flat brokerage fees and 5 bps of fixed slippage.
Once capital is deployed, live performance deteriorates by 800 bps against the simulated curve.

The explanation: Market Microstructure & Non-Linear Market Impact.

1. The Almgren-Chriss Framework (Temporary vs Permanent Impact):
Temporary impact reflects instantaneous order-book liquidity consumption. Permanent impact reflects information leakage: your own execution moves the equilibrium price against you.

2. The Square-Root Law of Price Impact:
Price impact scales with the square root of order size relative to Average Daily Volume (ADV):
Impact ≈ Y * σ * sqrt(Q / ADV)

With $50,000 simulated capital, the strategy looks like pure gold. With $20 million AUM, market impact absorbs 100% of the alpha before positions are even filled.

In institutional research, you must model the Strategy Capacity Frontier.

How do you account for non-linear execution frictions in your backtests?

#Microstructure #QuantFinance #AlgorithmicTrading #Execution #AssetManagement
