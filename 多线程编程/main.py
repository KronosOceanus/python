import threading as tr

print(tr.stack_size())      # 线程栈大小
tr.stack_size(60*1024)      # 设置线程栈大小
print(tr.stack_size())
print(tr.active_count())        # 活动线程数
print(tr.current_thread())      # 返回当前线程对象
print(tr.enumerate())       # 所有线程
def demo(v):
    print(v)

t=tr.Timer(3,demo,args=(5,))        # 创建线程
# t.start()       # 启动线程，3s 后调用函数
# t.cancel()      # 如果仍在等待时间到达，则取消（中断）

# join() 阻塞当前线程，等待被调用线程执行结束
import time

def func1(x,y):
    for i in range(x,y):
        print(i,end='\t')
    print()
    time.sleep(1)       # 把时间给别的线程

t1=tr.Thread(target=func1,args=(15,20))
# t1.start()
# t1.join(5)
# t2=tr.Thread(target=func1,args=(15,20))
# t2.start()

# is_alive() 判断线程是否处于运行状态
def func2():
    time.sleep(2)

# t3=tr.Thread(target=func2)
# print('t3:',t3.is_alive())
# t3.start()
# print('t3:',t3.is_alive())
# t3.join(1)      # 让步 1s
# print('t3:',t3.is_alive())
# t3.join()
# print('t3:',t3.is_alive())

# daemon=True 的子线程，会在主线程结束时直接退出（默认 False）
class mythread(tr.Thread):
    def __init__(self,num, threadname):
        tr.Thread.__init__(self,name=threadname)
        self.num=num
    def run(self):
        time.sleep(self.num)
        print(self.num)
t1=mythread(1,'t1')
t2=mythread(2,'t2')
t2.daemon=True
print(t1.daemon)
print(t2.daemon)
# t1.start()
# t2.start()      # 主线程结束，子线程直接退出

# 线程同步 Lock
class mythread0(tr.Thread):
    def __init__(self):
        tr.Thread.__init__(self)
    def run(self):
        global x
        lock.acquire()      # 获取锁
        lock.acquire()      # 可重入锁两次加锁
        x+=3
        print(x,end='\t')
        lock.release()      # 释放后才执行别的线程
        print(x,end='\t')
        lock.release()      # 最外层锁释放

lock=tr.RLock()     # 可重入锁，最外层锁释放才有作用

t1=[]
for i in range(10):
    t=mythread0()
    t1.append(t)

x=0
# for i in t1:
#     i.start()

# 互相当代对方释放锁，是死锁（二重加锁）

# 线程通信 Condition
from random import randint
from time import sleep

class Producer(tr.Thread):      # 生产者
    def __init__(self, threadname):
        tr.Thread.__init__(self,name=threadname)
    def run(self):
        global x
        while True:
            con.acquire()       # 获取锁
            if len(x)==10:
                con.wait()      # 生产者线程挂起
                print('Producer is waiting...')
            else:
                print('Producer:',end='\t')
                x.append(randint(1,1000))
                print(x)
                sleep(1)
                con.notify()        # 唤醒消费者线程
            con.release()
class Consumer(tr.Thread):      # 消费者
    def __init__(self, threadname):
        tr.Thread.__init__(self,name=threadname)
    def run(self):
        global x
        while True:
            con.acquire()
            if not x:
                con.wait()
                print('Consumer is waiting...')
            else:
                print('Consumer:',end='\t')
                print(x.pop(0))
                print(x)
                sleep(2)
                con.notify()
            con.release()

con=tr.Condition()
x=[]
p=Producer('Producer')
c=Consumer('Consumer')
# p.start()
# c.start()
# p.join()
# c.join()

# Queue 实现线程同步
import queue

class Producer(tr.Thread):
    def __init__(self,threadname):
        tr.Thread.__init__(self, name=threadname)
    def run(self):
        global myqueue
        # 队列尾部追加元素
        myqueue.put(self.getName())     # 放入当前线程
        print(self.getName(),' put ',self.getName(),' to queue')

class Consumer(tr.Thread):
    def __init__(self,threadname):
        tr.Thread.__init__(self,name=threadname)
    def run(self):
        global myqueue
        print(self.getName(),' get ',myqueue.get(),' from queue')

myqueue=queue.Queue()
plist=[]
clist=[]
for i in range(10):
    p=Producer('Producer'+str(i))
    plist.append(p)
    c=Consumer('Consumer'+str(i))
    clist.append(c)

# for p,c in zip(plist,clist):
#     p.start()
#     p.join()
#     c.start()
#     c.join()

# Event 实现线程通信
class mythread3(tr.Thread):
    def __init__(self,threadname):
        tr.Thread.__init__(self,name=threadname)
    def run(self):
        global myevent
        if myevent.isSet():     # 被标记
            myevent.clear()     # 清除标记
            myevent.wait()      # 未被标记则挂起，被标记则无视
            print(self.getName()+' set')
        else:
            print(self.getName()+ ' not set')
            myevent.set()

myevent=tr.Event()
myevent.set()       # 设置标志为真

# for i in range(10):
#     t=mythread3(str(i))
#     t.start()