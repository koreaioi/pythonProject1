import numpy as np, cv2

m1 = np.full((3,6), 10, np.uint8)
m2 = np.full((3,6), 50, np.uint8)
m_mask = np.zeros(m1.shape, np.uint8) #m1.shape -> (3,6)
m_mask[ : , 3: ] =1

m_add1 = cv2.add(m1,m2) # 행렬 덧셈
m_add2 = cv2.add(m1,m2,mask=m_mask) # 관심 영역만 덧셈 수행 mask에 있는 부분만

print(m_add1)
print(m_add2)
print(m_mask)
