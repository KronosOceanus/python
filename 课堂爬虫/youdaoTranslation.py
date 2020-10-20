from urllib import request,parse
import time,json,random,hashlib

content = input("请输入要翻译的内容：\n")
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}

# 加密方式（一般有两种，每次都从服务器请求，或者根据 js 计算）
u = 'fanyideskweb'
d = content       # 要翻译的字符串
f = str(int(time.time()*1000)+random.randint(1,10))
c = 'rY0D^0\'nM0}g5Mm1z%1G4'
sign = hashlib.md5((u+d+f+c).encode('utf-8')).hexdigest()       # 计算 sign（md5 编码的 16 进制字符串）

# 要发送的 POST 请求中 Header 中的信息
data['i']=content
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']=f
data['sign']=sign
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_REALTlME'

data = parse.urlencode(data).encode('utf-8')        # url 中文编码转换
req = request.Request(url,data=data)        # 加入请求头 Header，得到 Request 对象
response = request.urlopen(req)     # 模拟浏览器，发起 http 请求

res = response.read().decode('utf-8')       # 得到响应
j = json.loads(res)
j = j["translateResult"]
print('result:',j[0][0]['tgt'])