import numpy as np
import cv2

def load_image(no):
    fname = "images/test_car/{0:02d}.jpg".format(no)
    image = cv2.imread(fname, cv2.IMREAD_COLOR)
    if image is None:
        print(str(no) + "번 영상 파일이 없습니다.")
    return image


current_image = 1

while True:
    image = load_image(current_image)
    if image is None:
        break

    mask = np.ones((5, 17), np.uint8)  # 닫힘 연산 마스크
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 명암도 영상 변환
    gray = cv2.blur(gray, (5, 5))  # 블러링
    gray = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 5)  # 소벨 에지 검출

    # 이진화 및 닫힘 연산 수행
    _, th_img = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    morph = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations=3)

    cv2.imshow("image", image)
    cv2.imshow("binary image", th_img)
    cv2.imshow("opening", morph)

    key = cv2.waitKey()
    if key == 27:  # ESC를 누르면 종료합니다.
        break
    elif key == 82:  # 위쪽 화살표 키를 누르면 다음 영상을 로드합니다.
        current_image += 1
    elif key == 84:  # 아래쪽 화살표 키를 누르면 이전 영상을 로드합니다.
        current_image -= 1

cv2.destroyAllWindows()

