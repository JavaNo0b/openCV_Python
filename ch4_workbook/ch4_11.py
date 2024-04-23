# 10번 연습문제에서 다음을 추가하시오
# 1) 트랙바를 추가해서 선의 굵기를 1~10픽셀로 조절한다.
# 2) 트랙바를 추가해서 원의 반지름을 1~50픽셀로 조절한다.

import numpy as np, cv2

def onChangeLineThickness(trackbarValue):
    global thickness
    thickness = trackbarValue

def onChangeCircleRadius(trackbarValue):
    global radius
    radius = trackbarValue

def onMouse(event, x, y, flags, param):
    global image,radius,thickness
    #오른쪽 버튼 클릭 시
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x,y), radius, blue, thickness)
        cv2.imshow(title, image)
    #왼쪽 버튼 클릭 시
    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x + 30, y + 30), red, thickness, cv2.LINE_4)
        cv2.imshow(title, image)


blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
image = np.full((300, 500, 3), 255, np.uint8)
thickness = 1
radius = 20

title = 'ch4_10'
cv2.imshow(title, image)

cv2.createTrackbar('thickness', title, 1, 10, onChangeLineThickness)
cv2.createTrackbar('radius', title, 1, 50, onChangeCircleRadius)

cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()