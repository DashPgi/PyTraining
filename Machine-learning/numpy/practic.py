import numpy as np

# join and Split

A = np.random.default_rng(seed=1).integers(low=1, high=10,size=(3,3,3),dtype="int64")
B = np.random.default_rng(seed=1).integers(low=1, high=10,size=(3,3,3),dtype="int64")

print(A)
print(B)

C = np.concatenate((A, B))
print(f"C : {C}")
D = np.concatenate((A, B), axis=1)
print(f"D : {D}")
E = np.concatenate((A, B), axis=2)
print(f"E : {E}")


R = np.split(C,1)
C = np.split(C,1,axis=1)