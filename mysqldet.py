from pymysql import Connection
from config import host,user,password,db

def mysqlDeleteRow(table, row_id):
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

        # 获取游标对象
        cursor = con.cursor()

        # 使用游标对象，执行删除语句
        cursor.execute(f"DELETE FROM {table} WHERE id = {row_id}")

    except Exception as e:
        print("error", e)
    finally:
        if con:
            con.close()