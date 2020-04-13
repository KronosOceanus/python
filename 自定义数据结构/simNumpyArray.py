'''自定义矩阵'''
class simNumpyArray(object):
    def __init__(self, p):
        '''接收类型'''
        if type(p) not in (list, tuple, range):
            print('数据类型不符')
            return
        for item in p:
            if type(item) not in (int, float, complex):
                print('数据类型不符')
                return
        self.__data = [list(p)]     #初始化为 1,len(p) 矩阵
        self.__row = 1
        self.__col = len(p)

    def __del__(self):
        del self.__data

    # 将数组变为矩阵
    def reshape(self, size):
        '''参数必须为元组或列表，(row, col) 或者 [row, col]
            其中一个可以为 -1，表示自动计算'''
        if not (isinstance(size, list) or isinstance(size, tuple)):
            print('大小参数错误')
            return
        if len(size) != 2:
            print('大小参数错误')
            return
        if (not isinstance(size[0], int) or (not isinstance(size[1], int))):
            print('大小参数错误')
            return
        if size[0] != -1 and size[1] != -1 and size[0] * size[1] != self.__row * self.__col:    #行列数不等
            print('大小参数错误')
            return
        #自动计算
        if size[0] == -1:
            if size[1] == -1 or (self.__row * self.__col) % size[1] != 0:       #自动计算行列，不能整除
                print('大小参数错误')
                return
        if size[1] == -1:
            if size[0] == -1 or (self.__row * self.__col) % size[0] != 0:
                print('大小参数错误')
                return
        #重新合并数据，得到二维数组
        data = [t for i in self.__data for t in i]      #二重循环
        #修改大小
        if size[0] == -1:
            self.__row = int(self.__row * self.__col / size[1])
            self.__col = size[1]
        elif size[1] == -1:
            self.__row = int(self.__row * self.__col / size[0])
            self.__col = size[0]
        else:
            self.__row = size[0]
            self.__col = size[1]
        self.__data = [[data[row * self.__col + col] for col in range(self.__col)] for row in range(self.__row)]

    # 交互模式直接使用变量名作为表达式查看值时调用
    def __repr__(self):
        for i in self.__data:
            print(i)
        return ''

    # 使用 print 函数输出值时调用
    def __str__(self):
        return '\n'.join(map(str, self.__data))     # \n 会用于字典中每一个元素

    # 转置
    def T(self):
        b = simNumpyArray([t for i in self.__data for t in i])
        b.reshape((self.__row, self.__col))
        b.__data = list(map(list, zip(*b.__data)))      # * 表示多个参数（也可以是参数 list），完成转置
        b.__row, b.__col = b.__col, b.__row
        return b

    # 通用代码，用于矩阵与整数、实数、复数的加减乘除、整除、幂
    def __operate(self, n, op):
        b = simNumpyArray([t for i in self.__data for t in i])
        b.reshape((self.__row, self.__col))
        b.__data = [[eval(str(j) + op + str(n)) for j in item] for item in b.__data]
        return b

    # 通用代码，矩阵之间加减
    def __maxrixAddSub(self, n, op):
        c = simNumpyArray([1])
        c.__row = self.__row
        c.__col = self.__col    #列表元素相加                                    #([],[])     # ([],[])  ([], [])
        c.__data = [[eval(str(x[i]) + op + str(y[i])) for i in range(len(x))] for x, y in zip(self.__data, n.__data)]
        return c

    # 加单个数字，或者矩阵相加
    def __add__(self, n):
        if type(n) in (int, float, complex):
            return self.__operate(n, '+')
        elif isinstance(n, simNumpyArray):
            if n.__row == self.__row and n.__col == self.__col:
                return self.__maxrixAddSub(n, '+')
            else:
                print('两个矩阵必须同样大小')
                return
        else:
            print('数据格式错误')
            return

    # 减单个数字，或者矩阵相减
    def __sub__(self, n):
        if type(n) in (int, float, complex):
            return self.__operate(n, '-')
        elif isinstance(n, simNumpyArray):
            if n.__row == self.__row and n.__col == self.__col:
                return self.__maxrixAddSub(n, '-')
            else:
                print('两个矩阵必须同样大小')
                return
        else:
            print('数据格式错误')
            return

    # 乘单个数字，或者矩阵相乘
    def __mul__(self, n):
        if type(n) in (int, float, complex):
            return self.__operate(n, '*')
        elif isinstance(n, simNumpyArray):
            if n.__row == self.__col:       #可以相乘
                data = []       #临时数组 1
                for row in self.__data:     #矩阵 1 每一行
                    t = []      #临时数组 2
                    for ii in range(n.__col):   #矩阵 2 每一列
                        col = [c[ii] for c in n.__data]
                        tt = sum([i * j for i, j in zip(row, col)])     #行列压缩得到元组，求积
                        t.append(tt)        #添加到本行结果
                    data.append(t)      #添加一行
                c=simNumpyArray([t for i in data for t in i])       #得到最终数据
                c.reshape((self.__row, n.__col))
                return c
            else:
                print('矩阵大小错误')
                return
        else:
            print('数据格式错误')
            return

    # 除一个数字
    def __truediv__(self, n):
        if type(n) in (int, float, complex):
            return self.__operate(n, '/')
        else:
            print('数据格式错误')
            return

    # 整商
    def __floordiv__(self, n):
        if type(n) in (int, float, complex):
            return self.__operate(n, '//')
        else:
            print('数据格式错误')
            return

    # 幂运算
    def __pow__(self, n):
        if type(n) in (int, float, complex):
            return self.__operate(n, '**')
        else:
            print('数据格式错误')
            return

    # 判断相等
    def __eq__(self, n):
        if isinstance(n, simNumpyArray):
            if self.__data == n.__data:
                return True
            else:
                return False
        else:
            print('数字格式错误')
            return

    # 测试是否小于
    def __lt__(self, n):
        if isinstance(n, simNumpyArray):
            if self.__data < n.__data:      #矩阵大小比较
                return True
            else:
                return False
        else:
            print('数据格式错误')
            return

    # 成员测试运算符
    def __contains__(self, v):
        if v in self.__data:
            return True
        else:
            return False

    # 支持迭代
    def __iter__(self):
        return iter(self.__data)

    # 通用方法，计算三角函数（每个元素）
    def __triangle(self, method):
        try:
            b = simNumpyArray([t for i in self.__data for t in i])
            b.reshape((self.__row, self.__col))
            print("__import__('math')." + method + "()")
            b.__data = [[eval("__import__('math')." + method + "(" + str(j) + ")") for j in item] for item in b.__data]
            return b
        except:
            return '方法错误'

    # 属性，对所有元素求正弦
    @property
    def Sin(self):
        return self.__triangle('sin')

    # 属性，对所有元素求余弦
    @property
    def Cos(self):
        return self.__triangle('cos')