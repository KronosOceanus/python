import pymysql
db = pymysql.connect('localhost', 'root', 'java521....', 'python_test')
cursor=db.cursor()      #游标对象
cursor.execute('select version()')      #查询
data=cursor.fetchone()      #得到一条结果
print(data)

cursor.execute('drop table if exists employee')
sql='''create table employee(
        first_name char(20) not null,
        last_name char(20),
        age int,
        sex char(1),
        income float)'''
cursor.execute(sql)

