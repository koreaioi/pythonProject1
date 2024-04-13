import numpy as np

n = np.array([10,20,30,40,50,60,70,80,90,100], np.float32)

s = sum(n)
m = s/len(n)

print("합: {:.2f}".format(s))
print("평균: {:.2f}".format(m))