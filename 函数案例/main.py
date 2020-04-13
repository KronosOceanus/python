# 韩信点兵
from functools import reduce
from math import gcd
def isCoPrime(p):
    '''判断 p 中每个元组的第一个数是否互素'''
    for index, item1 in enumerate(p):
        for item2 in p[index + 1:]:
            if gcd(item1[0], item2[0]) != 1:
                return False
    return True

def extEuclid(Mi, mi):
    '''穷举法，求 Mi 关于模 mi 的乘法逆元'''
    for i in range(1, mi):
        if i * Mi % mi == 1:
            return i

def chineseRemainder(p):
    '''互素才能推出人数'''
    if not isCoPrime(p):
        return 'Data error.'
    pp = p[:]   #浅复制，防止修改参数
    ppp = [item[0] for item in pp]  #得到报数方式
    M = reduce(lambda x,y : x*y, ppp)   #报数方式总乘积
    print('M =',M)
    for index, item in enumerate(pp):
        Mi = int (M / item[0])  #除去本次报数方式之外的乘积
        bi = extEuclid(Mi, item[0])
        pp[index] = item + (Mi, bi)
    print(pp)
    result = sum([item[1] * item[2] * item[3] for item in pp])
    print(result)
    result = result % M
    if result == 1:
        result += M
    return result

# 数据格式 data[i] 表示一个军队, 其中每个元组为（报数方式，最后一个士兵每次报数）
data = [[(3,2), (5,3), (7,2)],
        [(5,1), (3,2)],
        [(5,1), (3,1)],
        [(5,4), (3,2)],
        [(7,2), (8,4), (9,3)],
        [(5,2), (6,4), (7,4)],
        [(3,2), (5,3), (7,4)]]
for p in data:
    print(p)
    print(chineseRemainder(p))
    print()



'''
 乘法逆元，是指群 G 中任意一个元素 a
 都在 G 中有唯一的逆元a'，具有性质 a×a'=a'×a=e，其中 e 为该群的单位元。
 当 a 与 b 互素时，a 关于模 b 的乘法逆元有解
 扩展欧几里得算法计算逆元
'''
def ext_euclid(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    if b == 0:
        return 1
    else:
        while (r != 0):
            q = old_r // r
            old_r, r = r, old_r - q * r
            old_s, s = s, old_s - q * s
    return old_s
# 驱动函数
def inv(a, p):
    _a = ext_euclid(a, p)
    return ((_a % p) + p) % p   # +p 再 %p 是为了防止负数出现

print(ext_euclid(35, 3))
print(inv(35, 3))

'''一维信号卷积'''
def conv(la, lb):
    result = []
    la.reverse()    #反转
    len1 = len(la)
    len2 = len(lb)
    for i in range(1, len1 + 1):    #算卷积，前闭后开循环
        t = la[len1 - i:]
        v = sum((item1 * item2 for item1, item2 in zip(t, lb)))
        result.append(v)
    for i in range(1, len2):    #直至移出
        t = lb[i:]
        v = sum((item1 * item2 for item1, item2 in zip(la, t)))
        result.append(v)
    return result

def mul(l):
    '''卷积结果转换为数字'''
    result = ''
    c = 0
    for item in l[::-1]:    #倒序遍历
        item = item + c     # c 进位记录
        n = str(item % 10)     #加上进位以后对 10 的余数
        c = item // 10
        result += n
    if c:
        result += str(c)
    return eval(result[::-1])   # eval 执行字符串表达式

def main(num1, num2):
    la = list(map(int, str(num1)))
    lb = list(map(int, str(num2)))
    result = conv(la, lb)

from random import randint
for i in range(100):
    num1 = randint(1, 9999)
    num2 = randint(1, 999999)
    main(num1, num2)

print(mul([11, 72, 53, 64, 85, 2]))

# 列表压缩原理（以短的为标准）
la = [1, 3]
lb = [2, 4, 7]
print(list((i1 * i2 for i1, i2 in zip(la, lb))))

# 汉诺塔 A -> B
def hano(num, A, B, C=None):
    global times    #记录移动次数
    assert type(num) == int, 'num must be integer'
    assert num>0, 'num must > 0'
    # 递归终止条件
    if num == 1:
        print('the {0} Times move:{1} --> {2}'.format(times, A, B))
        times += 1
    else:
        hano(num - 1, A, C, B)  #前 n-1 个盘子 A -> C
        hano(1, A, B)
        hano(num - 1, C, B, A)

times = 1
hano(3, 'A', 'B', 'C')

# 八皇后问题
def isValid(s, col):
    '''检测皇后位置是否合法'''
    row = len(s)
    for r, c in enumerate(s):
        #该列已经放过         对角线放过
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True

def queen(n, s=()):     # n 为皇后的数量，s 为当前已经摆放的皇后坐标元组
    '''返回每个皇后所在的列号（行号即 0 - 7 排列）'''
    if len(s) == n:     #递归终止条件
        return [s]
    res = []    #存放元组，每个元组包含每一行放的皇后的列数
    for col in range(n):
        if not isValid(s, col): continue
        for r in queen(n, s + (col,)):      #摆放下一行
            res.append(r)
    return res  #传递结果

result = [[(r, c) for r, c in enumerate(s)] for s in queen(8)]
print(len(result))      #摆放方法数
for r in result:
    print(r)
print(queen(8))