import numpy as np, cv2

# 안나올듯?
no, max_no, cnt = 0,20,1

while True:
    # 여기 아래만 추가
    no = no + cnt
    fname = "images/test_car/{0:0d}.jpg".format(no)
    image = cv2.imread(fname, cv2.IMREAD_COLOR)
    if image is None:
        print("{%02d}.jpg: 영상 파일 없음" % no)
        if no < 0: no = max_no
        elif no >= max_no: no =0
        continue
    # 여기까지

    mask = np.ones((5,17), np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 명암도 영상 변환
    gray = cv2.blur(gray (5,5)) #블러링
    gray = cv2.Sobel(gray, cv2.CV_8U, 1,0,5) # 소벨 엣지 검출

