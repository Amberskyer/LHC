# 图片的缩放
import cv2
import numpy as np

img = cv2.imread("girl.jpg", 1)
cv2.imshow("img", img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dst = np.zeros(imgInfo, np.uint8)  # 0-255
dst2 = np.zeros(imgInfo, np.uint8)  # 0-255

for i in range(0, height):
    for j in range(0, width - 20):
        dst[i, j + 20] = img[i, j]
        dst2[i, j] = img[i, j]
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
