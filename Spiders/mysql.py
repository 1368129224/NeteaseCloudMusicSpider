import requests
import pymysql
from concurrent.futures import ThreadPoolExecutor
from Helper import models
from Helper.SqlHelper import getMySqlTx


def get_artist_id(name, api):
    url_search_artist = 'http://localhost:3000/search?type=100&keywords={}'.format(name)
    resp = requests.get(url = url_search_artist)
    try:
        db = pymysql.connect(**getMySqlTx())
        cursor = db.cursor()
        artist = resp.json()['result']['artists'][0]
        try:
            cursor.execute("INSERT INTO T_Artists VALUES ({}, '{}')".format(artist['id'], artist['name']))
        except Exception as e:
            print(e)
            db.rollback()
        db.commit()
    except Exception as e:
        print(e)
        api.stopApi()
        api.startApi()
        return get_artist_id(name, api)
    finally:
        db.close()
    return (artist['id'], artist['name'])

def get_songs(artist_info, api):
    url_get_artist_songs = 'http://localhost:3000/artists?id={}'.format(artist_info[0])
    resp = requests.get(url = url_get_artist_songs)
    songs = []
    try:
        for index, item in enumerate(resp.json()['hotSongs']):
            songs.append({'rating':index + 1, 'aid':artist_info[0], 'sid':item['id'], 'sname':item['name']})
            # songs.append(models.HotSongs(id = item['id'], rating = index + 1, name = item['name'], artist_id = artist_info[0]))
        db = pymysql.connect(**getMySqlTx())
        cursor = db.cursor()
        for song in songs:
            try:
                cursor.execute("INSERT INTO T_HotSongs VALUES ({}, {}, '{}', {})".format(song['id'], song['rating'], song['name'], song['aid']))
            except Exception as e:
                print(e)
                db.rollback()
            db.commit()
    except Exception as e:
        print(e)
        api.stopApi()
        api.startApi()
        return get_songs(artist_info, api)
    finally:
        db.close()
    return songs

def request_comment(url, song_info, api, db):
    resp = requests.get(url=url)
    comments = []
    try:
        for item in resp.json()['comments']:
            comments.append(
                {'sid':song_info['sid'],'cid':item['commentId'], 'uid': item['user']['userId'], 'uname': item['user']['nickname'], 'likedCount': item['likedCount'],
                 'content': item['content']})
        cursor = db.cursor()
        for comment in comments:
            try:
                cursor.execute("INSERT INTO T_Comments VALUES ({}, {}, {}, {}, {}, '{}')".format( \
                    comment['cid'],comment['sid'],comment['likedCount'],comment['uid'],comment['uname'],comment['content']))
            except Exception as e:
                print(e)
                db.rollback()
            db.commit()
    except Exception as e:
        print(e)
        api.stopApi()
        api.startApi()
        request_comment(url, song_info, api, db)
    finally:
        db.close()

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
    urls = ['http://localhost:3000/comment/music?id={}&limit=100&offset={}'.format(
        song_info['sid'], i) for i in range(0, 11000, 100)]
    urls.extend(['http://localhost:3000/comment/music?id={}&limit=100&offset={}'.format(
        song_info['sid'], i) for i in range(total - 11000, total, 100)])
    song_infos = [song_info for i in range(0,len(urls))]
    apis = [api for i in range(0,len(urls))]
    dbs = [db for i in range(0, len(urls))]
    with ThreadPoolExecutor(128) as executor:
        executor.map(request_comment, urls, song_infos, apis, dbs)

def get_fans_info(aid, db):
    fans = models.select_fans_id(aid, db)

    pass