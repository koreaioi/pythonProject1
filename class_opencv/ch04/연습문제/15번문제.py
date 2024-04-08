import numpy as np, cv2

def change_bt(value):
    global capture
    capture.set(cv2.CAP_PROP_BRIGHTNESS,value)

def change_ct(value):
    global capture
    capture.set(cv2.CAP_PROP_CONTRAST,value)


capture = cv2.VideoCapture(0)
if not capture.isOpened() : raise Exception("카메라 연결 오류")

capture.set(cv2.CAP_PROP_FRAME_WIDTH,600)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,400)
capture.set(cv2.CAP_PROP_AUTOFOCUS,0)
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)

title = "title"

cv2.namedWindow(title)
cv2.createTrackbar("t1", title, 100,200, change_bt)
cv2.createTrackbar("t2", title, 0,40, change_ct)


while True:
    ret, frame = capture.read()

    if not ret: break
    if cv2.waitKey(30) >= 0: break

    cv2.imshow(title, frame)
