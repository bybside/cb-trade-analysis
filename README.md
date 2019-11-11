# Setup
  - install coinbase library (supported by coinbase): ```pip3 install coinbase```
  - api endpoint: <https://api.coinbase.com/v2/>
  - endpoint documentation: <https://developers.coinbase.com/api/v2?shell#data-endpoints>
  - official python client library: <https://github.com/coinbase/coinbase-python>
  - dbvisualizer installation: <https://www.dbvis.com/download/10.0>

# To-Do
  - look into pandas for further transaction analysis, e.g.:
    - average change in price
    - average percent change in price
  - setup database to store historical price information for each token (Coinbase limit: 10k requests/day)
  - store additional strategy information in database (transaction and wallet info, etc.)
        