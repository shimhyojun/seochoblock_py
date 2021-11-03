from re import A
from flask import Flask, request
from flask import Response
from flask_restx import Resource, Api

import ccxt
from werkzeug.wrappers import response
import db_module as db
import json
from flask import jsonify, render_template
from datetime import datetime

import pymysql

app = Flask(__name__)
api = Api(app)

markets = {}
count = 1
'''db 사용할 경우 다시 추가'''
# dbModule = db.upbit_BTC()



# 바이낸스 OPEN
@app.route('/binance-openapi', methods=['GET'])
def getPrice1():
    # binance = ccxt.binance()
    # keyList1 = ['ETH/BTC', 'LTC/BTC', 'BNB/BTC', 'NEO/BTC', 'QTUM/ETH', 'EOS/ETH', 'SNT/ETH', 'BNT/ETH', 'BCC/BTC', 'GAS/BTC', 'BNB/ETH', 'BTC/USDT', 'ETH/USDT', 'HSR/BTC', 'OAX/ETH', 'DNT/ETH', 'MCO/ETH', 'ICN/ETH', 'MCO/BTC', 'WTC/BTC', 'WTC/ETH', 'LRC/BTC', 'LRC/ETH', 'QTUM/BTC', 'YOYOW/BTC', 'OMG/BTC', 'OMG/ETH', 'ZRX/BTC', 'ZRX/ETH', 'STRAT/BTC', 'STRAT/ETH', 'SNGLS/BTC', 'SNGLS/ETH', 'BQX/BTC', 'BQX/ETH', 'KNC/BTC', 'KNC/ETH', 'FUN/BTC', 'FUN/ETH', 'SNM/BTC', 'SNM/ETH', 'NEO/ETH', 'IOTA/BTC', 'IOTA/ETH', 'LINK/BTC', 'LINK/ETH', 'XVG/BTC', 'XVG/ETH', 'SALT/BTC', 'SALT/ETH', 'MDA/BTC', 'MDA/ETH', 'MTL/BTC', 'MTL/ETH', 'SUB/BTC', 'SUB/ETH', 'EOS/BTC', 'SNT/BTC', 'ETC/ETH', 'ETC/BTC', 'MTH/BTC', 'MTH/ETH', 'ENG/BTC', 'ENG/ETH', 'DNT/BTC', 'ZEC/BTC', 'ZEC/ETH', 'BNT/BTC', 'AST/BTC', 'AST/ETH', 'DASH/BTC', 'DASH/ETH', 'OAX/BTC', 'ICN/BTC', 'BTG/BTC', 'BTG/ETH', 'EVX/BTC', 'EVX/ETH', 'REQ/BTC', 'REQ/ETH', 'VIB/BTC', 'VIB/ETH', 'HSR/ETH', 'TRX/BTC', 'TRX/ETH', 'POWR/BTC', 'POWR/ETH', 'ARK/BTC', 'ARK/ETH', 'YOYOW/ETH', 'XRP/BTC', 'XRP/ETH', 'MOD/BTC', 'MOD/ETH', 'ENJ/BTC', 'ENJ/ETH', 'STORJ/BTC', 'STORJ/ETH', 'BNB/USDT', 'VEN/BNB', 'YOYOW/BNB', 'POWR/BNB', 'VEN/BTC', 'VEN/ETH', 'KMD/BTC', 'KMD/ETH', 'NULS/BNB', 'RCN/BTC', 'RCN/ETH', 'RCN/BNB', 'NULS/BTC', 'NULS/ETH', 'RDN/BTC', 'RDN/ETH', 'RDN/BNB', 'XMR/BTC', 'XMR/ETH', 'DLT/BNB', 'WTC/BNB', 'DLT/BTC', 'DLT/ETH', 'AMB/BTC', 'AMB/ETH', 'AMB/BNB', 'BCC/ETH', 'BCC/USDT', 'BCC/BNB', 'BAT/BTC', 'BAT/ETH', 'BAT/BNB', 'BCPT/BTC', 'BCPT/ETH', 'BCPT/BNB', 'ARN/BTC', 'ARN/ETH', 'GVT/BTC', 'GVT/ETH', 'CDT/BTC', 'CDT/ETH', 'GXS/BTC', 'GXS/ETH', 'NEO/USDT', 'NEO/BNB', 'POE/BTC', 'POE/ETH', 'QSP/BTC', 'QSP/ETH', 'QSP/BNB', 'BTS/BTC', 'BTS/ETH', 'BTS/BNB', 'XZC/BTC', 'XZC/ETH', 'XZC/BNB', 'LSK/BTC', 'LSK/ETH', 'LSK/BNB', 'TNT/BTC', 'TNT/ETH', 'FUEL/BTC', 'FUEL/ETH', 'MANA/BTC', 'MANA/ETH', 'BCD/BTC', 'BCD/ETH', 'DGD/BTC', 'DGD/ETH', 'IOTA/BNB', 'ADX/BTC', 'ADX/ETH', 'ADX/BNB', 'ADA/BTC', 'ADA/ETH', 'PPT/BTC', 'PPT/ETH', 'CMT/BTC', 'CMT/ETH', 'CMT/BNB', 'XLM/BTC', 'XLM/ETH', 'XLM/BNB', 'CND/BTC', 'CND/ETH', 'CND/BNB', 'LEND/BTC', 'LEND/ETH', 'WABI/BTC', 'WABI/ETH', 'WABI/BNB', 'LTC/ETH', 'LTC/USDT', 'LTC/BNB', 'TNB/BTC', 'TNB/ETH', 'WAVES/BTC', 'WAVES/ETH', 'WAVES/BNB', 'GTO/BTC', 'GTO/ETH', 'GTO/BNB', 'ICX/BTC', 'ICX/ETH', 'ICX/BNB', 'OST/BTC', 'OST/ETH', 'OST/BNB', 'ELF/BTC', 'ELF/ETH', 'AION/BTC', 'AION/ETH', 'AION/BNB', 'NEBL/BTC', 'NEBL/ETH', 'NEBL/BNB', 'BRD/BTC', 'BRD/ETH', 'BRD/BNB', 'MCO/BNB', 'EDO/BTC', 'EDO/ETH', 'WINGS/BTC', 'WINGS/ETH', 'NAV/BTC', 'NAV/ETH', 'NAV/BNB', 'LUN/BTC', 'LUN/ETH', 'TRIG/BTC', 'TRIG/ETH', 'TRIG/BNB', 'APPC/BTC', 'APPC/ETH', 'APPC/BNB', 'VIBE/BTC', 'VIBE/ETH', 'RLC/BTC', 'RLC/ETH', 'RLC/BNB', 'INS/BTC', 'INS/ETH', 'PIVX/BTC', 'PIVX/ETH', 'PIVX/BNB', 'IOST/BTC', 'IOST/ETH', 'CHAT/BTC', 'CHAT/ETH', 'STEEM/BTC', 'STEEM/ETH', 'STEEM/BNB', 'NANO/BTC', 'NANO/ETH', 'NANO/BNB', 'VIA/BTC', 'VIA/ETH', 'VIA/BNB', 'BLZ/BTC', 'BLZ/ETH', 'BLZ/BNB', 'AE/BTC', 'AE/ETH', 'AE/BNB', 'RPX/BTC', 'RPX/ETH', 'RPX/BNB', 'NCASH/BTC', 'NCASH/ETH', 'NCASH/BNB', 'POA/BTC', 'POA/ETH', 'POA/BNB', 'ZIL/BTC', 'ZIL/ETH', 'ZIL/BNB', 'ONT/BTC', 'ONT/ETH', 'ONT/BNB', 'STORM/BTC', 'STORM/ETH', 'STORM/BNB', 'QTUM/BNB', 'QTUM/USDT', 'XEM/BTC', 'XEM/ETH', 'XEM/BNB', 'WAN/BTC', 'WAN/ETH', 'WAN/BNB', 'WPR/BTC', 'WPR/ETH', 'QLC/BTC', 'QLC/ETH', 'SYS/BTC', 'SYS/ETH', 'SYS/BNB', 'QLC/BNB', 'GRS/BTC', 'GRS/ETH', 'ADA/USDT', 'ADA/BNB', 'CLOAK/BTC', 'CLOAK/ETH', 'GNT/BTC', 'GNT/ETH', 'GNT/BNB', 'LOOM/BTC', 'LOOM/ETH', 'LOOM/BNB', 'XRP/USDT', 'BCN/BTC', 'BCN/ETH', 'BCN/BNB', 'REP/BTC', 'REP/ETH', 'REP/BNB', 'BTC/TUSD', 'TUSD/BTC', 'ETH/TUSD', 'TUSD/ETH', 'TUSD/BNB', 'ZEN/BTC', 'ZEN/ETH', 'ZEN/BNB', 'SKY/BTC', 'SKY/ETH', 'SKY/BNB', 'EOS/USDT', 'EOS/BNB', 'CVC/BTC', 'CVC/ETH', 'CVC/BNB', 'THETA/BTC', 'THETA/ETH', 'THETA/BNB', 'XRP/BNB', 'TUSD/USDT', 'IOTA/USDT', 'XLM/USDT', 'IOTX/BTC', 'IOTX/ETH', 'QKC/BTC', 'QKC/ETH', 'AGI/BTC', 'AGI/ETH', 'AGI/BNB', 'NXS/BTC', 'NXS/ETH', 'NXS/BNB', 'ENJ/BNB', 'DATA/BTC', 'DATA/ETH', 'ONT/USDT', 'TRX/BNB', 'TRX/USDT', 'ETC/USDT', 'ETC/BNB', 'ICX/USDT', 'SC/BTC', 'SC/ETH', 'SC/BNB', 'NPXS/BTC', 'NPXS/ETH', 'VEN/USDT', 'KEY/BTC', 'KEY/ETH', 'NAS/BTC', 'NAS/ETH', 'NAS/BNB', 'MFT/BTC', 'MFT/ETH', 'MFT/BNB', 'DENT/BTC', 'DENT/ETH', 'ARDR/BTC', 'ARDR/ETH', 'ARDR/BNB', 'NULS/USDT', 'HOT/BTC', 'HOT/ETH', 'VET/BTC', 'VET/ETH', 'VET/USDT', 'VET/BNB', 'DOCK/BTC', 'DOCK/ETH', 'POLY/BTC', 'POLY/BNB', 'PHX/BTC', 'PHX/ETH', 'PHX/BNB', 'HC/BTC', 'HC/ETH', 'GO/BTC', 'GO/BNB', 'PAX/BTC', 'PAX/BNB', 'PAX/USDT', 'PAX/ETH', 'RVN/BTC', 'RVN/BNB', 'DCR/BTC', 'DCR/BNB', 'USDC/BNB', 'MITH/BTC', 'MITH/BNB', 'BCH/BTC', 'BSV/BTC', 'BCH/USDT', 'BSV/USDT']

    # keyList2 = ['BNB/PAX', 'BTC/PAX', 'ETH/PAX', 'XRP/PAX', 'EOS/PAX', 'XLM/PAX', 'REN/BTC', 'REN/BNB', 'BNB/TUSD', 'XRP/TUSD', 'EOS/TUSD', 'XLM/TUSD', 'BNB/USDC', 'BTC/USDC', 'ETH/USDC', 'XRP/USDC', 'EOS/USDC', 'XLM/USDC', 'USDC/USDT', 'ADA/TUSD', 'TRX/TUSD', 'NEO/TUSD', 'TRX/XRP', 'XZC/XRP', 'PAX/TUSD', 'USDC/TUSD', 'USDC/PAX', 'LINK/USDT', 'LINK/TUSD', 'LINK/PAX', 'LINK/USDC', 'WAVES/USDT', 'WAVES/TUSD', 'WAVES/PAX', 'WAVES/USDC', 'BCH/TUSD', 'BCH/PAX', 'BCH/USDC', 'BSV/TUSD', 'BSV/PAX', 'BSV/USDC', 'LTC/TUSD', 'LTC/PAX', 'LTC/USDC', 'TRX/PAX', 'TRX/USDC', 'BTT/BTC', 'BTT/BNB', 'BTT/USDT', 'BNB/USDS', 'BTC/USDS', 'USDS/USDT', 'USDS/PAX', 'USDS/TUSD', 'USDS/USDC', 'BTT/PAX', 'BTT/TUSD', 'BTT/USDC', 'ONG/BNB', 'ONG/BTC', 'ONG/USDT', 'HOT/BNB', 'HOT/USDT', 'ZIL/USDT', 'ZRX/BNB', 'ZRX/USDT', 'FET/BNB', 'FET/BTC', 'FET/USDT', 'BAT/USDT', 'XMR/BNB', 'XMR/USDT', 'ZEC/BNB', 'ZEC/USDT', 'ZEC/PAX', 'ZEC/TUSD', 'ZEC/USDC', 'IOST/BNB', 'IOST/USDT', 'CELR/BNB', 'CELR/BTC', 'CELR/USDT', 'ADA/PAX', 'ADA/USDC', 'NEO/PAX', 'NEO/USDC', 'DASH/BNB', 'DASH/USDT', 'NANO/USDT', 'OMG/BNB', 'OMG/USDT', 'THETA/USDT', 'ENJ/USDT', 'MITH/USDT', 'MATIC/BNB', 'MATIC/BTC', 'MATIC/USDT', 'ATOM/BNB', 'ATOM/BTC', 'ATOM/USDT', 'ATOM/USDC', 'ATOM/PAX', 'ATOM/TUSD', 'ETC/USDC', 'ETC/PAX', 'ETC/TUSD', 'BAT/USDC', 'BAT/PAX', 'BAT/TUSD', 'PHB/BNB', 'PHB/BTC', 'PHB/USDC', 'PHB/TUSD', 'PHB/PAX', 'TFUEL/BNB', 'TFUEL/BTC', 'TFUEL/USDT', 'TFUEL/USDC', 'TFUEL/TUSD', 'TFUEL/PAX', 'ONE/BNB', 'ONE/BTC', 'ONE/USDT', 'ONE/TUSD', 'ONE/PAX', 'ONE/USDC', 'FTM/BNB', 'FTM/BTC', 'FTM/USDT', 'FTM/TUSD', 'FTM/PAX', 'FTM/USDC', 'BTCB/BTC', 'BCPT/TUSD', 'BCPT/PAX', 'BCPT/USDC', 'ALGO/BNB', 'ALGO/BTC', 'ALGO/USDT', 'ALGO/TUSD', 'ALGO/PAX', 'ALGO/USDC', 'USDSB/USDT', 'USDSB/USDS', 'GTO/USDT', 'GTO/PAX', 'GTO/TUSD', 'GTO/USDC', 'ERD/BNB', 'ERD/BTC', 'ERD/USDT', 'ERD/PAX', 'ERD/USDC', 'DOGE/BNB', 'DOGE/BTC', 'DOGE/USDT', 'DOGE/PAX', 'DOGE/USDC', 'DUSK/BNB', 'DUSK/BTC', 'DUSK/USDT', 'DUSK/USDC', 'DUSK/PAX', 'BGBP/USDC', 'ANKR/BNB', 'ANKR/BTC', 'ANKR/USDT', 'ANKR/TUSD', 'ANKR/PAX', 'ANKR/USDC', 'ONT/PAX', 'ONT/USDC', 'WIN/BNB', 'WIN/BTC', 'WIN/USDT', 'WIN/USDC', 'COS/BNB', 'COS/BTC', 'COS/USDT', 'TUSDB/TUSD', 'NPXS/USDT', 'NPXS/USDC', 'COCOS/BNB', 'COCOS/BTC', 'COCOS/USDT', 'MTL/USDT', 'TOMO/BNB', 'TOMO/BTC', 'TOMO/USDT', 'TOMO/USDC', 'PERL/BNB', 'PERL/BTC', 'PERL/USDC', 'PERL/USDT', 'DENT/USDT', 'MFT/USDT', 'KEY/USDT', 'STORM/USDT', 'DOCK/USDT', 'WAN/USDT', 'FUN/USDT', 'CVC/USDT', 'BTT/TRX', 'WIN/TRX', 'CHZ/BNB', 'CHZ/BTC', 'CHZ/USDT', 'BAND/BNB', 'BAND/BTC', 'BAND/USDT', 'BNB/BUSD', 'BTC/BUSD', 'BUSD/USDT', 'BEAM/BNB', 'BEAM/BTC', 'BEAM/USDT', 'XTZ/BNB', 'XTZ/BTC', 'XTZ/USDT', 'REN/USDT', 'RVN/USDT', 'HC/USDT', 'HBAR/BNB', 'HBAR/BTC', 'HBAR/USDT', 'NKN/BNB', 'NKN/BTC', 'NKN/USDT', 'XRP/BUSD', 'ETH/BUSD', 'BCH/BUSD', 'LTC/BUSD', 'LINK/BUSD', 'ETC/BUSD', 'STX/BNB', 'STX/BTC', 'STX/USDT', 'KAVA/BNB', 'KAVA/BTC', 'KAVA/USDT', 'BUSD/NGN', 'BNB/NGN', 'BTC/NGN', 'ARPA/BNB', 'ARPA/BTC', 'ARPA/USDT', 'TRX/BUSD', 'EOS/BUSD', 'IOTX/USDT', 'RLC/USDT', 'MCO/USDT', 'XLM/BUSD', 'ADA/BUSD', 'CTXC/BNB', 'CTXC/BTC', 'CTXC/USDT', 'BCH/BNB', 'BTC/RUB', 'ETH/RUB', 'XRP/RUB', 'BNB/RUB', 'TROY/BNB', 'TROY/BTC', 'TROY/USDT', 'BUSD/RUB', 'QTUM/BUSD', 'VET/BUSD', 'VITE/BNB', 'VITE/BTC', 'VITE/USDT', 'FTT/BNB', 'FTT/BTC', 'FTT/USDT', 'BTC/TRY', 'BNB/TRY', 'BUSD/TRY', 'ETH/TRY', 'XRP/TRY', 'USDT/TRY', 'USDT/RUB', 'BTC/EUR', 'ETH/EUR', 'BNB/EUR', 'XRP/EUR', 'EUR/BUSD', 'EUR/USDT', 'OGN/BNB', 'OGN/BTC', 'OGN/USDT', 'DREP/BNB', 'DREP/BTC', 'DREP/USDT', 'BULL/USDT', 'BULL/BUSD', 'BEAR/USDT', 'BEAR/BUSD', 'ETHBULL/USDT', 'ETHBULL/BUSD', 'ETHBEAR/USDT', 'ETHBEAR/BUSD', 'TCT/BNB', 'TCT/BTC', 'TCT/USDT', 'WRX/BNB', 'WRX/BTC', 'WRX/USDT', 'ICX/BUSD', 'BTS/USDT', 'BTS/BUSD', 'LSK/USDT', 'BNT/USDT', 'BNT/BUSD', 'LTO/BNB', 'LTO/BTC', 'LTO/USDT', 'ATOM/BUSD', 'DASH/BUSD', 'NEO/BUSD', 'WAVES/BUSD', 'XTZ/BUSD', 'EOSBULL/USDT', 'EOSBULL/BUSD', 'EOSBEAR/USDT', 'EOSBEAR/BUSD', 'XRPBULL/USDT', 'XRPBULL/BUSD', 'XRPBEAR/USDT', 'XRPBEAR/BUSD', 'BAT/BUSD', 'ENJ/BUSD', 'NANO/BUSD', 'ONT/BUSD', 'RVN/BUSD', 'STRAT/BUSD', 'STRAT/BNB', 'STRAT/USDT', 'AION/BUSD', 'AION/USDT', 'MBL/BNB', 'MBL/BTC', 'MBL/USDT', 'COTI/BNB', 'COTI/BTC', 'COTI/USDT', 'ALGO/BUSD', 'BTT/BUSD', 'TOMO/BUSD', 'XMR/BUSD', 'ZEC/BUSD', 'BNBBULL/USDT', 'BNBBULL/BUSD', 'BNBBEAR/USDT', 'BNBBEAR/BUSD', 'STPT/BNB', 'STPT/BTC', 'STPT/USDT', 'BTC/ZAR', 'ETH/ZAR', 'BNB/ZAR', 'USDT/ZAR', 'BUSD/ZAR', 'BTC/BKRW', 'ETH/BKRW', 'BNB/BKRW', 'WTC/USDT', 'DATA/BUSD', 'DATA/USDT', 'XZC/USDT', 'SOL/BNB', 'SOL/BTC', 'SOL/USDT', 'SOL/BUSD', 'BTC/IDRT', 'BNB/IDRT', 'USDT/IDRT', 'BUSD/IDRT', 'CTSI/BTC', 'CTSI/USDT', 'CTSI/BNB', 'CTSI/BUSD', 'HIVE/BNB', 'HIVE/BTC', 'HIVE/USDT', 'CHR/BNB', 'CHR/BTC', 'CHR/USDT', 'BTCUP/USDT', 'BTCDOWN/USDT', 'GXS/USDT', 'ARDR/USDT', 'ERD/BUSD', 'LEND/USDT', 'HBAR/BUSD', 'MATIC/BUSD', 'WRX/BUSD', 'ZIL/BUSD', 'MDT/BNB', 'MDT/BTC', 'MDT/USDT', 'STMX/BNB', 'STMX/BTC', 'STMX/ETH', 'STMX/USDT', 'KNC/BUSD', 'KNC/USDT', 'REP/BUSD', 'REP/USDT', 'LRC/BUSD', 'LRC/USDT', 'IQ/BNB', 'IQ/BUSD', 'PNT/BTC', 'PNT/USDT', 'BTC/GBP', 'ETH/GBP', 'XRP/GBP', 'BNB/GBP', 'GBP/BUSD', 'DGB/BNB', 'DGB/BTC', 'DGB/BUSD', 'BTC/UAH', 'USDT/UAH', 'COMP/BTC', 'COMP/BNB', 'COMP/BUSD', 'COMP/USDT', 'BTC/BIDR', 'ETH/BIDR', 'BNB/BIDR', 'BUSD/BIDR', 'USDT/BIDR', 'BKRW/USDT', 'BKRW/BUSD', 'SC/USDT', 'ZEN/USDT', 'SXP/BTC', 'SXP/BNB', 'SXP/BUSD', 'SNX/BTC', 'SNX/BNB', 'SNX/BUSD', 'SNX/USDT', 'ETHUP/USDT', 'ETHDOWN/USDT', 'ADAUP/USDT', 'ADADOWN/USDT', 'LINKUP/USDT', 'LINKDOWN/USDT', 'VTHO/BNB', 'VTHO/BUSD', 'VTHO/USDT', 'DCR/BUSD', 'DGB/USDT', 'GBP/USDT', 'STORJ/BUSD', 'SXP/USDT', 'IRIS/BNB', 'IRIS/BTC', 'IRIS/BUSD', 'MKR/BNB', 'MKR/BTC', 'MKR/USDT', 'MKR/BUSD', 'DAI/BNB', 'DAI/BTC', 'DAI/USDT', 'DAI/BUSD', 'RUNE/BNB', 'RUNE/BTC', 'RUNE/BUSD', 'MANA/BUSD', 'DOGE/BUSD', 'LEND/BUSD', 'ZRX/BUSD', 'DCR/USDT', 'STORJ/USDT', 'XRP/BKRW', 'ADA/BKRW', 'BTC/AUD', 'ETH/AUD', 'AUD/BUSD', 'FIO/BNB', 'FIO/BTC', 'FIO/BUSD', 'BNBUP/USDT', 'BNBDOWN/USDT', 'XTZUP/USDT', 'XTZDOWN/USDT', 'AVA/BNB', 'AVA/BTC', 'AVA/BUSD', 'USDT/BKRW', 'BUSD/BKRW', 'IOTA/BUSD', 'MANA/USDT', 'XRP/AUD', 'BNB/AUD', 'AUD/USDT', 'BAL/BNB', 'BAL/BTC', 'BAL/BUSD', 'YFI/BNB', 'YFI/BTC', 'YFI/BUSD', 'YFI/USDT', 'BLZ/BUSD', 'KMD/BUSD', 'BAL/USDT', 'BLZ/USDT', 'IRIS/USDT', 'KMD/USDT', 'BTC/DAI', 'ETH/DAI', 'BNB/DAI', 'USDT/DAI', 'BUSD/DAI', 'JST/BNB', 'JST/BTC', 'JST/BUSD', 'JST/USDT', 'SRM/BNB', 'SRM/BTC', 'SRM/BUSD', 'SRM/USDT', 'ANT/BNB', 'ANT/BTC', 'ANT/BUSD', 'ANT/USDT', 'CRV/BNB', 'CRV/BTC', 'CRV/BUSD', 'CRV/USDT', 'SAND/BNB', 'SAND/BTC', 'SAND/USDT', 'SAND/BUSD', 'OCEAN/BNB', 'OCEAN/BTC', 'OCEAN/BUSD', 'OCEAN/USDT', 'NMR/BNB', 'NMR/BTC', 'NMR/BUSD', 'NMR/USDT', 'DOT/BNB', 'DOT/BTC', 'DOT/BUSD', 'DOT/USDT', 'LUNA/BNB', 'LUNA/BTC', 'LUNA/BUSD', 'LUNA/USDT', 'IDEX/BTC', 'IDEX/BUSD', 'RSR/BNB', 'RSR/BTC', 'RSR/BUSD', 'RSR/USDT', 'PAXG/BNB', 'PAXG/BTC', 'PAXG/BUSD', 'PAXG/USDT', 'WNXM/BNB', 'WNXM/BTC', 'WNXM/BUSD', 'WNXM/USDT', 'TRB/BNB', 'TRB/BTC', 'TRB/BUSD', 'TRB/USDT', 'ETH/NGN', 'DOT/BIDR', 'LINK/AUD', 'SXP/AUD', 'BZRX/BNB', 'BZRX/BTC', 'BZRX/BUSD', 'BZRX/USDT', 'WBTC/BTC', 'WBTC/ETH']

    # keyList3 = ['SUSHI/BNB', 'SUSHI/BTC', 'SUSHI/BUSD', 'SUSHI/USDT', 'YFII/BNB', 'YFII/BTC', 'YFII/BUSD', 'YFII/USDT', 'KSM/BNB', 'KSM/BTC', 'KSM/BUSD', 'KSM/USDT', 'EGLD/BNB', 'EGLD/BTC', 'EGLD/BUSD', 'EGLD/USDT', 'DIA/BNB', 'DIA/BTC', 'DIA/BUSD', 'DIA/USDT', 'RUNE/USDT', 'FIO/USDT', 'UMA/BTC', 'UMA/USDT', 'EOSUP/USDT', 'EOSDOWN/USDT', 'TRXUP/USDT', 'TRXDOWN/USDT', 'XRPUP/USDT', 'XRPDOWN/USDT', 'DOTUP/USDT', 'DOTDOWN/USDT', 'SRM/BIDR', 'ONE/BIDR', 'LINK/TRY', 'USDT/NGN', 'BEL/BNB', 'BEL/BTC', 'BEL/BUSD', 'BEL/USDT', 'WING/BNB', 'WING/BTC', 'SWRV/BNB', 'SWRV/BUSD', 'WING/BUSD', 'WING/USDT', 'LTCUP/USDT', 'LTCDOWN/USDT', 'LEND/BKRW', 'SXP/EUR', 'CREAM/BNB', 'CREAM/BUSD', 'UNI/BNB', 'UNI/BTC', 'UNI/BUSD', 'UNI/USDT', 'NBS/BTC', 'NBS/USDT', 'OXT/BTC', 'OXT/USDT', 'SUN/BTC', 'SUN/USDT', 'AVAX/BNB', 'AVAX/BTC', 'AVAX/BUSD', 'AVAX/USDT', 'HNT/BTC', 'HNT/USDT', 'BAKE/BNB', 'BURGER/BNB', 'SXP/BIDR', 'LINK/BKRW', 'FLM/BNB', 'FLM/BTC', 'FLM/BUSD', 'FLM/USDT', 'SCRT/BTC', 'SCRT/ETH', 'CAKE/BNB', 'CAKE/BUSD', 'SPARTA/BNB', 'UNIUP/USDT', 'UNIDOWN/USDT', 'ORN/BTC', 'ORN/USDT', 'TRX/NGN', 'SXP/TRY', 'UTK/BTC', 'UTK/USDT', 'XVS/BNB', 'XVS/BTC', 'XVS/BUSD', 'XVS/USDT', 'ALPHA/BNB', 'ALPHA/BTC', 'ALPHA/BUSD', 'ALPHA/USDT', 'VIDT/BTC', 'VIDT/BUSD', 'AAVE/BNB', 'BTC/BRL', 'USDT/BRL', 'AAVE/BTC', 'AAVE/ETH', 'AAVE/BUSD', 'AAVE/USDT', 'AAVE/BKRW', 'NEAR/BNB', 'NEAR/BTC', 'NEAR/BUSD', 'NEAR/USDT', 'SXPUP/USDT', 'SXPDOWN/USDT', 'DOT/BKRW', 'SXP/GBP', 'FIL/BNB', 'FIL/BTC', 'FIL/BUSD', 'FIL/USDT', 'FILUP/USDT', 'FILDOWN/USDT', 'YFIUP/USDT', 'YFIDOWN/USDT', 'INJ/BNB', 'INJ/BTC', 'INJ/BUSD', 'INJ/USDT', 'AERGO/BTC', 'AERGO/BUSD', 'LINK/EUR', 'ONE/BUSD', 'EASY/ETH', 'AUDIO/BTC', 'AUDIO/BUSD', 'AUDIO/USDT', 'CTK/BNB', 'CTK/BTC', 'CTK/BUSD', 'CTK/USDT', 'BCHUP/USDT', 'BCHDOWN/USDT', 'BOT/BTC', 'BOT/BUSD', 'ETH/BRL', 'DOT/EUR', 'AKRO/BTC', 'AKRO/USDT', 'KP3R/BNB', 'KP3R/BUSD', 'AXS/BNB', 'AXS/BTC', 'AXS/BUSD', 'AXS/USDT', 'HARD/BNB', 'HARD/BTC', 'HARD/BUSD', 'HARD/USDT', 'BNB/BRL', 'LTC/EUR', 'RENBTC/BTC', 'RENBTC/ETH', 'DNT/BUSD', 'DNT/USDT', 'SLP/ETH', 'ADA/EUR', 'LTC/NGN', 'CVP/ETH', 'CVP/BUSD', 'STRAX/BTC', 'STRAX/ETH', 'STRAX/BUSD', 'STRAX/USDT', 'FOR/BTC', 'FOR/BUSD', 'UNFI/BNB', 'UNFI/BTC', 'UNFI/BUSD', 'UNFI/USDT', 'FRONT/ETH', 'FRONT/BUSD', 'BCHA/BUSD', 'ROSE/BTC', 'ROSE/BUSD', 'ROSE/USDT', 'AVAX/TRY', 'BUSD/BRL', 'AVA/USDT', 'SYS/BUSD', 'XEM/USDT', 'HEGIC/ETH', 'HEGIC/BUSD', 'AAVEUP/USDT', 'AAVEDOWN/USDT', 'PROM/BNB', 'PROM/BUSD', 'XRP/BRL', 'XRP/NGN', 'SKL/BTC', 'SKL/BUSD', 'SKL/USDT', 'BCH/EUR', 'YFI/EUR', 'ZIL/BIDR', 'SUSD/BTC', 'SUSD/ETH', 'SUSD/USDT', 'COVER/ETH', 'COVER/BUSD', 'GLM/BTC', 'GLM/ETH', 'GHST/ETH', 'GHST/BUSD', 'SUSHIUP/USDT', 'SUSHIDOWN/USDT', 'XLMUP/USDT', 'XLMDOWN/USDT', 'LINK/BRL', 'LINK/NGN', 'LTC/RUB', 'TRX/TRY', 'XLM/EUR', 'DF/ETH', 'DF/BUSD', 'GRT/BTC', 'GRT/ETH', 'GRT/USDT', 'JUV/BTC', 'JUV/BUSD', 'JUV/USDT', 'PSG/BTC', 'PSG/BUSD', 'PSG/USDT', 'BUSD/BVND', 'USDT/BVND', '1INCH/BTC', '1INCH/USDT', 'REEF/BTC', 'REEF/USDT', 'OG/BTC', 'OG/USDT', 'ATM/BTC', 'ATM/USDT', 'ASR/BTC', 'ASR/USDT', 'CELO/BTC', 'CELO/USDT', 'RIF/BTC', 'RIF/USDT', 'CHZ/TRY', 'XLM/TRY', 'LINK/GBP', 'GRT/EUR', 'BTCST/BTC', 'BTCST/BUSD', 'BTCST/USDT', 'TRU/BTC', 'TRU/BUSD', 'TRU/USDT', 'DEXE/ETH', 'DEXE/BUSD', 'EOS/EUR', 'LTC/BRL', 'USDC/BUSD', 'TUSD/BUSD', 'PAX/BUSD', 'CKB/BTC', 'CKB/BUSD', 'CKB/USDT', 'TWT/BTC', 'TWT/BUSD', 'TWT/USDT', 'FIRO/BTC', 'FIRO/ETH', 'FIRO/USDT', 'BETH/ETH', 'DOGE/EUR', 'DOGE/TRY', 'DOGE/AUD', 'DOGE/BRL', 'DOT/NGN', 'PROS/ETH', 'LIT/BTC', 'LIT/BUSD', 'LIT/USDT', 'BTC/VAI', 'BUSD/VAI', 'SFP/BTC', 'SFP/BUSD', 'SFP/USDT', 'DOGE/GBP', 'DOT/TRY', 'FXS/BTC', 'FXS/BUSD', 'DODO/BTC', 'DODO/BUSD', 'DODO/USDT', 'FRONT/BTC', 'EASY/BTC', 'CAKE/BTC', 'CAKE/USDT', 'BAKE/BUSD', 'UFT/ETH', 'UFT/BUSD', '1INCH/BUSD', 'BAND/BUSD', 'GRT/BUSD', 'IOST/BUSD', 'OMG/BUSD', 'REEF/BUSD', 'ACM/BTC', 'ACM/BUSD', 'ACM/USDT', 'AUCTION/BTC', 'AUCTION/BUSD', 'PHA/BTC', 'PHA/BUSD', 'DOT/GBP', 'ADA/TRY', 'ADA/BRL', 'ADA/GBP', 'TVK/BTC', 'TVK/BUSD', 'BADGER/BTC', 'BADGER/BUSD', 'BADGER/USDT', 'FIS/BTC', 'FIS/BUSD', 'FIS/USDT', 'DOT/BRL', 'ADA/AUD', 'HOT/TRY', 'EGLD/EUR', 'OM/BTC', 'OM/BUSD', 'OM/USDT', 'POND/BTC', 'POND/BUSD', 'POND/USDT', 'DEGO/BTC', 'DEGO/BUSD', 'DEGO/USDT', 'AVAX/EUR', 'BTT/TRY', 'CHZ/BRL', 'UNI/EUR', 'ALICE/BTC', 'ALICE/BUSD', 'ALICE/USDT', 'CHZ/BUSD', 'CHZ/EUR', 'CHZ/GBP', 'BIFI/BNB', 'BIFI/BUSD', 'LINA/BTC', 'LINA/BUSD', 'LINA/USDT', 'ADA/RUB', 'ENJ/BRL', 'ENJ/EUR', 'MATIC/EUR', 'NEO/TRY', 'PERP/BTC', 'PERP/BUSD', 'PERP/USDT', 'RAMP/BTC', 'RAMP/BUSD', 'RAMP/USDT', 'SUPER/BTC', 'SUPER/BUSD', 'SUPER/USDT', 'CFX/BTC', 'CFX/BUSD', 'CFX/USDT', 'ENJ/GBP', 'EOS/TRY', 'LTC/GBP', 'LUNA/EUR', 'RVN/TRY', 'THETA/EUR', 'XVG/BUSD', 'EPS/BTC', 'EPS/BUSD', 'EPS/USDT', 'AUTO/BTC', 'AUTO/BUSD', 'AUTO/USDT', 'TKO/BTC', 'TKO/BIDR', 'TKO/BUSD', 'TKO/USDT', 'PUNDIX/ETH', 'PUNDIX/USDT', 'BTT/BRL', 'BTT/EUR', 'HOT/EUR', 'WIN/EUR', 'TLM/BTC', 'TLM/BUSD', 'TLM/USDT', '1INCHUP/USDT', '1INCHDOWN/USDT', 'BTG/BUSD', 'BTG/USDT', 'HOT/BUSD', 'BNB/UAH', 'ONT/TRY', 'VET/EUR', 'VET/GBP', 'WIN/BRL', 'MIR/BTC', 'MIR/BUSD', 'MIR/USDT', 'BAR/BTC', 'BAR/BUSD', 'BAR/USDT', 'FORTH/BTC', 'FORTH/BUSD', 'FORTH/USDT', 'CAKE/GBP', 'DOGE/RUB', 'HOT/BRL', 'WRX/EUR', 'EZ/BTC', 'EZ/ETH', 'BAKE/USDT', 'BURGER/BUSD', 'BURGER/USDT', 'SLP/BUSD', 'SLP/USDT', 'TRX/AUD', 'TRX/EUR', 'VET/TRY', 'SHIB/USDT', 'SHIB/BUSD', 'ICP/BTC', 'ICP/BNB', 'ICP/BUSD', 'ICP/USDT', 'BTC/GYEN', 'USDT/GYEN', 'SHIB/EUR', 'SHIB/RUB', 'ETC/EUR', 'ETC/BRL', 'DOGE/BIDR', 'AR/BTC', 'AR/BNB', 'AR/BUSD', 'AR/USDT', 'POLS/BTC', 'POLS/BNB', 'POLS/BUSD', 'POLS/USDT', 'MDX/BTC', 'MDX/BNB', 'MDX/BUSD', 'MDX/USDT', 'MASK/BNB', 'MASK/BUSD', 'MASK/USDT', 'LPT/BTC', 'LPT/BNB', 'LPT/BUSD', 'LPT/USDT', 'ETH/UAH', 'MATIC/BRL', 'SOL/EUR', 'SHIB/BRL', 'AGIX/BTC', 'ICP/EUR', 'MATIC/GBP', 'SHIB/TRY', 'MATIC/BIDR', 'MATIC/RUB', 'NU/BTC', 'NU/BNB', 'NU/BUSD', 'NU/USDT', 'XVG/USDT', 'RLC/BUSD', 'CELR/BUSD', 'ATM/BUSD', 'ZEN/BUSD', 'FTM/BUSD', 'THETA/BUSD', 'WIN/BUSD', 'KAVA/BUSD', 'XEM/BUSD', 'ATA/BTC', 'ATA/BNB', 'ATA/BUSD', 'ATA/USDT', 'GTC/BTC', 'GTC/BNB', 'GTC/BUSD', 'GTC/USDT', 'TORN/BTC', 'TORN/BNB', 'TORN/BUSD', 'TORN/USDT', 'MATIC/TRY', 'ETC/GBP', 'SOL/GBP', 'BAKE/BTC', 'COTI/BUSD', 'KEEP/BTC', 'KEEP/BNB', 'KEEP/BUSD', 'KEEP/USDT', 'SOL/TRY', 'RUNE/GBP', 'SOL/BRL', 'SC/BUSD', 'CHR/BUSD', 'STMX/BUSD', 'HNT/BUSD', 'FTT/BUSD', 'DOCK/BUSD', 'ADA/BIDR', 'ERN/BNB', 'ERN/BUSD', 'ERN/USDT', 'KLAY/BTC', 'KLAY/BNB', 'KLAY/BUSD', 'KLAY/USDT', 'RUNE/EUR', 'MATIC/AUD', 'DOT/RUB', 'UTK/BUSD', 'IOTX/BUSD', 'PHA/USDT', 'SOL/RUB', 'RUNE/AUD', 'BUSD/UAH', 'BOND/BTC', 'BOND/BNB', 'BOND/BUSD', 'BOND/USDT', 'MLN/BTC', 'MLN/BNB', 'MLN/BUSD', 'MLN/USDT', 'GRT/TRY', 'CAKE/BRL', 'ICP/RUB', 'DOT/AUD', 'AAVE/BRL', 'EOS/AUD', 'DEXE/USDT', 'LTO/BUSD', 'ADX/BUSD', 'QUICK/BTC', 'QUICK/BNB', 'QUICK/BUSD', 'C98/USDT', 'C98/BUSD', 'C98/BNB', 'C98/BTC', 'CLV/BTC', 'CLV/BNB', 'CLV/BUSD', 'CLV/USDT', 'QNT/BTC', 'QNT/BNB', 'QNT/BUSD', 'QNT/USDT', 'FLOW/BTC', 'FLOW/BNB', 'FLOW/BUSD', 'FLOW/USDT', 'XEC/BUSD', 'AXS/BRL', 'AXS/AUD', 'TVK/USDT', 'MINA/BTC', 'MINA/BNB', 'MINA/BUSD', 'MINA/USDT', 'RAY/BNB', 'RAY/BUSD', 'RAY/USDT', 'FARM/BTC', 'FARM/BNB', 'FARM/BUSD', 'FARM/USDT', 'ALPACA/BTC', 'ALPACA/BNB', 'ALPACA/BUSD', 'ALPACA/USDT', 'TLM/TRY', 'QUICK/USDT', 'ORN/BUSD', 'MBOX/BTC', 'MBOX/BNB', 'MBOX/BUSD', 'MBOX/USDT', 'VGX/BTC', 'VGX/ETH', 'FOR/USDT', 'REQ/USDT', 'GHST/USDT', 'TRU/RUB', 'FIS/BRL', 'WAXP/USDT', 'WAXP/BUSD', 'WAXP/BNB', 'WAXP/BTC', 'TRIBE/BTC', 'TRIBE/BNB', 'TRIBE/BUSD', 'TRIBE/USDT', 'GNO/USDT', 'GNO/BUSD', 'GNO/BNB', 'GNO/BTC', 'ARPA/TRY', 'PROM/BTC', 'MTL/BUSD', 'OGN/BUSD', 'XEC/USDT', 'C98/BRL', 'SOL/AUD', 'SUSHI/BIDR', 'XRP/BIDR', 'POLY/BUSD', 'ELF/USDT', 'DYDX/USDT', 'DYDX/BUSD', 'DYDX/BNB', 'DYDX/BTC', 'ELF/BUSD', 'POLY/USDT', 'IDEX/USDT', 'VIDT/USDT', 'SOL/BIDR', 'AXS/BIDR', 'BTC/USDP', 'ETH/USDP', 'BNB/USDP', 'USDP/BUSD', 'USDP/USDT', 'GALA/USDT', 'GALA/BUSD', 'GALA/BNB', 'GALA/BTC', 'FTM/BIDR', 'ALGO/BIDR', 'CAKE/AUD', 'KSM/AUD', 'WAVES/RUB', 'SUN/BUSD', 'ILV/USDT', 'ILV/BUSD', 'ILV/BNB', 'ILV/BTC', 'REN/BUSD', 'YGG/USDT', 'YGG/BUSD', 'YGG/BNB', 'YGG/BTC', 'STX/BUSD', 'SYS/USDT', 'DF/USDT', 'SOL/USDC', 'ARPA/RUB', 'LTC/UAH', 'FET/BUSD', 'ARPA/BUSD', 'LSK/BUSD', 'AVAX/BIDR', 'ALICE/BIDR', 'FIDA/USDT', 'FIDA/BUSD', 'FIDA/BNB', 'FIDA/BTC', 'DENT/BUSD', 'FRONT/USDT', 'CVP/USDT', 'AGLD/BTC', 'AGLD/BNB', 'AGLD/BUSD', 'AGLD/USDT', 'RAD/BTC', 'RAD/BNB', 'RAD/BUSD', 'RAD/USDT', 'UNI/AUD', 'HIVE/BUSD', 'STPT/BUSD', 'BETA/BTC', 'BETA/BNB', 'BETA/BUSD', 'BETA/USDT', 'SHIB/AUD', 'RARE/BTC', 'RARE/BNB', 'RARE/BUSD', 'RARE/USDT', 'AVAX/BRL', 'AVAX/AUD', 'LUNA/AUD', 'TROY/BUSD', 'AXS/ETH', 'FTM/ETH', 'SOL/ETH', 'SSV/BTC', 'SSV/ETH', 'LAZIO/TRY', 'LAZIO/EUR', 'LAZIO/BTC', 'LAZIO/USDT', 'CHESS/BTC', 'CHESS/BNB', 'CHESS/BUSD', 'CHESS/USDT', 'FTM/AUD', 'FTM/BRL', 'SCRT/BUSD']
    # keyList = keyList1 + keyList2 + keyList3
    # busdList=[]

    # for i in range(len(keyList)):
    #     if '/BUSD' in keyList[i]:
    #         busdList.append(keyList[i])
    # binance_db = binance.fetch_tickers(symbols=busdList,params={})
    # BTCList = []

    # for i in range(len(busdList)):
    #     name = busdList[i]

    #     Binance_M = (binance_db[name]['symbol'])
    #     Binance_C = (binance_db[name]['info']['priceChangePercent'])
    #     Binance_T = (binance_db[name]['timestamp'])
    #     Binance_P = (binance_db[name]['info']['lastPrice'])
    #     Binance_V = (binance_db[name]['info']['volume']) 

    #     Binance = {'market':Binance_M ,'change_rate':Binance_C,'trade_timestamp':Binance_T,'trade_price':Binance_P,'trade_volume':Binance_V}
        
    #     BTCList.append(Binance)

    # try:
    #     return json.dumps(BTCList)
    # except Exception as e:
    #     print(str(e))
    #     return jsonify(str(e))
    binance = ccxt.binance()
    binance_db = binance.fetch_ticker(symbol='BTC/BUSD',params={})

    BTCList = []
    Binance_T = (binance_db['timestamp'])
    Binance_P = (binance_db['info']['lastPrice'])

    Binance = {'trade_timestamp':Binance_T,'trade_price':Binance_P}
    
    dbModule.execute("INSERT INTO Binance_bitcoin_price_tx(time_stamp, price) VALUES('{0}', '{1}');".format(Binance['trade_timestamp'], Binance['trade_price']))
        
    BTCList.append(Binance)
    
    dbModule.commit();
        
    try:
        return json.dumps(BTCList)
    except Exception as e:
        print(str(e))
            
        return jsonify(str(e))

   


