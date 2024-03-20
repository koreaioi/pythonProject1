import numpy as np, cv2


def onMouse(event, x, y, flags, param):
    global title, image

    if event == cv2.EVENT_RBUTTONDOWN:  # 우클릭 시
        pt = (x, y)
        cv2.circle(image, pt, radius, 0, line_thick)  # 흑백 이미지 이므로 color는 0(흑)
        cv2.imshow(title, image)
    elif event == cv2.EVENT_LBUTTONDOWN:
        pt1, pt2 = (x, y), (x + 30, y + 30)
        cv2.rectangle(image, pt1, pt2, 0, line_thick)
        cv2.imshow(title, image)


def onChange1(value):
    global image, title, line_thick

    line_thick = value
    cv2.setTrackbarPos(track_bar1, title, line_thick)
    cv2.imshow(title, image)

def onChange2(value):
    global image, title, radius

    radius = value
    cv2.setTrackbarPos(track_bar2, title, radius)
    cv2.imshow(title, image)


title = "Draw circle and rectangle"
track_bar1 = "line"  # 직선 트랙바
track_bar2 = "radius"  # 원 반지름 트랙바

image = np.zeros((300, 300), np.uint8)  # 컬러 이미지가 아니여서 (300,300)
image[:] = 255
line_thick = 1
radius = 20
black = (0, 0, 0)

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.createTrackbar(track_bar1, title, line_thick, 10, onChange1)
cv2.createTrackbar(track_bar2, title, radius, 50, onChange2)
cv2.waitKey(0)
cv2.destroyAllWindows()
