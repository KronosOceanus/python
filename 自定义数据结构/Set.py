'''自定义集合'''
class Set(object):
    def __init__(self, data=None):
        if data == None:
            self.__data = []
        else:
            if not hasattr(data, '__iter__'):
                raise Exception('数据不可迭代')
            temp = []
            for item in data:
                hash(item)      #集合中元素必须可以 hash
                if not item in temp:
                    temp.append(item)
            self.__data = temp

    def __del__(self):
        del self.__data

    def add(self, value):
        hash(value)
        if value not in self.__data:
            self.__data.append(value)
        else:
            print('元素已存在')

    def remove(self, value):
        if value in self.__data:
            self.__data.remove(value)
            print('删除成功')
        else:
            print('元素不存在')

    def pop(self):
        if not self.__data:
            print('集合为空，无法弹出')
            return
        import random
        item = random.choice(self.__data)
        print(item)
        self.__data.remove(item)

    '''差集 - '''
    def __sub__(self, otherSet):
        if not isinstance(otherSet, Set):
            raise Exception('类型错误')
        result = Set()
        for item in self.__data:
            if item not in otherSet.__data:
                result.__data.append(item)
        return result

    '''并集 | '''
    def __or__(self, otherSet):
        if not isinstance(otherSet, Set):
            raise Exception('类型错误')
        result = Set(self.__data)
        for item in otherSet.__data:
            if item not in result.__data:
                result.__data.append(item)
        return result

    '''交集'''
    def __and__(self, otherSet):
        if not isinstance(otherSet, Set):
            raise Exception('类型错误')
        result = Set()
        for item in self.__data:
            if item in otherSet.__data:
                result.__data.append(item)
        return result

    '''差集'''
    def __xor__(self, otherSet):
        return (self-otherSet) | (otherSet-self)

    '''相等判断'''
    def __eq__(self, otherSet):
        if not isinstance(otherSet, Set):
            raise Exception('类型错误')
        if sorted(self.__data) == sorted(otherSet.__data):
            return True
        else:
            return False

    '''相等'''
    def __gt__(self, otherSet):
        if not isinstance(otherSet, Set):
            raise Exception('类型错误')
        if self != otherSet:
            flag1 = True
            for item in self.__data:
                if item not in otherSet.__data:
                   #当前集合有元素不属于另一个集合
                   flag1 = False
                   break
            flag2 = True
            for item in otherSet.__data:
                if item not in self.__data:
                    flag2 = False
                    break
            if not flag1 and flag2:
                return True
            return False

    '''包含'''
    def __ge__(self, otherSet):
        if not isinstance(otherSet, Set):
            raise Exception('类型错误')
        return self == otherSet or self > otherSet

    '''判断真子集'''
    def issubset(self, otherSet):
        if not isinstance(otherSet, Set):
            raise Exception('类型错误')
        if self < otherSet:
            return True
        else:
            return False

    '''判断超集'''
    def issuperset(self, otherSet):
        if not isinstance(otherSet, Set):
            raise Exception('类型错误')
        if self > otherSet:
            return True
        else:
            return False

    '''清空元素'''
    def clear(self):
        while self.__data:
            del self.__data[-1]
        print('集合已清空')

    '''可迭代'''
    def __iter__(self):
        return iter(self.__data)

    '''in'''
    def __contains__(self, item):
        if item in self.__data:
            return True
        else:
            return False

    '''len()'''
    def __len__(self):
        return len(self.__data)

    def __repr__(self):
        return '{' + str(self.__data)[1:-1] + '}'

    def __str__(self):
        return '{' + str(self.__data)[1:-1] + '}'