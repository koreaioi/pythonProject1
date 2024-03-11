import numpy as np
import cv2

def onMouse(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("마우스 왼쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("마우스 오른쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONUP:
        print("마우스 오른쪽 버튼 떼기")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("마우스 왼쪽 버튼 더블클릭")


image = np.full((200,300), 255, np.uint8)
#크기 세로 200, 가로 300 인 이미지, 색은 255(흰색)

title1, title2 = "Mouse Event1", "Mouse Event2",

cv2.imshow(title1, image)
cv2.imshow(title2, image)

cv2.setMouseCallback(title1,onMouse)
#title1 window에서만 콜백이 이루어진다.
#title2 window에서는 마우스를 눌러도 아무런 반응 X
cv2.waitKey(0)
cv2.destroyAllWindows()

