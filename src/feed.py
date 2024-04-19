from datetime import datetime
import backtrader as bt
import yfinance as yf


# Define the data feed
def get(ticker, start, end, source="yahoo"):
    if source == "yahoo":
        return __yahoo__(ticker, start, end)
    else:
        raise ValueError("Data source not supported")


def __yahoo__(ticker, start, end):
    dataname = yf.download(ticker, start=start, end=end)
    data = bt.feeds.PandasData(dataname=dataname)
    return data
