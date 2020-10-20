import random
import math
import matplotlib.pyplot as plt

input = int(input('输入生成点的数量：'))
dot = [[0] * 2 for i in range(input)]       # 初始化点数组【坐标，最近距离】
mindis = 1000 * 1000        # 记录最短距离
fg = plt.figure()     # 画布
cn = fg.add_subplot(1, 1, 1)        # 子画布
cn.set_xlim(0, 1000)        # 设置尺寸
cn.set_ylim(0, 1000)
plt.ion()       # 交互模式，动态画图
a = [1000, 1000]        # a，b 为最近点对
b = [0, 0]
x = []
y = []
for i in range(input):
    dot[i][0] = random.randrange(1000)      # 随机坐标
    dot[i][1] = random.randrange(1000)
dot.sort()
for i in range(input):
    x.append(dot[i][0])
    y.append(dot[i][1])


def distance(x, y):
    return float(math.sqrt(x * x + y * y))


def dac(left, right):
    global mindis, a, b
    len = right - left
    length = (right + left)
    cn.scatter(x, y, color='b', marker='.')     # 画出所有点
    if len <= 0:
        dis = 9999999999999
        return dis
    elif len == 1:      # 两个点
        dis = distance(dot[right][0] - dot[left][0], dot[right][1] - dot[left][1])
        cn.plot([dot[left][0], dot[right][0]], [dot[left][1], dot[right][1]], color='r')
        plt.pause(0.1)
        cn.lines.pop()
        plt.pause(0.1)
        if dis < distance(a[0] - b[0], a[1] - b[1]):
            a = [dot[right][0], dot[right][1]]
            b = [dot[left][0], dot[left][1]]
        return dis      # 递归终点的最短距离
    else:
        n = int(length / 2)     # 中间点
        midline = (dot[n][0] + dot[n + 1][0]) / 2
        cn.plot([midline, midline], [0, 1000], color='b')       # 绘制中线
        plt.pause(0.1)
        dis1 = dac(left, n)     # 递归求解
        dis2 = dac(n + 1, right)
    if dis1 <= dis2:        # 分治后左右的 dist
        md = dis1
    else:
        md = dis2
    if mindis > md:     # 得到最小距离
        mindis = md
    for i in dot[left:n + 1]:       # 绘图处理中线左右的点
        if abs(i[0] - midline) <= md:
            for j in dot[n + 1:right + 1]:
                if j[0] - midline <= md:
                    if i[1] - md <= j[1] <= i[1] + md:        # 三个 if 选定矩形区域内的点
                        dis3 = distance(i[0] - j[0], i[1] - j[1])
                        if mindis > dis3:
                            mindis = dis3       # 得到最短距离
                        cn.plot([i[0], j[0]], [i[1], j[1]], color='r')
                        plt.pause(0.1)
                        cn.lines.pop()
                        plt.pause(0.1)
                        if dis3 < distance(a[0] - b[0], a[1] - b[1]):       # 比递归过程中已经找到的最短距离短
                            a = [i[0], i[1]]
                            b = [j[0], j[1]]
    cn.lines.pop()
    return mindis


list = []
c = [1000, 1000]
d = [0, 0]
for i in range(input):      # 暴力检验
    for j in range(i + 1, input):
        list.append(distance(dot[i][0] - dot[j][0], dot[i][1] - dot[j][1]))
        if distance(dot[i][0] - dot[j][0], dot[i][1] - dot[j][1]) < distance(c[0] - d[0], c[1] - d[1]):
            c = [dot[i][0], dot[i][1]]
            d = [dot[j][0], dot[j][1]]
list.sort()
print("检验：", list[0], c, d)
print("距离：", dac(0, input - 1))
print("最近对：", a, b)
cn.plot([a[0], b[0]], [a[1], b[1]], c='g')      # 画出最近点对连线
plt.pause(5)