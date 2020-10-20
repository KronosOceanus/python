from entity import User
from dao.base import session, decoration

# 查询
@decoration
def find_all_user():
    return session.query(User).all()
@decoration
def find_user_by_id(id):
    return session.query(User).filter(User.id==id).first()
@decoration
def find_user_by_username(username):
    return session.query(User).filter(User.username==username).first()
@decoration
def find_user_by_name(name):
    return session.query(User).filter(User.name==name).first()


@decoration
def add_user(user):
    '''用户注册'''
    # 用户名是否重复
    if session.query(User).filter(User.username==user.username).first()==None:
        session.add(user)
        return True
    else:       # 重复
        return False

@decoration
def update_user(user):
    '''修改信息（未修改会传入默认值）'''
    target=session.query(User).filter(User.id==user.id).first()
    # 修改
    target.password=user.password
    target.name=user.name
    target.signature=user.signature


# update_user(User(id=48,username='704690152', password='qwertyuiop', name='cs', signature='kkk'))