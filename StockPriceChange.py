import requests
from datetime import date

ALPHA_ADVANTAGE_API = "OFM3P9Z6AXF7NAXX"


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
        yesterday = date(date.today().year,date.today().month,date.today().day-1)
        before_yesterday = date(date.today().year,date.today().month,date.today().day-2)

        try:
            yesterdey_close = float (data["Time Series (Daily)"][yesterday.strftime('%Y-%m-%d')]['4. close'])
            before_yesterday_close = float (data["Time Series (Daily)"][before_yesterday.strftime('%Y-%m-%d')]['4. close'])

        except KeyError:
            print("Bad trading address..")
            return False

        else:
            print((before_yesterday_close/yesterdey_close-1)*100)
            if (before_yesterday_close/yesterdey_close-1)*100 > 5 or (before_yesterday_close/yesterdey_close-1)*100 < -5 :
                return True
