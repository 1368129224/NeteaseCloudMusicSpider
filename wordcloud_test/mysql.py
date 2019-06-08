import collections
import os
import re
import wordcloud
import numpy
import jieba
import pymysql
import requests
import json
from bs4 import BeautifulSoup
from PIL import Image
from Helper.SqlHelper import getMySqlTx
from Helper import BASE_PATH


def get_comments(id):
    comments = []
    db = pymysql.connect(**getMySqlTx())
    cursor = db.cursor()
    cursor.execute("SELECT content FROM {}_Comments".format(id))
    for row in cursor.fetchall():
        comments.append(row[0])
    db.close()
    return comments

def get_ids():
    ids = []
    db = pymysql.connect(**getMySqlTx())
    cursor = db.cursor()
    cursor.execute("SELECT id FROM `T_HotSongs` ORDER BY rating")
    for row in  cursor.fetchall():
        ids.append(row[0])
    db.close()
    return ids

def partition(comments):
    result = []
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"|。|，|？|！|“|”|\[|\]|—|《|》| |~|]|（|）|…|、|\+|：')
    for item in comments:
        words = jieba.cut(item)
        for word in words:
            if not re.match(pattern, word) and len(word) != 1:
                result.append(word)
        if len(result) != 0:
            result.pop()
    return result

def word_count(word_list):
    word_counts = collections.Counter(word_list)
    return word_counts

def draw_picture(word_counts, sid):
    mask = numpy.array(Image.open(os.path.join(BASE_PATH, 'wordcloud_test\picture.png')))
    w = wordcloud.WordCloud(
        width=960,
        height=540,
        font_path=os.path.join(BASE_PATH,'wordcloud_test\Deng.ttf'),
        mask=mask,
        max_words=100,
        max_font_size=100,
        background_color='white',
    )
    w.generate_from_frequencies(word_counts)
    w.to_file(os.path.join(BASE_PATH, 'wordcloud_pictures\{}.png'.format(sid)))

def request_loccodes():
    # 中华人民共和国行政区划代码
    # 14年
    url = 'http://files2.mca.gov.cn/cws/201502/20150225163817214.html'
    # 19年
    # url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/201901-06/201905271445.html'
    try:
        r = requests.get(url)
        if r.status_code == 200:
            r.encoding = "utf-8"
            soup = BeautifulSoup(r.text, 'lxml')
            items = soup.find_all('tr', attrs={"height": "19"})
            with open('loccodes.txt', 'a+', encoding='utf8') as f:
                for item in items:
                    f.write(item.find_all('td')[1].text + ',' + item.find_all('td')[2].text)
                    f.write('\n')
                    # locs[item.find_all('td')[1].text] = item.find_all('td')[2].text
    except Exception as e:
        print("获取失败！" + str(e))

def get_loccodes():
    codes = {}
    with open(os.path.join(BASE_PATH, 'Document\loccodes.txt'), 'r', encoding='utf8') as f:
        file = f.readlines()
        for line in file:
            l = line.split(',')
            codes[l[0]] = l[1].strip()
    return codes

def get_city():
    db = pymysql.connect(**getMySqlTx())
    cursor = db.cursor()
    cursor.execute("SELECT city, COUNT(city) FROM 5771_FansInfo WHERE city < 1000000 AND city > 1000 GROUP BY city")
    loccodes = get_loccodes()
    citys = {}
    for item in cursor.fetchall():
        try:
            if citys.get(loccodes[str(item[0])], None) != None:
                citys[loccodes[str(item[0])]] = citys[loccodes[str(item[0])]] + item[1]
            else:
                citys[loccodes[str(item[0])]] = item[1]
        except:
            temp = item[0] - (item[0] % 1000)
            if citys.get(loccodes[str(temp)], None) != None:
                citys[loccodes[str(temp)]] = citys[loccodes[str(temp)]] + item[1]
            else:
                citys[loccodes[str(temp)]] = item[1]
    db.close()
    return citys

def getlnglat(citys):
    url = "http://api.map.baidu.com/geocoder/v2/"
    ak = 'SWfy5j8unADeKluymL2UvEIRt5R88qsb'
    temp = []
    for city in citys:
        uri = url + '?' + 'address=' + city + '&output=json&ak=' + ak
        resp = requests.get(uri)
        temp.append(
            {
                'lat': resp.json()['result']['location']['lat'],
                'lng': resp.json()['result']['location']['lng'],
                'count': citys[city],
            }
        )
    return temp


# 生成热力图
def generate_map(aid, loc_counts):
    with open(os.path.join(BASE_PATH, 'Document\\template.html'), 'r', encoding='utf8') as f:
        source = f.readlines()
        print(source)
        with open("{}.html".format(aid), 'a', encoding='utf8') as result:
            for i in range(0, 27):
                result.write(source[i])
            for line in loc_counts:
                result.write(str(line) + ',')
            for i in range(27, len(source)):
                result.write(source[i])

if __name__ == '__main__':
    ids = get_ids()
    print(type(ids))
    print(ids)