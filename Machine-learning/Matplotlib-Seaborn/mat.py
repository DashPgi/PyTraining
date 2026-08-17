import matplotlib.pyplot as plt
import numpy as np

Country = ["Iran","USA","German","Israel"]
GDP = np.random.default_rng().integers(low=0,high=100,size=len(Country))

fig,ax = plt.subplots()

ax.bar(Country,GDP)
plt.show()