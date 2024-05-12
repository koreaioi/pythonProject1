import numpy as np,cv2

image1 = np.zeros((50,512), np.float32)
image2 = np.zeros((50,512), np.float32)

rows, cols = image1.shape

for i in range(rows):
    for j in range(cols):
        # image1.itemset((i,j), j//2)
        # image2.itemset((i,j), j//20*10)

        image1[i][j] = j//2
        image2[i][j] = j// 20 * 10

cv2.imshow("image1,", image1/255) # -> float임로 255로 나눠주기
cv2.imshow("image2,", image2/255)
cv2.waitKey(0)