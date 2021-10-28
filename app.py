from re import A
from flask import Flask, request
from flask import Response
from flask_restx import Resource, Api

import pymysql
import ccxt
from werkzeug.wrappers import response
import db_module as db
import json
from flask import jsonify, render_template
from datetime import datetime

app = Flask(__name__)
api = Api(app)

markets = {}
count = 1

'''
# mydb 내 upbit 데이터 사용
@app.route('/upbitsApi')
def Upbit_db():
    dbModule = db.upbit_DB()

    sql = "SELECT user_id, access_key, private_key FROM mydb.upbits ORDER BY id DESC"
    rows = dbModule.executeAll(sql)
    
    return Response(json.dumps(rows), mimetype='application/json')
'''

# 거래소 openapi 

@app.route('/binance-openapi', methods=['GET'])
def getPrice1():
    binance = ccxt.binance()
    binance_db = binance.fetch_tickers()

    return Response(binance_db)


@app.route('/bithumb-openapi',methods=['GET'])
def getPrice2():
    bithumb = ccxt.bithumb()
    bithumb_db = bithumb.fetch_tickers()

    return Response(bithumb_db)

@app.route('/coinone-openapi',methods=['GET'])
def getPrice3():
    coinone = ccxt.coinone()
    coinone_db = coinone.fetch_tickers()

    return Response(coinone_db)


