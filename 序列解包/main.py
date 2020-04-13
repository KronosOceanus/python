# 序列解包，对多个变量同时赋值
x, y, z = 1, 2, 3
v_tuple = (False, 3.5, 'exp')
(x, y, z) = v_tuple
x, y, z = v_tuple
x, y, z = range(3)
x, y, z = map(str, range(3))

a = [1, 2, 3]
b, c, d = a
print(b + c + d)
a = {'a':1, 'b':2}
b, c = a.items()
print(b)
print(c)

# 同时遍历多个序列
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
for k, v in zip(keys, values):
    print(k, v)

for i, k in enumerate(keys):
    print('{0} is {1}'.format(i, k))

# * 解包
print(*[1, 2, 3], 4, *(5, 6))
print({'x':1, **{'y':2}})