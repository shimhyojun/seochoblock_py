# 잔고조회 
import ccxt
import  keys

binance = ccxt.binance(config={
    'apiKey': keys.api_key,
    'secret':keys.secret
})
balance= binance.fetch_balance()
print(balance.keys())