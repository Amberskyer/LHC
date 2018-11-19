import numpy as np
import cv2

img = cv2.imread("girl.jpg", 1)
height = int(img.shape[0] * 0.2)
width = int(img.shape[1] * 0.2)

imgResize = cv2.resize(img, (width, height))
for i in range(0, height):
    for j in range(0, width):
        img[i + 200, j + 100] = imgResize[i, j]

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
