import numpy as np
import cv2

orange, blue, white = (0,165,255),(255,0,0),(255,255,255)
image = np.full((300,700,3),white, np.uint8)

pt1,pt2 = (180,150),(550,150) # 타원 중심
size = (120,60) #장축, 단축

cv2.circle(image, pt1, 1,0,2) # 타원 중심 표시 용도
cv2.circle(image, pt2, 1,0,2) # 타원 중심 표시 용도

#cv2.ellips("그림판", "중심점"(값 두개), "장축, 단축(x,y)",
#                   타원 전체 회전 각도 , 그리기 시작하는 각도, 그림 마무리 각도, 색깔, 굵기")
# 타원 그림을 먼저 그린 다음에 타원 전체를 회전하는 게 생각하기 쉬울 듯
cv2.ellipse(image, pt1,size,0,0,360,blue,1)
cv2.ellipse(image, pt2,size,90,0,360,blue,1)
cv2.ellipse(image, pt1,size,0,30,270,orange,4)
cv2.ellipse(image, pt2,size,90,-45,90,orange,4)

cv2.imshow("문자열",image)
cv2.waitKey(0)
cv2.destroyAllWindows()