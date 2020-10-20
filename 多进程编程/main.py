import multiprocessing as mp
import os
from statistics import mean

# 进程
def k(name):
    print('父进程 id：',os.getppid())
    print('当前进程 id：',os.getpid())
    print(name)

# if __name__=='__main__':        # 必须用这个
#     p=mp.Process(target=k, args=('bob',))
#     p.start()
#     p.join()

# 进程池
def f(x):
    return mean(x)

# if __name__=='__main__':
#     x=[list(range(10)),list(range(20,30)),
#        list(range(50,60)),list(range(80,90))]
#     with mp.Pool(5) as p:      # 5 个进程的进程池
#         print(p.map(f,x))

# 进程数据交换
def foo(q):
    q.put('hl')

# if __name__=='__main__':
#     mp.set_start_method('spawn')        # Windows 系统创建子进程的默认方式
#     q=mp.Queue()
#     p=mp.Process(target=foo, args=(q,))     # Queue 作为另一个进程参数
#     p.start()
#     p.join()
#     print(q.get())      # 从队列中获取数据

# # 上下文
# if __name__=='__main__':
#     ctx=mp.get_context('spawn')        # 得到上下文对象
#     q=ctx.Queue()
#     p=mp.Process(target=foo, args=(q,))     # Queue 作为另一个进程参数
#     p.start()
#     p.join()
#     print(q.get())      # 从队列中获取数据

def c(conn):
    conn.send('hl')
    conn.close()

# # 管道实现数据交换
# if __name__=='__main__':
#     parent_conn,child_conn=mp.Pipe()
#     p=mp.Process(target=c,args=(child_conn,))       # 将子进程连接端传给子进程
#     p.start()
#     p.join()
#     print(parent_conn.recv())       # 获取管道另一端
#     parent_conn.close()

def m(n, a):
    n.value=3.1415926
    for i in range(len(a)):
        a[i]=a[i]**2

# # 共享内存数据传递，适合大数据
# if __name__=='__main__':
#     num=mp.Value('d', 0.0)        # 实数
#     arr=mp.Array('i',range(10))       # 整形数组
#     p=mp.Process(target=m, args=(num, arr))
#     p.start()
#     p.join()
#     print(num.value)        # 共享内存
#     print(arr[:])

def kk(d,l,t):
    d['name']='Dong Fuguo'
    d['age']=38
    d['sex']='Male'
    d['affiliation']='SDIBT'
    l.reverse()
    t.value=3

# # Manager 对象实现进程间数据交换，与内存共享差不多
# # Manager 对象控制一个有很多线程对象的服务端京城，允许其他进程访问这些对象
# if __name__=='__main__':
#     with mp.Manager() as manager:
#         d=manager.dict()
#         l=manager.list(range(10))
#         t=manager.Value('i',0)     # 整形
#         p=mp.Process(target=kk, args=(d,l,t))
#         p.start()
#         p.join()
#         for item in d.items():
#             print(item)
#         print(l)
#         print(t.value)

# 进程同步
# Lock 实现
def kkk(l,i):
    l.acquire()     # 获取锁
    try:
        print('hhh',i)
    finally:
        l.release()

# if __name__=='__main__':
#     lock=mp.Lock()
#     for num in range(10):
#         mp.Process(target=kkk,args=(lock,num)).start()

# Event 实现
def kkkk(e,i):
    if e.is_set():
        e.wait()
        print('hhh',i)
        e.clear()
    else:
        e.set()

# if __name__=='__main__':
#     e=mp.Event()
#     for num in range(10):
#         mp.Process(target=kkkk,args=(e,num)).start()