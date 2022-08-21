from Tracking import *
from TrackingInvest import *
import pandas
from datetime import datetime

STOCK = "TSLA"
NO_SIG_CHANGE = -999


try:
    with open("tickers.txt") as tickers_list:
        tickers = pandas.read_csv(tickers_list)
        tickers_list = tickers[tickers["Group"] == "Invest"]["Ticker"].values

except FileNotFoundError:
    print ("No ticker file found..")

else:
    t1 = TrackingInvest("TSLA")
    t1.check_changes()

