import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import colorchooser
from PIL import Image

app=tk.Tk()
app.title('title')
app['width']=800
app['height']=600

# 控制是否允许画图的变量
yesno=tk.IntVar(value=0)
# 控制画图类型变量，曲线直线矩形文本橡皮
what=tk.IntVar(value=1)
# 记录鼠标位置
x=tk.IntVar(value=0)
y=tk.IntVar(value=0)
# 前景色
foreColor='#000000'
backColor='#FFFFFF'
# 创建画布
image=tk.PhotoImage()
canvas=tk.Canvas(app, bg='white',width=800,height=600)
canvas.create_image(800,600,image=image)
# 单击允许画图
def onLeftButtonDown(event):
    yesno.set(1)
    x.set(event.x)
    y.set(event.y)
    if what.get()==4:                  #全局变量 用户输入
        canvas.create_text(event.x,event.y,text=text)
canvas.bind('<Button-1>',onLeftButtonDown)      # 画布与案件绑定

# 记录最后绘制图形的 id
lastDraw=0
# 按住左键移动画图
def onLeftButtonMove(event):
    if yesno.get()==0:
        return
    if what.get()==1:       # 曲线
        # 两点之间画直线
        canvas.create_line(x.get(),y.get(),
                           event.x,event.y,fill=foreColor)
        x.set(event.x)      # 更新坐标
        y.set(event.y)
    elif what.get()==2:     # 先删除刚才的直线，再重新画一条
        global lastDraw
        try:
            canvas.delete(lastDraw)
        except:
            pass
        lastDraw=canvas.create_line(x.get(),y.get(),
                           event.x,event.y,fill=foreColor)
    elif what.get()==3:     # 矩形
        try:
            canvas.delete(lastDraw)
        except:
            pass
        lastDraw=canvas.create_rectangle(x.get(),y.get(),event.x,event.y,
                                        fill=backColor,outline=foreColor)
    elif what.get()==5:
        canvas.create_rectangle(event.x-5,event.y-5,event.x+5,event.y+5,
                                outline=backColor,fill=backColor)
canvas.bind('<B1-Motion>',onLeftButtonMove)

# 鼠标左键抬起，不允许画图
def onLeftButtonUp(event):
    if what.get()==2:
        canvas.create_line(x.get(),y.get(),
                           event.x,event.y,fill=foreColor)
    elif what.get()==3:
        canvas.create_rectangle(x.get(),y.get(),
                                event.x,event.y,
                                fill=backColor, outline=foreColor)
    yesno.set(0)
    global lastDraw
    lastDraw = 0
canvas.bind('<ButtonRelease-1>',onLeftButtonUp)

# 创建菜单
menu=tk.Menu(app,tearoff=0)
# 打开图像
def Open():
    filename=tk.filedialog.askopenfilename(title='Open Image',
                                           filetypes=[('iamge','*.jpg *.png *.gif')])
    if filename:
        global image
        image=tk.PhotoImage(file=filename)      # 只支持 gif 格式
        canvas.create_image(80,80,image=image)
menu.add_command(label='Open',command=Open)

# 添加菜单，清除绘制的所有图形
def Clear():
    for item in canvas.find_all():
        canvas.delete(item)
menu.add_command(label='Clear',command=Clear)
menu.add_separator()

# 子菜单，绘图类型
memuType=tk.Menu(menu,tearoff=0)
def drawCurve():
    what.set(1)
memuType.add_command(label='Curve',command=drawCurve)
def drawLine():
    what.set(2)
memuType.add_command(label='Line',command=drawLine)
def drawCRectangle():
    what.set(3)
memuType.add_command(label='Rec',command=drawCRectangle)
def drawText():
    global text
    text=tk.simpledialog.askstring(title='输入文字',
                                   prompt='')
    what.set(4)
memuType.add_command(label='Text',command=drawText)
memuType.add_separator()

# 选择景色
def chooseForeColor():
    global foreColor
    foreColor=colorchooser.askcolor()[1]
memuType.add_command(label='前景色',command=chooseForeColor)

# 橡皮
def onErase():
    what.set(5)
memuType.add_command(label='Erase',command=onErase)
menu.add_cascade(label='Type',menu=memuType)

# 鼠标右键抬起，弹出菜单
def onRightButtonUp(event):
    menu.post(event.x_root,event.y_root)
canvas.bind('<ButtonRelease-3>',onRightButtonUp)
canvas.pack(fill=tk.BOTH,expand=tk.YES)

app.mainloop()