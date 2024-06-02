import cv2

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

gaus = cv2.GaussianBlur(image ,(9,9), 0,0)

gaus1 = cv2.GaussianBlur(image, (3,3), 0)
gaus2 = cv2.GaussianBlur(image, (9,9), 0)
dst1 = gaus1 - gaus2 # DoG: 가우시안1 - 가우시안2
dst2 = cv2.Laplacian(gaus, cv2.CV_16S) # LoG: 가우시안에 라플라시안

cv2.imshow("image", image)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2.astype("uint8"))
cv2.waitKey(0)