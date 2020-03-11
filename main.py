import requests
import time
import pymysql
from bs4 import BeautifulSoup
from Spiders import spider as spmysql
from Wordcloud import mysql as wcmysql
from Helper.ApiHelper import api
from Helper.SqlHelper import getMySqlTx
from Helper import Database


if __name__ == '__main__':
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
        #     artist_info = spmysql.get_artist_id(name, Api)
        #     print(artist_info)
        #     # 创建粉丝表
        #     db = pymysql.connect(**getMySqlTx())
        #     Database.create_fans_table(artist_info[0], db)
        #     db.close()
        # except Exception as e:
        #     print('搜索歌手出错' + str(e))

        # 获取歌手前50首热门歌曲ID
        # try:
        #     songs = spmysql.get_songs(artist_info, Api)
        # except Exception as e:
        #     print('获取热门歌曲出错' + str(e))

        # 为每首歌创建表，并爬取评论存入表中
        # try:
        #     for song_info in songs:
        #         db = pymysql.connect(**getMySqlTx())
        #         Database.create_comments_table(song_info['sid'], db)
        #         db.close()
        #         spmysql.get_comments_multi_thread(song_info, Api)
        # except Exception as e:
        #     print('爬取评论出错' + str(e))

        # 获取用户信息
        try:
            spmysql.get_fans_infos_multi_thread(5771, Api)
        except  Exception as e:
            print('获取用户信息出错' + str(e))

        # finally:
        #     db.close()

        # 歌曲评论词云生成
        # ids = wcmysql.get_ids(5771)
        # for sid in ids:
        #     comments = wcmysql.get_comments(sid)
        #     partition_result = wcmysql.partition(comments)
        #     wordlist = wcmysql.word_count(partition_result)
        #     draw_picture = wcmysql.draw_picture(wordlist, sid)

        # 生成热力图
        # wcmysql.request_loccodes()
        # citys = wcmysql.get_city()
        # points = wcmysql.getlnglat(citys)
        # wcmysql.generate_map(5771, points)
        # print(points)

    except Exception as e:
        print('test' + str(e))
    finally:
        Api.stopApi()

    print(time.time() - start_time)
