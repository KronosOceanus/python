'''
可以在对方计算机防护机制不允许直接上传文件的情况下
（对方拥有python 解释器），将自己主机作为服务器
将文件上传到对方计算机

标准库 ftplib 提供了 FTP 客户端的主要功能
'''
import socket
import threading as tr
import os
import struct

'''服务端'''

# 对方计算机的用户账号，密码，对方访问自己计算机的主目录
users={'zhangsan':{'pwd':'zhangsan1234','home':r'd:\\'},
      'lisi':{'pwd':'lisi567','home':'c:\\'}}

def server(conn,addr,home):
    print('新客户端：'+str(addr))
    # 进入对方主目录
    os.chdir(home)
    while True:
        data=conn.recv(100).decode().lower()        # 接收客户端消息
        print(data)
        if data in ('quit','q'):        # 客户端退出
            break
        elif data in ('list','ls','dir'):       # 对方查看自己当前文件列表
            files=str(os.listdir(os.getcwd()))
            files=files.encode()
            conn.send(struct.pack('I',len(files)))      # 打包发送字节串大小（I 相当于标志）
            conn.send(files)
        elif ''.join(data.split())=='cd..':     # 上一级目录
            cwd=os.getcwd()
            newCwd=cwd[:cwd.rindex('\\')]       # 切片寻找
            if newCwd[-1]==':':     # 根目录
                newCwd += '\\'
            if newCwd.lower().startswith(home):     # 限定对方只能访问的盘
                os.chdir(newCwd)
                conn.send(b'ok')
            else:
                conn.send(b'error')
        elif data in ('cwd','cd'):      # 查看当前目录
            conn.send(str(os.getcwd()).encode())
        elif data.startswith('cd '):
            data=data.split(maxsplit=1)     # 最大分隔次数
            if len(data)==2 and os.path.isdir(data[1])\
                and data[1] != os.path.abspath(data[1]):    # 只允许相对路径访问
                os.chdir(data[1])
                conn.send(b'ok')
            else:
                conn.send(b'error')
        elif data.startswith('get '):       # 对方从自己计算机下载文件
            data=data.split(maxsplit=1)
            if len(data)==2 and os.path.isfile(data[1]):     # 检查文件是否存在
                conn.send(b'ok')
                fp=open(data[1],'rb')       # 打开文件
                while True:
                    content=fp.read(4096)
                    if not content:     # 发送文件结束
                        conn.send(b'overxxxx')
                        break
                    conn.send(content)      # 发送文件内容
                    if conn.recv(10)==b'ok':
                        continue
                fp.close()
        else:
            pass

    conn.close()
    print(str(addr) + '连接关闭')

# 创建 socket 监听本地端口，等待客户端连接
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('', 10600))
sock.listen(5)
while True:
    conn, addr=sock.accept()    # 对方登陆自己计算机
    userId, userPwd=conn.recv(1024).decode().split(',')     # 可证客户端输入的用户名和密码是否正确
    if userId in users and users[userId]['pwd']==userPwd:
        conn.send(b'ok')
        home=users[userId]['home']
        t=tr.Thread(target=server,args=(conn,addr,home))
        t.daemon=True
        t.start()
    else:
        conn.send(b'error')