# import coinbase.wallet.client
from models.cbclient import CBClient
from models.wallet import Wallet

def main():
    # TO-DO: add cash amount to transaction history
    wallet = Wallet("ETH", 10000)
    print(wallet)
    wallet.buy(500, "2017-03-01")
    print(wallet)
    wallet.sell(500, "2017-03-01")
    print(wallet)

main()
