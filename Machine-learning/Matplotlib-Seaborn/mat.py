import matplotlib.pyplot as plt
import numpy as np

data = np.random.default_rng().integers(low=1, high=100, size=100)
Index = np.random.default_rng().integers(low=1, high=100, size=100)

plt.plot(data,Index,
         label = 'Index')
plt.show()