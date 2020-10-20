import sys
import socket
import threading as tr

'''2.代理服务器'''
'''python D:\project\python\代理服务器端口映射\sockMiddle.py 30800 192.168.1.102 10000'''

# sockDst，conn 分别发送消息给服务端，客户端
def middle(conn,addr):
    sockDst=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockDst.connect((ipServer,portServer))      # 连接服务器
    while True:
        data=conn.recv(1024).decode()       # 收到消息要解码
        print('收到客户端消息：'+data)
        if data=='不要发给服务器':
            conn.send('该消息被代理服务器过滤'.encode())       # 发送给客户端
            print('该消息已过滤')
        elif data.lower()=='bye':
            print(str(addr)+'客户端连接关闭')
            break
        else:
            sockDst.send(data.encode())     # 发送消息到服务器
            print('已转发服务器')
            data_fromServer=sockDst.recv(1024).decode()
            print('收到服务器回复的消息：'+data_fromServer)
            if data_fromServer=='不要发给客户端':
                conn.send('该消息已被代理服务器修改'.encode())
                print('消息已被篡改')
            else:
                conn.send(b'Server reply:'+data_fromServer.encode())
                print('已转发服务器消息给客户端')
    conn.close()
    sockDst.close()

def main():
    sockSrc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockSrc.bind(('',portSrc))      # 本机 IP
    sockSrc.listen(200)
    print('代理已启动')
    while True:
        try:
            conn,addr=sockSrc.accept()
            t=tr.Thread(target=middle,args=(conn,addr))     # 启用线程，为新客户代理
            t.start()
            print('新客户：'+str(addr))
        except:
            pass

if __name__=='__main__':
    try:
        portSrc=int(sys.argv[1])        # 代理服务器监听端口 30800
        ipServer=sys.argv[2]        # 服务器 IP 192.168.1.102
        portServer=int(sys.argv[3])     # 服务器端口 10000
        main()
    except:
        print('Sth error')