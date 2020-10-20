import socket
import sys
import struct
import re
import getpass

'''python D:\project\python\FTP通信软件\ftpClient.py 192.168.1.103'''
'''avg_secure_vpn_setup.exe'''
def main(serverIP):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((serverIP,10600))    # 连接到服务器
    userId=input('请输入用户名：')
    # 获取密码（不回显）
    userPwd=getpass.getpass('请输入密码：')
    message=userId+','+userPwd
    sock.send(message.encode())     # 发送登录信息
    login=sock.recv(100)        # 登陆状态
    if login==b'error':
        print('用户名或密码错误')
        return
    # 计算包装内东西的长度（字节）
    intSize=struct.calcsize('I')
    while True:
        # 接受客户端命令
        command=input('>>').lower().strip()
        if not command:     # 未输入有效字符
            continue
        # 向服务端发送命令
        command=' '.join(command.split())
        sock.send(command.encode())
        # 退出
        if command in ('quit','q'):
            break
        # 查看文件列表
        elif command in ('list','ls','dir'):
            loc_size=struct.unpack('I',sock.recv(intSize))[0]
            files=eval(sock.recv(loc_size).decode())    # 控制接收长度
            for item in files:
                print(item)
        # 切换到上一级目录
        elif ''.join(command.split())=='cd..':
            print(sock.recv(100).decode())
        # 查看当前工作目录
        elif command in ('cwd','cd'):
            print(sock.recv(100).decode())
        # 切换至子文件夹
        elif command.startswith('cd '):
            print(sock.recv(100).decode())
        # 从服务器下载文件
        elif command.startswith('get '):
            isFileExist=sock.recv(20)
            # 文件不存在
            if isFileExist != b'ok':
                print('error')
            # 文件存在，开始下载
            else:
                print('downloading.',end=' ')
                fp=open(command.split()[1],'wb')
                print(fp.name)
                while True:
                    # 显示进度
                    print('.',end=' ')
                    data=sock.recv(4096)
                    print(data)
                    if data==b'overxxxx':
                        break
                    fp.write(data)
                    sock.send(b'ok')
                fp.close()
                print('ok')
        else:
            print('无效命令')
    sock.close()

if __name__=='__main__':
    if len(sys.argv)!=2:
        print('Usage:{0} serverIPAddress'.format(sys.argv[0]))
        exit()
    serverIP=sys.argv[1]
    # 判断是否为合法 IP 地址
    if re.match(r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$',serverIP):
        main(serverIP)
    else:
        print('服务器地址不合法')
        exit()