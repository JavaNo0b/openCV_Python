# 예제코드에서 화살표 키로 트랙바를 이동하는 코드를 추가하시오.

# import numpy as np
# import cv2
#
# def onChange(value):												# 트랙바 콜백 함수
#     global image                        	# 전역 변수 참조
#
#     add_value = value - int(image[0][0])        	# 트랙바 값과 영상 화소값 차분
#     print("추가 화소값:", add_value)
#
#     image[:] = image + add_value            		# 행렬과 스칼라 덧셈 수행
#     cv2.imshow(title, image)
#
# image = np.zeros((300, 500), np.uint8)           	# 영상 생성
#
# title = 'Trackbar Event'
# cv2.imshow(title, image)
#
# cv2.createTrackbar("Brightness", title, image[0][0], 255, onChange)	# 트랙바 콜백 함수 등록
# cv2.waitKey(0)
# cv2.destroyWindow(title)

import numpy as np
import cv2


def onChange(value):
    global image, title

    add_value = value - int(image[0][0])
    print("추가 화소값:", add_value)
    image[:] = image + add_value
    cv2.imshow(title, image)

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
def keyEvent(value):

    print(cv2.getTrackbarPos('Brightness', title))
    while True:
        key = cv2.waitKeyEx(100)

        if key == 27:
            cv2.destroyAllWindows()
            break
        elif key == 2424832:
            cv2.setTrackbarPos('Brightness', title, max(value - 10, 0))
            value -= 10
        elif key == 2555904:
            cv2.setTrackbarPos('Brightness', title, min(value + 10, 255))
            value += 10
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


image = np.zeros((300, 500), np.uint8)

title = 'Trackbar Event'
cv2.imshow(title, image)

cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)
keyEvent(cv2.getTrackbarPos('Brightness', title))