import numpy as np,cv2

data = [1,2,3,4,5,   6,7,8,9,10,11,12]
# 맨 마지막 인자가 채널 개수이므로 3으로 수정.
# 2 * 2 * 3 = 12 (원소 개수)
m1 = np.array(data).reshape(2,2,3)

b,g,r = cv2.split(m1)

print(b)
print(g)
print(r)