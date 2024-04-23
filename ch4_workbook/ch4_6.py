# 6. 300행, 400열의 행렬을 회색 바탕색(100)으로 생성해서 500행, 600열의 윈도우에 표시하시오.

import numpy as np
import cv2

image = np.full((300, 400), 100, dtype=np.uint8)
title = 'ch4_6'
cv2.namedWindow(title, cv2.WINDOW_NORMAL)

cv2.resizeWindow(title, 600, 500)

cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()