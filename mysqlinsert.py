from pymysql import Connection
from config import host,user,password,db

def mysqlInsertTable(table,row,name,ip,text,str) :
    con = None
    try:

        con = Connection(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db,
            autocommit=True
        )

        print(type(con))
        print(con.get_host_info())
        print(con.get_server_info())
        # 获取游标对象
        cursor = con.cursor()
        # 使用游标对象，执行sql语句
        sql = f"INSERT IGNORE INTO {table} (id, name, ip, text, time) VALUES (%s, %s, %s, %s, %s)"
        values = (row, name, ip, text, str)
        cursor.execute(sql, values)
        # 获取主键
        print("主键id=", con.insert_id())
    
    except Exception as e:
        print("error", e)
    finally:
        if con:
            con.close()