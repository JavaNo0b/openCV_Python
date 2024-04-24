# 다음 영상에서 특정 영역의 타원만을 복사하여 새 창에 표시하는 프로그램을 완성하시오.
# 힌트 : 마스크 행렬을 이용한다.
# cv2.bitwise_and(), cv2.bitwise_or() 등의 함수를 사용해서 같은결과가 나도록 구성한다.
# 타원 영역의 중심과 크기는 임의로 지정한다.


import numpy as np, cv2

image = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

mask = np.zeros(image.shape[:2], np.uint8)
center = (190,170)

# 빈부분-------------------------------------------------------
axes = (100, 50)  # 타원의 장축과 단축 길이 지정
angle = 0  # 타원의 기울기 각도
startAngle = 0  # 시작 각도
endAngle = 360  # 끝 각도

# 타원형 마스크 생성
cv2.ellipse(mask, center, axes, angle, startAngle, endAngle, (255, 255, 255), -1)

# 마스크를 이용해 원본 이미지에서 타원 부분만 추출
dst = cv2.bitwise_and(image, image, mask=mask)

#----------------------------------------------------------------


cv2.imshow("image",image)
cv2.imshow("dst",dst)
cv2.waitKey()