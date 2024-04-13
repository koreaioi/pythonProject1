import cv2

image = cv2.imread("color.jpg", cv2.IMREAD_COLOR)
if image is None : raise Exception("영상 파일 읽기 오류")
if image.ndim !=3 : raise Exception("컬러 영상 아님")

split = cv2.split(image) # image를 스플릿하면 이미지이다.

print(split[0].shape) # (360,480)
print(type(split), type(split[0]), type(split[0][0][0])) #튜플, 넘파이배열, int자료형
print(len(split)) # 3개

# cv2.imshow("image", image)
# cv2.imshow("split1",split[0])
# cv2.imshow("split2",split[1])
# cv2.imshow("split3",split[2])

cv2.waitKey(0)
cv2.destroyAllWindows()