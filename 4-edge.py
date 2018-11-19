import cv2
import numpy as np

# 灰度图片，方法四
img = cv2.imread("girl.jpg", 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# canny 1 gray 2 高斯 3 canny
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgG = cv2.GaussianBlur(gray, (3, 3), 0)
dst = cv2.Canny(imgG, 50, 50)  # 1 data 2 th 图片卷轴——>>th
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
