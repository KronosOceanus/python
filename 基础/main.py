from fractions import Fraction  #只导入类指定对象
from random import randint #随机数对象


# 基本数据类型
x = 'string'    #字符串和元组是不可变序列，不可按下标修改
print(type(x))
x = (1, 5, 6)
print(type(x))

x = 3
print(type(x))
x = [3, 4, 5, 'a']
print(type(x))
x = {1:'wo', 2:'ai', 3:'ni'}
print(type(x))
x = set('abc')
print(type(x))
x = True
print(type(x))
x = None
print(type(x))

print(isinstance('helloworld', str))    #是否可以类型转换
print(type({3}) in (list, tuple))

# 复数和分数
print(2 ** 5)
x = 3+4j
y = 2+5j
print(x * y)
print(abs(x * y))
print(x.conjugate())
x = Fraction(2, 5)
print(x)
print(x.numerator + x.denominator)

y = x;
print(id(x))
print(id(y))
x = 4
print(id(x))
print(id(y))
l = [0,2,1]     #列表中存储的是地址而不是元素值
print(id(l[-1]) == id(l[1]))
print(id(l[-1]) == id(l[2]))
print('id'.isidentifier())  #是否可以作为变量名称

# 进制转换
print(bin(554))
print(oct(554))
print(int(554))
print(hex(554))

# 字符与编码
print(chr(76))
print(ord('a'))

# 随机数与最值
a = [randint(0, 100) for i in range(10)]    #range生成指定范围的数字
print(max(a), min(a), sum(a))

import math
# 帮助
print(dir(math))    #查看math类可用对象
print(help(math.sin))   #查看方法具体用法
print(dir(2+4j))    #查看复数类型成员
print(dir(''))     #查看字符串类型成员  （带有下划线的成员有特殊意义）

# 基础运算符
# and not is or in
# @ 矩阵相乘
print(14//4)
for i in (2, 5, 7):
    print(i, end='\t')

# 科学计算
import numpy    #科学计算类
x = numpy.ones(3)   #生成全 1 矩阵
m = numpy.eye(3) * 3    #单位矩阵
m[0, 2] = 5  #设置指定位置元素（注意空格）
print(m @ x)

# 人机对话
import sys  #系统类
import pprint   #输出类
# x = input('please input:')  读取输入
print(x)
print(1, 3, 5, 7, sep='\t')     #修改默认分隔符
fp = open('test.txt', 'a+')
print('hello', file=fp)
fp.close()
# x = sys.stdin.read(5)   读取 5 个字符
# x = sys.stdin.readLine()    读取一行
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t)    #默认 80
pprint.pprint(t, width=30)

# 模块加载       设置别名（也可给对象设置别名）
# import 模块名 [as 别名]
print(sys.modules.items())  #预加载模块

# 定义函数，分辨启动方式
def main():
    if __name__ == '__main__':
        print('directly')
    elif __name__ == 'main':
        print('as a module')
main()

# 每个包中应该包含一个 __init__.py 文件，以表示这是一个包
import packag.echo
packag.echo.echo('hello')