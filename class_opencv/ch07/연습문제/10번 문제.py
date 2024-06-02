import numpy as np, cv2
from Common.filters import filter

image = cv2.imread("cannay_tset.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")

# 샤프닝 마스크 - 가운데만 강조
s_mask = np.array([[0,-1,0],
                 [-1,5,-1],
                 [0,-1,0]], np.float32)

# 블러링 마스크
b_mask = np.array([[1/9,1/9,1/9],
                   [1/9,1/9,1/9],
                   [1/9,1/9,1/9]],np.float32)


b,g,r = cv2.split(image)

dst1 = cv2.merge([filter(b, s_mask), filter(g,s_mask),filter(r,s_mask)])
dst2 = cv2.merge([filter(b, b_mask), filter(g,b_mask),filter(r,b_mask)])
dst3 = cv2.filter2D(image, cv2.CV_8U,b_mask) # fitler2D에 블러 마스크
dst4 = cv2.filter2D(image, cv2.CV_8U,s_mask) # filter2D에 샤프닝 마스크

cv2.imshow("image", "image")
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.imshow("dst4", dst4)


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