@app.route('/upbit-openapi',methods=['GET'])
def getPrice4():
    upbit = ccxt.upbit()
    keyList = ['1INCH/BTC', 'AAVE/BTC', 'ADA/BTC', 'AERGO/BTC', 'AHT/BTC', 'ALGO/BTC', 'ANKR/BTC', 'AQT/BTC', 'ARDR/BTC', 'ARK/BTC', 'ATOM/BTC', 'AUCTION/BTC', 'AXS/BTC', 'BASIC/BTC', 'BAT/BTC', 'BCH/BTC', 'BFC/BTC', 'BNT/BTC', 'BORA/BTC', 'BSV/BTC', 'BTT/BTC', 'CBK/BTC', 'CELO/BTC', 'CHR/BTC', 'CHZ/BTC', 'COMP/BTC', 'CRO/BTC', 'CRV/BTC', 'CTSI/BTC', 'CVC/BTC', 'DAD/BTC', 'DAI/BTC', 'DAWN/BTC', 'DENT/BTC', 'DGB/BTC', 'DKA/BTC', 'DNT/BTC', 'DOGE/BTC', 'DOT/BTC', 'ELF/BTC', 'ENJ/BTC', 'EOS/BTC', 'ETC/BTC', 'ETH/BTC', 'FCT2/BTC', 'FIL/BTC', 'FLOW/BTC', 'FOR/BTC', 'FX/BTC', 'GLM/BTC', 'GO/BTC', 'GRS/BTC', 'GRT/BTC', 'GXC/BTC', 'HBD/BTC', 'HIVE/BTC', 'HUM/BTC', 'HUNT/BTC', 'INJ/BTC', 'IOST/BTC', 'IOTX/BTC', 'IQ/BTC', 'JST/BTC', 'JUV/BTC', 'KAVA/BTC', 'LINA/BTC', 'LINK/BTC', 'LOOM/BTC', 'LRC/BTC', 'LSK/BTC', 'LTC/BTC', 'LUNA/BTC', 'MANA/BTC', 'MARO/BTC', 'MASK/BTC', 'MATIC/BTC', 'MED/BTC', 'META/BTC', 'MFT/BTC', 'MKR/BTC', 'MLK/BTC', 'MOC/BTC', 'MTL/BTC', 'MVL/BTC', 'NEAR/BTC', 'NKN/BTC', 'NMR/BTC', 'NU/BTC', 'OBSR/BTC', 'OGN/BTC', 'OMG/BTC', 'ONIT/BTC', 'ORBS/BTC', 'OXT/BTC', 'PCI/BTC', 'PLA/BTC', 'POLY/BTC', 'POWR/BTC', 'PROM/BTC', 'PSG/BTC', 'PUNDIX/BTC', 'QTCON/BTC', 'QTUM/BTC', 'REP/BTC', 'RFR/BTC', 'RLC/BTC', 'RSR/BTC', 'RVN/BTC', 'SAND/BTC', 'SBD/BTC', 'SC/BTC', 'SNT/BTC', 'SNX/BTC', 'SOL/BTC', 'SOLVE/BTC', 'SRM/BTC', 'SSX/BTC', 'STEEM/BTC', 'STMX/BTC', 'STORJ/BTC', 'STPT/BTC', 'STRAX/BTC', 'STRK/BTC', 'STX/BTC', 'SUN/BTC', 'SXP/BTC', 'Tokamak Network/BTC', 'TRX/BTC', 'TUSD/BTC', 'UNI/BTC', 'UPP/BTC', 'USDP/BTC', 'VAL/BTC', 'VET/BTC', 'WAVES/BTC', 'WAXP/BTC', 'XEM/BTC', 'XLM/BTC', 'XRP/BTC', 'XTZ/BTC', 'ZIL/BTC', 'ZRX/BTC', '1INCH/KRW', 'AAVE/KRW', 'ADA/KRW', 'AERGO/KRW', 'AHT/KRW', 'ANKR/KRW', 'AQT/KRW', 'ARDR/KRW', 'ARK/KRW', 'ATOM/KRW', 'AXS/KRW', 'BAT/KRW', 'BCH/KRW', 'BORA/KRW', 'BSV/KRW', 'BTC/KRW', 'BTG/KRW', 'BTT/KRW', 'CBK/KRW', 'CHZ/KRW', 'CRE/KRW', 'CRO/KRW', 'CVC/KRW', 'DAWN/KRW', 'DKA/KRW', 'DOGE/KRW', 'DOT/KRW', 'ELF/KRW', 'ENJ/KRW', 'EOS/KRW', 'ETC/KRW', 'ETH/KRW', 'FCT2/KRW', 'FLOW/KRW', 'GAS/KRW', 'GLM/KRW', 'GRS/KRW', 'HBAR/KRW', 'HIVE/KRW', 'HUM/KRW', 'HUNT/KRW', 'ICX/KRW', 'IOST/KRW', 'IOTA/KRW', 'IQ/KRW', 'JST/KRW', 'KAVA/KRW', 'KNC/KRW', 'LINK/KRW', 'LOOM/KRW', 'LSK/KRW', 'LTC/KRW', 'MANA/KRW', 'MATIC/KRW', 'MBL/KRW', 'MED/KRW', 'META/KRW', 'MFT/KRW', 'MLK/KRW', 'MOC/KRW', 'MTL/KRW', 'MVL/KRW', 'NEO/KRW', 'NU/KRW', 'OMG/KRW', 'ONG/KRW', 'ONT/KRW', 'ORBS/KRW', 'PLA/KRW', 'POLY/KRW', 'POWR/KRW', 'PUNDIX/KRW', 'QKC/KRW', 'QTUM/KRW', 'REP/KRW', 'RFR/KRW', 'SAND/KRW', 'SBD/KRW', 'SC/KRW', 'SNT/KRW', 'SOL/KRW', 'SRM/KRW', 'SSX/KRW', 'STEEM/KRW', 'STMX/KRW', 'STORJ/KRW', 'STPT/KRW', 'STRAX/KRW', 'STRK/KRW', 'STX/KRW', 'SXP/KRW', 'TFUEL/KRW', 'THETA/KRW', 'Tokamak Network/KRW', 'TRX/KRW', 'TT/KRW', 'UPP/KRW', 'VET/KRW', 'WAVES/KRW', 'WAXP/KRW', 'XEC/KRW', 'XEM/KRW', 'XLM/KRW', 'XRP/KRW', 'XTZ/KRW', 'ZIL/KRW', 'ZRX/KRW', 'ADA/USDT', 'BAT/USDT', 'BCH/USDT', 'BTC/USDT', 'DGB/USDT', 'DOGE/USDT', 'ETC/USDT', 'ETH/USDT', 'LTC/USDT', 'OMG/USDT', 'RVN/USDT', 'SC/USDT', 'TRX/USDT', 'TUSD/USDT', 'XRP/USDT', 'ZRX/USDT']
    krwList = []

    for i in range(len(keyList)):
        if '/KRW' in keyList[i]:
            krwList.append(keyList[i])
    
    upbit_db = upbit.fetch_tickers(symbols=krwList,params={})
    print(upbit_db)
    BTCList = []

    for i in range(len(krwList)):
        name = krwList[i]

        BTC_M = (upbit_db[name]['info']['market'])
        BTC_C = (upbit_db[name]['info']['change_rate'])
        BTC_T = (upbit_db[name]['info']['trade_timestamp'])
        BTC_P = (upbit_db[name]['info']['trade_price'])
        BTC_V = (upbit_db[name]['info']['trade_volume']) 

        BTC = {'market':BTC_M ,'change_rate':BTC_C,'trade_timestamp':BTC_T,'trade_price':BTC_P,'trade_volume':BTC_V}
        
        for name,description in BTC.items():
            BTCList.append({name:description})
    try:
        return jsonify(json.dumps(BTCList))
    except Exception as e:
        print(str(e))
        return jsonify(str(e))
   


   #------------------------------------------------
    # BTC_M = (upbit_db['BTC/KRW']['info']['market'])
    # BTC_C = (upbit_db['BTC/KRW']['info']['change_rate'])
    # BTC_T = (upbit_db['BTC/KRW']['info']['trade_timestamp'])
    # BTC_P = (upbit_db['BTC/KRW']['info']['trade_price'])
    # BTC_V = (upbit_db['BTC/KRW']['info']['trade_volume'])
    # BTC = {'market':BTC_M ,'change_rate':BTC_C,'trade_timestamp':BTC_T,'trade_price':BTC_P,'trade_volume':BTC_V}
