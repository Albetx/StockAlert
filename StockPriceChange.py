import requests
from datetime import datetime, timedelta

ALPHA_ADVANTAGE_API = "OFM3P9Z6AXF7NAXX"
ERROR1_BAD_TRADING_ADDRESS = -999


class StockPriceChange:

    def __init__(self, ticker_symbol):
        self.ticker = ticker_symbol


    def check_change(self):

        parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.ticker,
            "apikey": ALPHA_ADVANTAGE_API
        }

        response = requests.get("https://www.alphavantage.co/query", params=parameters);
        response.raise_for_status()
        data = response.json()

        # Skip off-market days of the week
        last_trading_date = datetime.today() - timedelta(days=1)
        while last_trading_date.weekday() == 5 or last_trading_date.weekday() == 6:
            last_trading_date -= timedelta(days=1)

        before_last_trading_date = datetime.today() - timedelta(days=2)
        while before_last_trading_date.weekday() == 5 or before_last_trading_date.weekday() == 6 or \
                before_last_trading_date.weekday() == last_trading_date.weekday():
            before_last_trading_date -= timedelta(days=1)

        try:
            last_close = float (data["Time Series (Daily)"][last_trading_date.strftime('%Y-%m-%d')]['4. close'])
            before_last_close = float (data["Time Series (Daily)"][before_last_trading_date.strftime('%Y-%m-%d')]['4. close'])

        except KeyError:
            return ERROR1_BAD_TRADING_ADDRESS

        else:
            change = (last_close / before_last_close - 1) * 100
            print(change)

            return change
