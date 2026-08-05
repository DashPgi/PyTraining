import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])

B = np.array([[6, 4], [5, 4], [3, 2]])

print(np.shape(A))
# 2 * 3
print(np.shape(B))
# 3*2

A_R = A[:, :, np.newaxis]
B_R = B[np.newaxis, :, :]

C = A_R + B_R

print(C)
print(C.shape)
