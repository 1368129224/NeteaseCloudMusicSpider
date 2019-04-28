import pymongo
from openpyxl import load_workbook

data = []
rows = ['UID', 'NICKNAME', 'FOLLOWS', 'FOLLOWEDS', 'LISTENSONG', 'LISTEN', 'SUBSCRIBED', 'CITY']
wb = load_workbook('T_User.xlsx')
sheet = wb['T_User']
for line in sheet:
    dic = {}
    for i,v in enumerate(line):
        dic[rows[i]] = v.value
        print(v.value, end=' ')
    print('\n')
    data.append(dic)
client  = pymongo.MongoClient('localhost',27017)
db = client['163music']
cl = db['userinfos']
cl.insert_many(data)
for item in cl.find():
    print(item)
