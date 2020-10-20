import tkinter as tk
from myWindow import myWindow

# 主窗口
root=tk.Tk()
root.config(width=400)
root.config(height=200)
# 标题
root.title('Multiple windows Demo')
window1=tk.IntVar(root,value=0)
window2=tk.IntVar(root,value=0)

# 创建并弹出新窗口
def buttonClick1():
    if window1.get()==0:
        window1.set(1)
        w1=myWindow(root,'F',1)
        button1.wait_window(w1.top)
        window1.set(0)
button1=tk.Button(root,text='F',command=buttonClick1)
button1.place(x=70,y=40,height=40,width=200)

def buttonClick2():
    if window2.get()==0:
        window2.set(1)
        w2=myWindow(root,'S',2)
        button2.wait_window(w2.top)
        window2.set(0)
button2=tk.Button(root,text='S',command=buttonClick2)
button2.place(x=70,y=100,height=40,width=200)

root.mainloop()