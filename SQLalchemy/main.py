from sqlalchemy import Column, String, Integer, \
    create_engine, ForeignKey,Table
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()     # 创建对象基类

# 好友中间表
friends_table=Table('friends_table',Base.metadata,
    Column('one_idfk',Integer,ForeignKey('user_table.id')),
    Column('another_idfk',Integer,ForeignKey('user_table.id')))

class User(Base):
    __tablename__='user_table'      # 表名

    # 表结构
    id=Column(Integer, primary_key=True, autoincrement=True)
    username=Column(String(11))
    password=Column(String(11))
    name=Column(String(11))
    signature=Column(String(100))
    # 一对多，歌单            类名
    songlist=relationship('Songlist')
    # 一对多，上传歌曲
    upsonglist=relationship('Song')
    # 多对多，好友
    friends=relationship('User',secondary=friends_table,
                         primaryjoin=(friends_table.c.one_idfk==id),    # 根据左边查询右边
                         secondaryjoin=(friends_table.c.another_idfk==id),
                         backref=backref('friends_table',lazy='dynamic'),       # lazy 表示延迟加载（用到才加载）
                         lazy='dynamic')

# 歌单收藏歌曲，多对多中间表
collect_table=Table('collect_table',Base.metadata,
    Column('songlist_idfk',Integer,ForeignKey('songlist_table.id')),
    Column('song_idfk',Integer,ForeignKey('song_table.id')))

class Songlist(Base):
    __tablename__='songlist_table'

    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(11))
    # 外键                                表名.字段名
    user_idfk=Column(Integer,ForeignKey('user_table.id'))
    # 单向多对多        类名      该参数连接中间表
    song=relationship('Song',secondary=collect_table)

class Song(Base):
    __tablename__='song_table'

    id=Column(Integer, primary_key=True, autoincrement=True)
    song_name=Column(String(20))
    singer=Column(String(11))
    lyrics=Column(String(500))
    # 用户外键（标明由哪个用户上传）
    user_idfk = Column(Integer, ForeignKey('user_table.id'))


# 初始化数据库连接
engine=create_engine('mysql+mysqlconnector://root:java521....@localhost:3306/music_player')
# 创建 DBSession
DBSession=sessionmaker(bind=engine)
# 创建对象
session=DBSession()
# 插入
# new_user=User(username='704690152',password='qwertyuiop',name='cs',signature='shift')
# new_songlist=Songlist(name='我喜欢的歌曲',user_idfk=1)
# new_song=Song(song_name='歌曲',singer='歌手',
#               lyrics='纯音乐请欣赏',user_idfk=1)
user1=User(username='782305468',password='asdfghjkl',name='ky',signature='sign')
user1.friends=[session.query(User).filter(User.name=='cs').first()]     # 与已存在的人创建关系

# session.add(new_user)
# session.add(new_song)
# session.add(new_songlist)
session.add(user1)

# 查询
user=session.query(User).get(1)
print(user.id, user.username)
for item in user.songlist:
    print(item.name)






session.commit()
session.close()