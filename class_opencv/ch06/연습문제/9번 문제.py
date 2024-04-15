import numpy as np, cv2

def bar(value):
    global alpha, beta, image1, image2, image

    alpha = cv2.getTrackbarPos("image1", title)/100
    beta = cv2.getTrackbarPos("image2", title)/100

    image3 = cv2.addWeighted(image1, alpha, image2, beta,0)
    image[:h, w:w*2] = image3

    cv2.imshow("title", image)


image1 = cv2.imread("add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("add2.jpg", cv2.IMREAD_GRAYSCALE)
alpha, beta = 0.5, 0.5
image3 = cv2.addWeighted(image1, alpha, image2, beta,0)
title = "title"

h,w = image1.shape
print(h , w)

image = np.zeros((h,w*3), np.uint8)

image[:h, :w] = image1
image[:h, w:w*2] = image3
image[:h , w*2:] = image2

cv2.imshow(title, image)

cv2.createTrackbar("image1", title, 50, 100, bar)
cv2.createTrackbar("image2", title, 50, 100, bar)

cv2.waitKey(0)