import sys
from Helper.ApiHelper import api
from Spiders.search_artist import get_artist_id, get_songs, get_comments, testa


Api = api()
name = input('请输入歌手名：')
id = get_artist_id(name, Api)
songs = get_songs(id, Api)
print(sys.getsizeof(id))
print(sys.getsizeof(songs))
get_comments(songs[0]['id'], Api)
# testa(Api)
