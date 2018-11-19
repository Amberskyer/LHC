import cv2
import numpy as np
import math

# 灰度图片，方法四
img = cv2.imread("girl.jpg", 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# sobel 1 算子模板 2 图片卷积 3 阈值判决
# [1  2  1        [ 1 0 -1
#  0  0  0         2 0 -2
# -1 -2 -1 ]        1 0 -1 ]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 最终的边缘检测图片
dst = np.zeros((height, width, 1), np.uint8)
# 遍历图片中的每一个点
# 我们的算子模板在最外围时会溢出
for i in range(0, height - 2):
    for j in range(0, width - 2):
        # 计算水平方向和竖直方向的梯度
        # 竖直方向的梯度
        # 取原图片 gray[i,j] gray[i,j+1] gray[i,j+2] gray[i+2,j] gray[i+2,j+1] gray[i+2,j+2] 六个点。乘以模板中对应元素
        # 其实是取九个点，因为第二行为0.不用写出来
        gx = gray[i, j] + gray[i + 1, j] * 2 + gray[i + 2, j] - gray[i, j + 2] - gray[i + 1, j + 2] * 2 - gray[
            i + 2, j + 2]
        gy = gray[i, j] * 1 + gray[i, j + 1] * 2 + gray[i, j + 2] * 1 - gray[i + 2, j] * 1 - gray[i + 2, j + 1] * 2 - \
             gray[i + 2, j + 2] * 1
        # 计算梯度
        grad = math.sqrt(gy * gy + gx * gx)
        # 大于阈值
        if grad > 50:
            dst[i, j] = 255
        else:
            dst[i, j] = 0
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
