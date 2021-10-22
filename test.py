import pymysql
import ccxt

conn=pymysql.connect(
    host='skuser35-mydb.cw2or7iuke4y.us-west-1.rds.amazonaws.com',
    user='root',
    password='test1357',
    db='mydb',
    charset='utf8',
    port= 3306 
)

curs = conn.cursor(pymysql.cursors.DictCursor)

# 아이디로 찾는 경우 

sql="select * from upbits where user_id=%s"
# 전체 목록 데이터화

user = input("아이디를 입력해주세요")
curs.execute(sql,user)
rows= curs.fetchall()

for row in rows:
    Open = row['access_key']

for row in rows:
    Private = row['private_key']


conn.close()

print(Open)
print(Private)

upbit = ccxt.upbit(config={
    'apiKey': 'Open',        
    'secret': 'Private'         
})
balance= upbit.fetch_balance()
print(upbit.keys())