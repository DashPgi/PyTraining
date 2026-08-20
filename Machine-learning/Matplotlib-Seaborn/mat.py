import matplotlib.pyplot as plt
import numpy as np

matrix = np.random.default_rng().integers(low=0,high=10000,size=[25,25])


plt.imshow(matrix)
plt.xticks(range(5), list("ABCDE"))

plt.colorbar()
plt.show()