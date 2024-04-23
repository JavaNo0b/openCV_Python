# 600행 400열의 윈도우를 만들고 영상 안의 (100,100)좌표에 200x300 크기의 빨간색 사각형을 그리시오.

import numpy as np
import cv2

image = np.zeros((600,400,3),np.uint8)
image[:] = 255


cv2.rectangle(image, (100,100,200,300), (0,0,255),1, cv2.LINE_AA)

cv2.imshow('4_9', image)
cv2.waitKey(0)
cv2.destroyAllWindows()