import os
from Helper import BASE_PATH


def getMySqlHome():
    sql = {}
    with open(os.path.join(BASE_PATH, 'Helper\mysql.home'), 'r') as f:
        lines = f.readlines()
        for line in lines:
            sql[line.split('=')[0]] = line.split('=')[1].replace('\n','')
    sql['port'] = int(sql['port'])
    sql['connect_timeout'] = int(sql['connect_timeout'])
    return sql

def getMySqlTx():
    sql = {}
    with open(os.path.join(BASE_PATH, 'Helper\mysql.tx'), 'r') as f:
        lines = f.readlines()
        for line in lines:
            sql[line.split('=')[0]] = line.split('=')[1].replace('\n','')
    sql['port'] = int(sql['port'])
    sql['connect_timeout'] = int(sql['connect_timeout'])
    return sql

def getMongoTx():
    with open(os.path.join(BASE_PATH, 'Helper\mongodb.tx'), 'r') as f:
        return f.readline()

if __name__ == '__main__':
    pass