import numpy as np,cv2

pts1 = np.array([(200,50,1) , (400,50,1), (400,250,1),(200,250,1)], np.float32)

theta = 30 * np.pi / 180

m = np.array([
             [np.cos(theta), -np.sin(theta), 0],
             [np.sin(theta), np.cos(theta), 0],
             [      0,      0,      1        ] ], np.float32)

delta = (pts1[2] - pts1[0]) // 2
center = pts1[0] + delta

t1 = np.eye(3, dtype = np.float32)
t2 = np.eye(3, dtype = np.float32)


t1[:2, 2] = center[:2] # 원점으로 옮기기
t2[:2, 2] = -center[:2] # 되돌아오기

# m - 회전 행렬
m2 = t1.dot(m).dot(t2)
m3  = t1.dot(m)

pts2 = cv2.gemm(pts1, m2, 1, None,1,flags=cv2.GEMM_2_T)
pts3 = cv2.gemm(pts1, m3, 1, None,1,flags=cv2.GEMM_2_T)

image = np.full((400,500,3), 255, np.uint8)
cv2.polylines(image, [np.int32(pts1[: , :2])], True, (0,255,0),2)
cv2.polylines(image, [np.int32(pts2[: , :2])], True, (255,0,0),3)
cv2.polylines(image, [np.int32(pts3[: , :2])], True, (255,0,0),3)
cv2.imshow("image", image)
cv2.waitKey(0)