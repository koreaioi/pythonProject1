import numpy as np,cv2

image = cv2.imread("bit_test.jpg", cv2.IMREAD_COLOR)
logo = cv2.imread("logo.jpg", cv2.IMREAD_COLOR)

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks) #B G R

# mask[0]은 파란색 + 흰색 -> 흰색, 나머지 색 -> 검정
# mask[1]은 초록색 + 흰색 -> 흰색, 나머지 색 -> 검정
# mask[2]은 빨간색 + 흰색 -> 흰색, 나머지 색 -> 검정

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)

bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

foregournd = cv2.bitwise_and(logo,logo, mask=fg_pass_mask)
cv2.imshow("logo", logo)
cv2.imshow("masks[0]", masks[0])
cv2.imshow("masks[1]", masks[1])
cv2.imshow("masks[2]", masks[2])

cv2.imshow("fg_pass", fg_pass_mask)
cv2.imshow("bg_pass", bg_pass_mask)

cv2.imshow("foreground", foregournd)

cv2.waitKey(0)


