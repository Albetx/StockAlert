from Tracking import *

DRAMATIC_CHANGE_PERCENT = 10.0


class TrackingInvest(Tracking):

    def __init__(self,ticker_symbol):
        super().__init__(ticker_symbol)
        self.dramatic_change = DRAMATIC_CHANGE_PERCENT
        self.daily_update = False
        self.monthly_update = True
        self.yearly_update = True
