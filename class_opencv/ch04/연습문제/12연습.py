import numpy as np, cv2

def onChange(value):
    global image
    #
    # add_value = value - int(image[0][0])
    # image = image + add_value
    image[:] = value
    cv2.imshow(title, image)

image = np.zeros((300,500), np.uint8)

title, bar_name = "ex12", "br"
cv2.imshow(title, image)
cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)

while(True):
    key = cv2.waitKeyEx(10)
    if key == 0x250000:
        value = cv2.getTrackbarPos(bar_name, title)
        cv2.setTrackbarPos(bar_name,title, value-1)
    elif key == 0x270000:
        value = cv2.getTrackbarPos(bar_name, title)
        cv2.setTrackbarPos(bar_name, title,value+1)
    elif key == 27 : break