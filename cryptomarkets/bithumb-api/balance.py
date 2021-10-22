# 잔고조회 
import ccxt
import  keys

bithumb = ccxt.bithumb(config={
    'apiKey': keys.api_key,
    'secret':keys.secret
})
balance= bithumb.fetch_balance()
print(bithumb.keys())