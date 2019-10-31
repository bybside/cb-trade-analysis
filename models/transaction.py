class Transaction:
    """
    this class is intended to track state
    changes in wallet volume and cash amount
    """
    def __init__(self, txn_type: str, amount: float, volume: float):
        self.__txn_type = txn_type
        self.__amount = amount
        self.__volume = volume

    def __repr__(self):
        return f"Transaction({self.__txn_type}, {self.__amount}, {self.__volume})"
