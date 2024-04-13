import numpy as np, cv2


image = np.ones((400,600,3), np.uint8) * 255


cx, cy = image.shape[1]//2, image.shape[0]//2
cr = image.shape[0]//4
new_r = cr//2

left_x, left_y = cx , cy - new_r
right_x, right_y = cx, cy + new_r

cv2.ellipse(image, (cx,cy),(cr,cr),0,90,270,(0,0,255),-1)
cv2.ellipse(image, (cx,cy),(cr,cr),0,270,450,(255,0,0),-1)

cv2.ellipse(image, (left_x,left_y),(new_r,new_r),0,90,270,(255,0,0),-1)
cv2.ellipse(image, (right_x,right_y),(new_r,new_r),0,270,450,(0,0,255),-1)

title = "title"

cv2.imshow(title, image)
cv2.waitKey(0)
