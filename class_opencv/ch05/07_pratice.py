import numpy as np,cv2
# 0 - 검정색
# 255(1) - 흰색

image1 = np.zeros((600,300), np.uint8) # 기본값 0이므로 배경은 검정
image2 = image1.copy()

x,y = image1.shape[:2] # image.shape = (300,300)
print(image1.shape)
cx, cy = (y//2),(x//2) # 중심 좌표
# circle(도화지, 센터좌표, 반지름, 색, 색범위)
cv2.circle(image1, (cx, cy), 100, 255, -1)
cv2.rectangle(image2, (0,0,cx,x), 255,-1)

cv2.imshow("image1" ,image1)
# cv2.imshow("image2" ,image2)

image3 = cv2.bitwise_and(image1, image2)
image4 = cv2.bitwise_or(image1, image2)
image5 = cv2.bitwise_xor(image1,image2)
image6 = cv2.bitwise_not(image1)

# cv2.imshow("image3", image3)
# cv2.imshow("image4", image4)
# cv2.imshow("image5", image5)
# cv2.imshow("image6", image6)

cv2.waitKey(0)
cv2.destroyAllWindows()
