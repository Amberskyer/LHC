import cv2
import numpy as np

img = cv2.imread('gxt.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

dst = cv2.equalizeHist(gray)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
