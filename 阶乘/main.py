n = int(input())
a = [0 for _ in range(10001)]
a[0] = 1    #第一个要乘的数
count1 = 0
count2 = 0
for i in range(2, n + 1):   #要乘的数字
    jw = 0  #进位
    for j in range(0, len(a)):  #低位相乘
        tmp = a[j] * i + jw
        if (tmp == 0) and (i != 2) and (j >= count2):
            break
        a[j] = (int(tmp % 10))
        jw = int(tmp / 10)
        if i != 2:
            count1 = j
    count2 = count1
for i in range(count1, -1, -1):    #倒序输出数组
    print(a[i], end='')
