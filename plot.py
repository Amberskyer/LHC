import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([3, 5, 7, 2, 6, 10, 15])
plt.plot(x, y)
plt.plot(x, y, 'g', lw=10)

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([3, 5, 7, 2, 6, 10, 15])
plt.bar(x, y, 0.5, alpha=1, color='b')
plt.show()

