import numpy as np
import cv2


ch0 = np.zeros((2,4), np.uint8) +10
ch1 = np.ones((2,4), np.uint8) * 20
ch2 = np.full((2,4), 30,np.uint8)

list_bgr = [ch0,ch1,ch2]
merge_bgr = cv2.merge(list_bgr)
split_bgr = cv2.split(merge_bgr)

print("[ch0] = \n%s" % ch0)
print("[ch1] = \n%s" % ch1)
print("[ch2] = \n%s" % ch2)

print("merge_bar = \n%s" % merge_bgr)
print(split_bgr)

print("split_bar[0] = \n%s" % split_bgr[0])
print("split_bar[1] = \n%s" % split_bgr[1])
print("split_bar[2] = \n%s" % split_bgr[2])