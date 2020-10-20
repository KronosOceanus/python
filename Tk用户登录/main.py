import tkinter
import tkinter.ttk
import tkinter.messagebox
import tkinter.simpledialog

# 用户登录
root=tkinter.Tk()       #主窗口
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

def login():        #登陆
    name=entryName.get()
    pwd=entryPwd.get()
    if name=='admin' and pwd=='123456':
        tkinter.messagebox.showinfo(title='success',message='登陆')
    else:
        tkinter.messagebox.showerror('false',message='fail!')

buttonOk=tkinter.Button(
    root,
    text='Login',
    command=login)
buttonOk.place(x=30,y=70,width=50,height=20)

root.mainloop()     #消息主循环
