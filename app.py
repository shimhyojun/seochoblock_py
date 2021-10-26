from flask import Flask, request
from flask import Response
from flask_restx import Resource, Api

import pymysql
import ccxt
import db_module as db
import json 
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
    upbit_db = upbit.fetch_tickers()

    return Response(upbit_db)

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

    return Response(json.dumps(rows), mimetype='application/json')

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

    return Response(json.dumps(rows), mimetype='application/json')


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

    return Response(json.dumps(rows), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
    