# 잔고조회 
import ccxt
import  keys

upbit = ccxt.upbit(config={
    'apiKey': keys.api_key,
    'secret':keys.secret
})
balance= upbit.fetch_balance()
print(upbit.keys())