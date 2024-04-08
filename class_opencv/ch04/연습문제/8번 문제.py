import numpy as np, cv2

image1 = np.zeros((200,300), np.uint8)
image2 = np.zeros((200,300), np.uint8)

title1 = "title1"
title2 = "title2"

cv2.imshow(title1, image1)
cv2.imshow(title2, image2)

cv2.moveWindow(title1, 0,0)
cv2.moveWindow(title2, 300,200)

cv2.waitKey(0)