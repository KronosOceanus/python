'''自定义数组'''
class MyArray(object):
    '''必须全是数字'''
    def __IsNumber(self, n):
        if not isinstance(n, (int, float, complex)):
            return False
        return True

    '''初始化'''
    def __init__(self, *args):
        if not args:
            self.__value = []
        else:
            for arg in args:
                if not self.__IsNumber(arg):
                    print('必须全是数字')
                    return
            self.__value = list(args)

    '''释放内部列表'''
    def __del__(self):
        del self.__value

    '''重载运算符 + '''
    def __add__(self, n):
        if self.__IsNumber(n):      #每个数字都 + n
            b = MyArray()
            b.__value = [item + n for item in self.__value]
            return b
        elif isinstance(n, MyArray):        #等长数组相加
            if len(n.__value) == len(self.__value):
                c = MyArray()
                c.__value = [i + j for i, j in zip(self.__value, n.__value)]
                return c
            else:
                print('数组长度不同')
        else:
            print('不支持运算')

    def show(self):
        print(list(self.__value))