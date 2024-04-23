# PC 카메라를 통해서 받아온 프레임에 다음의 영상처리를 수행하고, 결과 영상을 윈도우에 표시하는 프로그램을 작성하시오.
# 1) (200, 100)좌표에서 100x200 크기의 관심 영역 지정
# 2) 관심 영역에서 녹색 성분을 50만큼 증가
# 3) 관심 영역의 테두리를 두께 3의 빨간색으로 표시

import numpy as np, cv2

def put_string(frame, text, pt, value, color=(120, 200, 90)):             # 문자열 출력 함수 - 그림자 효과
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)  # 그림자 효과
    cv2.putText(frame, text, pt, font, 0.7, color, 2)  # 글자 적기

capture = cv2.VideoCapture(0)  # 0번 카메라 연결
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

# 카메라 속성 획득 및 출력
print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))

while True:
    ret, frame = capture.read()  # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    # 관심 영역 지정
    x, y = 200, 100
    width, height = 200, 100
    x1 = max(x - width // 2, 0)
    x2 = min(x + width // 2, frame.shape[1])
    y1 = max(y - height // 2, 0)
    y2 = min(y + height // 2, frame.shape[0])

    # 녹색 화소 50 추가
    roi = frame[y1:y2, x1:x2]
    roi[:, :, 1] = np.clip(roi[:, :, 1] + 50, 0, 255)

    # 테두리 그리기
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)

    title = "View Frame from Camera16"
    cv2.imshow(title, frame)  # 윈도우에 영상 띄우기

capture.release()