import numpy as np
import cv2

def onChange(value):	# 트랙바 콜백 함수
    global image, title # 전역 변수 참조

    #add_value = value - int(image[0][0]) # 트랙바 값과 영상 화소값 차분
    #print("추가 화소값:", add_value)
    #image = image + add_value            # 행렬과 스칼라 덧셈 수행
    # image[:] = cv2.getTrackbarPos('Brightness', title) # 바뀐 값으로 바로 화면 색 변경되도록 수정...
    image[:] = value
    cv2.imshow(title, image)

image = np.zeros((300, 500), np.uint8)  # 영상 생성

title = 'Trackbar Event'
cv2.imshow(title, image)
cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)	# 트랙바 콜백 함수 등록

while True:
    key = cv2.waitKeyEx(100) # 100ms동안 키 이벤트 대기
    if key == 27: break      # esc 키 누르면 종료

    # 왼쪽< 화살표 키 입력
    if key == 0x250000:
        value = cv2.getTrackbarPos('Brightness', title)
        cv2.setTrackbarPos('Brightness', title, value - 1)
    # 오른쪽> 화살표키 입력
    elif key == 0x270000:
        value = cv2.getTrackbarPos('Brightness', title)
        cv2.setTrackbarPos('Brightness', title, value + 1)

    image[:] = cv2.getTrackbarPos('Brightness', title)  # 바뀐 값으로 바로 화면 색 변경되도록 수정...
    cv2.imshow(title, image)

cv2.destroyAllWindows()
