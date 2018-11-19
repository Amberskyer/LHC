import cv2
import numpy as np


# 定义一个图片直方图方法
def ImageHist(image, type):
    color = (255, 255, 255)
    windowName = 'Gray'
    if type == 31:
        color = (255, 0, 0)
        windowName = 'B Hist'
    elif type == 32:
        color = (0, 255, 0)
        windowName = 'G Hist'
    elif type == 33:
        color = (0, 0, 255)
        windowName = 'R Hist'

    # 调用opencv api完成hist方法
    # 参数1 image 注意加上[] 变成一个list
    # 参数2 channels 通道 灰度直方图，下标[0]
    # 参数3 mask None 蒙版
    # 参数4 histSize 绘制直方图个数 256
    # 参数5 ranges 0-255
    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])

    # 定义最大值，定义最小值，定义最小值下标，定义最大值下标。
    minV, maxV, minL, maxL = cv2.minMaxLoc(hist)
    # 创建画布
    histImg = np.zeros([256, 256, 3], np.uint8)
    # 高度遍历
    for h in range(256):
        # 归一化数据，获取每一个直方图的数据*256 除以最大值。值会被归到0-256之间
        intenNormal = int(hist[h] * 256 / maxV)
        # 1. 画布；2.起点 3. 256 - 归一化之后的值
        cv2.line(histImg, (h, 256), (h, 256 - intenNormal), color)
    cv2.imshow(windowName, histImg)
    return histImg


img = cv2.imread('girl.jpg', 1)
# 将图片分层，RGB
channels = cv2.split(img)  # RGB - R G B
print(channels)
for i in range(0, 3):
    ImageHist(channels[i], 31 + i)
cv2.waitKey(0)
cv2.destroyAllWindows()
