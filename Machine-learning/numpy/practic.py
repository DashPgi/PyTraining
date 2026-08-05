import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])

B = np.array([3])

print(np.shape(A))
# 2 * 3
print(np.shape(B))
# 1*1
C = A * B
print(np.shape(C))
# 2*3
