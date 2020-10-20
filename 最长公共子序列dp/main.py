def LCS(A, B):
    '''table[i,j] 记录序列 Ai 和 Bj 的最长公共子序列的长度'''
    n=len(A)
    m=len(B)
    table = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:        # 子序列最后字母相同，则一定是最长公共子序列的最后一个字母
                table[i][j] = table[i - 1][j - 1] + 1       # 子问题长度 +1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])     # 否则去掉该字母，与子问题最大长度相同
    print(table[n][m])

LCS("ABCBDAB", "BDCABA")