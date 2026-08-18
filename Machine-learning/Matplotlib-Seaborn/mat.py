import matplotlib.pyplot as plt
import numpy as np

Country = ["Iran","USA","German","Israel"]
Pop = np.random.default_rng().integers(low=1,high=100,size=len(Country))

plt.figure(figsize=(8,8))
plt.pie(Pop,labels=Country,
        explode=[0,0,0,0.1], # for apart
        colors=["gray","blue","orange","lightblue"])
plt.show()