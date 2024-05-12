import numpy as np, cv2
from Common.filters import filter

image = cv2.imread("cannay_tset.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")

# 샤프닝 마스크
s_mask = np.array([[0,-1,0],
                 [-1,5,-1],
                 [0,-1,0]], np.float32)

b,g,r = cv2.split(image)
# 평균 필터링으로 블러링 수행
b = cv2.medianBlur(b, 3)
g = cv2.medianBlur(g, 3)
r = cv2.medianBlur(r, 3)
# 샤프닝 수행하기
b = filter(b, s_mask)
g = filter(g, s_mask)
r = filter(r, s_mask)
# 분리된 채널 합치기
image1 = cv2.merge([b,g,r])
cv2.imshow("image",image) # 원본
cv2.imshow("image1", image1) # 변형
cv2.waitKey(0)