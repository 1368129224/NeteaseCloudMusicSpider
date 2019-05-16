import pymongo
import openpyxl
from Helper import SqlHelper

# connstr = 'mongodb://zooter:zzc()1214@www.zooter.com.cn:27017/admin'
connstr = SqlHelper.getMongoTX()
client = pymongo.MongoClient(connstr)
db = client['163music']
cl = db['userinfos']

data = []
rows = ['UID', 'NICKNAME', 'FOLLOWS', 'FOLLOWEDS', 'LISTENSONG', 'LISTEN', 'SUBSCRIBED', 'CITY']
wb = openpyxl.load_workbook('T_User.xlsx')
sheet = wb['T_User']
for line in sheet:
    dic = {}
    for i,v in enumerate(line):
        dic[rows[i]] = v.value
        print(v.value, end=' ')
    print('\n')
    data.append(dic)

cl.insert_many(data)
for item in cl.find():
    print(item)