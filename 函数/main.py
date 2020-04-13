# 定义和调用时必须有括号
def Join(chList, seq='*'):  #默认值参数（必须在参数列表最右端）
    return seq.join(chList)
chL = ['a', 'c', 'f']
print(Join(chL))

a = 5
b = 2
a, b = b, a     #交换两个数
print(a)
print(b)

if True : print(1, end=' ');print(2)

# 查看日历
from datetime import date
daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def myCalendar(year, month):
    # 将 date（年月日）转化为星期几
    start = date(year, month, 1).timetuple().tm_wday
    # 日历头部位置
    print('{0}年{1}月日历'.format(year, month).center(28))
    print('\t'.join('日 一 二 三 四 五 六'.split()))
    # 获得该月有多少天
    day = daysOfMonth[month - 1]
    if month == 2:
        if year%400 == 0 or (year%4 == 0 and year%100 != 0):
            day += 1
    result = [' ' * 4 for i in range(start + 1)]    #输出第一行空白
    result += list(map(lambda d:str(d).ljust(4), range(1, day + 1)))    # range 是开区间
    for i, day in enumerate(result):
        if i != 0 and i%7 == 0:
            print()
        print(day, end='')
    print()

myCalendar(2020, 2)


import itertools
print(list(itertools.combinations([7, 8, 2], 2)))   #排列组合
x = 'Private Key'
y = itertools.cycle(x)      #迭代圈
for i in range(20):
    print(next(y), end=',')
print()
for i in range(5):
    print(next(y), end=',')
print()
x = range(1, 20)
y = (1, 0) * 9 + (1,)
print(y)
print(list(itertools.compress(x, y)))   #根据 y 过滤 x 序列值（为 0 则过滤掉）

def group(v):
    if v > 10:
        return 'greater than 10'
    elif v < 5:
        return 'less than 5'
    else:
        return 'between 5 and 10'
x = range(20)
y = itertools.groupby(x, group)     #根据函数返回值（作为 key）将 x 分组
for k, v in y:
    print(k, ':', list(v))

# 函数嵌套
def linear(a, b):
    def result(x):
        return a * x + b
    return result

print(linear(0.3, 2)(3))

# 判断文件输入者的信息（参数为另一个函数 / 可以做装饰器）
def check_permission(func):
    # */** 可变数量参数，存放在元组/字典中
    def warpper(* args, ** kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception('Sorry. You are not allowed.')
        return func(* args, ** kwargs)  #返回另一个函数，检验成功，可执行
    return warpper

class ReadWriteFile(object):
    # 函数作为装饰器
    @check_permission
    def read(self, username, filename):
        return open(filename, 'r').read()

    def write(self, username, filename, content):
        open(filename, 'a+').write(content)
    # 与装饰器功能一样
    write = check_permission(write)

# 创建类对象
t = ReadWriteFile()
t.write(username = 'admin', filename=r'sample.txt', content='hello world')
print('After calling to write……')
print(t.read(username = 'admin', filename=r'sample.txt'))

# 全局变量
def g():
    global x
    x = 5
g()
print(x)

import globalV
print(globalV.global_variable)

# lambda
g = lambda x, y=2:x + y
print(g(1))
l = [(lambda x:x ** 2), (lambda x:x ** 3)]
print(l[0](1), l[1](2))
l = [7, 8, 2, 3, 0, 5, 4, 6, 8]
l.sort(key=lambda x : x)
print(l)
l = enumerate(l)    #每个迭代对象是（下标，值）的形式
print(l.__next__())
print(l.__next__())
print(l.__next__())