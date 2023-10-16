import mysqlcreate as mc
import mysqlread as mr
import mysqladd as ma
import mysqlinsert as mi
import mysqldet as md
import gettime as gettime
import where

#创建table
def MC(name):
    mc.mysqlCreateTable(name)

#读取table
def MR(table):
    comment=mr.mysqlReadTable(table)
    return comment


#增加column
def MA(name,what):
    ma.mysqlAdd(name,what)


#增加row
def MI(table,name,ip,text):
    city = where.getWhere(ip)
    timeAndWhere=f"{gettime.gettime()}  {city['prov']}-{city['city']}"
    mi.mysqlInsertTable(table,"0",name,ip,text,f"{timeAndWhere}")

#删除row
def MD(table,row):
    md.mysqlDeleteRow(table,row)

