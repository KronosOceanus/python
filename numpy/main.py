import numpy as np

# 数组
print(np.array((1,2,3,4,5)))        #可迭代对象转数组
print(np.linspace(0,10,11))       #等差数组（起始，结束，等分数）
print(np.linspace(0,10,11))
print(np.logspace(0,100,10))       #对数数组
print(np.zeros((3,3)))      # 0 矩阵
print(np.ones((3,3)))       # 1 矩阵
print(np.identity(3))       #单位矩阵
print(np.empty((3,3)))      #空数组（元素值不确定）
print('==================')

# 数组与数值
x=np.array(range(1,6))
print(x*2)
print(x/2)
print(x//2)
print(x+2)
print(x%3)
print(x**3)
print('==================')

# 数组与数组
a=np.array((1,2,3))
b=np.array(([1,2,3],[4,5,6],[7,8,9]))
c=a*b       #乘每一列元素
print(c)
print(c/b)
print(c/a)
print(a+a)
print(a*a)
print(a-a)
print(a/a)

# 矩阵转置
b=np.array(([1,2,3],[4,5,6],[7,8,9]))
print(b.T)

# 向量内积
a=np.array((5,6,7))
b=np.array((6,6,6))
print(a.dot(b), np.dot(a,b))
c=np.array(([1,2,3],[4,5,6],[7,8,9]))
print(c.dot(a))     #与 c 的每一行计算内积
print(a.dot(c))     #列

# 访问
x=np.arange(0,100,10,dtype=np.floating)     #等差数组
index=np.random.randint(0,len(x), 5)        # 5个随机整数作为下标
print(x[index])     #同时访问多个元素

# 数组函数运算
x=np.arange(0,100,10,dtype=np.floating)
print(np.sin(x))
b=np.array(([1,2,3],[4,5,6],[7,8,9]))
print(np.cos(b))
print(np.round(b))
x=np.random.rand(10)
x*=10
print(x)
print(np.floor(x))      #上下取整
print(np.ceil(x))
print(np.sum(x))
print(np.sum(x, axis=0))        #纵向求和
print(np.sum(b, axis=1))        #横向
print(np.mean(x, axis=0))       #平均值
import random
weight=[random.random() for i in range(10)]
print(weight)
print(np.average(x, axis=0, weights=weight))        #加权
print(np.max(x))
print(np.max(b,axis=1))
print(np.std(b))        #标准差（也有行列参数）
print(np.sort(b,axis=0))

# 改变数组大小
a=np.arange(1,11,1)
print(a)
a.shape=2,5
print(a)
a.shape=5,-1        # -1 自适应
print(a)
b=a.reshape(2,5)
print(b)

# 切片
a=np.arange(10)
print(a)
print(a[::-1])      #倒序
print(a[::2])
print(a[:5])        #前 5
c=np.arange(25)     #创建数组
print(c)
c.shape=5,5
print(c[0,2:5])
print(c[2:5,2:5])       #子矩阵

# 布尔运算
x=np.random.rand(10)
print(x)
print(x>0.5)
print(x[x>0.5])     #过滤
a=np.array([1,2,3])
b=np.array([3,2,1])
print(a>b)
print(a[a==b])

# 广播
a=np.arange(0,60,10).reshape(-1,1)      #列向量
b=np.arange(0,6)
print(a)
print(b)
print(a+b)      #广播
print(a*b)

# 分段函数
x=np.random.randint(0,10,size=(1,10))
print(x)
print(np.where(x<5,0,1))        # <5 元素对应 0，其他对应 1
print(np.piecewise(x,[x<4,x>7],[lambda x:x*2,lambda x:x*3]))        #映射

# 计算唯一值并计数
x=np.random.randint(0,10,7)
print(x)
print(np.bincount(x))       #出现次数（0 表示出现 1 次）
print(np.unique(x))     #返回唯一元素值
x=np.random.randint(0,10,2)

# 矩阵运算
a=[3,5,7]
a_mat=np.matrix(a)
print(a_mat)
print(a_mat.T)
print(a_mat.size)
b=[1,2,3]
b_mat=np.matrix(b)
c=a_mat.T * b_mat
print(c)
print(c.diagonal())     #对角线元素
print(c.flatten())      #平铺