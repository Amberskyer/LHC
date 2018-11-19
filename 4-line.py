import numpy as np
import cv2

newImageInfo = (500, 500, 3)
dst = np.zeros(newImageInfo, np.uint8)

cv2.line(dst, (100, 100), (400, 400), (0, 0, 255))
cv2.line(dst, (100, 200), (400, 200), (0, 255, 255), 20)
cv2.line(dst, (100, 300), (400, 300), (0, 255, 0), 20, cv2.LINE_AA)

cv2.line(dst, (200, 150), (50, 250), (25, 100, 255))
cv2.line(dst, (50, 250), (400, 380), (25, 100, 255))
cv2.line(dst, (400, 380), (200, 150), (25, 100, 255))

cv2.imshow("dst", dst)

# img = np.zeros((512, 512, 3), np.uint8)
# img = cv2.line(img, (0, 0), (512, 512), (255, 255, 255), thickness=1)
# img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# img = cv2.circle(img, (447, 63), 63, (0, 0, 255), 0)
# img = cv2.ellipse(img, (256, 256), (200, 100), 0, 0, 180, (255, 0, 0), -1)
# cv2.imshow('123', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