# 빗썸 OPEN
# @app.route('/bithumb-openapi',methods=['GET'])
# def getPrice2():
#    bithumb= ccxt.bithumb()
#    keyList = ['BTC/KRW','ETH/KRW']
#    krwList = []
   
#    for i in range(len(keyList)):
#        if '/KRW' in keyList[i]:
#            krwList.append(keyList[i])
#     bithumb_db = bithumb.fetch_tickers(symbols=krwList,params={})
#     print(bithumb_db)
#     BTCList = []

#     for i in range(len(krwList)):
#         name = krwList[i]
#         Bithumb_T = (bithumb_db[name]['timestamp'])
#         Bithumb_P = (bithumb_db[name]['info']['last'])

#         Bithumb = {'trade_timestamp':Bithumb_T,'trade_price':Bithumb_P}
#         BTCList.append(Bithumb)
        
#     try:
#         return json.dumps(BTCList)
#     except Exception as e:
#         print(str(e))
            
#         return jsonify(str(e)) 

        ''''''
    # bithumb = ccxt.bithumb()
    # keyList = ['BTC/KRW', 'ETH/KRW', 'LTC/KRW', 'ETC/KRW', 'XRP/KRW', 'BCH/KRW', 'QTUM/KRW', 'BTG/KRW', 'EOS/KRW', 'ICX/KRW', 'TRX/KRW', 'ELF/KRW', 'OMG/KRW', 'KNC/KRW', 'GLM/KRW', 'ZIL/KRW', 'WAXP/KRW', 'POWR/KRW', 'LRC/KRW', 'STEEM/KRW', 'STRAX/KRW', 'ZRX/KRW', 'REP/KRW', 'XEM/KRW', 'SNT/KRW', 'ADA/KRW', 'CTXC/KRW', 'BAT/KRW', 'WTC/KRW', 'THETA/KRW', 'LOOM/KRW', 'WAVES/KRW', 'TRUE/KRW', 'LINK/KRW', 'ENJ/KRW', 'VET/KRW', 'MTL/KRW', 'IOST/KRW', 'TMTG/KRW', 'QKC/KRW', 'HDAC/KRW', 'AMO/KRW', 'BSV/KRW', 'ORBS/KRW', 'TFUEL/KRW', 'VALOR/KRW', 'CON/KRW', 'ANKR/KRW', 'MIX/KRW', 'CRO/KRW', 'FX/KRW', 'CHR/KRW', 'MBL/KRW', 'MXC/KRW', 'FCT/KRW', 'TRV/KRW', 'DAD/KRW', 'WOM/KRW', 'SOC/KRW', 'EM/KRW', 'BOA/KRW', 'FLETA/KRW', 'SXP/KRW', 'COS/KRW', 'APIX/KRW', 'EL/KRW', 'BASIC/KRW', 'HIVE/KRW', 'XPR/KRW', 'VRA/KRW', 'FIT/KRW', 'EGG/KRW', 'BORA/KRW', 'ARPA/KRW', 'APM/KRW', 'CKB/KRW', 'AERGO/KRW', 'ANW/KRW', 'CENNZ/KRW', 'EVZ/KRW', 'CYCLUB/KRW', 'SRM/KRW', 'QTCON/KRW', 'UNI/KRW', 'YFI/KRW', 'UMA/KRW', 'AAVE/KRW', 'COMP/KRW', 'REN/KRW', 'BAL/KRW', 'RSR/KRW', 'NMR/KRW', 'RLC/KRW', 'UOS/KRW', 'SAND/KRW', 'GOM2/KRW', 'RINGX/KRW', 'BEL/KRW', 'OBSR/KRW', 'ORC/KRW', 'POLA/KRW', 'AWO/KRW', 'ADP/KRW', 'DVI/KRW', 'GHX/KRW', 'MIR/KRW', 'MVC/KRW', 'BLY/KRW', 'WOZX/KRW', 'ANV/KRW', 'GRT/KRW', 'MM/KRW', 'BIOT/KRW', 'XNO/KRW', 'SNX/KRW', 'RAI/KRW', 'COLA/KRW', 'NU/KRW', 'OXT/KRW', 'LINA/KRW', 'MAP/KRW', 'AQT/KRW', 'WIKEN/KRW', 'CTSI/KRW', 'MANA/KRW', 'LPT/KRW', 'MKR/KRW', 'SUSHI/KRW', 'ASM/KRW', 'PUNDIX/KRW', 'CELR/KRW', 'LF/KRW', 'ARW/KRW', 'MSB/KRW', 'RLY/KRW', 'OCEAN/KRW', 'BFC/KRW', 'ALICE/KRW', 'CAKE/KRW', 'BNT/KRW', 'XVS/KRW', 'CHZ/KRW', 'AXS/KRW', 'DAI/KRW', 'MATIC/KRW', 'BAKE/KRW', 'VELO/KRW', 'BCD/KRW', 'XLM/KRW', 'GXC/KRW', 'BTT/KRW', 'VSYS/KRW', 'IPX/KRW', 'WICC/KRW', 'ONT/KRW', 'LUNA/KRW', 'AION/KRW', 'META/KRW', 'KLAY/KRW', 'ONG/KRW', 'ALGO/KRW', 'JST/KRW', 'XTZ/KRW', 'MLK/KRW', 'WEMIX/KRW', 'DOT/KRW', 'ATOM/KRW', 'SSX/KRW', 'TEMCO/KRW', 'HIBS/KRW', 'BURGER/KRW', 'DOGE/KRW', 'KSM/KRW', 'CTK/KRW', 'XYM/KRW', 'BNB/KRW', 'SUN/KRW', 'XEC/KRW', 'PCI/KRW', 'SOL/KRW']
    # krwList=[]
    
    # for i in range(len(keyList)):
    #     if '/KRW' in keyList[i]:
    #         krwList.append(keyList[i])
    
    # bithumb_db = bithumb.fetch_tickers(symbols=krwList,params={})
    # BTCList = []

    # for i in range(len(krwList)):
    #     name = krwList[i]

    #     Bithumb_M = (bithumb_db[name]['symbol'])
    #     Bithumb_C = (bithumb_db[name]['percentage'])
    #     Bithumb_T = (bithumb_db[name]['timestamp'])
    #     Bithumb_P = (bithumb_db[name]['last'])
    #     Bithumb_V = (bithumb_db[name]['info']['acc_trade_value']) 

    #     Bithumb = {'market':Bithumb_M ,'change_rate':Bithumb_C,'trade_timestamp':Bithumb_T,'trade_price':Bithumb_P,'trade_volume':Bithumb_V}
        
    #     BTCList.append(Bithumb)

    # try:
    #     return json.dumps(BTCList)
    # except Exception as e:
    #     print(str(e))
    #     return jsonify(str(e))

    # bithumb = ccxt.bithumb()
    # bithumb_db = bithumb.fetch_ticker(symbol='BTC/KRW',params={})
    # print(bithumb_db)
    # BTCList = []
    # Bithumb_T = (bithumb_db['timestamp'])
    # Bithumb_P = (bithumb_db['last'])

    # Bithumb = {'trade_timestamp':Bithumb_T,'trade_price':Bithumb_P}
    
    # dbModule.execute("INSERT INTO Bithumb_bitcoin_price_tx(time_stamp, price) VALUES('{0}', '{1}');".format(Bithumb['trade_timestamp'], Bithumb['trade_price']))
        
    # BTCList.append(Bithumb)
    
    # dbModule.commit();
        
    # try:
    #     return json.dumps(BTCList)
    # except Exception as e:
    #     print(str(e))
            
    #     return jsonify(str(e))

   
    

