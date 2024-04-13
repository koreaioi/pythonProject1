import numpy as np, cv2

image = cv2.imread("bit_test.jpg", cv2.IMREAD_COLOR)

if image is None : raise Exception("영상 파일 읽기 오류")

mask = np.zeros(image.shape[:2], np.uint8)
center = (190,200)

cv2.ellipse(mask,center, (80,120),0, 0, 360, 255,-1)
# mask = mask 
dst = cv2.bitwise_and(image, image, mask = mask)

# cv2.imshow("image", image)
cv2.imshow("mask" ,mask)
cv2.imshow("dst",dst)
cv2.waitKey(0)
