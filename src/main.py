from datetime import datetime
import backtrader as bt
import strategies
import feed

# DATA
TICKER = "BTC-USD"
START = "2024-01-01"
END = datetime.today().strftime("%Y-%m-%d")

# Strategy
STRATEGY = strategies.SmaCross

# Data feed
data = feed.get(TICKER, START, END)

# Create, load, and run cerebro (Backtrader's engine)
cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.addstrategy(STRATEGY)
cerebro.run()
cerebro.plot(style="candle", iplot=False)
