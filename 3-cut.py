# 图片的剪切
import cv2
import numpy as np

img = cv2.imread("girl.jpg", 1)
imgInfo = img.shape
print(imgInfo)
dst = img[100:200, 100:300]
cv2.imshow("img", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
