# import coinbase.wallet.client
from models.strategies.dollar_cost_average import DollarCostAverage

def main():
    dca_strategy = DollarCostAverage("ETH", 100000, 5, "2017-01-01", "2019-10-01")
    dca_strategy.run()
    print(dca_strategy)

main()
