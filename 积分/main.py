from scipy import integrate
import numpy as np

# 函数积分
def f(x):
    return x + 1
v, err = integrate.quad(f, 1, 2)        #定积分
print(v)

def k(x, a, b):
    return a * x + b
v, err = integrate.quad(k, 1, 2, args=(-1, 1))
print(v)

def m(x):
    return 1 / np.sqrt(abs(x))
v, err = integrate.quad(m, -1, 1, points=[0])       #断点积分
print(v)

# 绘制函数曲线
'''
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8, 3))
x = np.linspace(-1, 1, 10000)
ax.plot(x, m(x), lw=2)
ax.fill_between(x, m(x), color='green', alpha=0.5)
ax.set_xlabel('$x$', fontsize=18)
ax.set_ylabel('$m(x)$', fontsize=18)
ax.set_ylim(0, 25)
plt.show()
'''

# 点集积分
def f(x):
    return np.sqrt(x)
x = np.linspace(0, 2, 10)       #样本数据
y = f(x)
v = integrate.trapz(y, x)
print(v)

# 双重积分
def f(x, y):
    return x * y
def h(x):
    return x              #外层上下限      内层上下限
v, err = integrate.dblquad(f, 1, 2, lambda x:1, h)
print(v)

# 三重积分
f = lambda x, y, z : x
g = lambda x : 0
h = lambda x : (1 - x) / 2
q = lambda x, y : 0
r = lambda x, y : 1 - x - 2 * y
v, err = integrate.tplquad(f, 0, 1, g, h, q, r)     #参数由内向外的上下限
print(v)