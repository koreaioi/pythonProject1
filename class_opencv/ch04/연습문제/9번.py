import numpy as np,cv2

image = np.ones((600,400,3), np.uint8) * 255

cv2.rectangle(image, (100,100,200,300),(0,0,255),-1)
cv2.imshow("title", image)
cv2.waitKey(0)



# import numpy as np, cv2
#
# image1 = np.zeros((600,400,3), np.uint8)+255
#
# title1 = "title1"
# pt1, pt2 =(100,100) , (300,400)
# red = (0,0,255)
#
# cv2.rectangle(image1, pt1, pt2, red,cv2.FILLED)
#
# cv2.imshow(title1,image1)
# cv2.waitKey(0)






# import numpy as np,cv2
#
# title = 'Window'
#
# image = np.zeros((600,400,3), np.uint8)
# image[:] = (255,255,255) # 이미지(도화지)를 흰색으로 지정
#
# pt1, pt2 = (100,100), (300,400)
# red = (0,0,255) # 빨간색 미리 지정
#
# cv2.rectangle(image, pt1,pt2, red,cv2.FILLED)
# # 빨간색을 채울 때는, 굵기를 생략하고 바로 cv2.FillED
#
# cv2.namedWindow(title)
# cv2.resizeWindow(title, 400,600) # 600행 400열 - 윈도우 창은 반대이다.
# cv2.imshow(title, image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()