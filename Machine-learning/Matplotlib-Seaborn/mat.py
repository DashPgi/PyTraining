import matplotlib.pyplot as plt
import numpy as np

data = np.arange(0, 5, 0.5)
noise = np.random.normal(0, 1, len(data))

y = data ** 2  + noise
colors = y *100
scatter = plt.scatter(data, y,
            c=colors,
            cmap="plasma")
plt.colorbar(scatter,label = "Color bar")
plt.show()