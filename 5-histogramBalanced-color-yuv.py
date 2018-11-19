import cv2
import numpy as np

img = cv2.imread('girl.jpg', 1)
cv2.imshow('img', img)
imgYUV = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
channelYUV = cv2.split(imgYUV)
cv2.imshow('imgYUV', imgYUV)

channelYUV[0] = cv2.equalizeHist(channelYUV[0])
channels = cv2.merge(channelYUV)
result = cv2.cvtColor(channels, cv2.COLOR_YCrCb2BGR)
cv2.imshow('channels', channels)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
