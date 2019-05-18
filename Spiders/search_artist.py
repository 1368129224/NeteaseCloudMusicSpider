import requests
import csv
import sys
from fake_useragent import UserAgent
from Helper.ApiHelper import api

def get_artist_id(name, api):
    api.startApi()
    url_search_artist = 'http://localhost:3000/search?type=100&keywords={}'.format(name)
    resp = requests.get(url = url_search_artist)
    artist = resp.json()['result']['artists'][0]
    print(artist['id'], artist['name'])
    api.stopApi()
    return artist['id']

def get_songs(id, api):
    api.startApi()
    url_get_artist_songs = 'http://localhost:3000/artists?id={}'.format(id)
    resp = requests.get(url = url_get_artist_songs)
    songs = []
    for item in resp.json()['hotSongs']:
        songs.append({'id':item['id'], 'name':item['name']})
    api.stopApi()
    return songs

def get_comments(song_id, api):
    # session = requests.Session()
    # session.keep_alive = False
    # # session.adapters.DEFAULT_RETRIES = 5
    # requests.adapters.DEFAULT_RETRIES = 5
    ua = UserAgent()
    headers = {
        'UserAgent':ua.random
    }
    api.startApi()
    comments = []
    url_get_comment = 'http://localhost:3000/comment/music?id={}&limit=100&offset={}'.format(song_id, 0)
    resp = requests.get(url=url_get_comment, headers = headers)
    total = resp.json()['total']
    for i in range(0, 5100, 100):
        url_get_comment = 'http://localhost:3000/comment/music?id={}&limit=100&offset={}'.format(song_id, i)
        resp = requests.get(url=url_get_comment, headers = headers)
        for item in resp.json()['comments']:
            comments.append({'userId':item['user']['userId'], 'nickname':item['user']['nickname'], 'likedCount':item['likedCount'], 'content':item['content']})
        print(sys.getsizeof(comments))
    for i in range(total - 5000, total + 100, 100):
        url_get_comment = 'http://localhost:3000/comment/music?id={}&limit=100&offset={}'.format(song_id, i)
        resp = requests.get(url=url_get_comment, headers=headers)
        for item in resp.json()['comments']:
            comments.append({'userId': item['user']['userId'], 'nickname': item['user']['nickname'],
                             'likedCount': item['likedCount'], 'content': item['content']})
        print(sys.getsizeof(comments))
    api.stopApi()
    with open('comments.csv', 'a', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, dialect='excel')
        w.writerow(['userId', 'nickname', 'likedCount', 'content'])
        for line in comments:
            w.writerow([str(line['userId']), str(line['nickname']), str(line['likedCount']), str(line['content'])])

def testa(api):
    url = 'http://localhost:3000/comment/music?id=210049&limit=100&offset='
    ua = UserAgent()
    api.startApi()
    headers = {
        'UserAgent': ua.random
    }
    try:
        for i in range(0, 26000, 100):
            resp = requests.get(url=url + str(i), headers=headers)
            print(i, resp.status_code, resp.json()['code'])
    finally:
        api.stopApi()