#     try:
#         BTCList = []
    
    
#         for name,description in BTC.items():
#             BTCList.append({name:description})
#         return jsonify(json.dumps(BTCList))
#     except Exception as e:
#         print(str(e))
#         return jsonify(str(e))
# key list로 가져오고 원하는 문자열로 있다면 따로 class로 if 써서

# def getPrice4():
#     keyList = ['1INCH/BTC', 'AAVE/BTC', 'ADA/BTC', 'AERGO/BTC', 'AHT/BTC', 'ALGO/BTC', 'ANKR/BTC', 'AQT/BTC', 'ARDR/BTC', 'ARK/BTC', 'ATOM/BTC', 'AUCTION/BTC', 'AXS/BTC', 'BASIC/BTC', 'BAT/BTC', 'BCH/BTC', 'BFC/BTC', 'BNT/BTC', 'BORA/BTC', 'BSV/BTC', 'BTT/BTC', 'CBK/BTC', 'CELO/BTC', 'CHR/BTC', 'CHZ/BTC', 'COMP/BTC', 'CRO/BTC', 'CRV/BTC', 'CTSI/BTC', 'CVC/BTC', 'DAD/BTC', 'DAI/BTC', 'DAWN/BTC', 'DENT/BTC', 'DGB/BTC', 'DKA/BTC', 'DNT/BTC', 'DOGE/BTC', 'DOT/BTC', 'ELF/BTC', 'ENJ/BTC', 'EOS/BTC', 'ETC/BTC', 'ETH/BTC', 'FCT2/BTC', 'FIL/BTC', 'FLOW/BTC', 'FOR/BTC', 'FX/BTC', 'GLM/BTC', 'GO/BTC', 'GRS/BTC', 'GRT/BTC', 'GXC/BTC', 'HBD/BTC', 'HIVE/BTC', 'HUM/BTC', 'HUNT/BTC', 'INJ/BTC', 'IOST/BTC', 'IOTX/BTC', 'IQ/BTC', 'JST/BTC', 'JUV/BTC', 'KAVA/BTC', 'LINA/BTC', 'LINK/BTC', 'LOOM/BTC', 'LRC/BTC', 'LSK/BTC', 'LTC/BTC', 'LUNA/BTC', 'MANA/BTC', 'MARO/BTC', 'MASK/BTC', 'MATIC/BTC', 'MED/BTC', 'META/BTC', 'MFT/BTC', 'MKR/BTC', 'MLK/BTC', 'MOC/BTC', 'MTL/BTC', 'MVL/BTC', 'NEAR/BTC', 'NKN/BTC', 'NMR/BTC', 'NU/BTC', 'OBSR/BTC', 'OGN/BTC', 'OMG/BTC', 'ONIT/BTC', 'ORBS/BTC', 'OXT/BTC', 'PCI/BTC', 'PLA/BTC', 'POLY/BTC', 'POWR/BTC', 'PROM/BTC', 'PSG/BTC', 'PUNDIX/BTC', 'QTCON/BTC', 'QTUM/BTC', 'REP/BTC', 'RFR/BTC', 'RLC/BTC', 'RSR/BTC', 'RVN/BTC', 'SAND/BTC', 'SBD/BTC', 'SC/BTC', 'SNT/BTC', 'SNX/BTC', 'SOL/BTC', 'SOLVE/BTC', 'SRM/BTC', 'SSX/BTC', 'STEEM/BTC', 'STMX/BTC', 'STORJ/BTC', 'STPT/BTC', 'STRAX/BTC', 'STRK/BTC', 'STX/BTC', 'SUN/BTC', 'SXP/BTC', 'Tokamak Network/BTC', 'TRX/BTC', 'TUSD/BTC', 'UNI/BTC', 'UPP/BTC', 'USDP/BTC', 'VAL/BTC', 'VET/BTC', 'WAVES/BTC', 'WAXP/BTC', 'XEM/BTC', 'XLM/BTC', 'XRP/BTC', 'XTZ/BTC', 'ZIL/BTC', 'ZRX/BTC', '1INCH/KRW', 'AAVE/KRW', 'ADA/KRW', 'AERGO/KRW', 'AHT/KRW', 'ANKR/KRW', 'AQT/KRW', 'ARDR/KRW', 'ARK/KRW', 'ATOM/KRW', 'AXS/KRW', 'BAT/KRW', 'BCH/KRW', 'BORA/KRW', 'BSV/KRW', 'BTC/KRW', 'BTG/KRW', 'BTT/KRW', 'CBK/KRW', 'CHZ/KRW', 'CRE/KRW', 'CRO/KRW', 'CVC/KRW', 'DAWN/KRW', 'DKA/KRW', 'DOGE/KRW', 'DOT/KRW', 'ELF/KRW', 'ENJ/KRW', 'EOS/KRW', 'ETC/KRW', 'ETH/KRW', 'FCT2/KRW', 'FLOW/KRW', 'GAS/KRW', 'GLM/KRW', 'GRS/KRW', 'HBAR/KRW', 'HIVE/KRW', 'HUM/KRW', 'HUNT/KRW', 'ICX/KRW', 'IOST/KRW', 'IOTA/KRW', 'IQ/KRW', 'JST/KRW', 'KAVA/KRW', 'KNC/KRW', 'LINK/KRW', 'LOOM/KRW', 'LSK/KRW', 'LTC/KRW', 'MANA/KRW', 'MATIC/KRW', 'MBL/KRW', 'MED/KRW', 'META/KRW', 'MFT/KRW', 'MLK/KRW', 'MOC/KRW', 'MTL/KRW', 'MVL/KRW', 'NEO/KRW', 'NU/KRW', 'OMG/KRW', 'ONG/KRW', 'ONT/KRW', 'ORBS/KRW', 'PLA/KRW', 'POLY/KRW', 'POWR/KRW', 'PUNDIX/KRW', 'QKC/KRW', 'QTUM/KRW', 'REP/KRW', 'RFR/KRW', 'SAND/KRW', 'SBD/KRW', 'SC/KRW', 'SNT/KRW', 'SOL/KRW', 'SRM/KRW', 'SSX/KRW', 'STEEM/KRW', 'STMX/KRW', 'STORJ/KRW', 'STPT/KRW', 'STRAX/KRW', 'STRK/KRW', 'STX/KRW', 'SXP/KRW', 'TFUEL/KRW', 'THETA/KRW', 'Tokamak Network/KRW', 'TRX/KRW', 'TT/KRW', 'UPP/KRW', 'VET/KRW', 'WAVES/KRW', 'WAXP/KRW', 'XEC/KRW', 'XEM/KRW', 'XLM/KRW', 'XRP/KRW', 'XTZ/KRW', 'ZIL/KRW', 'ZRX/KRW', 'ADA/USDT', 'BAT/USDT', 'BCH/USDT', 'BTC/USDT', 'DGB/USDT', 'DOGE/USDT', 'ETC/USDT', 'ETH/USDT', 'LTC/USDT', 'OMG/USDT', 'RVN/USDT', 'SC/USDT', 'TRX/USDT', 'TUSD/USDT', 'XRP/USDT', 'ZRX/USDT']
#     krwList = []

