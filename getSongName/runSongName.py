import requests
import pymysql
from concurrent.futures import ThreadPoolExecutor
from Helper import SqlHelper,ApiHelper
from fake_useragent import UserAgent

def getSongIds():
    try:
        try:
            db = pymysql.connect(**SqlHelper.getSqlTx())
        except Exception as e:
            print('getSid connetct mysql error: {}'.format(e))
            try:
                db = pymysql.connect(**SqlHelper.getSqlTx())
            except Exception as e:
                print('getSid connetct mysql error: {}'.format(e))
        cursor = db.cursor()
        sql = 'SELECT DISTINCT SID FROM T_Song'
        cursor.execute(sql)
        result = cursor.fetchall()
        sids = []
        for item in result:
            sids.append(str(item[0]))
        db.close()
        return sids
    except Exception as e:
        print('getSid error {}'.format(e))

def getUrls(sids):
    tasks = []
    urls = []
    api_url = r'http://localhost:3000/song/detail?ids='
    while True:
        if sids:
            songs = []
            for i in range(0,20):
                if sids:
                    songs.append(sids.pop())
                else:
                    break
            tasks.append(','.join(songs))
        else:
            break
    for task in tasks:
        urls.append(api_url + task)
    return urls

def myThread(url,api):
    try:
        db = pymysql.connect(**SqlHelper.getSqlTx())
    except Exception as e:
        print('connect mysql error : {}'.format(e))
        try:
            db = pymysql.connect(**SqlHelper.getSqlTx())
        except Exception as e:
            print('retry connect mysql error : {}'.format(e))
    data = getData(url,api)
    saveData(data,db)
    db.close()

def getData(url,api):
    ua = UserAgent()
    headers = {
        'UserAgent':ua.random
    }
    data = []
    json = requests.get(url, headers).json()
    try:
        if json['code'] == 200:
            songs = json['songs']
            for song in songs:
                s = (
                    song['id'],
                    song['name']
                )
                data.append(s)
            return data
        elif json['code'] == -460:
            print('更换IP!')
            api.stopApi()
            api.startApi()
            getData(url,api)
        else:
            print(json)
            getData(url,api)
    except Exception as e:
        print('requestsget error : {}'.format(e))

def saveData(data,db):
    try:
        cursor = db.cursor()
        sql = 'INSERT INTO T_SongName VALUES (%s,%s)'
        for row in data:
            try:
                cursor.execute(sql, row)
            except Exception as e:
                print("{} 插入失败! {}".format(row, e))
                db.rollback()
            db.commit()
    except Exception as e:
        print('save data error : {}'.format(e))



def run():
    p = ApiHelper.api()
    p.startApi()
    ids = getSongIds()
    urls = getUrls(ids)
    apis = [p for i in range(len(urls))]
    with ThreadPoolExecutor(64) as executor:
        executor.map(myThread, urls, apis)
    p.stopApi()

if __name__ == '__main__':
    run()
