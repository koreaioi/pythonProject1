import numpy as np
import cv2


ch0 = np.zeros((2,4), np.uint8) +10
ch1 = np.ones((2,4), np.uint8) *20
ch2 = np.full((2,4),30, np.uint8) # 2,4 행렬을 모두(full) 30으로 초기화

# print("[ch0] = \n%s" % ch0)
# print("[ch1] = \n%s" % ch1)
# print("[ch2] = \n%s" % ch2)

list_bgr = [ch0,ch1,ch2] # 이상태가 이미 스플릿인거임

merge_bar = cv2.merge(list_bgr)
split_bar = cv2.split(merge_bar)

# print(merge_bar.shape) # merge한건 2, 4, 3이된다.
print(np.array(split_bar)) # split_bar를 np 배열로 만들기
print(np.array(split_bar).shape) # np 배열은 다름