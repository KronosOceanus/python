import re
text = 'alpha. beta...gamma delta'
print(re.split('[\.]+', text))      #使用指定字符作为分隔符 .
print(re.split('[\.]+', text, maxsplit=1))      #最多分隔次数

pat = '[a-zA-z]+'
print(re.findall(pat, text))

# 字符串替换
pat = '{name}'
text = 'Dear {name}...'
print(re.sub(pat, 'Mr.Dong', text))     # pat 匹配 text，再替换
s = 'a s d'
print(re.sub('a|s|d', 'good', s))

print(re.escape('http://www.python.org'))   #字符串转义
print(re.match('done|quit', 'done'))        #得到 match 对象
print(re.match('done|quit', 'doe'))         #得到 None

# 删除空白字符
s = 'aaa bbb     c d e     fffff'
print(''.join(s.split()))
print(re.split('[\s]+', s))     #使用空格分隔

# 特定搜索
example = 'ShanDong Institute of Business and Technology is a very beautiful school.'
print(re.findall('\\ba.+?\\b', example))        #以 a 开头，\\b 表示单词头尾，？ 表示非贪心
print(re.findall('\\ba.+\\b', example))     #贪心模式
print(re.findall('\\ba\w*\\b', example))
print(re.findall('\\Bo.+?\\b', example))        #不以 o 开头，且含有 o 单词的剩余部分
print(re.findall('\\b\w.+?\\b', example))       #所有单词
print(re.findall('\w+', example))
print(re.findall(r'\b\w.+?\b', example))        #使用原始字符串
print(re.split('\s', example))      #使用任何空白字符分隔
print(re.findall('\d+\.\d+\.\d+', 'Python 2.7.11'))        # x.x.x 形式的数字

# pattern
pattern = re.compile(r'\bB\w+\b')       #以 B 开头
print(pattern.findall(example))
pattern = re.compile(r'\w+g\b')     #以 g 结尾
print(pattern.findall(example))
pattern = re.compile(r'\b[a-zA-Z]{3}\b')        # 3 个字母长
print(pattern.findall(example))
print(pattern.match(example))       #从头
print(pattern.search(example))      #从整个
pattern = re.compile(r'\b\w*a\w*\b')        #所有含有 a 的单词
print(pattern.findall(example))
pattern = re.compile(r'\w+gy')      #以 gy 结尾
print(pattern.findall(example))

# 替换
pattern = re.compile(r'\b\w*a\w*\b')
print(pattern.sub('*', example))
print(pattern.sub('*', example, 1))     #只替换一次

# 分隔
example = r'one,two,three.four////five\six?seven[eight]nine|ten'
pattern = re.compile(r'[,./\\?[\]\|]+')      #指定可能的分隔符，+ 表示允许重复
print(pattern.split(example))

# match
# 删除指定内容
email = 'tony@tiremove_thisger.net'
m = re.search('remove_this', email)
print(email[:m.start()] + email[m.end():])
print(re.sub('remove_this', '', email))
print(email.replace('remove_this', ''))

# 提取电话号码
telNumber = '''Suppo aisdnasdi is 5035-1545154, yaisdnaisdha is 010-15458485, he sia ia 025-44444444'''
pattern = re.compile(r'(\d{3, 4})-(\d7, 8)')
index = 0
while True:
    matchResult = pattern.search(telNumber, index)      #从指定位置开始匹配
    if not matchResult:
        break
    print('-' * 30)
    print('Success:')
    for i in range(3):
        print('Searched content:', matchResult.group(i),'Start from:', matchResult.start(i),
              'End at:', matchResult.end(i),'Its span is:',matchResult.span(i))
    index = matchResult.end(2)