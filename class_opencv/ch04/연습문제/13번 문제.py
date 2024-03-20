import cv2

image = cv2.imread('color.jpg') # color.jpg 읽어오기
if image is None : raise Exception("이미지 읽기 에러") # 예외처리

params_jpg = [cv2.IMWRITE_JPEG_QUALITY, 100] # JPB 압축 설정 가장 높은값 100 (default - 95)
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9] # PNG 압축 설정 가장 높은 값 - 9 (default - 3)

cv2.imwrite("test.jpg",image, params_jpg)
cv2.imwrite("test.png",image, params_png)