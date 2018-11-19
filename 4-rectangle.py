import numpy as np
import cv2

newImageInfo = (500, 500, 3)
dst = np.zeros(newImageInfo, np.uint8)

cv2.rectangle(dst, (50, 100), (200, 300), (255, 0, 0), 5)

cv2.circle(dst, (250, 250), (50), (0, 255, 0), -1)

cv2.ellipse(dst, (256, 256), (150, 100), 0, 0, 180, (255, 255, 0), -1)

points = np.array([[150, 50], [140, 140], [200, 170], [250, 250], [150, 50]], np.int32)
points = points.reshape((-1, 1, 2))
cv2.polylines(dst, [points], True, (0, 255, 255))

cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
