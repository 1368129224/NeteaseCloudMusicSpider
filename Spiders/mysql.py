import requests
import pymysql
from concurrent.futures import ThreadPoolExecutor
from Helper.SqlHelper import getMySqlTx


def get_artist_id(name, api):
    '''
    搜索歌手
    :param name: 歌手名
    :param api: api
    :return: 元组:(歌手ID,歌手名)
    '''
    url_search_artist = 'http://localhost:3000/search?type=100&keywords={}'.format(name)
    resp = requests.get(url = url_search_artist)
    try:
        db = pymysql.connect(**getMySqlTx())
        cursor = db.cursor()
        artist = resp.json()['result']['artists'][0]
        try:
            cursor.execute("INSERT INTO T_Artists VALUES ({}, '{}')".format(artist['id'], artist['name']))
        except Exception as e:
            print('INSERT INTO T_Artists' + str(e))
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
    '''
    获取歌手的前50首热门歌曲
    :param artist_info: 歌手信息,即get_artist_id返回的元组:(歌手ID,歌手名)
    :param api: api
    :return: 列表:[{'rating':歌曲热门度, 'aid':歌手ID, 'sid':歌曲ID, 'sname':歌曲名},...]
    '''
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
                cursor.execute("INSERT INTO T_HotSongs VALUES ({}, {}, '{}', {})".format(
                    song['sid'], song['rating'], song['sname'], song['aid'])
                )
            except Exception as e:
                print('INSERT INTO T_HotSongs' + str(e))
                db.rollback()
            db.commit()
    except Exception as e:
        print('get_songs' + str(e))
        api.stopApi()
        api.startApi()
        return get_songs(artist_info, api)
    finally:
        db.close()
    return songs

def request_comment(url, song_info, api):
    '''
    获取歌曲评论
    :param url: 需要爬取的url
    :param song_info: 歌曲信息即,get_songs返回的列表的item:{'rating':歌曲热门度, 'aid':歌手ID, 'sid':歌曲ID, 'sname':歌曲名}
    :param api: api
    :return: None
    '''
    db = pymysql.connect(**getMySqlTx())
    resp = requests.get(url=url)
    comments = []
    try:
        for item in resp.json()['comments']:
            comments.append(
                [
                    item['commentId'],
                    song_info['sid'],
                    item['likedCount'],
                    item['user']['userId'],
                    item['user']['nickname'],
                    item['content']
                ]
            )
    except Exception as e:
        print(e)
        api.stopApi()
        api.startApi()
        request_comment(url, song_info, api)
    cursor = db.cursor()
    sql_comments = "INSERT INTO " + str(song_info['sid']) + "_Comments VALUES (%s, %s, %s, %s, %s, %s)"
    for comment in comments:
        try:
            cursor.execute(sql_comments, comment)
        except Exception as e:
            print('INSERT INTO Comments' + str(e))
            db.rollback()
        db.commit()
        try:
            cursor.execute("INSERT INTO `163music_new`.`"+ str(song_info['aid'])
                           + "_FansInfo`(`id`, `nickname`, `level`, `city`, `followeds`, `follows`, `playlists`) " \
                "VALUES ({}, NULL, NULL, NULL, NULL, NULL, NULL);".format(comment[3]))
        except Exception as e:
            pass
        db.commit()
    db.close()

def get_comments_multi_thread(song_info, api):
    '''
    多线程爬取评论入口
    :param song_info: 歌曲信息即,get_songs返回的列表的item:{'rating':歌曲热门度, 'aid':歌手ID, 'sid':歌曲ID, 'sname':歌曲名}
    :param api: api
    :return: None
    '''
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
        song_info['sid'], i) for i in range(0, 5500, 100)]
    urls.extend(['http://localhost:3000/comment/music?id={}&limit=100&offset={}'.format(
        song_info['sid'], i) for i in range(total - 5500, total, 100)])
    song_infos = [song_info for i in range(0,len(urls))]
    apis = [api for i in range(0,len(urls))]
    with ThreadPoolExecutor(192) as executor:
        executor.map(request_comment, urls, song_infos, apis)

def get_fans_infos_multi_thread(aid, api):
    '''
    多线程爬取粉丝信息入口
    :param aid: 歌手ID
    :param api: api
    :return: None
    '''
    db = pymysql.connect(**getMySqlTx())
    cursor = db.cursor(pymysql.cursors.SSCursor)
    cursor.execute("SELECT id FROM {}_FansInfo WHERE city IS NULL".format(aid))
    with ThreadPoolExecutor(64) as executor:
        for i in cursor:
            executor.submit(request_info, aid, i[0], api)
    db.close()

def request_info(aid, uid, api):
    '''
    爬取粉丝信息
    :param aid: 歌手ID
    :param uid: 粉丝ID
    :param api: api
    :return: None
    '''
    url_get_info = 'http://localhost:3000/user/detail?uid=' + str(uid)
    db = pymysql.connect(**getMySqlTx())
    cursor = db.cursor()
    resp = requests.get(url_get_info)
    if resp.json()['code'] == 404:
        cursor.execute("DELETE FROM `{}_FansInfo` WHERE id = {}".format(aid, uid))
        db.commit()
        db.close()
        return
    total = resp.json()
    info = {}
    try:
        info['nickname'] = total['profile']['nickname']
        info['gender'] = total['profile']['gender']
        info['level'] = total['level']
        info['city'] = total['profile']['city']
        info['followeds'] = total['profile']['followeds']
        info['follows'] = total['profile']['follows']
        info['playlist'] = total['profile']['playlistCount']
        try:
            cursor.execute(
                "UPDATE `163music_new`.`{}_FansInfo` SET `nickname` = '{}', `gender` = '{}', `level` = {}, `city` = {}, `followeds` = {}, `follows` = {}, `playlists` = {} WHERE `id` = {};".format(
                    aid,
                    info['nickname'],
                    info['gender'],
                    info['level'],
                    info['city'],
                    info['followeds'],
                    info['follows'],
                    info['playlist'],
                    uid,
                )
            )
        except Exception as e:
            print('update error:' + str(e))
        db.commit()
    except Exception as e:
        print("request_info" + str(e))
        api.stopApi()
        api.startApi()
        db.close()
        request_info(aid, uid, api)
    finally:
        db.close()