#     for i in range(len(keyList)):
#         if '/KRW' in keyList[i]:
#             krwList.append(keyList[i])
#         upbit = ccxt.upbit()

#     upbit_db = upbit.fetch_tickers()
    

#     return Response(a)


'''
@app.route('/binance-privateapi', methods=['GET'])
def getBalance1():
    binance_balance = ccxt.binance(config={
    'apiKey': pymysql.mydb.upbits.access_key,
    'secret':keys.secret
})
binance_balance= binance.fetch_balance()
print(binance_balance.keys())
'''


#private api
# 업비트
@app.route('/upbit-privateapi/<user_id>',methods=['GET'])
def Upbit_Apidb(user_id):
    dbModule = db.key_DB() 
    sql="select access_key, private_key from upbits where user_id='{}'".format(user_id)
    rows= dbModule.executeOne(sql)
    
    upbit = ccxt.upbit(config={ 
        'apiKey': rows['access_key'],        
        'secret': rows['private_key']         
        }
    )
    balance= upbit.fetch_balance()
    print(balance)

    return Response(json.dumps(balance), mimetype='application/json')

# 바이낸스
@app.route('/binance-privateapi/<user_id>',methods=['GET'])
def Binance_Apidb(user_id):
    dbModule = db.key_DB() 
    sql="select access_key, private_key from binances where user_id='{}'".format(user_id)
    rows= dbModule.executeOne(sql)

    binance = ccxt.binance(config={ 
        'apiKey': rows['access_key'],        
        'secret': rows['private_key']         
        }
    )
    balance= binance.fetch_balance()
    print(balance)

    return Response(json.dumps(balance), mimetype='application/json')


# 빗썸
@app.route('/bithumb-privateapi/<user_id>',methods=['GET'])
def Bithumb_Apidb(user_id):
    dbModule = db.key_DB() 
    sql="select access_key, private_key from bithumbs where id='{}'".format(user_id)
    rows= dbModule.executeOne(sql)
    bithumb = ccxt.bithumb(config={ 
        'apiKey': rows['access_key'],        
        'secret': rows['private_key']         
        }
    )
    balance= bithumb.fetch_balance()
    print(balance)

    return Response(json.dumps(balance), mimetype='application/json')

# 코인원
@app.route('/coinone-privateapi/<user_id>',methods=['GET'])
def Coinone_Apidb(user_id):
    dbModule = db.key_DB() 
    sql="select access_key, private_key from coinones where id='{}'".format(user_id)
    rows= dbModule.executeOne(sql)
    coinone = ccxt.coinone(config={ 
        'apiKey': rows['access_key'],        
        'secret': rows['private_key']         
        }
    )
    balance= coinone.fetch_balance()
    print(balance)

    return Response(json.dumps(balance), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
    