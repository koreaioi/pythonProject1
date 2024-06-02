import cv2

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

# OpenCV의 블러링 함수
blur_img = cv2.blur(image, (5,5), borderType=cv2.BORDER_CONSTANT)
# OpenCV의 박스 필터 함수
box_img = cv2.boxFilter(image, ddepth=-1, ksize=(5,5))
# OpenCV의 가우시안 필터
gauss_img = cv2.GaussianBlur(image, (5,5), 0) # x축 시그마는 0: 자동

# cv2.imshow