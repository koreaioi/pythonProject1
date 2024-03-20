import numpy as np, cv2

image = np.zeros((300,400), np.uint8)
image[:]=100

image2 = np.zeros((100,100), np.uint8)
image2[:]=0

title1 = 'Window1'
title2 = 'Window2'
cv2.namedWindow(title1, cv2.WINDOW_NORMAL) #이미지가 기존의 이미지 창 크기게 맞게 조절됨, 대신 윈도우 창을 조절할 수 없다.
cv2.moveWindow(title1, 100,200)
cv2.imshow(title1, image)

# cv2.namedWindow(title2, cv2.WINDOW_AUTOSIZE) #윈도우 창이 이미지에 맞게 조절되는 대신 윈도우 창 조절 x
# cv2.moveWindow(title2, 100,200)
# cv2.imshow(title2, image2)


cv2.waitKey(0)
cv2.destroyAllWindows()