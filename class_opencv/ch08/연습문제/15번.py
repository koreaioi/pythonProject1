import numpy as np, cv2
from Common.interpolation import rotate_pt

def calc_d(pts):
    d1 = np.subtract(pts[1], pts[0]).astype(float)        # 두 좌표간 차분 계산

    return d1  # 두 각도 간의 차분

def draw_point(x, y, color):
    pts.append([x,y])
    print("좌표:", len(pts), [x,y])
    cv2.circle(tmp, (x, y), 2, color, 2)  # 중심 좌표 표시
    cv2.imshow("image", tmp)

def onMouse(event, x, y, flags, param):
    global tmp, pts
    if (event == cv2.EVENT_LBUTTONDOWN and len(pts) == 0):  draw_point(x, y, (0,0,255))
    if (event == cv2.EVENT_RBUTTONDOWN and len(pts) == 1):
        draw_point(x, y, (0,255, 0))

    if len(pts) == 2:
        dxy = calc_d(pts)  # 회전각 계산
        print("차분x : %3.2f" % dxy[0])
        print("차분y : %3.2f" % dxy[1])

        M = np.float32([[1, 0, dxy[0]], [0, 1, dxy[1]]])
        # 평행이동하는 opencv함수 warpAffine
        dst = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
        cv2.imshow("image", dst)


        tmp = np.copy(image)                    # 임시 행렬 초기화
        pts = []

image = cv2.imread('affine.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일을 읽기 에러")
tmp = np.copy(image)
pts = []

cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse, 0)
cv2.waitKey(0)


