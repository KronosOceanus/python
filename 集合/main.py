# 相当于 HashSet
# 字典和集合都是用 hash 表存储元素，方便查找
# 只能包含不可变类型（可以计算 hash 的类型）（如：数字，字符串，元组）
a = {3, 5}
a = set(range(4, 18))
print(a)
a = set([1, 1, 1, 4])
print(a)
print(hash(5))

# 查找时间
import random
import time
x = list(range(10000))
y = set(range(10000))
z = dict(zip(range(10000), range(10000)))
r = random.randint(0, 9999)
start = time.time()
for i in range(9999):
    r in x
print('list, time used:', time.time() - start)
start = time.time()
for i in range(9999):
    r in y
print('set, time used:', time.time() - start)
start = time.time()
for i in range(9999):
    r in z
print('dict, time used:', time.time() - start)

# 操作
a.add(2)
print(a)
a.update({1, 6, 2, 1})
print(a)
print(a.pop())  #随机返回并删除
# a.remove(2)   #删除，不存在抛出异常
a.discard(5)    #删除，不存在忽略
a = {3, 7, 8}
b = {4, 5, 2}
print(a | b)    #并集
print(a.union(b))
print(a & b)    #交集
print(a.intersection(b))
print(a - b)  #差集
print(a.difference(b))
print(a ^ b)    #对称差集
print(a.symmetric_difference(b))
print(a < b)    #测试是否为子集
print(a.issubset(b))

# 枚举
from enum import Enum
class Color(Enum):   #创建枚举类
    red = 1
    blue = 2
    green = 3
print(Color.red)
print(list(Color))

# 提取序列中单一元素
import random
listRandom = [random.choice(range(100)) for i in range(100)]  #choice 返回列表中随机项
noRepeat = []
for i in listRandom:
    if i not in noRepeat:
        noRepeat.append(i)
print(len(listRandom))
print(len(noRepeat))
# 使用集合之后
newSet = set(listRandom)
print(len(newSet))

# 获取不重复序列
import random
import time
def RandomNumbers1(number, start, end):
    data = []
    while True:
        element = random.randint(start, end)
        if element not in data:
            data.append(element)
        if len(data) == number:
            return data

def RandomNumbers2(number, start, end):
    data = set()
    while True:
        element = random.randint(start, end)
        if element not in data:
            data.add(element)
        if len(data) == number:
            return data

start = time.time()
for i in range(10000):
    d1 = RandomNumbers1(50, 1, 1000)
print('Time used:', time.time() - start)

start = time.time()
for i in range(10000):
    d1 = RandomNumbers2(50, 1, 1000)
print('Time used:', time.time() - start)

print(random.sample(range(1000), 20))

# 集合推导式
print({x.strip() for x in (' he ', 'she   ', '   I')})
x = {random.randint(1, 500) for i in range(100)}
print(len(x))
print({str(x) for x in range(10)})