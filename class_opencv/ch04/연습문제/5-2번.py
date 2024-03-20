import numpy as np, cv2

image =np.zeros((400,600,3), np.uint8)
image[:] = (255,255,255)
pt1, pt2 = (50,100), (200,300) # 좌측 상단 좌표 (50,100), 우측 하단 좌표 (200,300)

cv2.line(image, pt1,pt2,(0,255,0),5)
cv2.rectangle(image, pt2, (300,400), (0,0,255), -1 , cv2.LINE_4,0)

cv2.imshow("Line & Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()