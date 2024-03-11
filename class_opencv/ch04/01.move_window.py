import numpy as np
import cv2

image = np.zeros((200,400), np.uint8) #행이 200, 열이 400
image[:]=200 #모든 값 200으로 채우기 (200d은 회색임)

title1, title2 = 'Position1', 'Position2'

cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2)
cv2.moveWindow(title1, 150,150) #윈도우 창 title1을 150,150 으로 이동
cv2.moveWindow(title2, 400,50) #윈도우 창 title2를 400, 50 으로 이동

cv2.imshow(title1, image)
cv2.imshow(title2, image)

cv2.waitKey(10000) #입력을 기다림 0이면 계속 기다리고, 1이상의 수를 넣으면 해당수 만큼 기다림
cv2.destroyAllWindows()

# waitKey(ms) 시간 만큼 키 입력을대기, 키 이벤트 반환시 해당 값 반환