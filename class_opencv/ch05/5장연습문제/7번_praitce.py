import numpy as np, cv2

logo = cv2.imread("logo.jpg", cv2.IMREAD_COLOR)
if logo is None: raise Exception("영상 파일 읽기 오류")

blue, green, red = cv2.split(logo)

zeros = np.zeros((blue.shape), np.uint8)
blueimg = cv2.merge([blue, zeros, zeros])
greenimg = cv2.merge([zeros, green, zeros])
redimg = cv2.merge([zeros, zeros, red])


cv2.imshow("blue", blueimg)
cv2.imshow("green", greenimg)
cv2.imshow("red", redimg)
cv2.waitKey(0)