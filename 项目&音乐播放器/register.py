import tkinter
import tkinter.ttk
import tkinter.messagebox
import tkinter.simpledialog
import os
from user import User
from database import insertUser, selectByUsername
from mail import send

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

labelPwd2=tkinter.Label(        #创建组件
    root,       #从属窗口
    text='ConPwd:',       #文本
    justify=tkinter.RIGHT,      #对齐方式
    width=80)       #宽度
labelPwd2.place(x=10,y=55,width=80,height=20)        #放置组件

varPwd2=tkinter.StringVar(root,value='')        #输入框
entryPwd2=tkinter.Entry(
    root,
    show='*',       #密码框
    width=80,
    textvariable=varPwd2
)
entryPwd2.place(x=100,y=55,width=80,height=20)

labelEmail=tkinter.Label(        #创建组件
    root,       #从属窗口
    text='Email:',       #文本
    justify=tkinter.RIGHT,      #对齐方式
    width=80)       #宽度
labelEmail.place(x=10,y=80,width=80,height=20)        #放置组件

varEmail=tkinter.StringVar(root,value='')        #输入框
entryEmail=tkinter.Entry(
    root,
    width=80,
    textvariable=varEmail
)
entryEmail.place(x=100,y=80,width=80,height=20)


def OK():       # 注册
    global root
    name = entryName.get()
    pwd = entryPwd.get()
    pwd2 = entryPwd2.get()
    email = entryEmail.get()
    if pwd != pwd2:
        tkinter.messagebox.showerror('false', message='两次密码不一致!')
        return
    u = User(name, pwd, email)
    if insertUser(u):
        tkinter.messagebox.showinfo(title='success', message='注册成功')
        send(u.email)
        root.destroy()
        os.system('python login.py')
    else:
        tkinter.messagebox.showerror('false', message='用户名重复!')

buttonOK=tkinter.Button(
    root,
    text='OK',
    command=OK)
buttonOK.place(x=60, y=150, width=50, height=20)

def login():        #登陆界面
    global root
    root.destroy()
    os.system('python login.py')

buttonLogin=tkinter.Button(
    root,
    text='Login',
    command=login)
buttonLogin.place(x=30, y=120, width=50, height=20)

def register():        #打开注册界面
    global root
    root.destroy()
    os.system('python register.py')

buttonRegister=tkinter.Button(
    root,
    text='Register',
    command=register)
buttonRegister.place(x=100, y=120, width=50, height=20)

buttonRegister['state']='disabled'
buttonLogin['state']='normal'

root.mainloop()     #消息主循环
