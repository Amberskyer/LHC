import numpy as np
import cv2

img = cv2.imread("girl.jpg", 1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.rectangle(img, (200, 100), (500, 400), (0, 255, 0), 3)
# 1 dst 2 文字内容 3写入坐标 4 5 字体 字体大小 6 color 7 粗细 8 line type
cv2.putText(img, "this is girl", (100, 300), font, 1,(200, 100, 255), 2, cv2.LINE_AA)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
