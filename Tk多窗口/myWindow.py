# 窗口类
import tkinter as tk
from tkinter import messagebox

class myWindow:
    def __init__(self,root,myTitle,flag):
        # 创建窗口
        self.top=tk.Toplevel(root,width=300,height=200)
        # 设置窗口标题
        self.top.title(myTitle)
        # 顶端显示
        self.top.attributes('-topmost',1)
        # 根据不同情况放置不同组件
        if flag==1:
            label=tk.Label(self.top,text=myTitle)
            label.place(x=50,y=50)
        elif flag==2:
            def buttonOK():
                tk.messagebox.showinfo(title='Pthon',
                                       message='shit')
            button=tk.Button(self.top,text=myTitle,command=buttonOK)
            button.place(x=50,y=50)
