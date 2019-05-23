import sys
from Helper.ApiHelper import api
from Helper.SqlHelper import getMongoTx
from Spiders.search_artist import get_artist_id, get_songs, get_comments_multi_thread
import pymongo
import time

start_time = time.time()
client = pymongo.MongoClient(getMongoTx())
db = client['163music']
Api = api()
Api.startApi()
name = input('请输入歌手名：').strip()
try:
    artist_info = get_artist_id(name, Api)
    songs = get_songs(artist_info, Api)
    print(sys.getsizeof(songs))
    for index, song_info in enumerate(songs):
        get_comments_multi_thread(song_info, Api, db)
finally:
    Api.stopApi()
print(time.time() - start_time)
