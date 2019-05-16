import requests
from Helper.ApiHelper import api


url_search_artist = 'http://localhost:3000/search?type=100&keywords='
Api = api()
Api.startApi()
name = input('请输入歌手名：')
resp = requests.get(url = url_search_artist + name)
artist = resp.json()['result']['artists'][0]
print(artist['id'], artist['name'])
Api.stopApi()