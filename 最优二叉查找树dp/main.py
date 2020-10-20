import random as r
import numpy as np
import sys

n=int(input('输入个数：'))
data=np.array([r.randint(1,100) for i in range(n)])
m=[[0] * n for i in range(n)]
s=[[0] * n for j in range(n)]


def bestBinaryTree():
    for i in range(n):
        m[i][i] = data[i]

    for k in range(1,n):
        for left in range(0,n-k):
            right=left+k
            m[left][right]=sys.maxsize

            pSum=0
            for i in range(left,right+1):
                pSum += data[i]

            for i in range(left+1, right):
                thisCost = m[left][i-1] + m[i+1][right] + pSum
                if thisCost < m[left][right]:
                    m[left][right]= thisCost
                    s[left][right]= i

            if m[left][right] == sys.maxsize:
                if m[left][left] < m[right][right]:
                    i=left
                else:
                    i=right
                m[left][right] = pSum + m[i][i]
                s[left][right] = i

bestBinaryTree()
for i in range(n):
    for j in range(n):
        print(m[i][j], end='\t')
    print()