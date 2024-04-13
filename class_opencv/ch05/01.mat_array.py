import cv2

image = cv2.imread("bit_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")

x_axis = cv2.flip(image, 0) # x축을 기준으로 뒤집기 - 상하
y_axis = cv2.flip(image, 1) # y축을 기준으로 뒤집기 - 좌우
xy_axis = cv2.flip(image,-1) # 상하좌우

rep_image = cv2.repeat(image, 2,3) # 배열이랑 똑같음 2,3 크기의 배열이랑 같음
tran_image = cv2.transpose(image) # 행렬을 전치한다.


# cv2.imshow("image", image)
# cv2.imshow("x_axis", x_axis)
# cv2.imshow("y_axis",y_axis)
cv2.imshow("xy_axis",rep_image)


cv2.waitKey(0)
cv2.destroyAllwindows()