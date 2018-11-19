import cv2

img = cv2.imread('./img/image1/jpg')
imgInfo = img.shape
size = (imgInfo[0], imgInfo[1])