# 코인원 OPEN
@app.route('/coinone-openapi',methods=['GET'])
def getPrice3():
    coinone= ccxt.coinone()
    keyList = ['BTC/KRW','ETH/KRW']
    krwList = []

    for i in range(len(keyList)):
        if '/KRW' in keyList[i]:
            krwList.append(keyList[i])

    coinone_db = coinone.fetch_tickers(symbols=krwList,params={})
    print(coinone_db)
    BTCList = []

    for i in range(len(krwList)):
        name = krwList[i]
        Coinone_T = (coinone_db[name]['timestamp'])
        Coinone_P = (coinone_db[name]['info']['last'])

        Coinone = {'trade_timestamp':Coinone_T,'trade_price':Coinone_P}
        BTCList.append(Coinone)
        
    try:
        return json.dumps(BTCList)
    except Exception as e:
        print(str(e))
            
        return jsonify(str(e))

    '''
    # coinone = ccxt.coinone()
    # keyList = ['XEC/KRW', 'DOGE/KRW', 'FIS/KRW', 'CRO/KRW', 'LIT/KRW', 'MEGA/KRW', 'TVK/KRW', 'PHA/KRW', 'ICX/KRW', 'UNI/KRW', 'FIL/KRW', 'ATT/KRW', 'LZM/KRW', 'MLK/KRW', 'POD/KRW', 'CAD/KRW', 'VIVI/KRW', 'TRIX/KRW', 'GRT/KRW', 'TOROCUS/KRW', 'RUSH/KRW', '1INCH/KRW', 'QTBK/KRW', 'FLOW/KRW', 'CBK/KRW', 'CELEB/KRW', 'CBANK/KRW', 'LINA/KRW', 'KSP/KRW', 'MIR/KRW', 'HANDY/KRW', 'BMP/KRW', 'ORC/KRW', 'DVI/KRW', 'PICA/KRW', 'MVC/KRW', 'BEL/KRW', 'TMC/KRW', 'TEN/KRW', 'CKB/KRW', 'DIA/KRW', 'CTSI/KRW', 'STND/KRW', 'SXP/KRW', 'KSM/KRW', 'IPX/KRW', 'VSYS/KRW', 'MAP/KRW', 'BZRX/KRW', 'NEST/KRW', 'SIX/KRW', 'KAI/KRW', 'CRV/KRW', 'DODO/KRW', 'UMA/KRW', 'KLAY/KRW', 'TMTG/KRW', 'JST/KRW', 'SHOW/KRW', 'BORA/KRW', 'GOM2/KRW', 'FET/KRW', 'MCH/KRW', 'LINK/KRW', 'COS/KRW', 'LBXC/KRW', 'ISDT/KRW', 'BNT/KRW', 'BAL/KRW', 'XPN/KRW', 'AOA/KRW', 'HIBS/KRW', 'IOTX/KRW', 'CLV/KRW', 'DRM/KRW', 'PCI/KRW', 'AAVE/KRW', 'MSB/KRW', 'BAAS/KRW', 'SUN/KRW', 'UOS/KRW', 'KAVA/KRW', 'ARPA/KRW', 'MNR/KRW', 'HUM/KRW', 'Soda Coin/KRW', 'AUCTION/KRW', 'BNA/KRW', 'PROM/KRW', 'ANC/KRW', 'KSC/KRW', 'PIB/KRW', 'NFUP/KRW', 'REDI/KRW', 'DRC/KRW', 'ABL/KRW', 'ISR/KRW', 'STPL/KRW', 'FLETA/KRW', 'SKLAY/KRW', 'BAT/KRW', 'LUNA/KRW', 'AIP/KRW', 'NEO/KRW', 'ASM/KRW', 'DAD/KRW', 'HINT/KRW', 'SAND/KRW', 'EGG/KRW', 'STPT/KRW', 'AMO/KRW', 'SNX/KRW', 'TRCL/KRW', 'IDV/KRW', 'MATIC/KRW', 'KDAG/KRW', 'TOMOE/KRW', 'BSV/KRW', 'BTT/KRW', 'CAMP/KRW', 'DOT/KRW', 'PXL/KRW', 'XLM/KRW', 'TEMCO/KRW', 'BIOT/KRW', 'ADA/KRW', 'DVX/KRW', 'BTG/KRW', 'LUA/KRW', 'LTC/KRW', 'QTCON/KRW', 'MOV/KRW', 'IOTA/KRW', 'SOBA/KRW', 'PURE/KRW', 'RNX/KRW', 'DATA/KRW', 'TOM/KRW', 'EXE/KRW', 'ASTA/KRW', 'ZRX/KRW', 'BCH/KRW', 'IBP/KRW', 'KNC/KRW', 'ATOM/KRW', 'ANKR/KRW', 'TIP/KRW', 'ETC/KRW', 'ETH/KRW', 'BTC/KRW', 'SUSHI/KRW', 'DUCATO/KRW', 'INJ/KRW', 'AXS/KRW', 'FRONT/KRW', 'ALPHA/KRW', 'SRM/KRW', 'FTT/KRW', 'ONX/KRW', 'HARD/KRW', 'HOT/KRW', 'OGN/KRW', 'MBL/KRW', 'STAKE/KRW', 'GAS/KRW', 'BAND/KRW', 'ORBS/KRW', 'ONG/KRW', 'CLB/KRW', 'TRX/KRW', 'ZIL/KRW', 'AXL/KRW', 'QTUM/KRW', 'EOS/KRW', 'ONT/KRW', 'XTZ/KRW', 'XRP/KRW', 'WNCG/KRW', 'SOL/KRW', 'SKU/KRW', 'AVAX/KRW', 'BASIC/KRW', 'DON/KRW', 'MTS/KRW', 'BFC/KRW', 'ACH/KRW', 'GET/KRW', 'COMP/KRW', 'KRT/KRW', 'MTA/KRW', 'OMG/KRW', 'REN/KRW', 'WIKEN/KRW', 'CRU/KRW']
    # krwList = []
    
    # for i in range(len(keyList)):
    #     if '/KRW' in keyList[i]:
    #         krwList.append(keyList[i])
        
    # coinone_db = coinone.fetch_tickers(symbols=krwList,params={})
    # BTCList = []

    # for i in range(len(krwList)):
    #     name = krwList[i]
    #     Coinone_M = (coinone_db[name]['symbol'])
    #     Coinone_C = (coinone_db[name]['percentage'])
    #     Coinone_T = (coinone_db[name]['timestamp'])
    #     Coinone_P = (coinone_db[name]['info']['last'])
    #     Coinone_V = (coinone_db[name]['info']['volume']) 

    #     Coinone = {'market':Coinone_M ,'change_rate':Coinone_C,'trade_timestamp':Coinone_T,'trade_price':Coinone_P,'trade_volume':Coinone_V}

    #     BTCList.append(Coinone)

    # try:
    #     return json.dumps(BTCList)
    # except Exception as e:
    #     print(str(e))
    #     return jsonify(str(e))
'''


