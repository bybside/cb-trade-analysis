from models.cbclient import CBClient
from models.transaction import Transaction
from models.transaction_types import TransactionTypes

class Wallet:
    """
    this class is intended to act as a paper trading
    wallet for historic trade strategy analysis

    TO-DO:
        - log initial transaction when wallet is
          initialized with init_cash_amount
    """
    def __init__(self, token: str, init_cash_amount: float):
        self.__cbclient = CBClient()
        self.__token = token
        self.__cash_amount = init_cash_amount
        self.__num_trades = 0
        # transactions will act as a history of trades by date
        self.__txns = []
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
        self.__log_transaction(TransactionTypes.BUY, -buy_total, volume)
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
        self.__log_transaction(TransactionTypes.SELL, sell_total, volume)
        self.__num_trades += 1
        return True
    
    def get_transactions(self):
        return self.__txns

    def get_token(self):
        return self.__token

    def get_cash_amount(self):
        return self.__cash_amount
    
    def get_total_volume(self):
        return self.__total_volume
    
    def __is_valid_buy(self, buy_amount: float):
        return buy_amount <= self.__cash_amount

    def __is_valid_sell(self, sell_amount: float):
        return sell_amount <= self.__total_volume
    
    def __log_transaction(self, txn_type: str, amount: float, volume: float):
        txn = Transaction(txn_type, amount, volume)
        self.__txns.append(txn)
    
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
