from Helper.SqlHelper import getMongoTx
import pymongo
import pkuseg


# client = pymongo.MongoClient(getMongoTx())
# db = client['163music']
# collection_names = db.list_collection_names()
# collection = db.get_collection(collection_names[0])
# result = collection.find({},{'_id':0, 'content':1})
# comments = []
# with open('comments.txt', 'w', encoding='utf-8') as f:
#     for item in result:
#         comments.append(item['content'])
#         f.write(item['content'])
if __name__ == '__main__':
    pkuseg.test('test.txt', 'output.txt', nthread=8)
