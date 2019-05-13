def getSqlHome():
    sql = {}
    with open('mysql.home', 'r') as f:
        lines = f.readlines()
        for line in lines:
            sql[line.split('=')[0]] = line.split('=')[1].replace('\n','')
    sql['port'] = int(sql['port'])
    sql['connect_timeout'] = int(sql['connect_timeout'])
    return sql

def getSqlTx():
    sql = {}
    with open('mysql.tx', 'r') as f:
        lines = f.readlines()
        for line in lines:
            sql[line.split('=')[0]] = line.split('=')[1].replace('\n','')
    sql['port'] = int(sql['port'])
    sql['connect_timeout'] = int(sql['connect_timeout'])
    return sql

def getMongoTX():
    return 'mongodb://zooter:zzc()1214@www.zooter.com.cn:27017/admin'