# 예제 코드를 수정해서 트랙바로 카메라 영상의 밝기와 대비 변경할 수 있도록 수정하시오.

import cv2
from Common.utils import put_string

def brightness_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_BRIGHTNESS, value) # 줌 설정

def exposure_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_EXPOSURE, value)

capture = cv2.VideoCapture(0)								# 0번 카메라 연결
if capture.isOpened() is None: raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)      # 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)     # 카메라 프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)          # 오토포커싱 중지
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)       # 프레임 밝기 초기화

title = "Change Camera Properties"              # 윈도우 이름 지정
cv2.namedWindow(title)                          # 윈도우 생성 - 반드시 생성 해야함
cv2.createTrackbar("brightness" , title, 1, 99, brightness_bar)
cv2.createTrackbar("exposure", title, -10, 40, exposure_bar)

while True:
    ret, frame = capture.read()                 # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    brightness = int(capture.get(cv2.CAP_PROP_BRIGHTNESS))
    exposure = int(capture.get(cv2.CAP_PROP_EXPOSURE))
    put_string(frame, "brightness : " , (10, 240), brightness)   # 줌 값 표시
    put_string(frame, "exposure : ", (10, 270), exposure)    # 초점 값 표시
    cv2.imshow(title, frame)

capture.release()