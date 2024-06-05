import numpy as np, cv2
from Common.filters import filter

image = cv2.imread("images/filter_sharpen.jpg", cv2.IMREAD_COLOR) # 영상 읽기
if image is None: raise Exception("영상파일 읽기 오류")

data = [1/9,1/9,1/9,
        1/9,1/9,1/9,
        1/9,1/9,1/9]
data2 = [[-1, -1, -1],
         [-1, 9, -1],
         [-1, -1, -1]]

mask1 = np.array(data, np.float32).reshape(3,3)
mask2 = np.array(data2, np.float32)

b, g, r = cv2.split(image)
filtered1 = [filter(b,mask1), filter(g,mask1), filter(r,mask1)]
filtered2 = [filter(b,mask2), filter(g,mask2), filter(r,mask2)]

dst1 = cv2.merge(filtered1)
dst2 = cv2.filter2D(image, cv2.CV_8U, mask1)
dst3 = cv2.merge(filtered2)
dst4 = cv2.filter2D(image, cv2.CV_8U, mask2)

cv2.imshow("image", image)
cv2.imshow("filtered1", cv2.convertScaleAbs(dst1))
cv2.imshow("filter2D1", cv2.convertScaleAbs(dst2))
cv2.imshow("filtered2", cv2.convertScaleAbs(dst3))
cv2.imshow("filter2D2", cv2.convertScaleAbs(dst4))

cv2.waitKey(0)





