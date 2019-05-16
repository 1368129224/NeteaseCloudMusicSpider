def getMySqlHome():
    sql = {}
    with open('mysql.home', 'r') as f:
        lines = f.readlines()
        for line in lines:
            sql[line.split('=')[0]] = line.split('=')[1].replace('\n','')
    sql['port'] = int(sql['port'])
    sql['connect_timeout'] = int(sql['connect_timeout'])
    return sql

def getMySqlTx():
    sql = {}
    with open('mysql.tx', 'r') as f:
        lines = f.readlines()
        for line in lines:
            sql[line.split('=')[0]] = line.split('=')[1].replace('\n','')
    sql['port'] = int(sql['port'])
    sql['connect_timeout'] = int(sql['connect_timeout'])
    return sql

def getMongoTx():
    with open('mongodb.tx', 'r') as f:
        return f.readline()