# 图片的平移
import cv2
import numpy as np

img = cv2.imread("girl.jpg", 1)
cv2.imshow("img", img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

matShift = np.float32([[1, 0, 10], [0, 1, 20]])
dst = cv2.warpAffine(img, matShift, (width, height))

cv2.imshow("shift", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
