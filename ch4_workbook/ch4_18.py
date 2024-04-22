import numpy as np, cv2

# 400x600 행렬을 흰색으로 생성
image = np.full((400, 600, 3), 255, dtype=np.uint8)

title = 'ch4_18'

cv2.namedWindow(title, cv2.WINDOW_NORMAL)

# x: x축 중심, y: y축 중심
x = image.shape[1]//2
y = image.shape[0]//2
# 중점
pt = (x, y)
# 태극의 반지름
radius = y//2

# 위쪽 빨간색 반원
cv2.ellipse(image, (x, y), (radius, radius), 0, 180, 360, (0, 0, 255), -1)
# 아래쪽 파란색 반원
cv2.ellipse(image, (x, y), (radius, radius), 0, 0, 180, (255, 0, 0), -1)
# 위쪽 파란색 반원
cv2.ellipse(image, (x+radius//2, y), (radius//2, radius//2), 0, 180, 360, (255, 0, 0), -1)
# 아래쪽 빨간색 반원
cv2.ellipse(image, (x-radius//2, y), (radius//2, radius//2), 0, 0, 180, (0, 0, 255), -1)


cv2.imshow(title,image)
cv2.waitKey(0)
cv2.destroyAllWindows()