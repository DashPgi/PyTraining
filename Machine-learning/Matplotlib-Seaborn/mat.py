import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 20)
y = abs(x)

plt.plot(x, y,
         label="Graph",
         color="black",
         marker="o",
         linestyle="--",
         )
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True,ls="--")
plt.legend(loc="upper center")



plt.title("This Is Title",
          fontsize=11,
          fontweight="bold",
          color="black",
          )
plt.show()
