# 현재가 가져오기
import ccxt
import pprint

coinone = ccxt.coinone()
btc = coinone.fetch_ticker("BTC/KRW")

# 뽑을 수 있는 목록 조회
# pprint.pprint(btc)

print("현재가",btc['last'])
