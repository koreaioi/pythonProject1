import numpy as np, cv2


def calc_histo(image, channels, bsize, ranges):
    ch = len(channels)
    shape = bsize if ch > 1 else (bsize[0], 1)
    hist = np.zeros(shape, np.float32)  # 히스토그램 누적 행렬
    gap = np.divide(ranges[1::2], bins)  # 계급 간격

    for row in image:  # 2차원 행렬 순회 방식
        for val in row:
            idx = np.divide(val[channels], gap).astype('uint')
            hist[tuple(idx)] += 1
    return hist


image = cv2.imread("bright.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 읽기 오류")

ch, bins, ranges = [0, 1], [4, 4], [0, 255, 0, 255]

hist1 = calc_histo(image, ch, bins, ranges)
hist2 = cv2.calcHist(image, ch, None, bins, ranges)

cv2.imshow("title", image)
cv2.waitKey(0)
