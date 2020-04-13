s = '中欧珊懂as'
print(len(s))

# 短字符串驻留？？？
a = '1234'
b = '1234'
print(id(a) == id(b))
a = '1234' * 500
b = '1234' * 500
print(id(a) == id(b))

# 字符串格式化
print('%d, %c' %(65, 65))
print('{0:.3f}'.format(1/3))
print('the {0:,} in hex is:{0:#x}, in oct is {0:#o}'.format(55))
p = (5, 8, 13)
print("X:{0[0]}; Y:{0[1]}; Z:{0[2]}".format(p))

weather = [("m", "r"), ("n", "s"), ("o", "t")]
formatter = "Weather of '{0[0]}' is {0[1]}".format
for item in map(formatter, weather):
    print(item)

# 格式化模板类
from string import Template
t = Template('My name is ${name}, and is ${age} years old.')
d = {'name':'Dong', 'age':39}
print(t.substitute(d))

# 常用方法
s = 'sdfghjkljhgfsdfghjkjhgfdsdghjhdfghj'
print(s.find('j'))
print(s.find('j', 10))
print(s.find('j', 10, 16))      #范围查找
print(s.rfind('j'))     #反向查找
print(s.index('j'))

# 字符匹配（返回索引数组）
from string import ascii_letters
from random import choice
from time import time

# 密度不同，检索方法不同
letters1 = ''.join([choice(ascii_letters) for i in range(9999)])    #适合 find
letters2 = ''.join([choice('ab') for i in range(9999)])     #适合逐字符查找

def position_of_character(sentence, ch):
    result = []
    index = 0
    index = sentence.find(ch, index + 1)
    while index != -1:
        result.append(index)
        index = sentence.find(ch, index + 1)
    return result

def demo(s, c):
    result = []
    for i, ch in enumerate(s):
        if ch == c:
            result.append(i)
    return result

print(position_of_character(letters1, 'a'))
print(demo(letters1, 'a'))
print(position_of_character(letters2, 'a'))
print(demo(letters2, 'a'))

s = "asjd,asda,sda,sa,dadasdas,da,das,d"
print(s.split(','))     #如果不指定分隔符，则字符串任何空白符号被认为是分隔符
print(s.partition(','))    #从左边第一个逗号切分
print(s.rpartition(','))    #右边
print(s.partition('sa'))     #字符串切分
s = "2014-10-31"
print(list(map(int, s.split("-"))))
print(s.split('-', maxsplit=1))     #指定最大分隔次数
li = {'apple', ' peach', 'banana', 'pear'}
print(','.join(li))     #字符串链接，比 +（涉及大量复制）效率高
s = 'aaa     bbb              s       d'
print(''.join(s.split()))

import timeit
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))      #执行 1w 次的时间

# 以下几个方法都生成新的字符串
s = 'qwSSqQQdaAd   qwqSSaasas'
print(s.upper())
print(s.capitalize())
print(s.title())        #单词首字母大写
print(s.swapcase())
print(s.replace('q', ';'))

# 字符映射
table = ''.maketrans('abcdef123', 'uvwxyz@#$')      #映射表
s = 'Python is a greate programming language. I like it!'
print(s.translate(table))       #按照映射表替换

# 凯撒加密算法
import string
lowerLetters = string.ascii_lowercase
upperLetters = string.ascii_uppercase
before = lowerLetters + upperLetters
print(before)
after = lowerLetters[3:] + lowerLetters[:3] + upperLetters[3:] + upperLetters[:3]       #从第三位循环位移
print(after)
table = ''.maketrans(before, after)     #将该字母替换为后面三个字母
example = 'If the implementation is easy to explain, it may be a good idea.'
print(example.translate(table))

# 随机密码
import string
x = string.digits + string.ascii_letters + string.punctuation
print(x)
import random
print(''.join([random.choice(x) for i in range(8)]))

# 原地修改的 unicode 数据对象
from io import StringIO
s = 'Hello world'
sio = StringIO(s)       #可变对象
print(sio.tell())       #返回当前位置
print(sio.read())       #开始读取
print(sio.getvalue())       #全部内容
print(sio.tell())
print(sio.seek(6))      #定义位置
print(sio.write('SDIBT'))       #从当前位置写入
print(sio.read())
print(sio.getvalue())
s = 'Hello world'
from array import array
sa = array('u', s)      #可变字符串对象
print(sa)
print(sa.tostring())
print(sa.tounicode())
sa[0] = 'F'
print(sa)
sa.insert(5, 'w')
print(sa)
sa.remove('l')
print(sa)

s = "  asd  asd  "
print(s.strip())        #删除两端空白

