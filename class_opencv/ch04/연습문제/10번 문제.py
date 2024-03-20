import numpy as np, cv2

def onMouse(event, x,y,flags, param):
    global title, image

    if event == cv2.EVENT_RBUTTONDOWN: # 우클릭 시
        pt = (x,y)
        cv2.circle(image, pt,20, 0,1) #흑백 이미지 이므로 color는 0(흑)
        cv2.imshow(title, image)
    elif event == cv2.EVENT_LBUTTONDOWN:
        pt1, pt2 = (x,y), (x+30,y+30)
        cv2.rectangle(image, pt1, pt2, 0,1)
        cv2.imshow(title, image)

title = "Draw circle and rectangle"
image = np.zeros((300,300), np.uint8) # 컬러 이미지가 아니여서 (300,300)
image[:] = 255
black = (0,0,0)

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()