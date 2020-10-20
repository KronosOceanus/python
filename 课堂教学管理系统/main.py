import datetime
import tkinter
import tkinter.scrolledtext
import tkinter.messagebox
import tkinter.filedialog
import tkinter.ttk
import socket
import sqlite3
import random
import threading
import time
import struct
import os
import sys
import string

# 升级 pip 到最新版本（python -m pip install --upgrade pip）
path='"'+os.path.dirname(sys.executable)+\
    '\\scripts\\pip" install --user --upgrade pip'
os.system(path)

# 导入必要扩展库
# docx
try:
    import docx
except:
    path = '"' + os.path.dirname(sys.executable) + \
           '\\scripts\\pip" install python-docx'
    os.system(path)
    import docx
# xlrd
try:
    import xlrd
except:
    path = '"' + os.path.dirname(sys.executable) + \
           '\\scripts\\pip" install xlrd'
    os.system(path)
    import xlrd
# docx
try:
    import openpyxl
except:
    path = '"' + os.path.dirname(sys.executable) + \
           '\\scripts\\pip" install openpyxl'
    os.system(path)
    import openpyxl

# 创建主窗口
root=tkinter.Tk()
root.geometry('360x340+400+300')
root.resizable(False, False)
root.title('课堂教学管理系统')
# 避免端口一直被占用
def closeWindow():
    # 结束点名
    if int_canDianming.get()==1:
        int_canDianming.set(0)
    # 结束收作业
    if int_zuoye.get()==1:
        int_zuoye.set(0)
    # 结束学生提问
    if int_xueshengTiwen.get()==1:
        int_xueshengTiwen.set(0)
    # 结束服务状态
    if int_server.get()==1:
        int_server.set(0)
    root.destroy()
# 绑定事件处理函数
root.protocol('WM_DELETE_WINDOW',closeWindow)