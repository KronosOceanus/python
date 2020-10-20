def powerSet(set):
    '''组合法'''
    result=[]
    result.append([])       # 空集
    for s in set:
        s=list(s)
        preSize=len(result)
        for i in range(0,preSize):
            result.append(result[i]+s)
    print(result)

powerSet(['a','b','c'])

def bitPowerSet(set):
    '''位图法'''
    result=[]
    result.append([])
    n=len(set)
    size=2**n
    for i in range(1,size):
        result.append(bit(i,set))
    print(result)


def bit(k,set):
    n=len(set)
    subResult=[]
    for i in range(0,n):
        if (k >> i) & 1 == 1:
            subResult.append(set[i])
    return subResult

bitPowerSet(['a','b','c'])