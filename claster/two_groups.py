from matplotlib import pyplot as plt
import numpy as np

a = np.array([10, 10])
b = np.array([20, 10])
rng = np.random.default_rng()
size = 50

group_ax = rng.uniform(low=0, high=8, size=size) + a[0]
group_bx = rng.uniform(low=0, high=8, size=size) + b[0]
group_ay = rng.uniform(low=0, high=8, size=size) + a[1]
group_by = rng.uniform(low=0, high=8, size=size) + b[1]

x1 = plt.scatter(group_ax, group_ay, c='r')
x2 = plt.scatter(group_bx, group_by, c='b')
plt.show()


