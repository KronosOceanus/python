from entity import User, Songlist, Song, Comment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import functools

engine=create_engine('mysql+mysqlconnector://root:java521....@localhost:3306/music_player',
                    max_overflow = 0,  # 超过连接池大小外最多创建的连接
                    pool_size = 5,  # 连接池大小
                    pool_timeout = 30,  # 池中没有线程最多等待的时间，否则报错
                    pool_recycle = -1)     # 初始化数据库连接
DBSession=sessionmaker(bind=engine)     # 创建 DBSession
session=DBSession()     # 适用多线程

# 装饰器 / AOP 编程（异常处理/抛到表层，归还连接）
def decoration(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        '''代理'''
        global result
        try:
            result = func(*args, **kwargs)      # 执行目标
        except:
            raise Exception('持久层/业务层出错了...')
        finally:
            session.commit()
            session.close()     # 交还给连接池
        return result

    return wrapper



# 添加
@decoration
def add_user(user):
    '''用户注册'''
    # 用户名是否重复
    if session.query(User).filter(User.username==user.username).first()==None:
        session.add(user)
    else:       # 重复
        return False

@decoration
def add_songlist(user_id, songlist):
    '''用户添加歌单'''
    # 该用户是否已有该歌单
    if session.query(Songlist).filter(Songlist.user_idfk==user_id).first()==None:
        songlist.user_idfk=user_id
        session.add(songlist)
    else:
        return False

@decoration
def add_comment(song_id, comment):
    '''歌曲添加评论'''
    comment.song_idfk=song_id
    session.add(comment)

@decoration
def add_up_song(user_id, song):
    '''用户上传歌曲'''
    if session.query(Song).filter(song.user_idfk==user_id).first()==None:
        song.user_idfk=user_id
        session.add(song)
    else:
        return False

@decoration
def add_song(songlist_id, song):
    '''歌单添加歌曲'''
    songlist=session.query(Songlist).filter(Songlist.id==songlist_id).first()
    if song not in songlist.songs:
        songlist.songs.append(song)     # 一对多添加关系
        session.add(songlist)
    else:
        return False

@decoration
def add_friends(one_id, another_id):
    '''添加好友'''
    one=session.query(User).filter(User.id==one_id).first()
    another=session.query(User).filter(User.id==another_id).first()
    if one not in another.friends or another not in one.friends:
        one.friends.append(another)     # 多对多添加
        session.add(one)
    else:
        return False


# 删除
@decoration
def delete_songlist(songlist_id):
    '''用户删除歌单'''
    songlist=session.query(Songlist).filter(Songlist.id==songlist_id).first()
    session.delete(songlist)





# 测试
# add_user(User(username='704690152',password='qwertyuiop',name='cs',signature='shift'))
# add_user(User(username='704690152',password='qwertyuiop',name='cs',signature='shift'))
# add_songlist(17,Songlist(name='钢琴'))
# add_song(3,session.query(Song).filter(Song.id==1).first())
# add_comment(2,Comment(comment='评论！！！！'))
# add_up_song(17,session.query(Song).filter(Song.id==1).first())
# add_friends(1,17)
# delete_songlist(3)