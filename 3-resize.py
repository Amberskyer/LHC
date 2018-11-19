# 图片的缩放
import cv2
import numpy as np

img = cv2.imread("girl.jpg", 1)

imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]

# 1放大 缩小 2 等比例 非
dstHeight = int(height * 0.5)
dstWidth = int(width * 0.5)

# 最近临域插值 双线性临域插值 像素关系重采样 立方插值
dst = cv2.resize(img, (dstWidth, dstHeight))

# 最近临域插值
dst2 = np.zeros((dstHeight, dstWidth, 3), np.uint8)
for i in range(0, dstHeight):
    for j in range(0, dstWidth):
        iNew = int(i << 1)
        jNew = int(j << 1)
        dst2[i, j] = img[iNew, jNew]

# 窗口显示图片
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
