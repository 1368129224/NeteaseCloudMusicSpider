import requests
import time
import pymysql
from bs4 import BeautifulSoup
from Spiders import mysql
from Helper.ApiHelper import api
from Helper.SqlHelper import getMySqlTx
from Helper import Database


if __name__ == '__main__':
    # print(get_loccodes())

    # 初始化数据库
    # Database.init_db()

    Api = api()
    Api.startApi()
    name = input('请输入歌手名：').strip()
    while name == '':
        name = input('请输入歌手名：').strip()
    start_time = time.time()
    try:
        # db = pymysql.connect(**getMySqlTx())

        # 搜索歌手
        # try:
        #     artist_info = mysql.get_artist_id(name, Api)
        #     print(artist_info)
        #     # 创建粉丝表
        #     db = pymysql.connect(**getMySqlTx())
        #     Database.create_fans_table(artist_info[0], db)
        #     db.close()
        # except Exception as e:
        #     print('搜索歌手出错' + str(e))

        # 获取歌手前50首热门歌曲ID
        # try:
        #     songs = mysql.get_songs(artist_info, Api)
        # except Exception as e:
        #     print('获取热门歌曲出错' + str(e))

        # 为每首歌创建表，并爬取评论存入表中
        # try:
        #     for song_info in songs:
        #         db = pymysql.connect(**getMySqlTx())
        #         Database.create_comments_table(song_info['sid'], db)
        #         db.close()
        #         mysql.get_comments_multi_thread(song_info, Api)
        # except Exception as e:
        #     print('爬取评论出错' + str(e))

        # 获取用户信息
        try:
            mysql.get_fans_infos_multi_thread(5771, Api)
        except  Exception as e:
            print('获取用户信息出错' + str(e))

        # finally:
        #     db.close()

    except Exception as e:
        print('test' + str(e))
    finally:
        Api.stopApi()
        # db.close()
    # print(artist_info)
    print(time.time() - start_time)
