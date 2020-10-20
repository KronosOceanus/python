'''给定一组物品，每种物品都有自己的重量和价格，
    在限定的总重量内，我们如何选择，才能使得物品的
    总价格最高。问题的名称来源于如何选择最合适的物
    品放置于给定背包中。

    对每一件物品遍历背包容量，当背包可容纳值大于
    等于当前物品，与之前已放进去的物品所得价值进
    行对比，考虑是否需要置换。

    定义 value(i,j)：
    当前背包容量 j，前 i 个物品最佳组合对应的价值'''
def bag(n,c,w,v):
    '''计算最大价值
        n 物品数量
        c 背包容量
        w 每个物品占位
        v 每个物品价值
        注意！！！：w,v 下标 i-1 代表前 i 个物品（从 0 开始 / 而 value 从 1 开始）'''
    value=[[0 for j in range(c+1)] for i in range(n+1)]
    for i in range(1,n+1):      # 前 i 个物品
        for j in range(1,c+1):      # 背包子容量
            value[i][j] = value[i-1][j]     # 默认前 i 个物品组合，新物品可能无法组合
            # 背包子容量能放入当前物体
            if j >= w[i-1]:
                combination=value[i-1][j-w[i-1]]+v[i-1]     # 当前背包子容量，减去新物品容量，的组合，加上当前物品价值，得到新的价值组合
                if value[i][j] < combination:       # 最优组合
                    value[i][j]=combination
    for x in value:
        print(x)
    show(n,c,w,value)

def show(n,c,w,value):
    '''得到最大价值组合（倒序遍历）
        当 value 大于上一行同样位置 value，表示放入了新物品'''
    print('最大价值：',value[n][c])
    x=[False for i in range(n)]
    j=c     # 背包容量
    for i in range(n,0,-1):
        if value[i][j] > value[i-1][j]:
            x[i-1]=True
            j -= w[i-1]     # 减去放入物品容量
    print('物品组合：')
    for i in range(n):
        if x[i]:
            print(i+1, end='\t')


bag(6,10,
    [2,2,3,1,5,2],
    [2,3,1,5,4,3])