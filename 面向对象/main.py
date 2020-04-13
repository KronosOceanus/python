class Car(object):  # 括号中是父类
    price = 10000   #类成员
    def __init__(self, speed):
        self.speed = speed      #对象成员,必须用 self
    def infor(self):
        print('this is a car')

car = Car(60)
car.infor()

def demo():
    pass    #什么也不做

class A:
    def __init__(self, value1=0, value2=0):     #构造器
        self._value1 = value1   # protect
        self.__value2 = value2  # private
    def setValue(self, value1, value2):
        self._value1 = value1
        self.__value2 = value2
    def show(self):
        print(self._value1)
        print(self.__value2)

a = A(7, 8)
print(a._value1)
print(a._A__value2)     #外部访问私有数据成员（对象._类名变量名）
a.show()
A.price = 1000
print(A.price)

class Demo(object):
    total = 0
    def __new__(cls, *args, **kwargs):      #该方法在 init 之前被调用
        if cls.total >= 1:
            raise Exception('单例模式！')
        else:
            return object.__new__(cls)

    def __init__(self):
        Demo.total += 1

t1 = Demo()
print(t1.total)
# t2 = Demo()      #单例模式

class Root:
    __total = 0
    def __init__(self, v):
        self.__value = v
        Root.__total += 1

    @classmethod    #类方法，cls 表示该类自身
    def classShowTotal(cls):
        print(cls.__total)

    @staticmethod   #静态方法
    def staticShowTotal():
        print(Root.__total)

r = Root(3)
r.classShowTotal()
r.staticShowTotal()
Root.classShowTotal()
Root.staticShowTotal()

# 属性
class Test:
    def __init__(self, value):
        self.__value = value

    '''@property        #设置可读属性
    def value(self):
        return self.__value
        '''
    def __get(self):
        return self.__value
    def __set(self, v):
        self.__value = v
    def __del(self):
        del self.__value
    value = property(__get, __set, __del)      #指定相应读/写/删除方法

t = Test(2)
print(t.value)
t.value = 8
print(t.value)
del t.value
t.v = 7     #动态添加
print(t.v)
del t.v     #动态删除

# 继承（支持多继承）
class Person(object):
    def __init__(self, name=''):
        self.setName(name)
    def setName(self, name):
        self.__name = name
    def show(self):
        print(self.__name)

class Teacher(Person):
    def __init__(self, name='', age=30):
        super(Teacher, self).__init__(name)     #初始化父类成员
        self.setAge(age)
    def setAge(self, age):
        self.__age = age
    def show(self):
        super(Teacher, self).show()
        print(self.__age)

t = Teacher('cs', 50)
t.show()
t.setName('mm')     #调用继承方法
t.show()

l = [[7, 2], [6, 5]]      #测试
k = [[1, 3], [7, 7]]
print('\t'.join(map(str, l)))
print(list(zip(l, k)))      #压缩成元组，变成列表
