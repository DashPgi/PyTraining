import matplotlib.pyplot as plt
import numpy as np

h = np.linspace(-5,5,150)
l = np.linspace(-4,4,150)

X,Y = np.meshgrid(h,l)
Z = np.sqrt(X**2+Y**2)
plt.contour(X,Y,Z,levels=0,colors='k')
plt.contourf(X,Y,Z)

plt.show()