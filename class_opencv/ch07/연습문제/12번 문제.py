import numpy as np
import cv2


# 이미지 load
image = cv2.imread("cannay_tset.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상 파일 읽기 오류")

# 2차 미분 마스크를 초기화
mask1 = np.array([[0, 1, 0],
                           [1, -4, 1],
                           [0, 1, 0]])

mask2 = np.array([[0, -1, 0],
                           [-1, 4, -1],
                           [0, -1, 0]])

mask3 = np.array([[-1,-1,-1],
                           [-1, 8, -1],
                           [-1,-1,-1]])

mask4 = np.array([[1,1,1],
                           [1, -8, 1],
                           [1,1,1]])

# 이미지에 라플라시안 마스크를 적용합니다.
# -1을 지정하면 src와 같은 타입의 dst 영상을 생성한다.
dst1 = cv2.filter2D(image, -1, mask1)
dst2 = cv2.filter2D(image, -1, mask2)
dst3 = cv2.filter2D(image, -1, mask3)
dst4 = cv2.filter2D(image, -1, mask4)

# 결과를 확인하기 위해 이미지를 출력합니다.
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()