import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

date = np.linspace(1, 15, 15)
beginPrice = np.array(
    [2438.71, 2500.88, 2534.95, 2512.52, 2594.04, 2743.26, 2697.47, 2695.24, 2678.23, 2722.13, 2674.93, 2744.13,
     2717.46, 2832.73, 2877.40])
endPrice = np.array(
    [2511.90, 2538.26, 2510.68, 2591.66, 2732.98, 2701.69, 2701.29, 2678.67, 2726.50, 2681.50, 2739.17, 2715.07,
     2823.58, 2864.90, 2919.08])
print(date)

for i in range(0, 15):
    dateOne = np.zeros([2])
    dateOne[0] = i
    dateOne[1] = i
    priceOne = np.zeros([2])
    priceOne[0] = beginPrice[i]
    priceOne[1] = endPrice[i]
    if endPrice[i] > beginPrice[i]:
        plt.plot(dateOne, priceOne, 'r', lw=8)
    else:
        plt.plot(dateOne, priceOne, 'g', lw=8)

print(dateOne)
print(priceOne)

plt.show()
