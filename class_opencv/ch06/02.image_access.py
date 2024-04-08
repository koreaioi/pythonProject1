import numpy as np,cv2

def pixel_access5(image):
    image = 256 - image
    return image


image = cv2.imread('bright.jpg', cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상 이미지 읽기 오류")

image2 = pixel_access5(image)

cv2.imshow("image1", image)
cv2.imshow("image2", image2)

cv2.waitKey(0)
