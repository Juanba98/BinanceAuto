#API https://python-binance.readthedocs.io/en/latest/
import os

from functions import *
from binance.client import Client
from binance.enums import *

#Keys
keys = readKeys()
apiKey = keys[0]
apiSecret = keys[1]

#Client
client = Client(apiKey,apiSecret)

#Account Info
info= client.get_account()
balances = getMyBalances(info)


#Min cuantity get_exchange_info()
printBalances(balances)
exchange = client.get_exchange_info()

#Sell All
sellAll(balances,client,exchange)

print("--------------------------------")

info= client.get_account()
balances = getMyBalances(info)

printBalances(balances)

os.system("pause")