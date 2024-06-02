import numpy as np, cv2

def morphology(img, mode=0, mask=None):
    dst = np.zeros(img.shape, np.uint8)
    if mask is None:
        mask = np.ones((3, 3), np.uint8)
    ycenter, xcenter = np.divmod(mask.shape[:2], 2)[0]

    mcnt = cv2.countNonZero(mask)
    for i in range(ycenter, img.shape[0] - ycenter):
        for j in range(xcenter, img.shape[1] - xcenter):
            y1, y2 = i-ycenter, i+ycenter +1
            x1, x2 = i-xcenter, i+xcenter +1
            roi = img[y1:y2, x1:x2]
            tmp = cv2.bitwise_and(roi, mask)
            cnt = cv2.countNonZero(tmp)

            if mode == cv2.MORPH_ERODE :
                dst[i,j] = 255 if (cnt == mcnt) else 0 # 침식
            elif mode == cv2.MORPH_DILATE :
                dst[i,j] = 0 if (cnt ==0) else 255 # 팽창

    return dst


image = cv2.imread('morph.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일읽기 오류")
image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1] # 영상 이진화

mask = np.array([0,1,0,
                 1,1,1,
                 0,1,0], np.uint8).reshape(3,3)

image1 = morphology(image, 'erode', mask=mask)
image2 = morphology(image, 'dilate', mask=mask)

cv2.imshow('image1', image1)
cv2.imshow('image2', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()