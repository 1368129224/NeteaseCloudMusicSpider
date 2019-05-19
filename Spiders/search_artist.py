import requests
import csv
import sys
from Helper import DB
from sqlalchemy.orm import sessionmaker
from concurrent.futures import ThreadPoolExecutor

def get_artist_id(name, api):
    try:
        api.startApi()
        url_search_artist = 'http://localhost:3000/search?type=100&keywords={}'.format(name)
        resp = requests.get(url = url_search_artist)
        artist = resp.json()['result']['artists'][0]
        print(artist['id'], artist['name'])
        session = sessionmaker(bind=DB.engine)
        session = session()
        DB.Base.metadata.create_all(DB.engine)
        row = DB.Atists(Aid = artist['id'], Aname = artist['name'])
        session.add(row)
        session.commit()
        session.close()
    finally:
        api.stopApi()
    return artist['id']

def get_songs(id, api):
    try:
        api.startApi()
        url_get_artist_songs = 'http://localhost:3000/artists?id={}'.format(id)
        resp = requests.get(url = url_get_artist_songs)
        session = sessionmaker(bind=DB.engine)
        session = session()
        DB.Base.metadata.create_all(DB.engine)
        songs = []
        for item in resp.json()['hotSongs']:
            songs.append({'id':item['id'], 'name':item['name']})
            row = DB.Songs(Sid=item['id'], Sname=item['name'], artist_Aid=id)
            session.add(row)
        session.commit()
        session.close()
    finally:
        api.stopApi()
    return songs

def request_comment(url, songid):
    resp = requests.get(url=url)
    session = sessionmaker(bind=DB.engine)
    session = session()
    DB.Base.metadata.create_all(DB.engine)
    for item in resp.json()['comments']:
        print(len(resp.json()['comments']))
        comments.append(
            {'commentId':item['commentId'], 'userId': item['user']['userId'], 'nickname': item['user']['nickname'], 'likedCount': item['likedCount'],
             'content': item['content']})
        row = DB.Comments(Cid=item['commentId'], Uid=item['user']['userId'], Uname=item['user']['nickname'], LikeCount=item['likedCount'], Content=item['content'], song_Sid=songid)
        session.add(row)
        print(sys.getsizeof(comments))
    session.commit()
    session.close()

def get_comments(song_id, song_name, api):
    api.startApi()
    url_get_comment = 'http://localhost:3000/comment/music?id={}&limit=100&offset={}'.format(song_id, 0)
    resp = requests.get(url=url_get_comment)
    total = resp.json()['total']
    urls = ['http://localhost:3000/comment/music?id={}&limit=100&offset={}'.format(song_id, i) for i in range(0, total + 100, 100)]
    ids = [song_id for i in range(0, total + 100, 100)]
    with ThreadPoolExecutor(128) as executor:
        executor.map(request_comment, urls, ids)
    api.stopApi()


