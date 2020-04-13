f1 = open('sample.txt', 'r')
f1.close()
print(f1.closed)
print(f1.mode)
print(f1.name)

s='Hello world\n文本文件的读取方法\n文本文件的写入方法\n'
with open('sample.txt', 'a+') as f:     #读写追加模式，自动管理资源
    f.write(s)

with open('sample.txt', 'r') as src, open('test.txt', 'w') as dst:
    dst.write(src.readline())

# json 支持
import json
x = [1, 2, 3]
print(json.dumps(x))       #对列表编码
print(json.loads(json.dumps(x)))        #解码
x = {'a':1, 'b':2, 'c':3}
y = json.dumps(x)
print(y)
print(type(y))
print(json.loads(y))
f = open('sample.txt', 'w')
json.dump(x, f)     #编码并写入文件
f.close()

# 读取文件
with open('sample.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)

with open('sample.txt') as f:
    for line in f:      #文件可迭代
        print(line)

with open('sample.txt') as f:
    lines = f.readlines()       #加载全部
    print(''.join(lines))

# 移动文本指针
f = open('sample.txt', 'r+')
print(f.tell())     #当前位置
print(f.read(20))
f.seek(13)      #重新指定位置
print(f.tell())
f.write('测试')
f.flush()       #把缓冲区内容写入磁盘文件
f.seek(0)
print(f.read())
f.close()

# 搜索整数，写入另一个文件
with open('data.txt', 'r') as fp:
    data = fp.readlines()
data = [line.strip() for line in data]
data = ','.join(data)
data = data.split(',')
data = [int(item) for item in data]
data.sort()
data = ','.join(map(str, data))     #变成字符串再写入
with open('data_asc.txt', 'w') as fp:
    fp.write(data)

# 电子表格和数据库内容
import csv                #读取时的每行开始标志
with open('test.csv', 'w', newline='') as fp:
    test_writer = csv.writer(fp, delimiter=' ', quotechar='"')
    test_writer.writerow(['red', 'blue', 'green'])      #写入一行
    test_writer.writerow(['test_string']*5)

with open('test.csv', newline='') as fp:
    test_reader = csv.reader(fp, delimiter=' ', quotechar='"')
    for row in test_reader:
        print(row)

with open('test.csv', newline='') as fp:
    test_reader = csv.reader(fp, delimiter=':', quotechar='"')      #分隔符不同
    for row in test_reader:
        print(row)

with open('name.csv', 'w') as fp:
    headers = ['姓氏', '名字']
    test_dictWriter = csv.DictWriter(fp, fieldnames=headers)    #设置表头
    test_dictWriter.writeheader()
    test_dictWriter.writerow({'姓氏':'张', '名字':'三' })
    test_dictWriter.writerow({'姓氏':'里', '名字':'四' })
with open('name.csv') as fp:
    test_dictReader = csv.DictReader(fp)
    print(','.join(test_dictReader.fieldnames))     #读取表头信息
    for row in test_dictReader:
        print(row['姓氏'],',',row['名字'])

# 文件每行尾部加上行号
filename = 'demo.py'
with open(filename, 'r') as fp:
    lines = fp.readlines()
maxLength = max(map(len, lines))    #最长行的长度
for index, line in enumerate(lines):    #遍历每一行
    newLine = line.rstrip()
    newLine = newLine + ' ' * (maxLength+5-len(newLine))    #添加空格，固定位置
    newLine = newLine + '#' + str(index+1) + '\n'   #添加行号
    lines[index] = newLine
with open(filename[:-3] + '_new.py', 'w') as fp:
    fp.writelines(lines)

# 计算文本文件最长行的长度和内容
with open('sample.txt') as fp:
    result = [0, '']
    for line in fp:
        t = len(line)
        if t > result[0]:
            result=[t, line]
print(result)