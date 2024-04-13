import numpy as np,cv2

m1 = np.full((3,6),10,np.uint8)
m2 = np.full((3,6),50,np.uint8)
m_mask = np.zeros(m1.shape, np.uint8)
m_mask[ : , 3:] = 1 # 첫행~끝행, 3열~끝열을 1로 마스킹 표시

m_add1 = cv2.add(m1,m2)
m_add2 = cv2.add(m1,m2,mask=m_mask) # 마스킹 부분만 add 수행

# print(m_add1)
# print(m_add2)

m_div1 = cv2.divide(m1,m2)
# 10 / 50 은 0.2가 나와야하는데 uint8 이어서 (3,6)행렬 값이 모두 0
print(m_div1)
# 실수형으로 변환
m1 = m1.astype(np.float32) #형 변환 방법1
m2 = np.float32(m2) # 형변환 방법2 추천
m_div2 = cv2.divide(m1,m2)
print(m_div2) # 0.2 출력