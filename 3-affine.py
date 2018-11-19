# 图片的仿射
import cv2
import numpy as np

img = cv2.imread("girl.jpg", 1)
# cv2.imshow("img", img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
print(imgInfo)
# src 3->dst 3  原图上(左上角 左下角 右上角) 转换到新图片上三个点
# 原图三个点
matSrc = np.float32([[0, 0], [0, height - 1], [width - 1, 0]])
# 新图上的位置
matDst = np.float32([[50, 50], [200, height - 100], [width - 200, 100]])

matAffine = cv2.getAffineTransform(matSrc, matDst)
dst = cv2.warpAffine(img, matAffine, (width, height))

cv2.imshow("affine", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
