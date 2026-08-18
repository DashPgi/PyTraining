import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 2)
y1 = x ** 2
y2 = x ** 3

fig, ax = plt.subplots()

ax.fill_between(x=x, y1=y1, y2=y2,
                color="skyblue",
                alpha=0.5)

ax.annotate("%x^2%",
            xy=(8, 100),
            xytext=(3, 1),
            arrowprops=dict(arrowstyle="->"))

ax.annotate("%x^3%",
            xy=(5, 125),
            xytext=(7, 10),
            arrowprops=dict(arrowstyle="->"))

plt.show()
