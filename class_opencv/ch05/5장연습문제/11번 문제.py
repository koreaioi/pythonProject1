import numpy as np, cv2

capture = cv2.VideoCapture(0)
if not capture.isOpened() : raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

x,y,w,h = (30,30,320,240)
# blue = np.full((360,640,3), (255,0,0),np.uint8)
mask = np.full((360,640), 0,np.uint8)
cv2.rectangle(mask, (x,y,w,h),255,-1)


while True:
    ret, frame = capture.read()
    if not ret : break
    # cv2.rectangle(frame, (x,y,w,h), (0,0,255),2) # 빨간색 그려주기
    print(frame.shape)
    inner = cv2.bitwise_and(frame,frame,mask=mask)
    # outter = cv2.bitwise_and(blue,blue, mask =mask) 핑크색 테두리생김

    if cv2.waitKey(30) >= 0:break
    cv2.imshow("ex11", inner)
    # cv2.resizeWindow("ex11",400,300)

capture.release()

