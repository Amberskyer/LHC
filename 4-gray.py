import cv2
import numpy as np

# 灰度图片 方法一
img0 = cv2.imread("girl.jpg", 0)
img1 = cv2.imread("girl.jpg", 1)
cv2.imshow("img0", img0)
cv2.imshow("img1", img1)
print(img0.shape)
print(img1.shape)

# 灰度图片 方法二
img = cv2.imread("girl.jpg", 1)
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
