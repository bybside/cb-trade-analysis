import pandas as pd
from models.strategy import Strategy

class DollarCostAverage(Strategy):
    """
    basic strategy will buy a predefined volume
    once a month and will never sell
    """
    def __init__(self, token: str, init_cash_amount: float, buy_volume: float, start_date: str, end_date: str):
        Strategy.__init__(self, token, init_cash_amount)
        self.__buy_volume = buy_volume
        self.__start_date = start_date
        self.__end_date = end_date

    def run(self):
        start_amount = self.wallet.get_cash_amount()
        daterange = pd.date_range(self.__start_date, self.__end_date, freq="M")
        for date in daterange:
            date = date.strftime("%Y-%m-%d")
            self.wallet.buy(self.__buy_volume, date)
        self.wallet.sell(self.wallet.get_total_volume(), date)
        end_amount = self.wallet.get_cash_amount()
        self.calculate_ror(start_amount, end_amount)

    def calculate_ror(self, start_amount: float, end_amount: float):
        raw_ror = ((end_amount - start_amount) / start_amount) * 100
        self.ror = round(raw_ror, 2)
    
    def __repr__(self):
        s = f"""
        DollarCostAverage(Strategy):
            token:       {self.wallet.get_token()}
            cash_amount: {self.wallet.get_cash_amount()}
            buy_volume:  {self.__buy_volume}
            start_date:  {self.__start_date}
            end_date:    {self.__end_date}
            ror:         {self.ror}%
        """
        return s
