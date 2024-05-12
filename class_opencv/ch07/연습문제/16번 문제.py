import numpy as np
import cv2

def morphology(img, operation, mask=None):
    dst = np.zeros(img.shape, np.uint8)
    if mask is None:
        mask = np.ones((3, 3), np.uint8)
    ycenter, xcenter = np.divmod(mask.shape[:2], 2)[0]

    for i in range(ycenter, img.shape[0] - ycenter):  # 입력 행렬 반복 순회
        for j in range(xcenter, img.shape[1] - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1  # 마스크 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1  # 마스크 너비 범위
            roi = img[y1:y2, x1:x2]  # 마스크 영역
            temp = cv2.bitwise_and(roi, mask)
            if operation == 'erode':
                cnt = cv2.countNonZero(temp)  # 일치한 화소수 계산
                dst[i, j] = 255 if (cnt == cv2.countNonZero(mask)) else 0  # 출력 화소에 저장
            elif operation == 'dilate':
                dst[i, j] = 0 if (cv2.countNonZero(temp) == 0) else 255  # 출력 화소에 저장
            else:
                raise ValueError("Operation must be either 'erode' or 'dilate'.")
    return dst

image = cv2.imread('morph.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일읽기 오류")

mask = np.ones((3, 3), np.uint8)

image1 = morphology(image, 'erode', mask=mask)
image2 = morphology(image, 'dilate', mask=mask)

cv2.imshow('image1', image1)
cv2.imshow('image2', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
