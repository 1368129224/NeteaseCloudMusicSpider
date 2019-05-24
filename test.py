from Helper.SqlHelper import getMongoTx
import pymongo
import jieba
import collections


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
    with open('comments.txt', 'r', encoding='utf-8') as s:
        comments = s.readlines()
        for item in comments:
            words = jieba.cut(item)
            for word in words:
                result.append(word)
    with open('result.txt', 'a+', encoding='utf-8') as r:
        for word in result:
            r.write(word + '\n')
if __name__ == '__main__':
    partition()
