import numpy as np

# indexing

A = np.random.default_rng(seed=1).integers(low= 0,high = 100,size=(5,5))

print(A)
print(A[A<30])
print(A[1,2])
print(A[[0,2],[1,2]])
print(A[:,[1,2]])
print(f"1 -- : {A[1:]}")
print(f"1 -- 5 : {A[1:5:2]}")
print(A[::,1,2])
