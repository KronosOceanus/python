# 检测本机所在局域网内的网络流量和数据包收发情况
# 对网络管理有重要意义，运行需要管理员权限
import socket
import threading
import time

activeDegree=dict()
flag=1

'''常用常量
地址簇：
    AF_UNIX：unix 本机通信
    AF_INET：IPv4
    AF_INET6： IPv6
socket 类型：
    SOCK_STREAM：TCP套接字类型
　　SOCK_DGRAM：UDP套接字类型
　　SOCK_RAW：原始套接字类型，这个套接字比较强大,创建这种套接字可以监听网卡上的所有数据帧
　　SOCK_RDM：是一种可靠的UDP形式，即保证交付数据报但不保证顺序。SOCK_RAM用来提供对原始协议的低级访问，
            在需要执行某些特殊操作时使用，如发送ICMP报文。SOCK_RAM通常仅限于高级用户或管理员运行的程序使用。'''

def main():
    global activeDegree
    global flag
    # 本机 IP
    HOST=socket.gethostbyname(socket.gethostname())
    # 创建原始 socket，适用于 Windows 平台，运行需要管理员权限
    # 对于其他系统，需要把 socket.IPPROTO_IP 改成 socket.IPPROTO_ICMP
    s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
    s.bind((HOST,0))
    # 设置捕获含有以下 IP 包头的数据包
    s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    # 启用混杂模式（接受所有经过它的数据流，无论去向）
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    # 捕捉数据包
    while flag:
        c=s.recvfrom(65565)
        host=c[1][0]
        activeDegree[host]=activeDegree.get(host,0)+1
        # 本机 IP
        if c[1][0] != '192.168.1.102':
            print(c)
    # 关闭混杂模式
    s.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)
    s.close()

t=threading.Thread(target=main)
t.start()
time.sleep(60)
flag=0
t.join()
for item in activeDegree.items():
    print(item)