# 动态编译（编译前执行检查操作）
print(eval("1 + 7"))
print('a' in "abesa")
s = 'Beautiful is better than ugly.'
print(s.startswith('Be'))
print(s.startswith('Be', 5))
print(s.startswith('Be', 0, 5))

# 接收一个字符串元组作为参数表示掐后缀
import os                       #列出目录下的文件名
print([filename for filename in os.listdir(r'D:\\') if filename.endswith(('.bmp', '.jpg', '.gif'))])
print('1234abcd'.isalnum())
print('abcd'.isalpha())
print('1234'.isdigit())
print('九'.isnumeric())

# 返回指定宽度的新字符串
print('Hello world!'.center(20))    #居中对齐，空格补充
print('Hello world'.center(20, '='))
print('Hello world'.rjust(20, '='))     #左对齐
print('abc'.zfill(5))

# 排版
import textwrap
doc = '''sd a
s asd a
d asd asd asdasda asssssssssssd
aaaaaaaaaaawwwwwwwwwwwwwwwwwww
assssssssssssssssssssssssssssssssssssssssssssss'''
print(textwrap.fill(doc, width=20))

s = 'asdasdad'
print(list(zip(s, s)))

# 加密解密
def crypt(source, key):
    from itertools import cycle
    result = ''
    tmp = cycle(key)        #无线重复该序列
    for ch in source:
        result += chr(ord(ch)^ord(next(tmp)))       #交 key 的下一个字母
    return result

source = 'Shandong Institute of Business and Technology'
key = 'Dong Fuguo'

print('Before Encrypted:' + source)
encrypted = crypt(source, key)
print('After Encrypted:' + encrypted)
decrypted = crypt(encrypted, key)       #再循环一次，解码
print('After Decrypted:' + decrypted)

# 生成大量随机信息
import random
import string
import codecs
StringBase = '\u7684\u4e00\u4e86\u662f\u6211\u4e0d\u5278\u4eba'     #常用汉字
StringBase = ''.join(StringBase.split('\\u'))

def getEmail():
    suffix = ['.com', '.org', '.net', '.cn']
    characters = string.ascii_letters + string.digits + '_'
    username = ''.join((random.choice(characters) for i in range(random.randint(6, 12))))
    domain = ''.join((random.choice(characters) for i in range(random.randint(3, 12))))
    return username + '@' + random.choice(suffix)

def getTelNo():
    return ''.join((str(random.randint(0, 9)) for i in range(11)))

def getNameOrAddress(flag):
    '''flag 为 1 表示返回随机姓名，0 随机地址'''
    result = ''
    if flag == 1:
        rangestart, rangeend = 2, 5
    elif flag == 0:
        rangestart, rangeend = 10, 31
    else:
        print('flag 错误.')
    for i in range(rangestart, rangeend):
        result += random.choice(StringBase)
    return result

def getSex():
    return random.choice(('男', '女'))

def getAge():
    return str(random.randint(18, 100))

def main(filename):
    '''打开并写入文件'''
    with codecs.open(filename, 'w', 'utf-8') as fp:
        fp.write('Name, Sex, Age, TelNO, Address, Email\n')
        for i in range(200):
            name = getNameOrAddress(1)
            sex = getSex()
            age = getAge()
            tel = getTelNo()
            address = getNameOrAddress(0)
            email = getEmail()
            line = ','.join([name, sex, age, tel, address, email]) + '\n'       # 迭代后面元素
            fp.write(line)

def output(filename):
    '''读取文件'''
    with codecs.open(filename, 'r', 'utf-8') as fp:
        while True:
            line = fp.readline()
            if not line:
                return
            print(line, end=' ')

if __name__ == '__main__':
    filename = 'information.txt'
    # main(filename)
    # output(filename)

# 中文分词
import jieba
x = '分词的准确度直接影响了后续文本处理和挖掘算法的最终效果。'
print(list(jieba.cut(x)))
print(list(jieba.cut('纸杯')))
print(list(jieba.cut('花纸杯')))
import snownlp
print(snownlp.SnowNLP(x).words)

# 汉字到拼音转换
from pypinyin import lazy_pinyin, pinyin
print(lazy_pinyin('彩虹山地'))
print(lazy_pinyin('彩虹山地', 1))       #带声调的拼音
print(lazy_pinyin('彩虹山地', 2))       #另一种拼音
print(lazy_pinyin('彩虹山地', 3))       #首字母
print(lazy_pinyin('重要', 1))      #多音字
print(lazy_pinyin('重阳', 1))
print(pinyin('重阳'))
print(pinyin('重阳节', heteronym=True))        #多音字所有读音
x = '中英文混合 test123'
print(lazy_pinyin(x))
print(lazy_pinyin(jieba.cut(x)))
x = '闪动啊实打实大地上'
print(sorted(x, key=lambda ch:lazy_pinyin(ch)))     #按拼音排序