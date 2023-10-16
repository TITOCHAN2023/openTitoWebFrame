import requests
import re

def getWhere(ip):
    url = "".format(ip)

    headers = {
        
    }
	#以上是爬取url 和反爬的用户模拟
	
    # 获取响应
    response = requests.get(url=url, headers=headers)

    response.encoding = ""
    #编码信息

    text = response.text

    info = ""
    	#对得到的text处理成字典返回主程序
    	#因个人情况而变
    return info