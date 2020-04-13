import xlrd as xl       # xlsx 支持
import numpy as np
from collections import Counter     #计数器
import matplotlib.pyplot as plt
import pandas as pd

data = xl.open_workbook("等位基因.xlsx")        #打开 excel 文件
table = data.sheets()[0]
if data.sheet_loaded(sheet_name_or_index=0):
    cols = table.ncols      #列数
    lists = [table.col_values(_) for _ in range(cols)]
    list_x = [_ for _ in range(1, len(lists) + 1)]
    list_A = []
    list_G = []
    list_C = []
    list_T = []
    for item in lists:
        dicts = dict(Counter(item))
        list_A.append(dicts.get('A', 0))
        list_G.append(dicts.get('T', 0))
        list_C.append(dicts.get('C', 0))
        list_T.append(dicts.get('G', 0))
    columns = ('A', 'G', 'C', 'T')
    data = []
    data.append(list_A)
    data.append(list_G)
    data.append(list_C)
    data.append(list_T)
    data = np.array(data)
    data = data.T       #转置
    df = pd.DataFrame(data, columns=columns, index=[_ for _ in range(1, cols + 1)])     #数据矩阵，对应基因，下标
    df.plot(kind='bar', stacked=True)       # stacked 表示堆放
    print(df)
    plt.show()
else:
    print("打开文件失败")
