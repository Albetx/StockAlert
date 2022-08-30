from Tracking import *

DRAMATIC_CHANGE_PERCENT = 2.0


class TrackingTrade(Tracking):

    def __init__(self,ticker_symbol):
        super().__init__(ticker_symbol)
        self.dramatic_change = DRAMATIC_CHANGE_PERCENT
        self.daily_update = True
        self.monthly_update = False
        self.yearly_update = False
