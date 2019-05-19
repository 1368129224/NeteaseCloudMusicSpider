from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

def getMySqlHome():
    sql = {}
    with open('mysql.home', 'r') as f:
        lines = f.readlines()
        for line in lines:
            sql[line.split('=')[0]] = line.split('=')[1].replace('\n','')
    sql['port'] = int(sql['port'])
    sql['connect_timeout'] = int(sql['connect_timeout'])
    return sql

def getMySqlTx():
    sql = {}
    with open('mysql.tx', 'r') as f:
        lines = f.readlines()
        for line in lines:
            sql[line.split('=')[0]] = line.split('=')[1].replace('\n','')
    sql['port'] = int(sql['port'])
    sql['connect_timeout'] = int(sql['connect_timeout'])
    return sql

def getMongoTx():
    with open('mongodb.tx', 'r') as f:
        return f.readline()

if __name__ == '__main__':
    Base = declarative_base()
    class Songs(Base):
        __tablename__ = 'songs'
        id = Column(Integer, primary_key=True)
        name = Column(String(128), index=True)

        def __repr__(self):
            return '{}:{}'.format(self.id, self.name)


    engine = create_engine('mysql+pymysql://root:Zzc@1214@www.zooter.com.cn:3306/163music_new?charset=utf8mb4')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    song = Songs(id=2, name='阴天')
    session.add(song)
    session.commit()
    result = session.query(Songs).all()
    print(result)
    session.close()