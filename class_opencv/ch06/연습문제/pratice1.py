import numpy as np, cv2

image1 = cv2.imread("bright.jpg", cv2.IMREAD_GRAYSCALE)

h,w = image1.shape
print(h,w)

image = np.zeros((h,w*3), np.uint8)

image[:, :w] = image1
image[:, w:w*2] = image1
image[:, w*2:] = image1

cv2.imshow("title", image)
cv2.waitKey(0)