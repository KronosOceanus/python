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
