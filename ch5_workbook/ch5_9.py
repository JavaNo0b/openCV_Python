# 3행 6열의 행렬을 생성하고, 행렬의 원소를 초기화한 후에 cv2.reduce() 함수를 이용해서
# 가로 방향과 세로 방향으로 감축하여 평균을 구한 결과를 출력하시오.

import numpy as np, cv2

m = np.random.rand(3,6) * 1000//10

reduce_avg_col = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_AVG) # 행방향 축소 -> 1열 생성
reduce_avg_row = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_AVG) # 열방향 축소 -> 1행 생성

print("[m1] = \n%s\n" %m)
print("[reduce_avg_col] =", reduce_avg_col.flatten())
print("[reduce_avg_row] =", reduce_avg_row.flatten())
