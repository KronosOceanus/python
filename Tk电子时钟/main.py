import tkinter as tk
import threading
import datetime
import time

app=tk.Tk()
# 不显示标题栏
app.overrideredirect(True)
# 半透明窗体
app.attributes('-alpha',0.9)
# 窗口总在顶端显示
app.attributes('-topmost',1)
# 初始大小与位置
app.geometry('225x110+100+100')
labelDateTime=tk.Label(app)     #创建标签，与画布用法相同
labelDateTime.pack(fill=tk.BOTH,expand=tk.YES)      # 填充，拉伸
labelDateTime.configure(bg='gray')      # 背景色
# 鼠标位置
x=tk.IntVar(value=0)
y=tk.IntVar(value=0)
# 窗口拖动
canMove=tk.IntVar(value=0)
# 是否运行
still=tk.IntVar(value=1)

# 变换透明度，表示可移动
def onLeftButtonDown(event):
    app.attributes('-alpha',0.4)
    # 记录当前位置
    x.set(event.x)
    y.set(event.y)
    canMove.set(1)
labelDateTime.bind('<Button-1>',onLeftButtonDown)

# 透明度恢复
def onLeftButtonUp(event):
    app.attributes('-alpha',0.9)
    canMove.set(0)
labelDateTime.bind('<ButtonRelease-1>',onLeftButtonUp)

def onLeftButtonMove(event):
    if canMove.get()==0:
        return
    # 移动位置
    newx=app.winfo_x()+(event.x-x.get())
    newy=app.winfo_y()+(event.y-y.get())
    g='225x110+'+str(newx)+'+'+str(newy)
    app.geometry(g)
labelDateTime.bind('<B1-Motion>',onLeftButtonMove)

# 关闭
def onRightButtonDown(event):
    still.set(0)        # 停止运行
    t.join(0.2)
    # 关闭窗口
    app.destroy()
labelDateTime.bind('<Button-3>',onRightButtonDown)

# 显示当前线程时间函数
def nowDatetime():
    while still.get()==1:
        now=datetime.datetime.now()
        s=str(now.year)+'-'+str(now.month)+'-'+str(now.day)+' '
        s+=str(now.hour)+'-'+str(now.minute)+'-'+str(now.second)
        # 显示当前时间
        labelDateTime['text']=s
        time.sleep(0.2)     # 刷新间隔
t=threading.Thread(target=nowDatetime)      # 创建线程
t.daemon=True       # 后台
t.start()

app.mainloop()