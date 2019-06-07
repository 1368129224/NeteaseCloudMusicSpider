import pymysql
from Helper.SqlHelper import getMySqlTx


def init_db():
    '''
    初始化数据库
    :return:
    '''
    db = pymysql.connect(**getMySqlTx())
    cursor = db.cursor()
    #删除存在表
    cursor.execute('drop table if exists T_Artists')
    cursor.execute('drop table if exists T_HotSongs')
    cursor.execute('drop table if exists T_FansInfo')
    #创建表
    cursor.execute("CREATE TABLE T_Artists( \
                        id INT NOT NULL   COMMENT 'aid 歌手ID' , \
                        name VARCHAR(128)    COMMENT 'aname 歌手名' , \
                        PRIMARY KEY (id) \
                    ) COMMENT = '歌手表 ';;")
    cursor.execute("CREATE TABLE T_HotSongs( \
                        id INT NOT NULL   COMMENT 'sid 歌曲ID' , \
                        rating INT    COMMENT 'rating 热度排名' , \
                        name VARCHAR(128)    COMMENT 'name 歌曲名' , \
                        aid INT    COMMENT 'artist_id 歌手ID' , \
                        PRIMARY KEY (id) \
                    ) COMMENT = '热门歌曲表 ';;")
    cursor.execute("CREATE TABLE T_FansInfo( \
                        id INT NOT NULL   COMMENT 'id 粉丝ID' , \
                        aid INT    COMMENT 'aid 歌手ID' , \
                        nickname VARCHAR(128)    COMMENT 'nickname 昵称' , \
                        level INT    COMMENT 'level 等级' , \
                        city INT    COMMENT 'city 城市' , \
                        followeds INT    COMMENT 'followeds 粉丝数' , \
                        follows INT    COMMENT 'follows 关注数' , \
                        playlists INT    COMMENT 'playlists 歌单数量' , \
                        PRIMARY KEY (id) \
                    ) COMMENT = '粉丝表 ';;")
    db.close()

def create_comments_table(sid, db):
    '''
    创建歌曲评论表
    :param sid: 歌曲ID
    :param db: 数据库链接
    :return:
    '''
    cursor = db.cursor()
    cursor.execute("CREATE TABLE {}_Comments( \
                        cid INT NOT NULL   COMMENT 'cid 评论ID' , \
                        sid INT    COMMENT 'sid 歌曲ID' , \
                        likedCount INT    COMMENT 'likedCount 点赞数' , \
                        uid INT    COMMENT 'uid 评论者ID' , \
                        uname VARCHAR(128)    COMMENT 'uname 评论者昵称' , \
                        content TEXT    COMMENT 'content 评论内容' , \
                        PRIMARY KEY (cid) \
                    ) COMMENT = '评论表 ';;".format(sid))

def create_fans_table(aid, db):
    '''
    创建歌手粉丝表
    :param aid: 歌手ID
    :param db: 数据库连接
    :return:
    '''
    cursor = db.cursor()
    cursor.execute("CREATE TABLE {}_FansInfo( \
                        id INT NOT NULL   COMMENT 'id 粉丝ID' , \
                        nickname VARCHAR(128)    COMMENT 'nickname 昵称' , \
                        level INT    COMMENT 'level 等级' , \
                        city INT    COMMENT 'city 城市' , \
                        followeds INT    COMMENT 'followeds 粉丝数' , \
                        follows INT    COMMENT 'follows 关注数' , \
                        playlists INT    COMMENT 'playlists 歌单数量' , \
                        PRIMARY KEY (id) \
                    ) COMMENT = '粉丝表 ';;".format(aid))
