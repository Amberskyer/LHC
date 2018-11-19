import cv2
import numpy as np

img = cv2.imread("girl.jpg", 1)
cv2.imshow("img", img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]

for m in range(80, 120):
    for n in range(150, 300):
        if m % 10 == 0 and n % 10 == 0:
            for i in range(0, 10):
                for j in range(0, 10):
                    (b, g, r) = img[m, n]
                    img[m + i, n + j] = (b, g, r)
cv2.imshow("dst", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
