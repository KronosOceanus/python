import numpy as np
import matplotlib.pyplot as plt

plt.xlim((0,100))
plt.ylim((0,0.3))
sample1 = np.random.binomial(10, 0.5, size=1000)
sample2 = np.random.binomial(100, 0.5, size=1000)
sample3 = np.random.binomial(110, 0.5, size=1000)
plt.hist(sample1 + sample2, rwidth=0.9, alpha=0.6, density=True, label="n1+n2")
plt.hist(sample1, rwidth=0.9, alpha=0.6, density=True, label="n1")
plt.hist(sample2, rwidth=0.9, alpha=0.6, density=True, label="n2")
plt.hist(sample3, rwidth=0.9, alpha=0.6, density=True, label="n3=n1+n2")
plt.title("直方图")
plt.legend()
plt.show()
