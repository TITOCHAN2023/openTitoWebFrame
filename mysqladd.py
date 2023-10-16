from pymysql import Connection
from config import host,user,password,db


def mysqlAdd(tableName,element) :
    con = None
    try:

        con = Connection(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db
        )

        print(type(con))
        print(con.get_host_info())
        print(con.get_server_info())
        # 创建游标对象
        cursor = con.cursor()

        # 定义建表sql语句
        sql = "ALTER TABLE "+tableName+" ADD COLUMN "+element+" VARCHAR(40) DEFAULT NULL"
        

        # 使用游标对象，执行sql
        cursor.execute(sql)
    
    except Exception as e:
        print("error", e)
    finally:
        if con:
            con.close()