# 1 load xml 2 load jpg 3 haar gray 4 (检测)detect 5 draw(绘制方框)
import cv2
import numpy as np

# 加载load xml 参数1 file name
face_xml = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_xml = cv2.CascadeClassifier('haarcascade_eye.xml')

# load jpg
img = cv2.imread('psb.jpg')
cv2.imshow('src', img)

# haar gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces 1 data 2 scale 3 5
# 检测人脸: 1 灰度图片数据 2 缩放系数 3 目标大小
faces = face_xml.detectMultiScale(gray, 1.3, 5)
# 人脸个数
print('face=', len(faces))

# draw方框
for (x, y, w, h) in faces:
    # 起始坐标。起始坐标。
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # 我们已经找到的人脸区域
    roi_face = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    # 参数1 gray
    eyes = eye_xml.detectMultiScale(roi_face)
    print('eye=', len(eyes))
    for (e_x, e_y, e_w, e_h) in eyes:
        cv2.rectangle(roi_color, (e_x, e_y), (e_x + e_w, e_y + e_h), (0, 255, 0), 2)
cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
