import matplotlib.pyplot as plt     #约定俗成的写法plt
import numpy as np

X = np.linspace(0, 10, 11)
Y = 1/(1+2 ** X)
plt.plot(X, Y)
plt.xticks(X)

# 在ipython的交互环境中需要这句话才能显示出来
plt.show()