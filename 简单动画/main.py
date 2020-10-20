import tkinter as tk
import time

app=tk.Tk()
app.title('tk animation')
app['width']=800
app['height']=600
canvas=tk.Canvas(app,bg='white',width=800,height=600)
image=tk.PhotoImage(file='cole.png')
# 记录图片编号
id_actor=canvas.create_image(80,80,image=image)
# 控制是否自己运动
flag=False

# 单击移动
def onLeftButtonDown(event):
    global flag
    flag=True
    while flag:
        canvas.move(id_actor,5,0)       # 编号，沿 x,y 方向移动距离
        canvas.update()     # 更新
        time.sleep(0.05)
canvas.bind('<Button-1>',onLeftButtonDown)

def onLeftButtonUp(event):
    global flag
    flag=False
canvas.bind('<ButtonRelease-1>',onLeftButtonUp)

def onRightButtonDown(event):
    app.destroy()
canvas.bind('<Button-3>',onRightButtonDown)

# 键盘控制移动方向
def keyCon(event):
    if event.keysym=='Left':
        canvas.move(id_actor,-200,0)
        canvas.update()
canvas.bind_all('<KeyPress-Left>',keyCon)       # 绑定键盘

canvas.pack(fill=tk.BOTH,expand=tk.YES)
canvas.focus()      # 获得键盘焦点

app.mainloop()