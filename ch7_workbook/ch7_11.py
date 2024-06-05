import numpy as np, cv2
from  Common.filters import differential

image = cv2.imread("images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1, 0, 0,                         # 로버츠
         0, 1, 0,
         0, 0, 0]
data2 = [0, 0, -1,
         0, 1, 0,
         0, 0, 0]

data3 = [-1, 0, 1,                         # 프리윗 수직 마스크
         -1, 0, 1,
         -1, 0, 1]
data4 = [-1,-1,-1,                         # 프리윗 수평 마스크
          0, 0, 0,
          1, 1, 1]

data5 = [-1, 0, 1,                         # 소벨
         -2, 0, 2,
         -1, 0, 1]
data6 = [-1,-2,-1,                         # 소벨
          0, 0, 0,
          1, 2, 1]

dst1, _, _ = differential(image, data1, data2)
dst2, _, _ = differential(image, data3, data4)
dst3, _, _ = differential(image, data5, data6)

cv2.imshow("image", image)
cv2.imshow("ro", dst1)
cv2.imshow("pr", dst2)
cv2.imshow("so", dst3)

cv2.waitKey(0)