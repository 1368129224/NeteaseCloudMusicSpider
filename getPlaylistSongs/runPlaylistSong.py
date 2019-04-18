import requests
import pymysql
import time
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent
from Helper import SqlHelper, ApiHelper


def getSongsJson(pid, api, cat):
    '''
    传入歌单ID，爬取歌单中歌曲并存入数据库
    :param api: api
    :param pid: 歌单ID
    :return: 歌单中的歌曲数量
    '''
    ua = UserAgent()
    start_time = time.time()
    headers = {
        'User-Agent': ua.random
    }
    try:
        db = pymysql.connect(**SqlHelper.getSqlTx())
    except Exception as e:
        print('pid: {} connect mysql error: {}'.format(pid, e))
        try:
            db = pymysql.connect(**SqlHelper.getSqlTx())
        except Exception as e:
            print('pid: {} connect mysql error: {}'.format(pid, e))
    songResult = []
    url = r'http://localhost:3000/playlist/detail?id='
    url = url + repr(pid)
    req = requests.get(url, headers=headers)
    json = req.json()
    try:
        if json['code'] == 200:
            data = json['playlist']['trackIds']
            for item in data:
                song = (
                    pid,
                    item['id'],
                    'null'
                )
                songResult.append(song)
            saveSongData(songResult, db, cat)
            # with open('songlog.txt', 'a') as f:
            #     f.write('PID: {} , {} 首,用时 {}\n'.format(pid, json['playlist']['trackCount'], time.time() - start_time))
            print(
                'PID: {} , {} 首,用时 {}'.format(
                    pid,
                    json['playlist']['trackCount'],
                    time.time() -
                    start_time))
            return json['playlist']['trackCount']
        elif json["code"] == -460:
            print('更换IP!')
            api.stopApi()
            api.startApi()
            getSongsJson(pid,api,cat)
        else:
            print(json)
            getSongsJson(pid,api,cat)
    except Exception as e:
        print('main error pid {} e {}'.format(pid, e))
    finally:
        db.close()


def saveSongData(data, db, cat):
    '''
    储存歌曲数据到数据库中
    :param data: [歌单ID,歌曲ID,歌曲名]
    :param db: 数据库连接
    :return: None
    '''
    try:
        cursor = db.cursor()
        sql = "INSERT INTO T_{}Song VALUES (%s, %s, %s)".format(ApiHelper.catlist[cat])
        for row in data:
            try:
                cursor.execute(sql, row)
            except Exception as e:
                print("{} 插入失败! {}".format(row, e))
                db.rollback()
            db.commit()
    except Exception as e:
        print('saveSogData error {}'.format(e))


def getPid(cat):
    '''
    从数据库获取待爬取的歌单ID
    :return: 歌单ID
    '''
    try:
        try:
            db = pymysql.connect(**SqlHelper.getSqlTx())
        except Exception as e:
            print('getPid connetct mysql error: {}'.format(e))
            try:
                db = pymysql.connect(**SqlHelper.getSqlTx())
            except Exception as e:
                print('getPid connetct mysql error: {}'.format(e))
        cursor = db.cursor()
        sql = 'SELECT PID FROM T_{} WHERE PID IN (SELECT t.PID FROM(SELECT PID FROM T_{} ORDER BY SUBSCRIBEDCOUNT DESC LIMIT 0, 500)AS t) ORDER BY T_{}.TRACKCOUNT DESC'.format(ApiHelper.catlist[cat],ApiHelper.catlist[cat],ApiHelper.catlist[cat])
        cursor.execute(sql)
        result = cursor.fetchall()
        pid = []
        for item in result:
            pid.append(item[0])
        db.close()
        return pid
    except Exception as e:
        print('getPid error {}'.format(e))


def runPlaylistSong():
    '''
    获取待爬取的歌单后提交进线程池
    :return: None
    '''
    p = ApiHelper.api()
    p.startApi()
    pid = getPid()
    api = [p for i in range(len(pid))]
    with ThreadPoolExecutor(96) as executor:
        result = executor.map(getSongsJson, pid, api)
    print('已抓取{}个歌单,共计{}首歌.'.format(len(pid), sum(result)))
    p.stopApi()


def run(cat):
    p = ApiHelper.api()
    p.startApi()
    pid = getPid(cat)
    api = [p for i in range(len(pid))]
    c = [cat for i in range(len(pid))]
    with ThreadPoolExecutor(96) as executor:
        result = executor.map(getSongsJson, pid, api, c)
    print('已抓取{}个歌单,共计{}首歌.'.format(len(pid), sum(result)))
    p.stopApi()


if __name__ == '__main__':
    start_time = time.perf_counter()
    runPlaylistSong()
    print('last time: {}'.format(time.perf_counter() - start_time))
