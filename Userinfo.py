import requests
import pymysql
import time
from concurrent import futures
from Helper import SqlHelper

def saveData(conn):
    global result
    sql = "INSERT INTO T_User VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    for row in result:
        try:
            cursor.execute(sql, row)
        except Exception as e:
            print("插入失败! {}".format(e))
            conn.rollback()
    conn.commit()
    result = []

def run(uid):
    global total, result
    print("正在爬取uid: {} 用户的信息".format(uid))
    url = api_url + repr(uid)
    req = requests.get(url).json()
    try:
        if req["code"] != 404:
            user_info = (
                req["userPoint"]["userId"],  # UID
                req["profile"]["nickname"],  # 昵称
                req["profile"]["followeds"],  # 粉丝数
                req["profile"]["follows"],  # 关注数
                req["listenSongs"],  # 听歌数
                req["profile"]["playlistCount"],  # 歌单播放数
                req["profile"]["playlistBeSubscribedCount"],  # 歌单收藏数
                req["profile"]["city"],  # 城市
            )
            result.append(user_info)
            total += 1
        else:
            print("uid={}的用户不存在".format(uid))
    except Exception as e:
        print("json error!")
        print(e)

result = []
total = 0
api_url = "http://127.0.0.1:3000/user/detail?uid="
start = 38166000
end = 38167000

if __name__ == '__main__':
    starttime = time.perf_counter()
    print("启动爬虫，开始爬取数据")
    sql = SqlHelper.getSql()
    db = pymysql.connect(**sql)
    cursor = db.cursor()
    for j in range(1, 10000):
        begin = 1000 * j
        for i in range(begin, begin + 1000):
            with futures.ThreadPoolExecutor() as executor:
                executor.submit(run, i)
        saveData(db)
    db.close()
    elapsed = (time.perf_counter() - starttime)
    print("爬取uid {} - {} 的用户,共 {} 条，有效数据 {} 条.共用时 {:.2f} s.".format(start, end, end-start, total, elapsed))
