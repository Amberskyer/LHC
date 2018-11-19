# 颜色映射
import cv2
import numpy as np

# 灰度图片，方法四
img = cv2.imread("girl.jpg", 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# canny 1 gray 2 高斯 3 canny
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = np.zeros((height, width, 3), np.uint8)
for i in range(0, height):
    for j in range(0, width - 1):
        (b, g, r) = img[i, j]
        b = b * 1.5
        g = g * 1.3
        if b > 255:
            b = 255
        if g > 255:
            g = 255
        dst[i, j] = (b, g, r)

cv2.imshow("img", img)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
