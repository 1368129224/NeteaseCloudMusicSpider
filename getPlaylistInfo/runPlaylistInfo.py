import requests
import pymysql
import time
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent
from Helper import ApiHelper,SqlHelper


def init(cat):
    try:
        db = pymysql.connect(**SqlHelper.getSqlTx())
    except Exception as e:
        print('connect mysql error: {}'.format(e))
        try:
            db = pymysql.connect(**SqlHelper.getSqlTx())
        except Exception as e:
            print('connect mysql error: {}'.format(e))
    cursor = db.cursor()
    sql = 'drop table if exists T_{};'.format(ApiHelper.catlist[cat])
    cursor.execute(sql)
    sql = 'drop table if exists T_{}Song;'.format(ApiHelper.catlist[cat])
    cursor.execute(sql)
    sql = r"""CREATE TABLE T_{}(
    PID BIGINT NOT NULL   COMMENT '歌单ID' ,
    NAME VARCHAR(128)    COMMENT '歌单名' ,
    USERID INT    COMMENT '创建者ID' ,
    SUBSCRIBEDCOUNT INT    COMMENT '收藏数' ,
    TRACKCOUNT INT    COMMENT '歌曲数' ,
    PLAYCOUNT INT    COMMENT '播放数' ,
    SHARECOUNT INT    COMMENT '分享数' ,
    COMMENTCOUNT INT    COMMENT '评论数' ,
    PRIMARY KEY (PID)
    ) COMMENT = '{}歌单表';/*SQL@Run*/""".format(ApiHelper.catlist[cat],cat)
    cursor.execute(sql)
    sql = r"""CREATE TABLE T_{}Song(
    PID BIGINT    COMMENT '歌单ID' ,
    SID BIGINT    COMMENT '歌曲ID' ,
    SNAME VARCHAR(1024)    COMMENT '歌曲名'
    ) COMMENT = '{}歌单歌曲表 ';/*SQL@Run*/""".format(ApiHelper.catlist[cat],cat)
    cursor.execute(sql)


def getPlaylistJson(offset,api,cat):
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
    url = r'http://localhost:3000/top/playlist?limit=10&order=hot&cat={}&offset='.format(cat)
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
            saveBasicData(playlistResult,db,cat)
            saveTagData(tagResult,db)
            return offset
        elif json["code"] == -460:
            print('更换IP!')
            api.stopApi()
            api.startApi()
            getPlaylistJson(offset,api,cat)
        else:
            print(json)
            getPlaylistJson(offset,api,cat)
    except Exception as e:
        print('getPlaylistJson error offset {} e {}'.format(offset,e))
    finally:
        db.close()


def saveBasicData(data,db,cat):
    '''
    保存歌单数据到数据库
    :param data: [歌单ID,歌单名,用户ID,收藏数,歌曲数,播放次数,分享次数,评论数]
    :param db: 数据库连接
    :return: None
    '''
    cursor = db.cursor()
    sql = "INSERT INTO T_{} VALUES (%s, %s, %s, %s, %s, %s, %s, %s)".format(ApiHelper.catlist[cat])
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


def run(cat):
    '''
    获取特定分类的歌单数量传入进程池并开始爬取
    :param cat:
    :return:
    '''
    init(cat)
    p = ApiHelper.api()
    p.startApi()
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    url = r'http://localhost:3000/top/playlist?limit=10&order=hot&cat={}&offset=0'.format(cat)
    num = requests.get(url, headers=headers).json()['total']
    offset = [num for num in range(0, (num // 10 + 2) * 10, 10)]
    c = [cat for num in range(len(offset))]
    api = [p for i in range(len(offset))]
    with ThreadPoolExecutor(32) as executor:
        executor.map(getPlaylistJson, offset, api, c)
    print('已抓取{}个歌单'.format(num))
    p.stopApi()

if __name__ == '__main__':
    start_time = time.perf_counter()
    run('华语')
    print('last time: {}'.format(time.perf_counter() - start_time))