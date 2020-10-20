import pymysql
from user import User

db = pymysql.connect('localhost', 'root', 'java521....', 'python_test')
cursor=db.cursor()      #游标对象

# 添加用户
def insertUser(user):
    sql = "insert into user(username, password, email) values('%s', '%s', '%s')" % \
          (user.username, user.password, user.email)
    try:
        if selectByUsername(user.username) == None:
            cursor.execute(sql)
            db.commit()
            return True
        else:
            return False
    except:
        db.rollback()

# 根据 username 查询
def selectByUsername(username):
    sql = 'select * from user where username = ' + username
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        if result != None:
            u = User(result[1], result[2], result[3])
            u.id = result[0]
            return u
    except:
        pass