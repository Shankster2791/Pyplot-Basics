#Q2. Represent the following table using bar chart:

import matplotlib.pyplot as plt
import numpy as np

method = np.array(['A','B','C','D'])
res1 = np.array([2,5,8,5])
res2 = np.array([3,2,5,7])
x1 = np.arange(len(res1))
x2 = [x + 0.25 for x in x1]
plt.bar(x1, res1, color='blue',width=0.25,  label='Result 1')
plt.bar(x2, res2, color='red',width=0.25, label='Result 2')
plt.xticks([x + 0.1 for x in x1], method)
plt.legend()
plt.show()
