import numpy as np, cv2

def filter1(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows,cols), np.float32)
    ycenter, xcenter = rows//2, cols//2

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1
            x1, x2 = j - xcenter, j + xcenter + 1
            roi = image[y1:y2, x1:x2].astype('float32')
            tmp = cv2.multiply(roi, mask)
            dst[i,j] = cv2.sumElems(tmp)[0]

    return dst


def filter2(image, kernel):
    height, width = image.shape
    k_height, k_width = kernel.shape
    output = np.zeros_like(image)
    offset_y,offset_x = k_height // 2, k_width // 2

    for y in range(height):
        for x in range(width):
            pixel_value = 0
            for ky in range(k_height):
                for kx in range(k_width):
                    img_y = y + ky - offset_y
                    img_x = x + kx - offset_x
                    if img_y >= 0 and img_y < height and img_x >= 0 and img_x < width:
                        pixel_value += image[img_y, img_x] * kernel[ky, kx]
            output[y, x] = pixel_value

    return output

image = cv2.imread('cannay_tset.jpg', cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상 파일 읽기 오류")
mask = np.ones((3, 3), dtype=np.float32) / 9.0

result1 = filter1(image, mask)
result2 = filter2(image, mask)
result3 = cv2.filter2D(image, -1, mask)

cv2.imshow('result1', result1) # 행렬 처리 방식
cv2.imshow('result2', result2) # 화소 직접 근접
cv2.imshow('result3', result3) # cv2 내장 함수인 filter2D사용
cv2.waitKey(0)
cv2.destroyAllWindows()


#
#
# def filter1(image, mask):
#     rows, cols = image.shape[:2]
#     dst = np.zeros((rows,cols), np.float32)
#     ycenter, xcenter = rows//2, cols//2
#
#     for i in range(ycenter, rows - ycenter):
#         for j in range(xcenter, cols - xcenter):
#             y1, y2 = i - ycenter, i + ycenter + 1
#             x1, x2 = j - xcenter, j + xcenter + 1
#             roi = image[y1:y2, x1:x2].astype('float32')
#             tmp = cv2.multiply(roi, mask)
#             dst[i,j] = cv2.sumElems(tmp)[0]
#
#     return dst
#
#
#
# image = cv2.imread("cannay_tset.jpg", cv2.IMREAD_GRAYSCALE)
# if image is None : raise Exception("영상 파일 읽기 오류")
#
# data = [[1/9, 1/9, 1/9],
#         [1/9, 1/9, 1/9],
#         [1/9, 1/9, 1/9]]
#
# data1 = np.array(data, np.float32)
# # data2 = np.array(data)
#
# blur1 = filter1(image, data1)
# blur1 = blur1.astype('uint8')
#
# cv2.imshow("image", image)
# cv2.imshow("blur", blur1)
# cv2.waitKey(0)
