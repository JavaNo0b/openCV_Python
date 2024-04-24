
# import numpy as np, cv2
#
# data = [1,2,3,4,5,6,7,8,9,10,11,12]
# m1 = np.array(data).reshape(2,3,2) // 스플릿을 하기 위해서 마지막 부분이 3채널로 돼있어야 한다. -> 스플릿 된 상태는 처음이 3채널
#
# r,g,b = cv2.split(m1)
#
# print("[m1] = %s" %m1)
# print("[r, g, b] = %s, %s, %s" %(r, g, b))

import numpy as np, cv2

data = [1,2,3,4,5,6,7,8,9,10,11,12]
m1 = np.array(data).reshape(2,2,3)

r,g,b = cv2.split(m1)

print("[m1] = %s" %m1)
print("[r, g, b] = %s, %s, %s" %(r, g, b))