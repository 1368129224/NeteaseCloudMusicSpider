import sys
from Helper.ApiHelper import api
from Spiders.search_artist import get_artist_id, get_songs, get_comments

Api = api()
name = input('请输入歌手名：')
id = get_artist_id(name, Api)
songs = get_songs(id, Api)
print(sys.getsizeof(id))
print(sys.getsizeof(songs))
for item in songs:
    get_comments(item['id'], item['name'], Api)
