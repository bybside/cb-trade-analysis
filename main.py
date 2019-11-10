# import coinbase.wallet.client
from models.strategies.dollar_cost_average import DollarCostAverage

def main():
    dca_strategy = DollarCostAverage(token="BTC",
                                     init_cash_amount=1000000,
                                     buy_volume=0.25,
                                     freq="W",
                                     start_date="2017-01-01",
                                     end_date="2019-11-08")
    dca_strategy.run()
    print("=== run info ===")
    print(dca_strategy)
    print("=== wallet info ===")
    print(dca_strategy.wallet)

main()
