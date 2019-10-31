from models.cbclient import CBClient
from models.transaction import Transaction

class Wallet:
    """
    this class is intended to act as a paper trading
    wallet for historic trade strategy analysis
    """
    def __init__(self, token: str, init_cash_amount: float):
        self.__cbclient = CBClient()
        self.__token = token
        self.__cash_amount = init_cash_amount
        self.__num_trades = 0
        # transactions will act as a history of trades by date
        self.__txns = set()
        self.__total_volume = 0

    def buy(self, volume: float, date: str):
        data = self.__cbclient.get_spot(self.__token, date)
        price = float(data["amount"])
        buy_total = volume * price
        # return if pending purchase amount exceeds cash amount
        if not self.__is_valid_buy(buy_total):
            return False
        self.__cash_amount -= buy_total
        self.__total_volume += volume
        self.__log_transaction("BUY", -buy_total, volume)
        self.__num_trades += 1
        return True

    def sell(self, volume: float, date: str):
        # return if sell amount exceeds total volume
        if not self.__is_valid_sell(volume):
            return False
        data = self.__cbclient.get_spot(self.__token, date)
        price = float(data["amount"])
        sell_total = volume * price
        self.__total_volume -= volume
        self.__cash_amount += sell_total
        self.__log_transaction("SELL", sell_total, volume)
        self.__num_trades += 1
        return True
    
    def __is_valid_buy(self, buy_amount: float):
        return buy_amount <= self.__cash_amount

    def __is_valid_sell(self, sell_amount: float):
        return sell_amount <= self.__total_volume
    
    def __log_transaction(self, txn_type: str, amount: float, volume: float):
        txn = Transaction(txn_type, amount, volume)
        self.__txns.add(txn)
    
    def __repr__(self):
        s = f"""
        Wallet:
            token:        {self.__token}
            cash_amount:  {self.__cash_amount}
            num_trades:   {self.__num_trades}
            txns:         {self.__txns}
            total_volume: {self.__total_volume}
        """
        return s
