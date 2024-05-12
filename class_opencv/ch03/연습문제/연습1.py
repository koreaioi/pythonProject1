import numpy as np,cv2

image = cv2.imread("bit_test.jpg", cv2.IMREAD_COLOR)
if image is None : raise Exception("영상 읽기 오류")

mask = np.zeros(image.shape[:2], np.uint8)
cv2.ellipse(mask, (190,170),(80,100), 0,0,360,255,-1)

dst = cv2.bitwise_and(image, image, mask =mask)
cv2.imshow("title1",image)
cv2.imshow("title",dst)
cv2.waitKey(0)