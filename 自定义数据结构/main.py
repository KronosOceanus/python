# 自定义数组
from MyArray import MyArray
x = MyArray(7, 8, 2, 3, 5)
y = MyArray(1, 7, 5, 6, 4)
(x + y).show()
y = 8
(x + y).show()

# 自定义矩阵
from simNumpyArray import simNumpyArray
x = simNumpyArray((7, 8, 2, 3, 0, 5, 4, 6, 8))
y = simNumpyArray([7, 0, 4, 6, 9, 0, 1, 5, 2])
x.reshape((3, 3))
y.reshape((3, 3))
print(x)
print(y)
print(x + y)
print(x.T())
print(x.Sin)

# 自定义队列
from myQueue import myQueue
q = myQueue()
for i in range(5):
    q.put(i)
q.show()
for i in range(5):
    print(q.get(), end='\t')

print()

# 自定义栈
from Stack import Stack
s = Stack()
for i in range(5):
    s.push(i)
s.show()
for i in range(5):
    print(s.pop(), end='\t')

print()

# 堆
import heapq
import random
data = random.sample(range(1000), 10)
print(data)
heapq.heapify(data)
print(data)
heapq.heappush(data, 500)
for i in range(11):
    print(heapq.heappop(data), end='\t')

print()

# 自定义有向图
from DirectedGraph import DirectedGraph
d = {'A':['B', 'C', 'D'],
     'B':['E'],
     'C':['D', 'F'],
     'D':['B', 'E', 'G'],
     'E':['D'],
     'F':['D', 'G'],
     'G':['E']}
g = DirectedGraph(d)
g.searchPath('A', 'D')

# 自定义集合
from Set import Set
s1 = Set([7, 8, 2, 3, 0, 5, 4, 6, 8])
s2 = Set([7, 0, 4, 6, 9, 0, 1, 5, 2])
print(s1 - s2)
print(s1)