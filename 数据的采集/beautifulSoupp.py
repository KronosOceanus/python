import re,bs4,requests
from bs4 import BeautifulSoup

ht = requests.get('https://www.baidu.com')
bs1 = BeautifulSoup(ht.content, 'html.parser')
print(bs1.prettify())       #输出整个页面

print('title----')
print(bs1.title)

print('title.name----')
print(bs1.title.name)

print('title.parent.name----')
print(bs1.title.parent.name)

print('find all "a"')       #找到所有超链接
print(bs1.find_all('a'))

print('text of all "a"')
for one in bs1.find_all('a'):      #等价 bs1('a')
    print(one.text)

res = bs1.find(text=re.compile('地图'))
for one in res.parent.parent.previous_siblings:
    print(one)