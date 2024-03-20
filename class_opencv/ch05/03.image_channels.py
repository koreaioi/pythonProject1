import cv2

image = cv2.imread("color.jpg", cv2.IMREAD_COLOR)
if image is None : raise Exception("영상 파일 읽기 오류")
if image.ndim != 3: raise Exception("컬러 영상 아님")

bgr = cv2.split(image) # 이미지를 채널 분리, splite 으로 분리시 B, G, R 역순으로 저장됨

print("bgr 자료형: ", type(bgr), type(bgr[0]), type(bgr[0][0][0]))
print("bgr 원소 개수: ", len(bgr), len(bgr[0]))
# 리스트에는 원소 개수가 3개 ,리스트 안에 있는 넘파이 배열은 360개, 배열 안에는 int
print(bgr[0].shape)
print(len(bgr[0]), len(bgr[0][0]))

cv2.imshow("image", image)
cv2.imshow("Blue Channel", bgr[0])
cv2.imshow("Green Channel", bgr[1])
cv2.imshow("Red Channel", bgr[2])
cv2.waitKey(0)