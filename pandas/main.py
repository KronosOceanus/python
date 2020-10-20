import pandas as pd
import numpy as np

# 生成数组
x=pd.Series([1,3,5,np.nan])     # NaN，带索引的一维数组
print(x)                                            #间隔为天
dates=pd.date_range(start='20130101',end='20131231',freq='D')
print(dates)                                        #间隔为月
dates=pd.date_range(start='20130101',end='20131231',freq='M')
print(dates)        # 12*4 矩阵           行号         列号
df=pd.DataFrame(np.random.randn(12,4),index=dates,columns=list('ABCD'))
print(df)

# 查看数组
# print(df.head())    #默认前 5 行
# print(df.head(3))
# print(df.tail())    #最后 2 行
# print(df.index)
# print(df.columns)
# print(df.values)

# 统计消息（平均值，标准差，最小最大值等）
print(df.describe())

print(df.T)

# 排序
print(df.sort_index(axis=0, ascending=False))       #行索引排序
print(df.sort_index(axis=1, ascending=False))       #列索引排序
print(df.sort_values(by='A'))       #数据排序（根据'A'列）

# 数据选择
print(df['A'])
print(df[0:2])      #行
print(df.loc[:,['A','C']])      #列
print(df.loc['2013-12-31',['A','D']])       #只能指定 key
print(df.iloc[2:4,1:2])
print(df[df.A>1])

# 修改
df.iat[0,2]=3
df.loc[:,'D']=[np.random.randint(50,60) for i in range(12)]     #修改一行
df['C']=-df['C']

# 缺失值处理
df1=df.reindex(index=['2013-01-31','2013-02-28',
                      '2013-03-31','2013-04-30',
                      '2013-05-31','2013-06-30',
                      '2013-07-31','2013-08-31',
                      '2013-09-30','2013-10-31',
                      '2013-11-30','2013-12-31'],
               columns=list(df.columns)+['G'])      #多加一列，缺失值默认 NaN
print(df1)
df1.iat[0,4]=3
print(df1)
print(df.dropna())      #不包含缺失值的行
df1['G'].fillna(5,inplace=True)     #使用指定值填充缺失值
print(df1)

# 数据操作
print(df1.mean())       #列平均值
print(df1.mean(1))      #行平均值
print(df1.shift(1))     #数据移位（行，空缺用 NaN 代替）
print(df1['D'].value_counts())      #直方图统计
df2=pd.DataFrame(np.random.randn(10,4))
print(df2[:3])
p1=df2[:3]
p2=df2[3:7]
p3=df2[7:]
print(pd.concat([p1,p2,p3]))        #合并
print(df.groupby('A').sum())       #分组计算

# 结合 plt 绘图
import matplotlib.pyplot as plt
df=pd.DataFrame(np.random.randn(1000,2),columns=['B','C']).cumsum()     #行号
df['A']=pd.Series(list(range(len(df))))     #添加一行
# df.plot(x='A')
# plt.show()

# 柱状图
df=pd.DataFrame(np.random.rand(10,4), columns=['a','b','c','d'])
# df.plot(kind='bar')
# df.plot(kind='barh',stacked=True)       #（图的种类，是否叠加）
# plt.show()

# 读取文件
import csv
with open('name.csv', 'w') as fp:
    headers = ['姓氏', '名字']
    test_dictWriter = csv.DictWriter(fp, fieldnames=headers)    #设置表头
    test_dictWriter.writeheader()
    test_dictWriter.writerow({'姓氏':'张', '名字':'三' })     #字典写入
    test_dictWriter.writerow({'姓氏':'里', '名字':'四' })
print(pd.read_csv('name.csv',encoding='GBK'))