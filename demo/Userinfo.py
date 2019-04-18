import requests
import pymysql
import time
import random
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED
from Helper import SqlHelper
from fake_useragent import UserAgent

def saveData(result):
    sql = SqlHelper.getSql()
    db = pymysql.connect(**sql)
    cursor = db.cursor()
    sql = "INSERT INTO T_User VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    for row in result:
        try:
            cursor.execute(sql, row)
        except Exception as e:
            print("{} 插入失败! {}".format(row,e))
            db.rollback()
    db.commit()
    db.close()

def changeIP():
    try:
        with open(r"G:\163music\util\request.js", "r+", encoding="utf8") as f:
            f.seek(2784)
            random.seed(a=None)
            ip = repr(random.randint(100,255))
            print(ip)
            f.write(ip)
        return ip
    except Exception as e:
        print(e)
        return None

def startApi():
    p = subprocess.Popen('node app.js',cwd=r"G:\163music", stdout=None, stderr=None)
    return p

def stopApi(p):
    p.terminate()

def run(uid):
    global total, ua, s, p
    headers = {
        'User-Agent': ua.random
    }
    result = []
    url = api_url + repr(uid)
    print("正在爬取uid: {} 用户的信息".format(uid))
    print(url)
    req = s.get(url, headers=headers)
    req = req.json()
    try:
        if req["code"] == 200:
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
            saveData(result)
            lock.acquire()
            total += 1
            lock.release()
            return uid
        elif req["code"] == -460:
            print("ip被封了！当前uid: {}".format(uid))
            with open("log2.txt", "w")as f:
                f.write("ip被封了！当前uid: {} ".format(uid) + time.strftime("%H:%M:%S %Y", time.localtime()) + "\n")
            print("更换IP")
            return -1
        else:
            print("uid={}的用户不存在".format(uid))
            return -2
    except Exception as e:
        print("{} get json error! {}".format(uid, e))

total = 0
api_url = "http://127.0.0.1:3000/user/detail?uid="
requests.DEFAULT_RETRIES = 5
s = requests.session()
s.keep_alive = False
ua = UserAgent()
lock = threading.Lock()
p = startApi()
start = 3548195
end = 7540000

if __name__ == '__main__':
    starttime = time.perf_counter()
    print(p.pid)
    time.sleep(2)
    print("启动爬虫，开始爬取数据")
    for i in range(498,500):
        try:
            with ThreadPoolExecutor(24) as executor:
                all_task = [executor.submit(run, j) for j in range(i*10000, i*10000 + 10000)]
                for task in as_completed(all_task):
                    flag = task.result()
                    if flag == -1:
                        lock.acquire()
                        stopApi(p)
                        changeIP()
                        p = startApi()
                        lock.release()
                    elif flag == -2:
                        print(" 不存在")
                    else:
                        print(" UID {} 抓取成功".format(flag))
            wait(all_task, return_when=ALL_COMPLETED)
            elapsed = (time.perf_counter() - starttime)
            print("爬取uid {} - {} 的用户,共 {} 条，有效数据 {} 条.共用时 {:.2f} s.".format(start, end, end - start, total, elapsed))
        except Exception as e:
            print("出错了！{}".format(e))
            elapsed = (time.perf_counter() - starttime)
            print("爬取uid {} - {} 的用户,共 {} 条，有效数据 {} 条.共用时 {:.2f} s.".format(start, end, end - start, total, elapsed))
    stopApi(p)
