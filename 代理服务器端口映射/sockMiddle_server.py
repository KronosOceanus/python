import sys
import socket
import threading as tr
'''1.服务端'''
'''python D:\project\python\代理服务器端口映射\sockMiddle_server.py 10000 192.168.1.102'''
'''在两个端口之间进行消息转发，实现内网外网通信'''

# 传入连接，回复消息，原样返回
def replyMessage(conn):
    while True:
        data=conn.recv(1024)
        conn.send(data)
        if data.decode().lower()=='bye':
            break
    conn.close()

def main():
    sockSrc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockSrc.bind(('',port))     # 本机 IP
    sockSrc.listen(200)     # 最大连接排队数量
    while True:
        try:
            conn,addr=sockSrc.accept()
            if addr[0] != onlyYou:      # 只允许特定主机（服务端）访问本服务器
                conn.close()
                continue
            t=tr.Thread(target=replyMessage, args=(conn,))      # 启动线程，回复消息
            t.start()
        except:
            print('error')

if __name__=='__main__':
    try:
        port=int(sys.argv[1])       # 服务器监听端口 10000
        onlyYou=sys.argv[2]     # 允许访问的客户端 IP 192.168.1.102
        main()
    except:
        print('必须给定端口参数')