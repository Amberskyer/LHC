import cv2
import numpy as np

img0 = cv2.imread("girl.jpg", 1)
img1 = cv2.imread("psb.jpg", 1)
# cv2.imshow("img", img0)
# cv2.imshow("img", img1)
imgInfo = img0.shape
height = imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]

roiH = int(height / 2)
roiW = int(width / 2)
img0ROI = img0[0:roiH, 0: roiW]
img1ROI = img1[0:roiH, 0: roiW]

dst = np.zeros(imgInfo, np.uint8)
dst2 = np.zeros((roiH, roiW, 3), np.uint8)

# api 图片1 权重 图片2 权重 未知
dst = cv2.addWeighted(img0ROI, 0.5, img1ROI, 0.5, 0)
# 原理 两个图片的bgr取平均值
for i in range(0, roiH):
    for j in range(0, roiW):
        (b0, g0, r0) = img0ROI[i, j]
        (b1, g1, r1) = img1ROI[i, j]
        b = int(b0 >> 1) + int(b1 >> 1)
        g = int(g0 >> 1) + int(g1 >> 1)
        r = int(r0 >> 1) + int(r1 >> 1)
        dst2[i, j] = (b, g, r)

cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
