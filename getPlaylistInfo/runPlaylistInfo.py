import requests
import pymysql
import time
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent
from Helper import ApiHelper,SqlHelper


def getPlaylistJson(offset,api):
    '''
    获取特定分类的所有歌单的信息并存入数据库
    :param offset: 歌单数量偏移量
    :param api: api
    :return: offset
    '''
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    try:
        db = pymysql.connect(**SqlHelper.getSqlTx())
    except Exception as e:
        print('offset: {} connect mysql error: {}'.format(offset, e))
        try:
            db = pymysql.connect(**SqlHelper.getSqlTx())
        except Exception as e:
            print('offset: {} connect mysql error: {}'.format(offset, e))
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
            return offset
        elif json["code"] == -460:
            print('更换IP!')
            api.stopApi()
            api.startApi()
            getPlaylistJson(offset,api)
        else:
            print(json)
            getPlaylistJson(offset,api)
    except Exception as e:
        print('getPlaylistJson error offset {} e {}'.format(offset,e))
    finally:
        db.close()


def saveBasicData(data,db):
    '''
    保存歌单数据到数据库
    :param data: [歌单ID,歌单名,用户ID,收藏数,歌曲数,播放次数,分享次数,评论数]
    :param db: 数据库连接
    :return: None
    '''
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
    '''
    保存歌单标签到数据库
    :param data: [歌单ID,标签]
    :param db: 数据库连接
    :return: None
    '''
    cursor = db.cursor()
    sql = "INSERT INTO T_Tag VALUES (%s, %s)"
    for row in data:
        try:
            cursor.execute(sql, row)
        except Exception as e:
            print("{} 插入失败! {}".format(row, e))
            db.rollback()
    db.commit()


def runPlaylistInfo():
    '''
    获取特定分类的歌单数量传入进程池并开始爬取
    :return: None
    '''
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    p = ApiHelper.api()
    p.startApi()
    url = r'http://localhost:3000/top/playlist?limit=10&order=hot&cat=%E5%8D%8E%E8%AF%AD&offset=0'
    num = requests.get(url,headers=headers).json()['total']
    offset = [num for num in range(0, (num // 10 + 2) * 10, 10)]
    api = [p for i in range(len(offset))]
    with ThreadPoolExecutor(32) as executor:
        executor.map(getPlaylistJson, offset,api)
    print('已抓取{}个歌单'.format(num))
    p.stopApi()

if __name__ == '__main__':
    start_time = time.perf_counter()
    runPlaylistInfo()
    print('last time: {}'.format(time.perf_counter() - start_time))