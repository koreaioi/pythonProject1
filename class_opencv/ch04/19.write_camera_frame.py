# 카메라에서 받아오는 프레임을 하나의 동영상 파일로 저장
import cv2

capture = cv2.VideoCapture(0) # 0 번째 카메라에 연결
if not capture.isOpened() : raise Exception("카메라 연결 안됨")

fps = 29.97
delay = round(1000/fps)
size = (640,360)
fourcc = cv2.VideoWriter_fourcc(*'DX50')
