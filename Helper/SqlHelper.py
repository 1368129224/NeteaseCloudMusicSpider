def getSql():
    sql = {}
    with open('mysql.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            sql[line.split('=')[0]] = line.split('=')[1].replace('\n','')
    sql['port'] = int(sql['port'])
    return sql