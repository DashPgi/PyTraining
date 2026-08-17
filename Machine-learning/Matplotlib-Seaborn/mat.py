import matplotlib.pyplot as plt
import numpy as np

Country = ["Iran","USA","German","Israel"]
GDP = np.random.default_rng().integers(low=0,high=100,size=len(Country))

bars = plt.bar(Country,GDP) # bar -> vertical,barh -> horizontal
bars[0].set_color('red')
bars[1].set_hatch("/")
bars[1].set_color('darkblue')
bars[2].set_color('orange')
bars[3].set_color('blue')
plt.show()