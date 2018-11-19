# 图片的镜像
import cv2
import numpy as np

img = cv2.imread("girl.jpg", 1)
cv2.imshow("img", img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]
newImgInfo = (height * 2, width, deep)

dst = np.zeros(newImgInfo, np.uint8)
# for i in range(0, height * 2):
#     for j in range(0, width):
#         if i < height:
#             dst[i, j] = img[i, j]
#         else:
#             dst[i, j] = img[-(i - height), j]


for i in range(0, 1):
    print(i)
    for j in range(0, width):
        dst[i, j] = img[i, j]
        dst[(2 * height - i - 1), j] = img[i, j]

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
