import numpy as np, cv2


image1 = cv2.imread("add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("add2.jpg", cv2.IMREAD_GRAYSCALE)

alpha, beta = 0.5, 0.5
image3 = cv2.addWeighted(image1, alpha, image2, beta,0)

h,w = image1.shape
print(h , w)

image = np.zeros((h,w*3), np.uint8)

image[:h, :w] = image1
image[:h, w:w*2] = image3
image[:h , w*2:] = image2

cv2.imshow("image", image)
cv2.waitKey(0)