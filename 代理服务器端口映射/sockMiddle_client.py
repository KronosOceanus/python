import sys
import socket
'''客户端'''
'''python D:\project\python\代理服务器端口映射\sockMiddle_client.py 192.168.1.102 30800'''

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip,port))     # 直接连接代理服务器
    while True:
        data=input('请输入')
        sock.send(data.encode())
        print(sock.recv(1024).decode())
        if data.lower()=='bye':
            break
    sock.close()

if __name__=='__main__':
    try:
        ip=sys.argv[1]      # 代理服务器的 IP 和端口
        port=int(sys.argv[2])
        main()
    except:
        print('Sth error')