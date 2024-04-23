# 다음의 마우스 이벤트 제어 프로그램ㅇ르 작성하시오.
# 1) 마우스 오른쪽 버튼 클릭 시 원(클릭 좌표에서 반지름 20화소)를 그린다.
# 2) 마우스 왼쪽 버튼 클릭 시 사각형(크기 30x30)을 그린다.

import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global image
    #오른쪽 버튼 클릭 시
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x,y), 20, blue, 1)
        cv2.imshow(title, image)
    #왼쪽 버튼 클릭 시
    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x + 30, y + 30), red, 1, cv2.LINE_4)
        cv2.imshow(title, image)


blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
image = np.full((300, 500, 3), 255, np.uint8)

title = 'ch4_10'
cv2.imshow(title, image)

cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()