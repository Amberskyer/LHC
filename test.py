import cv2

src = cv2.imread("girl.jpg", 1)
cv2.imshow("img", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
