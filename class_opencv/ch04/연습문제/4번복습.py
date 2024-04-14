import numpy as np, cv2

image = np.full((300,400), 100,np.uint8)

title = "title"

cv2.imshow(title, image)
cv2.resizeWindow(title, 600,500)
cv2.waitKey(0)
