# 还可以用来积分
# 常数
from scipy import constants as C
print(C.pi)
print(C.golden)     #黄金比例
print(C.c)      #光速
print(C.h)      #普朗克
print(C.mile)       #单位换算
print(C.inch)
print(C.degree)     #度与弧度
print(C.minute)
print(C.g)      #重力加速度

# 特殊函数
from scipy import special as S
print(S.cbrt(8))        #立方根
print(S.exp10(3))       # 10 ** 3
print(S.sindg(90))      #正弦函数，参数为角度
print(S.round(3.1))     #四舍五入
print(S.comb(5,3))      #组合数 C
print(S.perm(5,3))      #排列数 A
print(S.gamma(4))
print(S.beta(10,200))
print(S.sinc(0))

# 信号处理
import numpy as np
x=np.array([1,2,3])
h=np.array([4,5,6])
import scipy.signal
print(scipy.signal.convolve(x,h))       #一维卷积
# 二维卷积
from scipy import signal,misc
import matplotlib.pyplot as plt
image=misc.ascent()       #二维图像数组
w=np.zeros((50,50))     #全 0 二维数组
w[0][0] = 1.0       #修改参数，调整滤波器
w[49][25] = 1.0
image_new=signal.fftconvolve(image, w)      # FFT 算法卷积

# plt.figure()        #可以指定，图像名，大小，分辨，背景，边框
# plt.imshow(image_new)       #显示
# plt.gray()      #灰色
# plt.title('Filtered image')
# plt.show()

# 模糊处理
image=misc.ascent()
w=signal.gaussian(50,10.0)      #高斯滤波数组（个数，范围）
print(w)
image_new=signal.sepfir2d(image,w,w)        #高斯模糊
# plt.imshow(image_new)
# plt.show()

# 中值滤波
import random
x=np.arange(0,100,10)
random.shuffle(x)      #打乱顺序
print(x)
print(signal.medfilt(x,3))      #中值滤波

# 图像处理（N 维）
from scipy import ndimage
face=misc.face()
plt.figure()        #创建图形
# plt.imshow(face)        #绘制
# plt.show()
# blurred_face=ndimage.gaussian_filter(face,sigma=7)      # sigma 与模糊程度成正比
# plt.imshow(blurred_face)
# plt.show()
# blurred_face1=ndimage.gaussian_filter(face,sigma=1)
# blurred_face3=ndimage.gaussian_filter(face,sigma=3)     #边缘锐化
# sharp_face=blurred_face3+6*(blurred_face3-blurred_face1)
# plt.imshow(sharp_face)
# plt.show()

# 数学形态学
square=np.zeros((32,32))
square[10:20,10:20]=1
                    # 2*15 数组
x,y=(32*np.random.random((2,15))).astype(np.int)        #随机位置
square[x,y]=1
# plt.imshow(square)
# plt.show()
# open_square=ndimage.binary_erosion(square)      #开运算，先腐蚀再膨胀（闭运算反之），除去孤立小点
# plt.imshow(open_square)
# plt.show()

# 图像测量（最大值，平均值，中值，等）
print(ndimage.measurements.maximum(face))       #最大值
print(ndimage.measurements.maximum_position(face))      #位置

# 积分！！！
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