import cv2
import numpy as np
import random

img = cv2.imread("girl.jpg", 1)
cv2.imshow("img", img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]
# 目标效果: 先行后列 ，行高度，列宽度
dst = np.zeros(imgInfo, np.uint8)
# 定义一个范围，水平竖直都有可能
mm = 8

for m in range(0, height - mm):
    for n in range(0, width - mm):
        # 选取随机数 0-8 之间数据。
        # 如果产生为8，当前已经位于最后一个像素点，会超出范围
        index = int(random.random() * 8)  # 0-8
        (b, g, r) = img[m + index, n + index]
        dst[m, n] = (b, g, r)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
