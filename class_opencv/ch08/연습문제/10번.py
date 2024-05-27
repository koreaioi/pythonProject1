import numpy as np, cv2


def contain(p,shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] <shape[1]

def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)            # 목적 영상 생성
    for i in range(img.shape[0]):                           # 목적 영상 순회 - 역방향 사상
        for j in range(img.shape[1]):
            x, y = np.subtract((j, i) , pt)
            if contain((y, x), img.shape):
                dst[i, j] = img[y, x]
    return dst

image = cv2.imread("translate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")

dst1 = translate(image, (50,60))

M = np.float32([[1, 0, 50], [0, 1, 60]])
# 평행이동하는 opencv함수 warpAffine
dst2 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))


cv2.imshow("image", image)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)