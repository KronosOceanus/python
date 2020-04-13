# pickle
import pickle
# 序列化写入
n=7
i=13000000
a=99.056
s='中国人民 123abc'
lst=[[1,2,3],[4,5,6],[7,8,9]]
tu=(-5,10,8)
coll={4,5,6}
dic={'a':'apple','b':'banana','g':'grape'}
f=open('sample_pickle.dat','wb')    #写 二进制
try:
    pickle.dump(n, f)   #对象个数
    pickle.dump(i, f)   #写入
    pickle.dump(a, f)
    pickle.dump(s, f)
    pickle.dump(lst, f)
    pickle.dump(tu, f)
    pickle.dump(coll, f)
    pickle.dump(dic, f)
except:
    print('写文件异常')
finally:
    f.close()

# 读取
f=open('sample_pickle.dat','rb')
n=pickle.load(f)
for i in range(n):
    x=pickle.load(f)
    print(x)
f.close()

# 序列化之后的字节
print(pickle.dumps([1,2,3]))

# 文本文件转换成二进制文件
with open('text.txt') as src, open('test_pickle.dat','wb') as dest:
    lines=src.readlines()
    pickle.dump(len(lines), dest)
    for line in lines:
        pickle.dump(line, dest)
with open('test_pickle.dat','rb') as fp:
    n=pickle.load(fp)
    for i in range(n):
        print(pickle.load(fp), end='')
    print()

# struct
import struct
# 序列化写入
n=13000000
x=96.45
b=True
s='a1#中国'
sn=struct.pack('if?',n,x,b)     #序列化，if? 分别表示整数/实数/布尔
f=open('sample_struct.dat','wb')
f.write(sn)
f.write(s.encode())
f.close()

# 读取
f=open('sample_struct.dat','rb')
sn=f.read(9)
tu=struct.unpack('if?',sn)      #反序列化格式
print(tu)       #元组
n,x,b1=tu
print(n, x, b1)
s=f.read(9)
s=s.decode()
print(s)

# 读取字节长度
print(len(struct.pack('if?', 13000,56.0,True)))
print(len('a!@中国'.encode()))

# shelve 像字典一样操作二进制文件
import shelve
fp=shelve.open('shelve_test.dat')
zhangsan={'age':37, 'sex':'Male'}
fp['zhangsan']=zhangsan
lisi={'age':39, 'sex':'Male'}
fp['lisi']=lisi
fp.close()
fp=shelve.open('shelve_test.dat')
print(fp['zhangsan']['age'])

# marshal 对象序列化
import marshal
x1=30
x2=5.0
x3=[1,2,3]
x4=(4,5,6)
x5={'a':1, 'b':2, 'c':3}
x6={7,8,9}
x=[eval('x'+str(i)) for i in range(1, 7)]   #序列化对象 放入列表
with open('test.dat','wb') as fp:
    marshal.dump(len(x), fp)
    for item in x:
        marshal.dump(item, fp)
with open('test.dat','rb') as fp:
    n=marshal.load(fp)
    for i in range(n):
        print(marshal.load(fp), end='\t')