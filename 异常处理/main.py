# try...except...else...    try 没有异常则执行 else
# 可以捕获多个不同异常
# assert 语句用于测试，使用 -O 选项编译时，assert 语句将被删除

# 单元测试 unittest
import unittest
# setUp()/tearDown() 在测试前/后自动调用

# 测试，并将结果写入文件
import Stack
class TestStack(unittest.TestCase):
    def setUp(self):
        self.fp=open('test_Stack_result.txt','a')

    def tearDown(self):
        self.fp.close()

    def test_isEmpty(self):
        try:
            s=Stack.Stack()
            self.assertTrue(s.isEmpty())
            self.fp.write('1\n')
        except Exception as e:
            self.fp.write('0\n')

    def test_empty(self):
        try:
            s=Stack.Stack(5)
            for i in ['a','b','c']:
                s.push(i)
            s.empty()
            self.assertTrue(s.isEmpty())
            self.fp.write('1\n')
        except Exception as e:
            self.fp.write('0\n')

# unittest.main()

# 出错日志信息（重定向输出）
import sys
import logging

old=sys.stderr      #原输出
fp=open('log_test.txt','a')
sys.stderr=fp
logging.debug('Debugging imformation')
logging.info('Informational message')
sys.stderr=old
fp.close()

# 检测时间用 time 的 time()

# 检测内存
from memory_profiler import profile

@profile
def isPrime(n):
    if n==2:
        return True
    for i in range(2, int(n**0.5)+2):
        if n%i==0:
            return False
    return True

isPrime(99999999999999)