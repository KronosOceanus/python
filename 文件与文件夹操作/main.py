# os
import os
import os.path as op

p='D:\\youtube\\音\\トラック１～６　フルデータ.mp3'
q='D:\\youtube\\音乐\\牵牛花之诗-AZKi.mp3'
print(op.basename(p))       #路径名最后
print(op.exists('test.txt'))       #存在
# os.rename('test.txt', 'text.txt')       #重命名
print(op.dirname(p))       #文件夹名
print(op.split(p))     #切分，元组
print(op.splitdrive(p))
print(op.splitext(p))
print(os.getcwd())      #当前工作目录
# os.mkdir(os.getcwd()+'\\temp')      #创建目录
os.chdir(os.getcwd()+'\\temp')      #改变工作目录
print(os.getcwd())
os.mkdir(os.getcwd()+'\\test')
print(os.listdir('.'))     #列出当前目录
os.rmdir('test')        #删除目录
print(op.commonpath([p,q]))

# shutil
import shutil

shutil.copyfile(p, p[:-4]+'2.mp3')      #复制文件
# shutil.make_archive('D:\\youtube\\音', 'zip', 'D:\\youtube', '音')      #压缩文件
# shutil.unpack_archive('D:\\youtube\\音.zip', 'D:\\youtube\\音')       #解压
# shutil.rmtree('D:\\youtube\\音')       #删除文件夹

# 处理删除文件/文件夹失败的情况
import stat
def remove_readonly(func, path, _):     #回调函数
    os.chmod(path, stat.S_IWRITE)       #删除文件的只读属性
    func(path)      #再次执行删除操作
# shutil.rmtree('D:\\youtube\\音', onerror=remove_readonly())        #指定回调函数

# 复制文件夹
from shutil import copytree, ignore_patterns
# copytree('D:\\project\\python\\文件与文件夹操作\\temp',
#         'D:\\project\\python\\文件与文件夹操作\\temmp',
#         ignore=ignore_patterns('n*'))     #指定忽略前后缀

# 遍历
def visitDir(path):
    if not op.isdir(path):
        return
    for fileName in os.listdir(path):      #列出文件/夹
        sub_path=op.join(path, fileName)
        print(sub_path)
        if op.isdir(sub_path):      #递归
            visitDir(sub_path)
visitDir('D:\\project\\python\\文件与文件夹操作\\temp')
# 用 os.walk() 遍历
def visitDir2(path):
    if not op.isdir(path):
        return
    list_dirs=os.walk(path)     #元组
    for root, dirs, files in list_dirs:
        for d in dirs:
            print(op.join(root, d))
        for f in files:
            print(op.join(root, f))
visitDir2('D:\\project\\python\\文件与文件夹操作\\temp')

# 其他功能
import subprocess
notepad='C:\\windows\\notepad.exe'
h=subprocess.Popen('', executable=notepad)       #打开记事本
h.terminate()       #结束进程
h=subprocess.Popen('', executable=notepad)
h.kill()
# os.popen(notepad)

import win32api
# win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 0)      # 0 表示后台运行
# win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 1)
# win32api.ShellExecute(0, 'open', 'www.hao123.com', '', '', 1)       #网址