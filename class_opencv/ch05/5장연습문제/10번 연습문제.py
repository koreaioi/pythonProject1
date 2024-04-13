import numpy as np, cv2
from Common.utils import put_string

capture = cv2.VideoCapture(0)
if not capture.isOpened(): raise Exception("카메라 연결 안됨")

while True:
    ret, frame = capture.read()
    if not ret : break

    x,y,w,h = (200,100, 200,100)
    cv2.rectangle(frame, (x,y,w,h), (0,0,255),2)
    tmp = frame[y:y+h, x:x+w]
    
    # x2,y2 = 400,200
    # cv2.rectangle(frame, (x,y),(x2,y2), (0,0,255),2)
    # tmp = frame[y:y+100, x:x+200]

    # 함수이용
    average1 = tuple(map(int, cv2.mean(tmp)))

    # 행렬 순회
    value = np.array([0,0,0],np.uint8)
    for row in tmp:
        for pixel in row:
            value += pixel
    average2 = (value / (w*h)).astype(int)

    put_string(frame, "average1 : " , (10,30), average1[:-1])
    put_string(frame, "average2 : " , (50,70), average2)

    if cv2.waitKey(30) >= 0 : break
    cv2.imshow("ex10", frame)
capture.release()