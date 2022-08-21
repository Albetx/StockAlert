from StockPriceChange import *
from News import *
from datetime import date
from datetime import datetime
from SendEmail import *

DRAMATIC_CHANGE_PERCENT = 5
NO_SIG_CHANGE = -999
NUMBER_OF_ARTICLES = 3
TRADE_OPEN_HOUR = 17
TRADE_CLOSE_HOUR = 23
MY_EMAIL = "Albetx@gmail.com"
DRAMATIC_CHANGE_CODE = 100
DAILY_UPDATE_CODE = 200
MONTHLY_UPDATE_CODE = 300
YEARLY_UPDATE_CODE = 400


class Tracking:

    def __init__(self, ticker_symbol):
        self.ticker = ticker_symbol
        self.dramatic_change = DRAMATIC_CHANGE_PERCENT
        self.daily_update = False
        self.monthly_update = True
        self.yearly_update = True
        self.news = News(self.ticker)
        self.sender = SendEmail(MY_EMAIL, self.ticker)

    # Checks if there is a dramatic change (depending on the attribute) in the stock,
    # If yes: get the last NUMBER_OF_ARTICLES and send it by mail
    # Else: Do nothing
    def check_changes(self):
        spc = StockPriceChange(self.ticker)
        change = spc.check_change(self.dramatic_change)

        if change != NO_SIG_CHANGE:
            articles = self.news.get_news(NUMBER_OF_ARTICLES)
            self.sender.send(articles, change, DRAMATIC_CHANGE_CODE)


    def periodic_update(self):

        date_time = datetime.now()

        if self.daily_update and date_time.minute == 0 and TRADE_OPEN_HOUR < date_time.hour < TRADE_CLOSE_HOUR:
            articles = self.news.get_news(NUMBER_OF_ARTICLES)



        # TODO: Add periodic update for monthly and yearly updates






