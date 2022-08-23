from Tracking import *
from TrackingInvest import *
from TrackingTrade import *
import pandas
from datetime import datetime

STOCK = "TSLA"
NO_SIG_CHANGE = -999


try:
    with open("tickers.txt") as tickers_list_Invest:
        tickers_table = pandas.read_csv(tickers_list_Invest)
        tickers_list_Invest = tickers_table[tickers_table["Group"] == "Invest"]["Ticker"].values
        tickers_list_Trade = tickers_table[tickers_table["Group"] == "Trade"]["Ticker"].values
        tickers_list_Track = tickers_table[tickers_table["Group"] == "Track"]["Ticker"].values

except FileNotFoundError:
    print("No ticker file found..")

else:
    # Invest group
    for ticker in tickers_list_Invest:
        t1 = TrackingInvest(ticker)
        t1.check_changes()
        t1.periodic_update()
    # Trade group
    for ticker in tickers_list_Trade:
        t1 = TrackingTrade(ticker)
        t1.check_changes()
        t1.periodic_update()
    # Track group
    for ticker in tickers_list_Track:
        t1 = Tracking(ticker)
        t1.check_changes()
        t1.periodic_update()


# TODO: Add UI
