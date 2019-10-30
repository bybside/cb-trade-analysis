import requests
import pandas as pd

class CBClient:
    """
    this class is intended to pull price history
    data from Coinbase's data endpoints
    """
    def __init__(self):
        self.__ENDPOINT = "https://api.coinbase.com/v2/"
        self.__TOKENS = {"BTC", "ETH", "XRP", "BAT"}
    
    def get_spot_over_time(self, token="BTC", start_date="2017-01-01", end_date="2019-10-28"):
        data = []
        daterange = pd.date_range(start_date, end_date)
        for date in daterange:
            date = date.strftime("%Y-%m-%d")
            spot = self.get_spot(token, date)
            data.append(spot)
        return data

    def get_tokens(self):
        return self.__TOKENS

    def get_spot(self, token: str, date: str):
        if token not in self.__TOKENS:
            return
        req = f"{self.__ENDPOINT}/prices/{token}-USD/spot?date={date}"
        response = requests.get(req)
        spot = response.json()
        spot["data"]["date"] = date
        return spot["data"]

    def get_iso_time(self):
        req = f"{self.__ENDPOINT}/time"
        response = requests.get(req)
        time = response.json()
        return time["data"]
