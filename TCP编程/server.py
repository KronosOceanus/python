import socket

words={'h':'k','sd':'38'}       # 问题：回答
HOST=''
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      # TCP
s.bind((HOST,PORT))     # 绑定
s.listen(1)     # 监听 1 个客户端连接
print('正在监听：',PORT)
conn,addr=s.accept()        # 连接和地址
print('Connected by',addr)
while True:
    data=conn.recv(1024).decode()       # 数据大小
    if not data:
        break
    print('接收数据：',data)
    conn.sendall(words.get(data,'Nothing').encode())        # 字符串匹配（设置默认值）
conn.close()
s.close()