import numpy as np
from numpy import dtype, integer

print(np.zeros((1,2),dtype="int64"))
print(np.ones((1,2),dtype="int64"))
print(np.full((1,2),2,dtype="int64"))
print(np.empty((1,2),dtype="int64"))

print(np.arange(1,15,2))
print(np.arange(1,24,2).reshape(2,3,2))

print(np.linspace(0,50,5).reshape(2,5),dtype="int64")

print(np.random.default_rng(seed=2).integer(low=10,high=50,size=(3,3,3)))