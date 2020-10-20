# 操作 mysql
import pymysql
db = pymysql.connect('localhost', 'root', 'java521....', 'python_test')
cursor=db.cursor()      #游标对象
cursor.execute('select version()')      #查询
data=cursor.fetchone()      #得到一条结果
print(data)

# 建表
# cursor.execute('drop table if exists employee')
# sql='''create table employee(
#         first_name char(20) not null,
#         last_name char(20),
#         age int,
#         sex char(1),
#         income float)'''
# cursor.execute(sql)

# 插入
sql="""insert into employee(first_name,
        last_name,age,sex,income)
        values('Mac','Monhan',20,'M',2.2)"""
sql="insert into employee(first_name,\
        last_name,age,sex,income)\
        values('%s','%s','%s','%s','%s')" % \
    ('Mac','Mohan',20,'M',2.2)      #另一种写法（% \ 后面是变量）
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

# 查询
sql="select * from employee \
    where income > %s" % (1)
try:
    cursor.execute(sql)
    result=cursor.fetchall()    #全部结果行
    for row in result:
        for i in range(4):
            print(row[i], end='\t')
        print()
except:
    pass

# 更新
sql="update employee set age = age + 1 where sex = '%c'" % ('M')
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

# 删除
sql="delete from employee where age > %s" % (20)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()


# 操作 mongodb
import pymongo
client=pymongo.MongoClient('localhost',27017)       # 默认端口

db=client.students        # 获取数据库
print(db.list_collection_names())       # 数据集合名称列表
st=db.students      # 获取数据集合
for item in st.find():      # 查询
    print(item)

# 插入
lisi={'name':'lisi','age':22,'sex':'female'}
wangwu={'name':'Wangwu','age':20,'sex':'male'}
st.insert_many([lisi,wangwu])

# 条件查询
for item in st.find({'name':'Wangwu'}):
    print(item)

for item in st.find().sort('name',pymongo.ASCENDING):
    print(item)
print(st.find_one())
print(st.find_one({'name':'Zhangsan'}))

# 修改
st.create_index([('name',pymongo.ASCENDING)])       # 创建索引
st.update_one({'name':'Zhangsan'},{'$set':{'age':25}})

# 清空
st.delete_many({'age':20})