import collections
import os
import re
import wordcloud
import numpy
import jieba
import pymysql
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

if __name__ == '__main__':
    ids = get_ids()
    print(type(ids))
    print(ids)