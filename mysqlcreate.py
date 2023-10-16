from pymysql import Connection
from config import host,user,password,db


# 先创建数据库：https://cdn.mysql.com//Downloads/MySQLInstaller/mysql-installer-web-community-8.0.34.0.msi
# 创建数据库连接
def mysqlCreateTable(name) :
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
        sql = "CREATE TABLE `" +name+ """` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(20) DEFAULT NULL,
        `ip` varchar(20) DEFAULT NULL,
        `text` varchar(200) DEFAULT NULL,
        `time` varchar(40) DEFAULT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8
        """

        # 使用游标对象，执行sql
        cursor.execute(sql)
        


    except Exception as e:
        print("error", e)
    finally:
        if con:
            con.close()


# # 定义建表sql语句
    # sql = """CREATE TABLE `t_student3` (
    #   `id` int(11) NOT NULL AUTO_INCREMENT,
    #   `name` varchar(10) DEFAULT NULL,
    #   `age` int(11) DEFAULT NULL,
    #   PRIMARY KEY (`id`)
    # ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    # """
    
    #对表中的字段进行增，删，改的操作
    # #格式：alter table 表名 add/drop/modify/change [column] .......
    
    # #向表中添加字段:alter table 表名 add [column] 字段名 字段类型;
    # ALTER TABLE stu ADD COLUMN age INT;
    
    # #删除表中的字段:alter table 表名 drop [column] 字段名：
    # ALTER TABLE stu DROP age;
    
    # #修改字段的名字:alter table 表名 change [column] 旧字段名 新字段名 字段类型;
    # ALTER TABLE stu CHANGE COLUMN sname s2name VARCHAR(20);
    
    # #修改字段的类型:alter table 表名 modify [column] 字段名 字段类型;
    # ALTER TABLE stu MODIFY id VARCHAR(20);
    
    
    # #修改表的名字: alter table 旧表名 rename to 新表名：
    # ALTER TABLE stu4 RENAME TO stu5;

    #cursor.execute("select * from t_student1")
    # # 获取查询所有结果
    # result = cursor.fetchall()
    # print(type(result), result)
    # for row in result:
    #     print(row)