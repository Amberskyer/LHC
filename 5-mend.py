import cv2
import numpy as np

img = cv2.imread("girl.jpg", 1)

for i in range(100, 150):
    img[i, 125] = (255, 255, 255)
    img[i + 1, 125] = (255, 255, 255)
    img[i - 1, 125] = (255, 255, 255)

for i in range(100, 150):
    img[125, i] = (255, 255, 255)
    img[125, i + 1] = (255, 255, 255)
    img[125, i - 1] = (255, 255, 255)

cv2.imshow('img', img)

imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

point = np.zeros((height, width, 1), np.uint8)

for i in range(100, 150):
    point[i, 125] = 255
    point[i + 1, 125] = 255
    point[i - 1, 125] = 255

for i in range(100, 150):
    point[125, i] = 255
    point[125, i + 1] = 255
    point[125, i - 1] = 255

cv2.imshow('point', point)

dst = cv2.inpaint(img, point, 3, cv2.INPAINT_TELEA)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows();
