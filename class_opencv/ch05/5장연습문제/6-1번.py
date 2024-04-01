import numpy as np

# np.array를 사용해야 한다.

m1 = np.array([1,2,3,1,2,3])
m2 = np.array([3,3,4,2,2,3])

# m1 = [1,2,3,1,2,3]
# m2 = [3,3,4,2,2,3]
# m3 = np.add(m1,m2)
# m4 = np.subtract(m1,m2)

m3 = m1 + m2
m4 = m1 - m2

print(m3)
print(m4)