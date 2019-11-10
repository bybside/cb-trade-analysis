import pandas as pd
from models.strategy import Strategy

class DollarCostAverage(Strategy):
    """
    basic strategy will buy a predefined volume
    on a given frequency (e.g. once a month) and
    will sell-off all holdings on a given end date
    """
    def __init__(self, token: str, init_cash_amount: float, buy_volume: float, freq: str, start_date: str, end_date: str):
        Strategy.__init__(self, token, init_cash_amount)
        self.__buy_volume = buy_volume
        self.__freq = freq
        self.__start_date = start_date
        self.__end_date = end_date

    def run(self):
        daterange = pd.date_range(self.__start_date, self.__end_date, freq=self.__freq)
        for date in daterange:
            date = date.strftime("%Y-%m-%d")
            self.wallet.buy(self.__buy_volume, date)
        self.wallet.sell(self.wallet.get_total_volume(), date)
        # ending cash will be the wallet's current cash amount after token sell-off
        self.end_amount = self.wallet.get_cash_amount()
        self.calculate_ror()
    
    def __repr__(self):
        s = f"""
        DollarCostAverage(Strategy):
            token:       {self.wallet.get_token()}
            cash_amount: {self.wallet.get_cash_amount()}
            buy_volume:  {self.__buy_volume}
            freq:        {self.__freq}
            start_date:  {self.__start_date}
            end_date:    {self.__end_date}
            ror:         {self.ror}%
        """
        return s
