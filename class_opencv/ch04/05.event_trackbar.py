import numpy as np
import cv2

def onChange(value): #값을 바꿀 때 사용하는 콜백 함수
    global image, title # 전역 변수로 참조

    add_value = value - int(image[0][0]) # 내가 누른 값 - 현재 화면 색 -> 화소값 변화량 출력을 위함.
    print("추가 화소값:", add_value)
    image[:] = image + add_value

    # image[:] = value # 이 코드만 실행해도 화면 변화는 문제가 없다. -> 이미지의 색깔이 모두 같을 때 만 가능.
    cv2.imshow(title,image)
    # cv2.imshow('윈도우 제목'. '이미지')

image = np.zeros((300,500), np.uint8) #zeros는 색을 0(검정)으로 한다는 뜻인가?
#세로 300, 가로 500인 이미지 사진 생성

title = 'Trackbar Event'
cv2.imshow(title, image)

#cv2.createTrackbar('트랙바 이름', '윈도우 이름', 색(초기값), count(max값), 콜백함수)
cv2.createTrackbar('Brightness', title, 100, 255, onChange)
cv2.waitKey(0)
#image[0][0]은 0,0의 색깔 즉, 검은색이다. 어차피 모든 영역이 검정이라 image[10][10], image[100][100]을 해도 검정이나옴
# 트랙바의 밝기 범위를 0 ~ 255
cv2.destroyAllWindows()

# 이미지에서의 100, 200은 세로로 부터 100, 가로로 부터 200이다.
# 윈도우에서의 100, 200은 세로로 부터 200, 가로로 부터 100이다.
# 그래서 02.~.py에서 윈도우를 이미지 크기와 같이 200,300으로 resize하면 짤리는 이유이다.
