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
        
    def __get_user_palylist(self, uid):
        url = f'http://localhost:3000/user/playlist?uid={uid}'
        playlist_json_data = requests.get(url).json()['playlist']
        new_playlists = []
        for l in playlist_json_data:
            playlist_info = {
                'id': l.get('id', None),
                'updateTime': l.get('updateTime', None),
                'trackCount': l.get('trackCount', None),
                'commentThreadId': l.get('commentThreadId', None),
                'playCount': l.get('playCount', None),
                'createTime': l.get('createTime', None),
                'subscribedCount': l.get('subscribedCount', None),
                'name': l.get('name', None),
                'tags': l.get('tags', None),
            }
            new_playlists.append(playlist_info)
        db.users.update_one({'uid': uid}, {'$set': {'playlists': new_playlists}})

    def run(self):
        api = Api()
        api.startApi()

        for uid in range(self.__start_uid, self.__end_uid):
            self.__get_user_info(uid)
            self.__get_user_palylist(uid)

        api.stopApi()

if __name__ == '__main__':
    user = GetUserInfo(38166722, 38166723)
    user.run()