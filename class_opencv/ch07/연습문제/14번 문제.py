import numpy as np, cv2

def onChange(value):
    global image, title
    image[:] = value
    cv2.imshow(title, image)


# image = np.zeros((300, 500), np.uint8)
image = cv2.imread("cannay_tset.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

title = 'title'
t_bar1="t_bar1"
cv2.imshow(title, image)
cv2.createTrackbar(t_bar1, title, image[0][0], 255, onChange)
while True:
    key = cv2.waitKeyEx(100)
    if key == 27: break

    if key == 0x250000:
        value = cv2.getTrackbarPos(t_bar1, title)
        cv2.setTrackbarPos(t_bar1, title, value - 1)
    elif key == 0x270000:
        value = cv2.getTrackbarPos(t_bar1, title)
        cv2.setTrackbarPos(t_bar1, title, value + 1)

    image[:] = cv2.getTrackbarPos(t_bar1, title)
    cv2.imshow(title, image)

cv2.destroyAllWindows()