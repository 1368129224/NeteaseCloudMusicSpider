from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Atists(Base):
    __tablename__ = 'artists'
    Aid = Column(Integer, primary_key=True)
    Aname = Column(String(64), index=True)

    def __repr__(self):
        return '{}:{}'.format(self.Aid, self.Aname)

class Songs(Base):
    __tablename__ = 'songs'
    Sid = Column(Integer, primary_key=True)
    Sname = Column(String(128), index=True)
    artist_Aid = Column(Integer, ForeignKey('artists.Aid'))

    def __repr__(self):
        return '{}:{}'.format(self.artist_Aid, self.Sname)

class Comments(Base):
    __tablename__ = 'comments'
    Cid = Column(Integer, primary_key=True)
    Uid = Column(Integer)
    Uname = Column(String(64))
    LikeCount = Column(Integer)
    Content = Column(String(512))
    song_Sid = Column(Integer, ForeignKey('songs.Sid'))

    def __repr__(self):
        return '{}:{}'.format(self.song_Sid, self.Cid)

engine = create_engine('mysql+pymysql://root:Zzc@1214@www.zooter.com.cn:3306/163music_new?charset=utf8mb4')
