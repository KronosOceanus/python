import re,requests
ss = 'I love you, do you?'

res = re.match(r'((\w)+(\W))+',ss)
print(res.group())

res = re.search(r'(\w+)(,)',ss)     #整个扫描
print(res.group(0))
print(res.group(1))
print(res.group(2))

res = re.split('\W+', ss)       #分割
print(res)

res = re.split('\W+', ss, maxsplit=1)       #分割次数
print(res)

res = re.sub(r'(\w+)(,)', 'her,', ss)       #替换
print(res)

res = re.subn(r'(\w+)(,)', 'her,', ss)      #替换，返回替换次数
print(res)

res = re.findall(r'(\w+)', ss)      #整个扫描，返回列表
print(res)

pt = re.compile(r'(\w+)')       #实现编译，不用多次输入正则
ss = 'Another kind of calling'
res = pt.findall(ss)
print(res)

r = requests.get('https://www.baidu.com').content.decode('utf-8')
print(r)
pt = re.compile(r'(<title>)([\S\s]+)(</title>)')
print(pt.search(r).group())