import cv2

image = cv2.imread("flip_test.jpg", cv2.IMREAD_COLOR)
if image is None : raise Exception("파일 읽기 오류")

x_axis = cv2.flip(image,0)
y_axis = cv2.flip(image,1)
xy_axis = cv2.flip(image,-1)
rep_imag = cv2.repeat(image, 1,2,)
tras_image = cv2.transpose(image)

titles = ['image', 'x_axis', 'xy_axis','rep_imag' ,'tras_image']
for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)
cv2.destroyAllWindows()
