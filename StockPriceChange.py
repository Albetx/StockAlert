import calendar

import requests
from datetime import datetime, timedelta
import holidays
from calendar import monthrange

ALPHA_ADVANTAGE_API = "OFM3P9Z6AXF7NAXX"
ERROR1_BAD_TRADING_ADDRESS = -999
DRAMATIC_CHANGE_CODE = 100
DAILY_UPDATE_CODE = 200
MONTHLY_UPDATE_CODE = 300
YEARLY_UPDATE_CODE = 400


class StockPriceChange:

    def __init__(self, ticker_symbol):
        self.ticker = ticker_symbol

    def check_change(self, update_code: int):

        # Skip off-market days of the week
        last_trading_date = datetime.today() - timedelta(days=1)
        while last_trading_date.weekday() > 4 or last_trading_date in holidays.US():
            last_trading_date -= timedelta(days=1)

        time_series_param = "TIME_SERIES_DAILY" # Default time series param for the API server
        time_series_dic_key = "Time Series (Daily)"
        # Set compared date depending on the update code
        if update_code == DRAMATIC_CHANGE_CODE or update_code == DAILY_UPDATE_CODE:
            compared_trading_date = datetime.today() - timedelta(days=2)
        elif update_code == MONTHLY_UPDATE_CODE:
            compared_trading_date = datetime.today() - timedelta(days=30)
        # Yearly update - default
        else:
            compared_trading_date = datetime(datetime.today().year-1, datetime.today().month-1,
                                             calendar.monthrange(datetime.today().year-1, datetime.today().month-1)[1])
            time_series_param = "TIME_SERIES_MONTHLY"
            time_series_dic_key = "Monthly Time Series"

        # Skip off-market days of the week
        while compared_trading_date.weekday() > 4 or last_trading_date in holidays.US() or compared_trading_date.date() == last_trading_date.date():
            compared_trading_date -= timedelta(days=1)

        parameters = {
            "function": time_series_param,
            "symbol": self.ticker,
            "apikey": ALPHA_ADVANTAGE_API
        }

        response = requests.get("https://www.alphavantage.co/query", params=parameters);
        response.raise_for_status()
        data = response.json()

        try:
            print(f"last_trading_date: {last_trading_date}, comp date: {compared_trading_date}")
            last_close = float (data[time_series_dic_key][last_trading_date.strftime('%Y-%m-%d')]['4. close'])
            before_last_close = float (data[time_series_dic_key][compared_trading_date.strftime('%Y-%m-%d')]['4. close'])

        except KeyError:
            return ERROR1_BAD_TRADING_ADDRESS

        else:
            change = (last_close / before_last_close - 1) * 100
            print(change)

            return change
