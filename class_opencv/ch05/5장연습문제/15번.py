import numpy as np, cv2

pts1 = np.array([(200,50,10),(400,50,1),
                 (400,250,1), (200,250, 1)], np.float32)

theta = 45 * np.pi / 180 # 회전각
m = np.array([ [np.cos(theta), -np.sin(theta), 0],
               [np.sin(theta), np.cos(theta), 0],
               [0,0,1]
], np.float32)

delta = (pts1[2] - pts1[0])//2
center = pts1[0] + delta # 중심좌표

t1 = np.eye(3, dtype=np.float32)
t2 = np.eye(3, dtype=np.float32)




# pts2 = cv2.genm(pts1, m2,1,None,1,flags = cv2.GEMM_2_T)