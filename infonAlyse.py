import pandas
import pymysql
import matplotlib.pyplot as plt
from Helper import SqlHelper

result = []

sql = SqlHelper.getSql()
db = pymysql.connect(**sql)
cursor = db.cursor()
cursor.execute("SELECT LISTENSONG FROM T_User")
for res in cursor.fetchall():
    result.append(res[0])
myser = pandas.cut(result,bins=[0,0.5,1,100,1000,2000,4000,6000,8000,10000],include_lowest=True)
print(myser.value_counts())