import requests
from utils.ApiHelper import Api
from utils import db


class GetUserInfo:
    def __init__(self, start_uid, end_uid):
        '''
        设定uid范围
        :param start_uid: 起始值
        :param end_uid: 结束值
        '''
        self.__start_uid = start_uid
        self.__end_uid = end_uid

    def __get_user_info(self, uid):
        url = f'http://localhost:3000/user/detail?uid={uid}'
        json_data = requests.get(url).json()
        if json_data['code'] == 404:
            return False
        user_info = {
            'uid': uid,
            'level': json_data.get('level', None), # 等级
            'listenSongs': json_data.get('listenSongs', None), # 听歌数量
            'profile': {
                'city': json_data['profile'].get('birthday', None), # 城市
                'birthday': json_data['profile'].get('birthday', None), # 生日
                'gender': json_data['profile'].get('gender', None), # 性别
                'nickname': json_data['profile'].get('nickname', None), # 昵称
                'createTime': json_data['profile'].get('createTime', None), # 创建时间
                'followeds': json_data['profile'].get('followeds', None), # 粉丝数
                'follows': json_data['profile'].get('follows', None), # 关注数
                'eventCount': json_data['profile'].get('eventCount', None), # 动态数
                'playlistCount': json_data['profile'].get('playlistCount', None), # 歌单数
            },
            'createDays': json_data.get('createDays', None) # 账号使用时长
        }
        db.users.insert_one(user_info)
        return True
        
    def __get_user_palylist(self, uid):
        url = f'http://localhost:3000/user/playlist?uid={uid}'
        resp_json = requests.get(url).json()
        if resp_json['code'] == 404:
            return
        playlist_json_data = resp_json['playlist']
        new_playlists = []
        for l in playlist_json_data:
            detail = self.__get_playlist_info(l.get('id', None))
            playlist_info = {
                'id': l.get('id', None), # 歌单ID
                'updateTime': l.get('updateTime', None), # 更新时间
                'trackCount': l.get('trackCount', None), # 歌曲数量
                'commentThreadId': l.get('commentThreadId', None), # 评论ID
                'playCount': l.get('playCount', None), # 播放次数
                'createTime': l.get('createTime', None), # 创建时间
                'subscribedCount': l.get('subscribedCount', None), # 收藏数
                'name': l.get('name', None), # 歌单名
                'tags': l.get('tags', None), # 歌单标签
            }
            playlist_info.update(detail)
            new_playlists.append(playlist_info)
        db.users.update_one({'uid': uid}, {'$set': {'playlists': new_playlists}})

    def __get_playlist_info(self, pid):
        url = f'http://localhost:3000/playlist/detail?id={pid}'
        resp_json =  requests.get(url).json()
        if resp_json['code'] == 404:
            return
        playlist_info_data = resp_json.get('playlist', None)
        subscribers = []
        for subscriber in playlist_info_data.get('subscribers'):
            subscribers.append({
                'userId': subscriber.get('userId', None)
            })
        tracks = []
        for track in playlist_info_data.get('tracks'):
            tracks.append({
                'name': track.get('name', None),
                'id': track.get('id', None),
                'artistId': track['al'].get('id', None),
                'artistName': track['al'].get('name', None),
            })
        data = {
            'subscribers': subscribers,
            'tracks': tracks
        }
        return data


    def run(self):
        api = Api()
        api.startApi()
        try:
            for uid in range(self.__start_uid, self.__end_uid):
                if self.__get_user_info(uid):
                    self.__get_user_palylist(uid)
        except Exception as e:
            print(e)
        finally:
            api.stopApi()

if __name__ == '__main__':
    user = GetUserInfo(38166622, 38166723)
    user.run()