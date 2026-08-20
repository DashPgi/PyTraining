import matplotlib.pyplot as plt
import numpy as np

dt = np.random.normal(0, 1, 1000)
dt2 = np.random.normal(1, 1.25, 1000)
dt3 = np.random.normal(2, 1.75, 1000)
plt.violinplot([dt, dt2, dt3],
               showmeans=True,
               showmedians=True)
plt.show()