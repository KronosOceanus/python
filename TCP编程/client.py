import socket
import sys

HOST='127.0.0.1'
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((HOST,PORT))      # 连接服务器
except:
    sys.exit()
while True:
    c=input('Input the content you want to send:')
    # 发送数据
    s.sendall(c.encode())
    data=s.recv(1024).decode()
    print('回复：',data)
    if c.lower()=='bye':
        break
s.close()