# 相当于 HashMap
# 各种函数默认作用于键
# 无序
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
m = dict(zip(keys, values))
print(m)
n = dict.fromkeys(['name', 'age', 'sex'])   #值为 None
n['name'] = 'cs'
print(n)

# 添加/删除
m.update(n)
print(m)
del m['age']
print(m)
# del m
# 弹出并删除
print(m.popitem())
print(m.pop('a'))

# 访问
print(m.get('age'))
print(m.setdefault('age', 18))  #设置默认值
print(list([item for item in m]))   #键
print(list([item for item in m.items()]))   #键值对
print(m.keys())
print(m.values())

# 统计
import string
import random
x = string.ascii_letters + string.digits + string.punctuation   #生成所有字符
print(x)
y = [random.choice(x) for i in range(1000)]     #1000个随机数的列表
z = ''.join(y)      #列表字符连接成字符串
d = dict()      #空字典
for ch in z:    #遍历字符串，修改每个字符的频次
    d[ch] = d.get(ch, 0) + 1
print(d.items())
# 其他实现方法（计数器类）
from collections import Counter
frequences = Counter(z)
print(frequences.items())   #直接统计
print(frequences.most_common(1))    #出现次数最多的一个字符
print(frequences.most_common(3))    #前三个

# 当前作用域内所有全局变量和局部变量的字典
a = (1, 2, 3, 4, 5)
b = 'hello world.'
def demo():
    a = 3
    b = [1, 2, 3]
    print('local:', locals())
    print('globals:', globals())
demo()

# 有序字典（插入顺序）
import collections
x = collections.OrderedDict()
x['a'] = 3
x['b'] = 9
print(x)
print(sorted(x.items(), key=lambda item:item[0], reverse=True))

# 字典推导式
print({i:str(i) for i in range(5)})