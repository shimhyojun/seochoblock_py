# 잔고조회 
import ccxt
import  keys

coinone = ccxt.coinone(config={
    'apiKey': keys.api_key,
    'secret':keys.secret
})
balance= coinone.fetch_balance()
print(coinone.keys())