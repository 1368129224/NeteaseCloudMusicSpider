import requests
import time
import pymysql
from bs4 import BeautifulSoup
from Spiders import mysql
from Helper.ApiHelper import api
from Helper.SqlHelper import getMySqlTx
from Helper import Database


def get_loccodes():
    # 中华人民共和国行政区划代码
    url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/201901-06/201905271445.html'
    locs = {}
    try:
        r = requests.get(url)
        if r.status_code == 200:
            r.encoding = "utf-8"
            soup = BeautifulSoup(r.text, 'lxml')
            items = soup.find_all('tr', attrs={"height": "19"})
            # 城市编码的个数
            print(print(len(items)))
            for item in items:
                # 提取数据
                # print(item.find_all('td')[1].text, item.find_all('td')[2].text)
                locs[item.find_all('td')[1].text] = item.find_all('td')[2].text
    except Exception as e:
        print("获取失败！" + str(e))

    # 可视化输出
    # print(locs)
    return locs

if __name__ == '__main__':
    # print(get_loccodes())

    # 初始化数据库
    Database.init_db()

    Api = api()
    Api.startApi()
    name = input('请输入歌手名：').strip()
    while name == '':
        name = input('请输入歌手名：').strip()
    start_time = time.time()
    try:
        # db = pymysql.connect(**getMySqlTx())

        # 搜索歌手
        try:
            artist_info = mysql.get_artist_id(name, Api)
            print(artist_info)
            # 创建粉丝表
            db = pymysql.connect(**getMySqlTx())
            Database.create_fans_table(artist_info[0], db)
            db.close()
        except Exception as e:
            print('搜索歌手出错' + str(e))
            exit()

        # 获取歌手前50首热门歌曲ID
        try:
            songs = mysql.get_songs(artist_info, Api)
        except Exception as e:
            print('获取热门歌曲出错' + str(e))
            exit()

        # 为每首歌创建表，并爬取评论存入表中
        try:
            for song_info in songs:
                db = pymysql.connect(**getMySqlTx())
                Database.create_comments_table(song_info['sid'], db)
                db.close()
                mysql.get_comments_multi_thread(song_info, Api)
        except Exception as e:
            print('爬取评论出错' + str(e))
            exit()

        finally:
            db.close()

    except Exception as e:
        print('test' + str(e))
    finally:
        Api.stopApi()
        # db.close()
    # print(artist_info)
    print(time.time() - start_time)
