import numpy as np
import cv2

image = np.full((300, 400), 100, dtype=np.uint8)
title = 'ch4_6'
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)

cv2.resizeWindow(title, 600, 500)

cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()