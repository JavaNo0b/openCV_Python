# pc카메라로 영상을 받아들여서 다음과 같이 윈도운의 특정 영역에서 재생하시오.
# 1) 메인 윈도우는 400x300 크기로 한다.
# 2) 관심 영역은 30,30좌표에서 320x240 크기로 한다.
# 3) 관심 영역에 빨간색 테두리를 두른다.

import cv2
import numpy as np

# 카메라를 초기화합니다.
cap = cv2.VideoCapture(0)

# 메인 윈도우의 크기를 설정합니다.
cv2.namedWindow('Main Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Main Window', 300, 400)

while True:
    # 카메라로부터 영상을 읽어옵니다.
    ret, frame = cap.read()

    if not ret:
        print("카메라로부터 영상을 불러오는데 실패했습니다.")
        break


    # 관심 영역만 원본 영상에서 추출합니다.
    roi = frame[30:270, 30:350].copy()

    # 전체 프레임을 검은색으로 채웁니다.
    frame[:,:,:] = 0

    # 관심 영역에 빨간색 테두리를 추가합니다.
    cv2.rectangle(roi,(0,0), (320, 240), (0, 0, 255), 2)

    # 원본 프레임에 관심 영역을 덮어씌웁니다.
    frame[30:270, 30:350] = roi

    # 메인 윈도우에 영상을 보여줍니다.
    cv2.imshow('Main Window', frame)

    # ESC 키를 누르면 루프를 종료합니다.
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 자원을 해제하고 윈도우를 닫습니다.
cap.release()
cv2.destroyAllWindows()