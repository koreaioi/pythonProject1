import numpy as np, cv2

v1 = np.array([1,2,3], np.float32) # 실수형 1차원 리스트로 행렬생성
v2 = np.array([[1],[2],[3]], np.float32) # 2차원 리스트 3행1열 생성
v3 = np.array([[1,2,3]], np.float32) # 2차원리스트 1행 3열 생성

# exp() e의1승, e의2승, e의 3승 을 계산
v_exp = cv2.exp(v1) # 1차원 행렬의지수
m_exp1 = cv2.exp(v2)
m_exp2 = cv2.exp(v3) # 들어가있는 값은 셋 다 같음
v_log = cv2.log(v1) # 밑이 e인 로그
m_sqrt = cv2.sqrt(v2) #루트씌우기
m_pow = cv2.pow(v3, 3) # 1의 3승, 2의 3승, 3의 3승 -> 각 행렬의 3승

print(v_log)
print(m_sqrt)
print(m_pow)
