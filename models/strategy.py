from models.wallet import Wallet

class Strategy:
    """
    this class is intended as an abstract base class
    for implementing various trading strategies
    """
    def __init__(self, token: str, init_cash_amount: float):
        self.wallet = Wallet(token, init_cash_amount)
        # rate of return will be calculated once strategy is executed
        self.ror = 0
    
    def run(self):
        pass

    def calculate_ror(self):
        pass
