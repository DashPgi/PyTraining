import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 20)
y = abs(x**2)

plt.plot(x, y,
         label="Graph",
         color="blue",
         marker="o",
         )
plt.legend()
plt.title("This Is Title",
          fontsize=11,
          fontweight="bold",
          color="blue",
          )
plt.show()
