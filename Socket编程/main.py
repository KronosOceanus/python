import socket   # 获取本机 IP（也可以在 dos 中用 ipconfig/all 查看）
import uuid

ip=socket.gethostbyname(socket.gethostname())
node=uuid.getnode()
macHex=uuid.UUID(int=node).hex[-12:]
mac=[]
for i in range(len(macHex))[::2]:
    mac.append(macHex[i:i+2])
max=':'.join(mac)
print('IP:',ip)         # ip 最后为 255，是广播，局域网内所有主机都会收到信息
print('mac:',mac)       # 网卡物理地址