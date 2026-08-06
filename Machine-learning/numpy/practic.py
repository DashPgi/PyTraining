import numpy as np

# need For Studing and Research !!!

rng = np.random.default_rng()
normal = rng.normal(loc=10,scale=3,size=10)
uniform = rng.uniform(low=0,high=10,size=10)
exp = rng.exponential(scale=3,size=10)
bino = rng.binomial(size=10)

print(normal)
print(uniform)
print(exp)
print(bino)
