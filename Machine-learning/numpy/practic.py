import numpy as np

# 1D Array Creation
A = np.arange(3) # range for generate number in araray
B = np.arange(0,20,2)
C = np.linspace(1,4,1)

print(C)
print(B)
print(A)

# 2D Array Creation

A2 = np.eye(3)
B2 = np.eye(2,3)
print(A2)
print(B2)

C2 = np.diag([1,2,3]) # for diagonal
print(C2)
D2 = np.array([[1,2,3],[4,5,6]])
print(np.diag(D2)) # show D2's diagonal
