import numpy as np, cv2

def onMouse(event, x,y, flags, param):
    global image, title,r,thick_line

    if event == cv2.EVENT_RBUTTONDOWN:
        pt = (x,y)
        cv2.circle(image, pt, r, 0,1)
        cv2.imshow(title,image)
    elif event == cv2.EVENT_LBUTTONDOWN:
        pt1,pt2 = (x,y),(x+30,y+30)
        cv2.rectangle(image, pt1,pt2,0,thick_line)
        cv2.imshow(title,image)

        

def onChange1(value):
    global image, title, thick_line
    thick_line = value
    cv2.setTrackbarPos(t_bar2, title, r)
    cv2.imshow(title, image)


def onChange2(value):
    global image, title, r
    r = value
    cv2.setTrackbarPos(t_bar2, title, r)
    cv2.imshow(title, image)




image = np.ones((1000,1000), np.uint8) * 255
title="title"
t_bar1 = "tbar1"
t_bar2 = "tbar2"
thick_line = 1
r = 20

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.createTrackbar(t_bar1, title, thick_line,10,onChange1)
cv2.createTrackbar(t_bar2, title, r,50,onChange2)
cv2.waitKey(0)

