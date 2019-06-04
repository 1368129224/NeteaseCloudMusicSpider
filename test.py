import requests
import time
from bs4 import BeautifulSoup
from Spiders import mysql
from Helper.ApiHelper import api
from Helper import models


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

    models.init_db()
    Api = api()
    Api.startApi()
    name = input('请输入歌手名：').strip()
    while name == '':
        name = input('请输入歌手名：').strip()
    start_time = time.time()
    try:
        artist_info = mysql.get_artist_id(name, Api)
        print(artist_info)
    #     songs = mysql.get_songs(artist_info, Api)
    #     for song_info in songs:
    #         mysql.get_comments_multi_thread(song_info, Api)
    finally:
        Api.stopApi()
    # print(artist_info)
    print(time.time() - start_time)
