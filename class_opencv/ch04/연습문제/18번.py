import numpy as np
import cv2

red, blue = (0,0,255) ,(255,0,0) # B G R
white, black = (255,255,255), (0,0,0)

image = np.full((400,600,3), white,np.uint8)

center = (image.shape[1]//2 , image.shape[0]//2) # 영상 중심의 좌표
r = image.shape[0]//4 # 반지름은 높이의 1/4
small_center1 = (center[0] - r//2, center[1])
small_center2 = (center[0] + r//2, center[1])

bigsize =(r,r)
smallsize = (r//2, r//2)
print(r)

cv2.ellipse(image, center,bigsize,0,180,360,red,-1)
cv2.ellipse(image, center,bigsize,0,0,180,blue,-1)
cv2.ellipse(image, small_center1,smallsize,0,0,180,red,-1)
cv2.ellipse(image, small_center2,smallsize,0,180,360,blue,-1)

cv2.imshow('Draw Circle',image)
cv2.waitKey(0)


