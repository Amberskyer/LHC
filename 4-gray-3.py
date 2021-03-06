import cv2
import numpy as np

# 灰度图片，方法四
img = cv2.imread("girl.jpg", 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

dst = np.zeros(imgInfo, np.uint8)

for i in range(0, height):
    for j in range(0, width):
        (b, g, r) = img[i, j]
        gray = int(b) * 0.299 + i-+nt(g) * 0.587 + int(r) * 0.114
        dst[i, j] = (gray, gray, gray)

cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
