import numpy as np
import cv2

def onChange(value):
    global image, title

    add_value = value - int(image[0][0])
    print("추가 화소값:", add_value)
    image[:] = image + add_value
    cv2.imshow(title, image)

# 화면에서 좌클릭 - 색깔+10, 우클릭: 색깔-10
def onMouse(event, x, y, flgas, param):
    global image, bar_name

    #add_value는 10
    if event == cv2.EVENT_RBUTTONDOWN: #마우스 우클릭 버튼
        if (image[0][0] < 246): image[:] = image + 10;
        cv2.setTrackbarPos(bar_name, title, image[0][0]) # 트랙바에 표시되는 값도 갱신
    elif event == cv2.EVENT_LBUTTONDOWN:
        if(image[0][0] >= 10):
            image[:] = image - 10
        cv2.setTrackbarPos(bar_name, title, image[0][0]) # 트랙바에 표시되는 값도 갱신
        cv2.imshow(title, image),




image = np.zeros((300,500), np.uint8)
title = "Trackbar & Mouse Event"
bar_name = 'Brightness'
cv2.imshow(title, image)

cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
