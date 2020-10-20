import socket       # 客户端

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)       # IPv4 UDP
s.bind((''),5000)       # 空表示任何本机可用 IP 地址
while True:
    data, addr=s.recvfrom(1024)
    print(data.decode(), addr[1], addr[0])
    if data.decode().lower()=='bye':
        break
s.close()