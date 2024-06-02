import numpy as np, cv2


def onMouse(event, x, y, flags, param):
    global pt1, pt2, mouse_mode

    if event == cv2.EVENT_LBUTTONUP:  # 마우스 이동이 끝나면
        pt2 = (x, y)  # 최종 위치 저장
        mouse_mode = 1  # 마우스 모드 1로

        # 차분
        dx, dy = np.subtract(pt2, pt1).astype(float)
        dst = translate(image, (dx, dy)) # 평행이동을 위해 추가한 내용
        cv2.imshow(title, dst) # 이동 후 보여주기

    elif event == cv2.EVENT_LBUTTONDOWN:  # 마우스 클릭시
        pt1 = (x, y)  # 처음 pt만 저장하고 마우스 모드를 2로 이동
        mouse_mode = 2

    if mouse_mode >= 2:  # 마우스가 이동 중 일 때
        pt2 = (x, y)
        tmp = np.copy(image)  # 임시 그림을 화면에 보여주기 위함
        cv2.line(tmp, pt1, pt2, (255, 0, 0), 2)  # 직 선 그리기
        cv2.imshow(title, tmp)  # 실시간 반영


def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x, y = np.subtract((j, i), pt)
            if contain((y, x), img.shape):
                dst[i, j] = img[y, x]
    return dst

def contain(p, shape):  # 영역을 벗어났는지 확인
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]


image = cv2.imread('affine.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일을 읽기 에러")

mouse_mode = 0
title = "title"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
