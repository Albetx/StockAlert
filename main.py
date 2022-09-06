import time
from Tracking import *
from TrackingInvest import *
from TrackingTrade import *
import pandas
import UserInterface as userI

STOCK = "TSLA"
NO_SIG_CHANGE = -999

start_time = time.time()

try:
    with open("tickers.txt") as tickers_list:
        tickers_table = pandas.read_csv(tickers_list)
        tickers_list = tickers_table["Ticker"].values
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

    print(f"STATUS: Total time:{time.time() - start_time}, CPU time:{time.process_time()}")

    userI.UserInterface(tickers_table)


