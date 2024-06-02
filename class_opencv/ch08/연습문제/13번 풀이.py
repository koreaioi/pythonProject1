import numpy as np, cv2

def onMouse(event, x,y,flags,param):
    global pt1, pt2, mouse_mode

    if event == cv2.EVENT_LBUTTONUP: # 마우스 이동이 끝나면
        pt2 = (x,y) # 최종 위치 저장
        mouse_mode = 1 # 마우스 모드 1로

        dx, dy = np.subtract(pt2,pt1).astype(float)
        angle = cv2.fastAtan2(dy,dx) # 각도 계산
        print(angle)

    elif event == cv2.EVENT_LBUTTONDOWN: # 마우스 클릭시
        pt1 = (x,y) # 처음 pt만 저장하고 마우스 모드를 2로 이동
        mouse_mode = 2

    if mouse_mode >= 2: # 마우스가 이동 중 일 때
        pt2 = (x,y)
        tmp = np.copy(image) # 임시 그림을 화면에 보여주기 위함
        cv2.line(tmp, pt1, pt2, (255,0,0), 2 ) #직 선 그리기
        cv2.imshow(title, tmp) # 실시간 반영

image = np.full((300,500,3), (255,255,255), np.uint8)
mouse_mode = 0
title = "title"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)

