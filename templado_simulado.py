import sys

import matplotlib.pyplot as plt
import numpy as np
import operator

conexion = {}
fig = plt.figure()
ax = fig.gca()
ax.set_xticks(np.arange(0, 26, 1))
ax.set_yticks(np.arange(0, 26, 1))
count = 0

for i in xrange(1, 26):
    for j in xrange(1, 26):
        conexion[(i, j)] = count
        count += 1
        plt.scatter(i, j, color='r')


print(sorted(conexion.items(), key=operator.itemgetter(1)))
plt.grid()
plt.show()