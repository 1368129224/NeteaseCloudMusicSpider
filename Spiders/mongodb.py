import requests
import sys
from concurrent.futures import ThreadPoolExecutor

def get_artist_id(name, api):
    url_search_artist = 'http://localhost:3000/search?type=100&keywords={}'.format(name)
    resp = requests.get(url = url_search_artist)
    try:
        artist = resp.json()['result']['artists'][0]
        print(artist['id'], artist['name'])
    except Exception as e:
        api.stopApi()
        api.startApi()
        return get_artist_id(name, api)
    return (artist['id'], artist['name'])

def get_songs(artist_info, api):
    url_get_artist_songs = 'http://localhost:3000/artists?id={}'.format(artist_info[0])
    resp = requests.get(url = url_get_artist_songs)
    songs = []
    try:
        for index, item in enumerate(resp.json()['hotSongs']):
            songs.append({'rating':index + 1, 'aid':artist_info[0], 'aname':artist_info[1], 'sid':item['id'], 'sname':item['name']})
    except Exception as e:
        print('get_songs' + e)
        api.stopApi()
        api.startApi()
        return get_songs(artist_info, api)
    return songs

def request_comment(url, song_info, db, api):
    collection = db[str(song_info['rating']) + '@' +str(song_info['sid']) + '@' + str(song_info['sname'])]
    resp = requests.get(url=url)
    comments = []
    try:
        for item in resp.json()['comments']:
            comments.append(
                {'aid':song_info['aid'],'aname':song_info['aname'],'sid':song_info['sid'],'sname':song_info['sname'],'commentId':item['commentId'], 'userId': item['user']['userId'], 'nickname': item['user']['nickname'], 'likedCount': item['likedCount'],
                 'content': item['content']})
        collection.insert_many(comments)
    except Exception as e:
        print('request_comment' + e)
        api.stopApi()
        api.startApi()
        request_comment(url, song_info, db, api)

def get_comments_multi_thread(song_info, api, db):
    url_get_comment = 'http://localhost:3000/comment/music?id={}&limit=100&offset={}'.format(song_info['sid'], 0)
    try:
        resp = requests.get(url=url_get_comment)
        total = resp.json()['total']
    except Exception as e:
        api.stopApi()
        api.startApi()
        resp = requests.get(url=url_get_comment)
        total = resp.json()['total']
    urls = ['http://localhost:3000/comment/music?id={}&limit=100&offset={}'.format(song_info['sid'], i) for i in range(0, total + 100, 100)]
    song_infos = [song_info for i in range(0, total + 100, 100)]
    dbs = [db for i in range(0, total + 100, 100)]
    apis = [api for i in range(0, total + 100, 100)]
    with ThreadPoolExecutor(64) as executor:
        executor.map(request_comment, urls, song_infos, dbs, apis)

