import tkinter
import tkinter.ttk
import tkinter.messagebox
import tkinter.simpledialog
import os
from database import selectByUsername

# 用户登录
root=tkinter.Tk()       #主窗口
root.title('LR')
labelName=tkinter.Label(        #创建组件
    root,       #从属窗口
    text='UserName:',       #文本
    justify=tkinter.RIGHT,      #对齐方式
    width=80)       #宽度
labelName.place(x=10,y=5,width=80,height=20)        #放置组件

varName=tkinter.StringVar(root,value='')        #输入框
entryName=tkinter.Entry(
    root,
    width=80,
    textvariable=varName
)
entryName.place(x=100,y=5,width=80,height=20)

labelPwd=tkinter.Label(        #创建组件
    root,       #从属窗口
    text='UserPwd:',       #文本
    justify=tkinter.RIGHT,      #对齐方式
    width=80)       #宽度
labelPwd.place(x=10,y=30,width=80,height=20)        #放置组件

varPwd=tkinter.StringVar(root,value='')        #输入框
entryPwd=tkinter.Entry(
    root,
    show='*',       #密码框
    width=80,
    textvariable=varPwd
)
entryPwd.place(x=100,y=30,width=80,height=20)

def OK():       # 登陆
    global root
    name = entryName.get()
    pwd = entryPwd.get()
    u = selectByUsername(name)
    if u == None:
        tkinter.messagebox.showerror('false', message='用户名不存在!')
        return
    if u.password == pwd:
        tkinter.messagebox.showinfo(title='success', message='登陆成功')
        root.destroy()
        os.system('python music.py')
    else:
        tkinter.messagebox.showerror('false', message='密码错误!')

buttonOK=tkinter.Button(
    root,
    text='OK',
    command=OK)
buttonOK.place(x=60, y=100, width=50, height=20)

def login():        #登陆界面
    global root
    root.destroy()
    os.system('python login.py')

buttonLogin=tkinter.Button(
    root,
    text='Login',
    command=login)
buttonLogin.place(x=30, y=70, width=50, height=20)

def register():        #打开注册界面
    global root
    root.destroy()
    os.system('python register.py')

buttonRegister=tkinter.Button(
    root,
    text='Register',
    command=register)
buttonRegister.place(x=100, y=70, width=50, height=20)

buttonLogin['state']='disabled'
buttonRegister['state']='normal'

root.mainloop()     #消息主循环
