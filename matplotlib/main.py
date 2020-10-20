import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm        # 中文
import matplotlib as mpl        # 3d 绘画
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d
from matplotlib.path import Path        # 自定义绘图
from matplotlib.patches import PathPatch
import sys
import tkinter as Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

# # 正弦曲线
# t=np.arange(0.0,2.0*np.pi,0.01)     #坐标起止，间隔
# s=np.sin(t)
# pl.plot(t,s)
# pl.xlabel('x')
# pl.ylabel('y')
# pl.title('sin')
# # pl.show()
#
# # 散点图
# a=np.arange(0,2.0*np.pi,0.1)
# b=np.cos(a)
# pl.scatter(a,b)     #散点图
# pl.show()
# x=np.random.random(100)
# y=np.random.random(100)
# #             大小     颜色     符号形状
# pl.scatter(x,y,s=x*500,c=u'r',marker=u'*')
# pl.show()
#
# # 饼状图
# labels='Frogs','Hogs','Dogs','Logs'
# colors=['yellowgreen','gold','#FF0000','lightcoral']
# explode=(0,0.1,0,0.1)       # 第 2，4 个切片裂开
#
# fig=plt.figure()
# ax=fig.gca()        #饼状图
# ax.pie(np.random.random(4),explode=explode,labels=labels,
#        colors=colors,autopct='%1.1f%%',shadow=True,
#        startangle=90,radius=0.25,
#        center=(0,0),frame=True)
# ax.pie(np.random.random(4),explode=explode,labels=labels,
#        colors=colors,autopct='%1.1f%%',shadow=True,
#        startangle=90,radius=0.25,
#        center=(1,1),frame=True)
# ax.pie(np.random.random(4),explode=explode,labels=labels,
#        colors=colors,autopct='%1.1f%%',shadow=True,
#        startangle=90,radius=0.25,
#        center=(0,1),frame=True)
# ax.pie(np.random.random(4),explode=explode,labels=labels,
#        colors=colors,autopct='%1.1f%%',shadow=True,
#        startangle=90,radius=0.25,
#        center=(1,0),frame=True)
# ax.set_xticks([0,1])
# ax.set_yticks([0,1])
# ax.set_xticklabels(['Sunny','Cloudy'])
# ax.set_yticklabels(['Dry','Rainy'])
# ax.set_xlim((-0.5,1.5))
# ax.set_ylim((-0.5,1.5))
# ax.set_aspect('equal')
# plt.show()
#
# # 中文标签和图例                   字体
# myfont=fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf')
# t=np.arange(0.0,2.0*np.pi,0.01)
# s=np.sin(t)
# z=np.cos(t)
# pl.plot(t,s,label='正弦')     #图例标签
# pl.plot(t,z,label='余弦')
# pl.xlabel('x-变量',fontproperties='STKAITI',fontsize=20)
# pl.ylabel('y-值',fontproperties='STKAITI',fontsize=20)
# pl.title('sin-cos函数',fontproperties='STKAITI',fontsize=24)
# pl.legend(prop=myfont)      #图例
# pl.show()
#
# # 带公式的图
# x=np.linspace(0,2*np.pi,500)
# y=np.sin(x)
# z=np.cos(x*x)
# plt.figure(figsize=(8,5))
# #           $ $ 引入 LaTex 公式             2 个像素宽
# plt.plot(x,y,label='$sin(x)$',color='red',linewidth=2)
# plt.plot(x,z,'b--',label='$cos(x^2)$')
# plt.xlabel('Time(s)')
# plt.ylabel('Volt')
# plt.title('Sin and Cos figure using pyplot')
# plt.ylim(-1.2,1.2)
# plt.legend()
# plt.show()
#
# # 多个图形单独显示
# x=np.linspace(0,2*np.pi,500)
# y1=np.sin(x)
# y2=np.cos(x)
# y3=np.sin(x*x)
# plt.figure(1)
# ax1=plt.subplot(2,2,1)      #画布分割成 2 行 2 列，第一块图
# ax2=plt.subplot(2,2,2)
# ax3=plt.subplot(2,1,2)
# plt.sca(ax1)        #选中
# plt.plot(x,y1,color='red')
# plt.ylim(-1.2,1.2)      # y 坐标范围
# plt.sca(ax2)
# plt.plot(x,y2,'b--')        # -- 表示虚线
# plt.ylim(-1.2,1.2)
# plt.sca(ax3)
# plt.plot(x,y3,'g--')
# plt.ylim(-1.2,1.2)
# plt.show()
#
# # 三维参数曲线
# mpl.rcParams['legend.fontsize']=10      #图例字号
# fig=plt.figure()
# ax=fig.gca(projection='3d')     #三维图形
# theta=np.linspace(-4*np.pi,4*np.pi,100)
# z=np.linspace(-4,4,100)*0.3     #测试数据
# r=z**3+1
# x=r*np.sin(theta)
# y=r*np.cos(theta)
# ax.plot(x,y,z,label='parametric curve')
# ax.legend()
# plt.show()
#
# # 三维图形
# x,y=np.mgrid[-2:2:20j, -2:2:20j]        #多维结构【维数（取值：范围：个数）】
# print(x)
# z=50*np.sin(x+y)
# ax=plt.subplot(111,projection='3d')
# ax.plot_surface(x,y,z,rstride=2,cstride=1,
#                 cmap=plt.cm.Blues_r)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()
#
# # 自定义图形
# fig,ax=plt.subplots()       # 多个子画布
# path_data=[
#     (Path.MOVETO,(1.54,-2.11)),
#     (Path.CURVE4,(0.35,-1.1)),      # 4 个控制点，3 次贝塞尔曲线
#     (Path.CURVE3,(0.55,0.77)),      # 3 ... 2 ...
#     (Path.LINETO,(0.85,1.15)),      #当前位置画直线
#     (Path.CLOSEPOLY,(1.54,-2.11)),      #当前位置画直线并闭合
# ]
# codes,verts=zip(* path_data)        # * 表示元组解压
# path=Path(verts, codes)
# patch=PathPatch(path,facecolor='r',alpha=0.9)       #按指令和坐标绘图
# ax.add_patch(patch)     #形状，添加到画布
# x,y=zip(* path.vertices)        #绘制控制多边形和连接点
# line,=ax.plot(x,y,'go-')
# ax.grid()       #显示网络
# ax.axis('equal')        #坐标轴刻度大小一致
# plt.show()

# tkinter 中使用
mpl.use('TkAgg')
root=Tk.Tk()
root.title('matplotlib in TK')      #窗体
f=Figure(figsize=(5,4),dpi=100)     #设置图形尺寸与质量
a=f.add_subplot(111)        #添加子画布
t=np.arange(0.0,3,0.01)
s=np.sin(2*np.pi*t)
a.plot(t,s)

canvas=FigureCanvasTkAgg(f,master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=Tk.TOP,fill=Tk.BOTH,expand=1)
