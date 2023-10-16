import datetime


def gettime():
    # 获取当前时间, 其中中包含了year, month, hour, 需要import datetime

    # 获取今天的日期 2021-01-12
    #today = datetime.date.today()
    # 获取今天的时间 2021-01-12 15:30:39.603681
    #nowtime = datetime.datetime.now()

    
    

    # 打印字符串 2021-01-12 15:30:39
    return datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

    


