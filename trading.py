import alpaca_trade_api as tradeapi
import os
import random
akey = os.environ['alpacakey']
sskey= os.environ['skey']
BASE_URL = "https://paper-api.alpaca.markets"
api = tradeapi.REST(key_id=akey, 
                    secret_key=sskey,
                    base_url=BASE_URL,
                    api_version='v2')

def getinfo(STOCK_NAME):
  barset = api.get_barset(STOCK_NAME, 'day', limit=1)
  aapl_bars = barset[STOCK_NAME]
  return aapl_bars[0].o