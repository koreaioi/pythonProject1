import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global pt1, pt2, mouse_mode

    if event == cv2.EVENT_LBUTTONUP:  # 마우스 이동이 끝나면
        pt2 = (x, y)  # 최종 위치 저장
        mouse_mode = 1  # 마우스 모드 1로

        # 차분
        dx, dy = np.subtract(pt2, pt1).astype(float)
        angle = cv2.fastAtan2(dy,dx) # 각도 계산
        # pt1을 중심으로 angle만큼 전환하는데 역변환이라 -가 붙음
        # pt1 매개변수 위치는 회전 중심으로할 좌표를 넣는다.
        # angle은 반시계 방향으로 회전하고 시계방향은 음수로 표현한다.
        rot_mat = cv2.getRotationMatrix2D(pt1, -angle, 1)
        dst = cv2.warpAffine(image, rot_mat, image.shape[::-1], cv2.INTER_LINEAR)
        cv2.imshow(title, dst)

    elif event == cv2.EVENT_LBUTTONDOWN:  # 마우스 클릭시
        pt1 = (x, y)  # 처음 pt만 저장하고 마우스 모드를 2로 이동
        mouse_mode = 2

    if mouse_mode >= 2:  # 마우스가 이동 중 일 때
        pt2 = (x, y)
        tmp = np.copy(image)  # 임시 그림을 화면에 보여주기 위함
        cv2.line(tmp, pt1, pt2, (255, 0, 0), 2)  # 직 선 그리기
        cv2.imshow(title, tmp)  # 실시간 반영


image = cv2.imread('affine.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일을 읽기 에러")

mouse_mode = 0
title = "title"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
