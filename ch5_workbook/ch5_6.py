# 다음 예시코드는 에러가 발생한다 수정 후 실행 결과를 적어라.

# import numpy as np, cv2
#
# m1 = [1,2,3,1,2,3]
# m2 = [3,3,4,2,2,3]
# m3 = m1 + m2
# m4 = m1 - m2
#
# print("[m1] = %s" %m1)
# print("[m2] = %s" %m2)
# print("[m3] = %s" %m3)
# print("[m4] = %s" %m4)

import numpy as np
import cv2

m1 = np.array([1, 2, 3, 1, 2, 3])
m2 = np.array([3, 3, 4, 2, 2, 3])

# NumPy 배열의 덧셈 및 뺄셈
m3 = m1 + m2
m4 = m1 - m2

print("[m1] = %s" % m1)
print("[m2] = %s" % m2)
print("[m3] = %s" % m3)
print("[m4] = %s" % m4)

#----------------------------------------------------
