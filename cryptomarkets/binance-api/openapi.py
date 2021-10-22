# 현재가 가져오기
import ccxt
import pprint

binance = ccxt.binance()
btc = binance.fetch_tickers()

# 뽑을 수 있는 목록 조회
# pprint.pprint(btc)

#print("현재가",btc['last'])
print(btc)
# 거래소에 있는 데이터 전부입니다. 제가 선정한 거래소 내 데이터값을 코인들 전부입니다.근데 제가 전에 봤던 유튜브에선 전체 데이터를 뽑아오던게 있어서.. 그럼 전부 기입해줬을 거라는 거겠죠..? 