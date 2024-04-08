import numpy as np, cv2

title1 = "title1"


mat = np.ones((300,400),np.uint8) * 100


cv2.namedWindow(title1, cv2.WINDOW_NORMAL)
cv2.resizeWindow(title1, (600,500))
cv2.imshow(title1, mat)

cv2.waitKey(0)

