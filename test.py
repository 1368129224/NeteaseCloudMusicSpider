import requests
from bs4 import BeautifulSoup
from wordcloud_test import mysql as wcmysql


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
    ids = wcmysql.get_ids()
    for sid in ids:
        comments = wcmysql.get_comments(sid)
        partition_result = wcmysql.partition(comments)
        wordlist = wcmysql.word_count(partition_result)
        draw_picture = wcmysql.draw_picture(wordlist, sid)

    # 测试
    # comments = wcmysql.get_comments(ids[0])
    # partition_result = wcmysql.partition(comments)
    # wordlist = wcmysql.word_count(partition_result)
    # draw_picture = wcmysql.draw_picture(wordlist, ids[0])
