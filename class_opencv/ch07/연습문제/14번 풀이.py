import numpy as np, cv2

th1 = 50
th2 = 100

def onTrackbar1(value):
    th1 = cv2.getTrackbarPos('th1', 'window')
    canny = cv2.Canny(image, th1, th2) # Canny한 값(이미지)를 다시 cv.imshow
    cv2.imshow("window", canny)

def onTrackbar2(value):
    th2 = cv2.getTrackbarPos('th2', 'window')
    canny = cv2.Canny(image, th1, th2) # Canny한 값(이미지)를 다시 cv.imshow
    cv2.imshow("window", canny)

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

cv2.imshow("window", image)
cv2.createTrackbar("th1", "window",th1,255, onTrackbar1)
cv2.createTrackbar("th1", "window",th2,255, onTrackbar2)
cv2.waitKey(0)