# 列表存储地址，所以能够存储不同类型的数据
l = list((3, 5, 7, 9))  #将其它数据类型转换为列表（list()等被称为工厂函数）
print(l)
print(list(range(1, 10, 2)))
l2 = list('hello world')
print(l2)
print({3, 7, 8})
print(list({'a':3, 'b':5}))
print(list({'a':3, 'b':5}.items()))
print(list())
print(l[-1])

del(l[-2])
print(l)

# 垃圾回收
import gc
gc.collect()

# 列表方法（不生成新对象）
l.append(5)
l.extend(l2)    #将 l2 添加到 l 后面
l.insert(5, 7)   #在 5 处添加 7
l.remove(7)     #删除第一次出现的 7
l.pop(3)      #删除并返回下表为 3 的元素
l.index(5)      #根据下标得到元素
l.count(5)      #统计出现次数
l.reverse()     #反转
l.copy()       #浅复制
l.sort(key=lambda item:len(str(item)), reverse=True)        #排序，传入排序依据，升序（False）降序（True）
print(l)
l.clear()       #清空
print(l)

l = l+[4]   #返回新列表
l = l * 2
print(l)

# 复杂排序
from operator import itemgetter
gameresult = [['Bob', 95, 'A'],
             ['Alan', 86, 'C'],
             ['Mandy', 89, 'E']]
print(sorted(gameresult, key=itemgetter(1)))
print(sorted(gameresult, key=itemgetter(0, 1)))   #多次排序（基数排序）
print(sorted(gameresult, key=itemgetter(1), reverse=True))
la = [1, 2, 3]
lb = ['a', 'b', 'c']
pairs = zip(la, lb)     #以 la 内容为依据对 lb 排序，对应位置元素配对
print([item[1] for item in sorted(pairs, key=lambda x:x[0], reverse=True)])     #列表推导式
print(sorted(['avc', 'c', 'ccc', 'e', 'f'], key=lambda item:(len(item), item)))     #先按照长度排序，再正常排序

# 内置函数
print(list(zip(l, [2] * 1)))    #多列表元素重新组合，zip 函数将两个参数压缩成元组
print(list(enumerate(l)))       #迭代
print(list(map(str, range(5))))     #转为字符串

def add(v):
    return v+5  #单参数函数
print(list(map(add, range(10))))     #映射函数到一个序列上
def add(x, y):
    return x+y
print(list(map(add, range(5), range(5, 10))))   #映射双参数函数到两个序列上

from functools import reduce
print(reduce(add, range(10)))   #将双参数函数累积到序列上
print(reduce(lambda x, y: x + y, range(10)))

seq = ['a', 'c', 'asda5a4!!', '!ADASD!']
def fun(x):
    return x.isalnum()  #测试是否为字母或者数字
print(list(filter(fun, seq)))
print(list(filter(lambda x:x.isalnum(), seq)))

# 向量运算
import numpy
import random
import operator
x = [random.randint(1, 10) for i in range(10)]
y = [random.randint(1, 10) for i in range(10)]
print(x)
print(y)
print(sum(map(operator.mul, x, y)))     #向量积

# 列表推导式[表达式 for 变量 in 序列或迭代对象]
# 表达式也可以是 函数
la = [x * x for x in range(10)]
print(la)
la = list(map(lambda x : x * x, range(10)))
print(la)
lb = ['aa', 'bb', 'cc']
la = [w.strip() for w in lb]
print(la)
l = [[1, 2, 3], [4, 5, 6], [6, 7, 8]]
print([num for elem in l for num in elem])  #循环嵌套

# 过滤
import os
# 列出当前目录下所有 .py 文件
print([filename for filename in os.listdir('.') if filename.endswith('.py')])
l = [i for i in range(-5, 5)]
print([i for i in l if i > 0])
score = {'libai':25, 'lisdasd':55, 'nmd':77}    #筛选成绩
print(max(score.values()))
print(min(score.values()))
print(sum(score.values())/len(score))
print([name for name, scor in score.items() if scor == 25])

import random
l = [random.randint(1, 10) for i in range(20)]
m = min(l)
print([index for index, value in enumerate(l) if value == m])   #查找下标
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])   #多序列元素任意组合

# 矩阵转置
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print([[row[i] for row in matrix] for i in range(4)])
print(list(map(list, zip(* matrix))))   #内置函数转置

# 文件迭代（先写入文件）
# fp = open('test.txt', 'a+')
# fp.close()
fp = open('test.txt', 'r')
print([line for line in fp])
fp.close()

# 生成范围内的素数
import math
print([p for p in range(2, 100) if 0 not in [p%d for d in range(2, int(math.sqrt(p)) + 1)]])

# 切片（返回列表元素的浅复制）
# 获得子集
l = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
print(l[::])    #所有元素
print(l[::-1])  #逆序
print(l[::2])   #间隔取（偶数位）
print(l[1::2])  #间隔取（奇数位）
print(l[3:6])   #指定开始和结束位置
print(l[0:100]) #尾部截断
print(l[100:])  #空列表

# 增删改
l[len(l):] = [9]  #尾部添加元素
l[:3] = [1, 2, 3]   #替换列表元素
l[:3] = []  #删除列表元素
l = list(range(10))
l[::2] = [0] * (len(l) // 2)    #替换列表元素
print(l)
l[3:3] = [4, 5]  #指定位置插入元素
del l[:3]   #删除元素
print(l)

# 浅复制
la = [3, 5, 7]
lb = la
lb[1] = 8
print(la)
print(la == lb)
print(la is lb)

la = [3, 5, 7]
lb = la[::]
print(la == lb)
print(la is lb)     #不是同一个对象,地址不同

l = list(range(10))
#   l[::2] = [3, 5]     #切片左边不连续，左右不能不等长
l[:5] = [3, 5]      #切片左边连续，可以不等长
print(l)