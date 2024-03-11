import numpy as np
import cv2

image = np.zeros((200,300), np.uint8) # 이미지의 크기는 200, 300
image.fill(255) # 흰색 지정

title1, title2 = "AUTOSIZE", "NORMAL",
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)  # 윈도우 안의 이미지 크기는 불변
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)    # 윈도우 안의 이미지는 윈도우 크기에 따라 가변
#AUTOSIZE 라는 이름에 속지말자, 오토사이즈는 이미지 크기가 불변.

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 400,300) # 윈도우의 크기 변경 400, 300
cv2.resizeWindow(title2, 300,200) # 윈도우의 크기 변경 400, 300 //image 사이즈와 행과 열이 다른듯..

cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 크기 (200, 300)은 세로로 200, 가로로 300
# 윈도우 크기 (300, 200)은 세로로 200, 가로로 200
# 이미지 윈도우 서로 반대이다.