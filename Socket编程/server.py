import socket       # 服务端
import sys
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                                # 客户端 IP
s.sendto(sys.argv[1].encode(),("192.168.0.103",5000))
s.close()