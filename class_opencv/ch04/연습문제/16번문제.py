import cv2

capture = cv2.VideoCapture(0)
if not capture.isOpened() : raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
capture.set(cv2.CAP_PROP_BRIGHTNESS, 0)
capture.set(cv2.CAP_PROP_AUTOFOCUS,0)

title = "title"
cv2.namedWindow(title)

while True:
    ret, frame = capture.read()
    if not ret : raise Exception("영상 읽기 오류")
    if cv2.waitKey(100) == 27 : break # esc 누르면 종료

    blue, green, red = cv2.split(frame)
    green[100:300, 200:300] = green[100:300,200:300] + 50
    frame = cv2.merge([blue, green, red])

    cv2.rectangle(frame, (200,100),(300,300),(0,0,255),3)

    cv2.imshow(title, frame)

capture.release()












# import cv2
#
# capture = cv2.VideoCapture(0)
# if not capture.isOpened(): raise Exception("카메라 연결 안됨")
#
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
# capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)
# capture.set(cv2.CAP_PROP_BRIGHTNESS, 0)
#
# title = "title"
# cv2.namedWindow(title)
#
# while True:
#     ret, frame = capture.read()
#
#     if ret is None: break
#     if cv2.waitKey(100) == 27: break  # esc누르면 종료
#
#     blue, green, red = cv2.split(frame)
#     # cv2.add(green[100:300, 200:300], 50) #첫번째 영상 , 두번쨰 영상 or 스칼라, 결과를 담을 영상
#     green[100:300,200:300] = green[100:300, 200:300] + 50
#     frame = cv2.merge([blue, green, red])  # 단일 채널 영상 합성
#
#     cv2.rectangle(frame, (200, 100), (300, 300), (0, 0, 255), 3)
#
#     cv2.imshow(title, frame)
#
# capture.release()
