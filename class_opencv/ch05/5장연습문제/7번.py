import numpy as np, cv2

logo = cv2.imread("logo.jpg", cv2.IMREAD_COLOR)
if logo is None : raise Exception("영상 파일 읽기 오류")

blue, green, red = cv2.split(logo)
# 3개의 채널을 각각 하나씪 분리 -> blue를 출력시 3개의 채널이 없으므로 흑백으로 나오게된다.
# 3개의 채널로 합쳐서 컬러색으로 만들어줌

zero = np.zeros((blue.shape), np.uint8)

blue = cv2.merge([blue,zero,zero])
green = cv2.merge([zero,green,zero])
red = cv2.merge([zero,zero,red])

# print(blue.shape)
# print(logo.shape)


# cv2.imshow("logo", logo)
cv2.imshow("blue", blue)
cv2.imshow("green", green)
cv2.imshow("red", red)

cv2.waitKey(0)
cv2.destroyAllWindows()
