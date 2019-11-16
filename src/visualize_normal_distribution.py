import matplotlib.pyplot as plt
import numpy as np 

x = np.random.normal(size=10000, scale=3)
y = np.random.normal(size=10000, scale=3)

plt.scatter(x,y, s=1, alpha=0.1)

plt.scatter(0,0,s=10,c="black")

plt.xlim(-10,10)
plt.ylim(-10,10)

plt.xlabel("km")
plt.ylabel("km")

plt.savefig("img/normal_distribution.png")