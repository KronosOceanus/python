# 元组是不可更改的，调用函数时可使用元组传参
x = (3,)
x = tuple(range(5))
print(x)
x = ([3, 5], 2)
x[0][0] = 7
x[0].append(8)
print(x)

# 生成器推导式，生成器对象遍历完之后就没了
g = (i for i in range(10))
x = tuple(g)
print(x)
print(list(g))
g = (i for i in range(3))
print(g.__next__())     #遍历
print(g.__next__())
print(g.__next__())

# 生成斐波那契数列
def f():    #创建可迭代的生成器对象
    a, b = 1, 1     #初始值
    while True:
        yield a
        a, b = b, a+b

a = f()     #创建
for i in range(10):
    print(a.__next__(), end=' ')

print()
for i in f():   #第一个 > 100 的数
    if i>100:
        print(i, end=' ')
        break
