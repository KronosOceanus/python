import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def get_random_points(N):
    np.random.seed(42)
    random_points = np.random.rand(N, 2)        #随机产生 N 个点
    return random_points

# 计算pi的值，并将圆内外的点分开，方便做图
def cal_pi(random_points):
    inCircle_points = []  # 圆内部点
    outCircle_points = []  # 外部点（以及边上的点）

    for point in random_points:
        x = point[0]
        y = point[1]
        if (x - 0.5) ** 2 + (y - 0.5) ** 2 < 0.25:      #距离区分
            inCircle_points.append([x, y])
        else:
            outCircle_points.append([x, y])

    ratio = len(inCircle_points) / len(random_points)
    pi = 4 * ratio

    return pi, inCircle_points, outCircle_points

def plot_data(random_points):
    '''绘图'''
    pi_estimation, inCircle_points, outCircle_points = cal_pi(random_points)
    print('估计的pi值为:', pi_estimation)

    fig1 = plt.figure()     #画布
    # 绘制圆的轮廓      1x1网格，第一子图
    ax1 = fig1.add_subplot(111, aspect='equal')     #子画布
    ax1.add_patch(      #中心坐标         中心填充
        patches.Circle((0.5, 0.5), 0.5, fill=False, lw=2))      #添加形状

    # 绘制圆内外的点                    横坐标                           纵坐标
    ax1.plot(np.array(inCircle_points)[:, 0], np.array(inCircle_points)[:, 1],
             #颜色    透明度      标准尺寸
             'go', alpha=0.3, markersize=0.5)
    ax1.plot(np.array(outCircle_points)[:, 0], np.array(outCircle_points)[:, 1], 'ro', alpha=0.3, markersize=0.5)

    #          x      y
    plt.axis([0, 1, 0, 1])  # 座标轴范围约束
    plt.title('$\pi\\approx' + str(pi_estimation) + '$')        #标题
    plt.show()

if __name__ == '__main__':
    N = 30000
    random_points = get_random_points(N)
    plot_data(random_points)