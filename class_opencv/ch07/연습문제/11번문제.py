import numpy as np
import cv2

# 이미지를 불러옵니다.
image = cv2.imread('cannay_tset.jpg', cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상 파일 읽기 오류")

height, width = image.shape

# 마스크 생성하기
# 로버츠 마스크
roberts_x = np.array([[-1, 0, 0],
                       [ 0, 1, 0],
                       [ 0, 0, 0]])

roberts_y = np.array([[0, 0, -1],
                       [0, 1, 0],
                       [0, 0, 0]])

# 프리윗 마스크
prewitt_x = np.array([[-1, 0, 1],
                       [-1, 0, 1],
                       [-1, 0, 1]])

prewitt_y = np.array([[-1, -1, -1],
                       [0, 0, 0],
                       [1, 1, 1]])

# 소벨 마스크
sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

# 수직 방향의 미분을 수행하는 마스크
sobel_y = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])

# 이미지에 미분 연산을 적용합니다.
# 각 방향의 미분을 따로 계산하여 각각의 그래디언트를 얻습니다.
roberts1 = cv2.filter2D(image, -1, roberts_x)
roberts2 = cv2.filter2D(image, -1, roberts_y)

prewitt1 = cv2.filter2D(image, -1, prewitt_x)
prewitt2 = cv2.filter2D(image, -1, prewitt_y)

sobel1 = cv2.filter2D(image, -1, sobel_x)
sobel2 = cv2.filter2D(image, -1, sobel_y)

# 결과를 확인하기 위해 이미지를 출력합니다.
cv2.imshow('roberts1', roberts1)
cv2.imshow('roberts2', roberts2)
cv2.imshow('prewitt1', prewitt1)
cv2.imshow('prewitt2', prewitt2)
cv2.imshow('sobel1', sobel1)
cv2.imshow('sobel2', sobel2)
cv2.waitKey(0)
cv2.destroyAllWindows()
