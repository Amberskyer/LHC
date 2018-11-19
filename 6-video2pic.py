import cv2

cap = cv2.VideoCapture('ljh.mp4')
isOpened = cap.isOpened
print(isOpened)
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(fps, width, height)

i = 0
while isOpened:
    if i == 10:
        break
    else:
        i = i + 1
    (flag, frame) = cap.read()
    fileName = 'image' + str(i) + ".jpg"
    print(fileName)
    if flag == True:
        cv2.imwrite("./img/"+fileName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])

print('end')
