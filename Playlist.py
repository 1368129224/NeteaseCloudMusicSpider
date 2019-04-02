import requests
import pymysql
import time
import random
import subprocess
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent

###获取收藏数前500歌单中的所有歌曲
def getSongsJson(pid):
    '''
    传入歌单ID，爬取歌单中歌曲并存入数据库
    :param pid: 歌单ID
    :return: 歌单ID
    '''
    global api
    start_time = time.time()
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    try:
        db = pymysql.connect(**getSql())
    except Exception as e:
        print('pid: {} connetct mysql error: {}'.format(pid,e))
        try:
            db = pymysql.connect(**getSql())
        except Exception as e:
            print('pid: {} connetct mysql error: {}'.format(pid, e))
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
            saveSongData(songResult,db)
            # with open('songlog.txt', 'a') as f:
            #     f.write('PID: {} , {} 首,用时 {}\n'.format(pid, json['playlist']['trackCount'], time.time() - start_time))
            print('PID: {} , {} 首,用时 {}'.format(pid,json['playlist']['trackCount'],time.time()-start_time))
            return pid
        elif json["code"] == -460:
            print('更换IP!')
            stopApi(api)
            changeIP()
            api = startApi()
            getSongsJson(pid)
        else:
            print(json)
            getSongsJson(pid)
    except Exception as e:
        print('getSongsJson error pid {} e {}'.format(pid,e))
    finally:
        db.close()


def saveSongData(data,db):
    '''
    储存歌曲数据到数据库中
    :param data: [歌单ID,歌曲ID,歌曲名]
    :param db: 数据库连接
    :return: None
    '''
    try:
        cursor = db.cursor()
        sql = "INSERT INTO T_Song VALUES (%s, %s, %s)"
        for row in data:
            try:
                cursor.execute(sql, row)
            except Exception as e:
                print("{} 插入失败! {}".format(row, e))
                db.rollback()
            db.commit()
    except Exception as e:
        print('saveSogData error {}'.format(e))


def getPid():
    '''
    从数据库获取待爬取的歌单ID
    :return: 歌单ID
    '''
    try:
        db = pymysql.connect(**getSql())
        cursor = db.cursor()
        sql = 'SELECT PID FROM T_Playlist WHERE PID IN (SELECT t.PID FROM(SELECT PID FROM T_Playlist ORDER BY SUBSCRIBEDCOUNT DESC LIMIT 0, 500)AS t) ORDER BY T_Playlist.TRACKCOUNT DESC'
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
    pid = getPid()
    with ThreadPoolExecutor(96) as executor:
        executor.map(getSongsJson, pid)
###


###获取指定分类的歌单
def runPlaylistInfo():
    offset = [num for num in range(0, 1310, 10)]
    with ThreadPoolExecutor(32) as executor:
        executor.map(getPlaylistJson, offset)


def getPlaylistJson(offset):
    global ua, api
    headers = {
        'User-Agent': ua.random
    }
    db = pymysql.connect(**getSql())
    url = r'http://localhost:3000/top/playlist?limit=10&order=hot&cat=%E5%8D%8E%E8%AF%AD&offset='
    url = url + repr(offset)
    playlistResult = []
    tagResult = []
    req = requests.get(url, headers=headers)
    json = req.json()
    try:
        if json['code'] == 200:
            data = json['playlists']
            for item in data:
                playlist = (
                    item['id'],
                    item['name'],
                    item['userId'],
                    item['subscribedCount'],
                    item['trackCount'],
                    item['playCount'],
                    item['shareCount'],
                    item['commentCount']
                )
                tags = item['tags']
                for tag in tags:
                    ptag = (
                        item['id'],
                        tag
                    )
                    tagResult.append(ptag)
                playlistResult.append(playlist)
            saveBasicData(playlistResult,db)
            saveTagData(tagResult,db)
            db.close()
            return 0
        elif json["code"] == -460:
            print('更换IP!')
            stopApi(api)
            changeIP()
            api = startApi()
            getPlaylistJson(offset)
        else:
            print(json)
            db.close()
            exit(-1)
    except Exception as e:
        print('getPlaylistJson error pid {} e {}'.format(offset,e))
    finally:
        db.close()


def saveBasicData(data,db):
    cursor = db.cursor()
    sql = "INSERT INTO T_Playlist VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    for row in data:
        try:
            cursor.execute(sql, row)
        except Exception as e:
            print("{} 插入失败! {}".format(row, e))
            db.rollback()
    db.commit()


def saveTagData(data,db):
    cursor = db.cursor()
    sql = "INSERT INTO T_Tag VALUES (%s, %s)"
    for row in data:
        try:
            cursor.execute(sql, row)
        except Exception as e:
            print("{} 插入失败! {}".format(row, e))
            db.rollback()
    db.commit()
###


###公用方法
def getSql():
    sql = {}
    with open('mysql.tx', 'r') as f:
        lines = f.readlines()
        for line in lines:
            sql[line.split('=')[0]] = line.split('=')[1].replace('\n', '')
    sql['port'] = int(sql['port'])
    sql['connect_timeout'] = int(sql['connect_timeout'])
    return sql


def changeIP():
    try:
        with open(r"G:\163music\util\request.js", "r+", encoding="utf8") as f:
            f.seek(2782)
            random.seed(a=None)
            ip = repr(random.randint(100, 255)) + '.' + \
                repr(random.randint(100, 255))
            print(ip)
            f.write(ip)
        return ip
    except Exception as e:
        print(e)
        return None


def startApi():
    changeIP()
    p = subprocess.Popen(
        'node app.js',
        cwd=r"G:\163music",
        stdout=None,
        stderr=None)
    return p


def stopApi(p):
    p.terminate()
###

if __name__ == '__main__':
    start_time = time.perf_counter()
    api = startApi()

    try:
        # runPlaylistInfo()
        runPlaylistSong()
    finally:
        stopApi(api)

    print('last time: {}'.format(time.perf_counter() - start_time))

