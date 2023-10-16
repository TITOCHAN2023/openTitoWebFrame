from pymysql import Connection
from config import host,user,password,db

def mysqlReadTable(table) :
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
        # 创建游标对象

        cursor = con.cursor()

        cursor.execute("select * from "+table)
         # 获取查询所有结果
        result = cursor.fetchall()
        return result
        # print(type(result), result)
        # for row in result:
        #     print(row)
    
    except Exception as e:
        print("error", e)
    finally:
        if con:
            con.close()