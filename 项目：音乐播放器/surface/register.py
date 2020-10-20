import tkinter
import tkinter.ttk
import tkinter.messagebox
import tkinter.simpledialog

import dao.userDao as ud
from entity import User

# 用户登录
root=tkinter.Tk()       #主窗口
labelUserName=tkinter.Label(        #创建组件
    root,       #从属窗口
    text='UserName:',       #文本
    justify=tkinter.RIGHT,      #对齐方式
    width=80)       #宽度
labelUserName.place(x=10, y=5, width=80, height=20)        #放置组件

varName=tkinter.StringVar(root,value='')        #输入框
entryUserName=tkinter.Entry(
    root,
    width=80,
    textvariable=varName
)
entryUserName.place(x=100, y=5, width=80, height=20)
#-------------------------------------
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
#-------------------------------------
labelName=tkinter.Label(        #创建组件
    root,       #从属窗口
    text='Name:',       #文本
    justify=tkinter.RIGHT,      #对齐方式
    width=80)       #宽度
labelName.place(x=10,y=55,width=80,height=20)        #放置组件

varName=tkinter.StringVar(root,value='')        #输入框
entryName=tkinter.Entry(
    root,
    width=80,
    textvariable=varName
)
entryName.place(x=100,y=55,width=80,height=20)




def regist():        #登陆
    username=entryUserName.get()
    password=entryPwd.get()
    name=entryName.get()
    user=User(username=username,password=password,name=name)
    if ud.add_user(user):
        tkinter.messagebox.showinfo(title='success',message='注册成功')
    else:
        tkinter.messagebox.showerror('false',message='注册失败，用户名重复')

buttonRegist=tkinter.Button(
    root,
    text='regist',
    command=regist)
buttonRegist.place(x=30,y=95,width=50,height=20)

root.mainloop()     #消息主循环
