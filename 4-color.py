import cv2
import numpy as np

img = cv2.imread("girl.jpg", 1)
cv2.imshow("img", img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]

dst = np.zeros(imgInfo, np.uint8)

for i in range(0, height):
    for j in range(0, width):
        (b, g, r) = img[i, j]
        dst[i, j] = (255 - b, 255 - g, 255 - r)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
