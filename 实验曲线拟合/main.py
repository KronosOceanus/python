import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
from scipy.optimize import curve_fit        # 曲线拟合


# 自定义函数 e指数形式
def func(x, a, b):
    return a * x + b

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False

# 定义x、y散点坐标
x = [24.8,23.8,21.6,19.5,18.1,16.5]
x = np.array(x)
y = [1.46,1.63,1.70,1.73,1.76,1.79]
y = np.array(y)

# 非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)
# 获取popt里面是拟合系数
print(popt)
a = popt[0]
b = popt[1]
yvals = func(x, a, b)  # 拟合y值
print('popt:', popt)
print('系数a:', a)
print('系数b:', b)
print('系数pcov:', pcov)
print('系数yvals:', yvals)
# 绘图
plot1 = plt.plot(x, y, 's', label='original values')
plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
plt.xlabel('U/V')
plt.ylabel('I/mA')
plt.legend(loc=4)  # 指定legend的位置右下角
plt.title('Is=25mA U0=1.96V\n伏安特性曲线，其中斜率为 %s'%a)
plt.show()
