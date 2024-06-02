import cv2
from Common.filters import differential

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

# 로버츠 마크스
data1 = [-1,0,0,
          0,1,0,
          0,0,0,]
data2 = [0,0,-1,
         0,1,0,
         0,0,0]

# 프리윗 마스크
data3 = [-1,-1,-1,
         0,0,0,
         1,1,1]

data4 = [-1,0,1,
         -1,0,1,
         -1,0,1]

# 소벨 마스크

data5 = [-1,0,1,
         -2,0,2,
         -1,0,1]

data6 = [-1,-2,-1,
          0, 0, 0,
          1 ,2, 1]

dst1, _, _ = differential(image, data1, data2)
dst2, _, _ = differential(image, data3, data4)
dst3, _, _ = differential(image, data5, data6)

cv2.imshow("image", image)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)