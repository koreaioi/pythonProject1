import cv2

def zoom_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_ZOOM, value)

def focus_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_FOCUS,value)

def brightness_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_BRIGHTNESS, value)

def contrast_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_CONTRAST, value)


capture = cv2.VideoCapture(0)
if not capture.isOpened() : raise Exception("카메라 연결 오류")

capture.set(cv2.CAP_PROP_FRAME_WIDTH,400)  # 너비 400
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300) # 높이 300
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0) # 자동 초점 중지
capture.set(cv2.CAP_PROP_BRIGHTNESS,100) #프레임 밝기 100으로 초기화

title ="Change Camera Properites"
cv2.namedWindow(title)
cv2.createTrackbar('zoom',title, 0,10,zoom_bar)
cv2.createTrackbar('focus',title, 0,40,focus_bar)
cv2.createTrackbar('brightness',title, 0,40,brightness_bar)
cv2.createTrackbar('contrast',title, 0,40,contrast_bar)

while True:
    ret, frame = capture.read()
    if not ret : break
    if cv2.waitKey(30) >= 0: break

    cv2.imshow(title, frame)


# cv2.CAP_PROP_CONTRAST 대비
# cv2.CAP_PROP_BRIGHTNESE 밝기