import cv2

capture =cv2.VideoCapture(0)
if capture.isOpened() == False : raise Exception("카메라 연결 오류")

fps = 15.0
delay = round(1000/15)
size = (640, 360)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') #DX50 = DivX MPEG-4


writer = cv2.VideoWriter('flip_test.avi', fourcc, fps, size)
if writer.isOpened() == False : raise Exception("동영상 파일 개방 dksehla")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])  # 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1]) # 카메라 프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)          # 오토포커싱 중지
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)       # 프레임 밝기 초기화

while True:
    ret, frame = capture.read()
    if not ret : break
    if cv2.waitKey(delay) >= 0 : break

    frame = cv2.flip(frame,1)
    writer.write(frame)
    cv2.imshow("View Frame from Camera", frame)

writer.release()
capture.release()