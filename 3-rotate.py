# 图片的旋转
import cv2

img = cv2.imread("girl.jpg", 1)
# 图片信息获取
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# 定义一个旋转矩阵 2*3
# getRotationMatrix2D 获取旋转矩阵
matRotate = cv2.getRotationMatrix2D((0, height), 10, 0.5)
# mat rotate 参数1 旋转center点(width，height) 2 旋转的angle(角度) 3 scale(缩放系数)

# 为什么一个矩阵旋转的列子，要进行缩放0.5设置让它不超出边界

# 100*100 25 四个角会超出。
dst = cv2.warpAffine(img, matRotate, (width, height))

# 展示
cv2.imshow('img', img)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
