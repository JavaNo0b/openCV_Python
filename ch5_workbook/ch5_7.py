# logo 파일을 입력 받고 3개 채널을 분리하고, 각 채널을 컬러 영상을 윈도우에 표시하라.
# 힌트 : cv2.imshow()함수로 단일 채널 행렬을 출력하면 명암도 영상으로 표현된다.
# 컬러 영상을 출력하려면 3개 채널을 합성해야한다.

import numpy as np, cv2

logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)
if logo is None: raise Exception("영상파일 읽기 오류")

blue, green, red = cv2.split(logo)


# 빈부분 -----------------------------------------------------------------------------------------

# 각 채널만 강조한 컬러 이미지 생성
blue_img = cv2.merge([blue, np.zeros(blue.shape, dtype=blue.dtype), np.zeros(blue.shape, dtype=blue.dtype)])
green_img = cv2.merge([np.zeros(green.shape, dtype=green.dtype), green, np.zeros(green.shape, dtype=green.dtype)])
red_img = cv2.merge([np.zeros(red.shape, dtype=red.dtype), np.zeros(red.shape, dtype=red.dtype), red])

#------------------------------------------------------------------------------------------------


cv2.imshow("logo", logo)
cv2.imshow("blue_img",blue_img)
cv2.imshow("green_img",green_img)
cv2.imshow("red_img",red_img)
cv2.waitKey()