#업비트 Open
@app.route('/upbit-openapi',methods=['GET'])
def getPrice4():
    upbit = ccxt.upbit()
    keyList = ['BTC/KRW','ETH/KRW']
    krwList = []

    for i in range(len(keyList)):
        if '/KRW' in keyList[i]:
            krwList.append(keyList[i])

    upbit_db = upbit.fetch_tickers(symbols=krwList,params={})
    print(upbit_db)
    BTCList = []

    for i in range(len(krwList)):
        name = krwList[i]

        UPbit_M = (upbit_db[name]['info']['market'])
        UPbit_T = (upbit_db[name]['info']['trade_timestamp'])
        UPbit_P = (upbit_db[name]['info']['trade_price'])

        Upbit = {'market':UPbit_M, 'trade_timestamp':UPbit_T,'trade_price':UPbit_P}

        BTCList.append(Upbit)

    try:
        return json.dumps(BTCList)
    except Exception as e:
        print(str(e))
        
        return jsonify(str(e))
    
    '''전체 목록 가져오는 경우'''
    # keyList = ['1INCH/BTC', 'AAVE/BTC', 'ADA/BTC', 'AERGO/BTC', 'AHT/BTC', 'ALGO/BTC', 'ANKR/BTC', 'AQT/BTC', 'ARDR/BTC', 'ARK/BTC', 'ATOM/BTC', 'AUCTION/BTC', 'AXS/BTC', 'BASIC/BTC', 'BAT/BTC', 'BCH/BTC', 'BFC/BTC', 'BNT/BTC', 'BORA/BTC', 'BSV/BTC', 'BTT/BTC', 'CBK/BTC', 'CELO/BTC', 'CHR/BTC', 'CHZ/BTC', 'COMP/BTC', 'CRO/BTC', 'CRV/BTC', 'CTSI/BTC', 'CVC/BTC', 'DAD/BTC', 'DAI/BTC', 'DAWN/BTC', 'DENT/BTC', 'DGB/BTC', 'DKA/BTC', 'DNT/BTC', 'DOGE/BTC', 'DOT/BTC', 'ELF/BTC', 'ENJ/BTC', 'EOS/BTC', 'ETC/BTC', 'ETH/BTC', 'FCT2/BTC', 'FIL/BTC', 'FLOW/BTC', 'FOR/BTC', 'FX/BTC', 'GLM/BTC', 'GO/BTC', 'GRS/BTC', 'GRT/BTC', 'GXC/BTC', 'HBD/BTC', 'HIVE/BTC', 'HUM/BTC', 'HUNT/BTC', 'INJ/BTC', 'IOST/BTC', 'IOTX/BTC', 'IQ/BTC', 'JST/BTC', 'JUV/BTC', 'KAVA/BTC', 'LINA/BTC', 'LINK/BTC', 'LOOM/BTC', 'LRC/BTC', 'LSK/BTC', 'LTC/BTC', 'LUNA/BTC', 'MANA/BTC', 'MARO/BTC', 'MASK/BTC', 'MATIC/BTC', 'MED/BTC', 'META/BTC', 'MFT/BTC', 'MKR/BTC', 'MLK/BTC', 'MOC/BTC', 'MTL/BTC', 'MVL/BTC', 'NEAR/BTC', 'NKN/BTC', 'NMR/BTC', 'NU/BTC', 'OBSR/BTC', 'OGN/BTC', 'OMG/BTC', 'ONIT/BTC', 'ORBS/BTC', 'OXT/BTC', 'PCI/BTC', 'PLA/BTC', 'POLY/BTC', 'POWR/BTC', 'PROM/BTC', 'PSG/BTC', 'PUNDIX/BTC', 'QTCON/BTC', 'QTUM/BTC', 'REP/BTC', 'RFR/BTC', 'RLC/BTC', 'RSR/BTC', 'RVN/BTC', 'SAND/BTC', 'SBD/BTC', 'SC/BTC', 'SNT/BTC', 'SNX/BTC', 'SOL/BTC', 'SOLVE/BTC', 'SRM/BTC', 'SSX/BTC', 'STEEM/BTC', 'STMX/BTC', 'STORJ/BTC', 'STPT/BTC', 'STRAX/BTC', 'STRK/BTC', 'STX/BTC', 'SUN/BTC', 'SXP/BTC', 'Tokamak Network/BTC', 'TRX/BTC', 'TUSD/BTC', 'UNI/BTC', 'UPP/BTC', 'USDP/BTC', 'VAL/BTC', 'VET/BTC', 'WAVES/BTC', 'WAXP/BTC', 'XEM/BTC', 'XLM/BTC', 'XRP/BTC', 'XTZ/BTC', 'ZIL/BTC', 'ZRX/BTC', '1INCH/KRW', 'AAVE/KRW', 'ADA/KRW', 'AERGO/KRW', 'AHT/KRW', 'ANKR/KRW', 'AQT/KRW', 'ARDR/KRW', 'ARK/KRW', 'ATOM/KRW', 'AXS/KRW', 'BAT/KRW', 'BCH/KRW', 'BORA/KRW', 'BSV/KRW', 'BTC/KRW', 'BTG/KRW', 'BTT/KRW', 'CBK/KRW', 'CHZ/KRW', 'CRE/KRW', 'CRO/KRW', 'CVC/KRW', 'DAWN/KRW', 'DKA/KRW', 'DOGE/KRW', 'DOT/KRW', 'ELF/KRW', 'ENJ/KRW', 'EOS/KRW', 'ETC/KRW', 'ETH/KRW', 'FCT2/KRW', 'FLOW/KRW', 'GAS/KRW', 'GLM/KRW', 'GRS/KRW', 'HBAR/KRW', 'HIVE/KRW', 'HUM/KRW', 'HUNT/KRW', 'ICX/KRW', 'IOST/KRW', 'IOTA/KRW', 'IQ/KRW', 'JST/KRW', 'KAVA/KRW', 'KNC/KRW', 'LINK/KRW', 'LOOM/KRW', 'LSK/KRW', 'LTC/KRW', 'MANA/KRW', 'MATIC/KRW', 'MBL/KRW', 'MED/KRW', 'META/KRW', 'MFT/KRW', 'MLK/KRW', 'MOC/KRW', 'MTL/KRW', 'MVL/KRW', 'NEO/KRW', 'NU/KRW', 'OMG/KRW', 'ONG/KRW', 'ONT/KRW', 'ORBS/KRW', 'PLA/KRW', 'POLY/KRW', 'POWR/KRW', 'PUNDIX/KRW', 'QKC/KRW', 'QTUM/KRW', 'REP/KRW', 'RFR/KRW', 'SAND/KRW', 'SBD/KRW', 'SC/KRW', 'SNT/KRW', 'SOL/KRW', 'SRM/KRW', 'SSX/KRW', 'STEEM/KRW', 'STMX/KRW', 'STORJ/KRW', 'STPT/KRW', 'STRAX/KRW', 'STRK/KRW', 'STX/KRW', 'SXP/KRW', 'TFUEL/KRW', 'THETA/KRW', 'Tokamak Network/KRW', 'TRX/KRW', 'TT/KRW', 'UPP/KRW', 'VET/KRW', 'WAVES/KRW', 'WAXP/KRW', 'XEC/KRW', 'XEM/KRW', 'XLM/KRW', 'XRP/KRW', 'XTZ/KRW', 'ZIL/KRW', 'ZRX/KRW', 'ADA/USDT', 'BAT/USDT', 'BCH/USDT', 'BTC/USDT', 'DGB/USDT', 'DOGE/USDT', 'ETC/USDT', 'ETH/USDT', 'LTC/USDT', 'OMG/USDT', 'RVN/USDT', 'SC/USDT', 'TRX/USDT', 'TUSD/USDT', 'XRP/USDT', 'ZRX/USDT']
    # krwList = []

    # for i in range(len(keyList)):
    #     if '/KRW' in keyList[i]:
    #         krwList.append(keyList[i])
    # upbit_db = upbit.fetch_tickers(symbols=krwList,params={})
    # BTCList = []

    # for i in range(len(krwList)):
    #     name = krwList[i]

    #     UPbit_M = (upbit_db[name]['info']['market'])
    #     UPbit_C = (upbit_db[name]['info']['change_rate'])
    #     UPbit_T = (upbit_db[name]['info']['trade_timestamp'])
    #     UPbit_P = (upbit_db[name]['info']['trade_price'])
    #     UPbit_V = (upbit_db[name]['info']['trade_volume']) 

    #     Upbit = {'market':UPbit_M ,'change_rate':UPbit_C,'trade_timestamp':UPbit_T,'trade_price':UPbit_P,'trade_volume':UPbit_V}

    
    '''db 연동해서 사용할 경우'''
    # upbit_db = upbit.fetch_tickers(symbol='BTC/KRW',params={})
    # BTCList = []
    # UPbit_T = (upbit_db['info']['trade_timestamp'])
    # UPbit_P = (upbit_db['info']['trade_price'])

    # Upbit = {'trade_timestamp':UPbit_T,'trade_price':UPbit_P}
    
    # dbModule.execute("INSERT INTO bitcoin_price_tx(time_stamp, price) VALUES('{0}', '{1}');".format(Upbit['trade_timestamp'], Upbit['trade_price']))
        
    # BTCList.append(Upbit)
    
    # dbModule.commit();
        
    # try:
    #     return json.dumps(BTCList)
    # except Exception as e:
    #     print(str(e))
            
    #     return jsonify(str(e))
    

'''====================== private APi ================================================================================================='''


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
    