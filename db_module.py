import pymysql


# SQL에 데이터 정리
class key_DB:
    def __init__(self):
        self.db = pymysql.connect(
            host='skuser35-mydb.cw2or7iuke4y.us-west-1.rds.amazonaws.com',
            user='root',
            password='test1357',
            db='mydb',
            port=3306,
            charset='utf8'
        )

        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row
        
    def commit(self):
        self.db.commit()