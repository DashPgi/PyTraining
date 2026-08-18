import matplotlib.pyplot as plt
import numpy as np

rand = np.random.randn(10000)

data2 = rand + 2

plt.hist(rand,
         bins=50,  # -> Time to Repeat
         edgecolor="black",
         )
plt.hist(data2,
         edgecolor="white",
         color="green",
         bins=50,  # -> Time to Repeat
         )

plt.show()
