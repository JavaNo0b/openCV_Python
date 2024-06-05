import numpy as np, cv2
from  Common.filters import filter

th1 = 50
th2 = 100

image = cv2.imread("images/canny.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

def onTrackBar1(value):
    th1 = cv2.getTrackbarPos("th1", "Canny Edge")

    canny = cv2.Canny(image, th1, th2)
    cv2.imshow("Canny Edge", canny)

def onTrackBar2(value):
    th2 = cv2.getTrackbarPos("th2", "Canny Edge")

    canny = cv2.Canny(image, th1, th2)
    cv2.imshow("Canny Edge", canny)

cv2.imshow("image", image)
cv2.imshow("Canny Edge", image)

cv2.createTrackbar("th1", "Canny Edge", 50, 255, onTrackBar1)
cv2.createTrackbar("th2", "Canny Edge", 100, 255, onTrackBar2)

cv2.waitKey(0)