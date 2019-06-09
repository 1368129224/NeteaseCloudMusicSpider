from Helper.SqlHelper import getMongoTx
from PIL import Image
import pymongo
import jieba
import collections
import re
import wordcloud
import numpy


def save_comments():
    client = pymongo.MongoClient(getMongoTx())
    db = client['163music']
    collection_names = db.list_collection_names()
    collection = db.get_collection(collection_names[0])
    result = collection.find({}, {'_id': 0, 'content': 1})
    with open('comments.txt', 'w', encoding='utf-8') as f:
        for item in result:
            f.write(item['content'].replace('\n', '') + '\n')

def partition():
    result = []
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"|。|，|？|！|“|”|\[|\]|—|《|》| |~|]|（|）|…|、|\+|：')
    with open('comments.txt', 'r', encoding='utf-8') as s:
        comments = s.readlines()
        for item in comments:
            words = jieba.cut(item)
            for word in words:
                if not re.match(pattern, word) and len(word) != 1:
                    result.append(word)
            result.pop()
    return result

def save_to_file(result):
    '''保存partition的结果到文件'''
    with open('result.txt', 'a+', encoding='utf-8', newline='') as r:
        for word in result:
            r.write(word + '\n')

def word_count(word_list):
    word_counts = collections.Counter(word_list)
    word_counts_top100 = word_counts.most_common(100)
    return word_counts
    # with open('top100.txt', 'w', encoding='utf-8') as f:
    #     for i in word_counts_top100:
    #         f.write(str(i) + '\n')


def generate_image(word_counts):
    mask = numpy.array(Image.open('picture.png'))
    w = wordcloud.WordCloud(
        width=960,
        height=540,
        font_path='Deng.ttf',
        mask=mask,
        max_words=100,
        max_font_size = 100
    )
    w.generate_from_frequencies(word_counts)
    w.to_file('test.png')

if __name__ == '__main__':
    print(type(word_count(partition())))
