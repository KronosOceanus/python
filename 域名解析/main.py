import urllib.request
import urllib.parse

# 读取网页内容
fp=urllib.request.urlopen(r'http://www.hao123.com')
print(fp.read(100))
print(fp.read(100).decode())
fp.close()

# 使用 get 方法读取并显示指定 URL 内容
# params=urllib.parse.urlencode({'spam':1,'eggs':2,'bacon':0})
# url='http://www.musi-cal.com/cgi-bin/query?%s' %params
# with urllib.request.urlopen(url) as f:
#     print(f.read().decode('utf-8'))

# 使用 post
data=urllib.parse.urlencode({'spam':1,'eggs':2,'bacon':0})
data=data.encode('ascii')
url='http://request.in/xrb182xr'
with urllib.request.urlopen(url, data) as f:
    print(f.read().decode('utf-8'))

# 使用 http 代理
# proxies={'http':'http://proxy.example.com:8080/'}    # 代理
# opener=urllib.request.FancyURLopener(proxies)
# with opener.open('http://www.hao123.com') as f:
#     print(f.read().decode('utf-8'))

# 用浏览器打开网页
import webbrowser
webbrowser.open('http://www.hao123.com')

# 域名解析
from urllib.parse import urlparse,urljoin,urlsplit

o=urlparse('http://www.hao123.com')
print(o.hostname)
print(o)

# URL 合并
print(urljoin('http://www.hao123.com/left','right'))

# URL 分割
url='https://www.bilibili.com/video/BV1pZ4y1p7Km'
print(urlsplit(url))