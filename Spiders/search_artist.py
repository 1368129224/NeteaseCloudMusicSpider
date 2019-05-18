import requests
import csv
import sys
from Helper.ApiHelper import comments
from concurrent.futures import ThreadPoolExecutor

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

def request_comment(url):
    resp = requests.get(url=url)
    comments = []
    for item in resp.json()['comments']:
        print(len(resp.json()['comments']))
        comments.append(
            {'userId': item['user']['userId'], 'nickname': item['user']['nickname'], 'likedCount': item['likedCount'],
             'content': item['content']})
        print(sys.getsizeof(comments))

def get_comments(song_id, song_name, api):
    api.startApi()
    url_get_comment = 'http://localhost:3000/comment/music?id={}&limit=100&offset={}'.format(song_id, 0)
    resp = requests.get(url=url_get_comment)
    total = resp.json()['total']
    urls = ['http://localhost:3000/comment/music?id={}&limit=100&offset={}'.format(song_id, i) for i in range(0, total + 100, 100)]
    with ThreadPoolExecutor(128) as executor:
        executor.map(request_comment, urls)
    api.stopApi()
    print(comments)
    with open('{}-{}.csv'.format(song_id, song_name), 'a', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, dialect='excel')
        w.writerow(['userId', 'nickname', 'likedCount', 'content'])
        for line in comments:
            w.writerow([str(line['userId']), str(line['nickname']), str(line['likedCount']), str(line['content'])])


