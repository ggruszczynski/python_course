import numpy as np
# import matplotlib.pyplot as plt
# %matplotlib notebook

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


import matplotlib.pyplot as plt

POS_WEIGHT = 1.0
NEG_WEIGHT = 2.0
MIN_OPERATION_NUMBER = 50

UNKNOWN_TRUST = 0.0
MAX_TRUST = 1.0
MIN_TRUST = -1.0

NEIGHBOUR_WEIGHT_BASE = 2.0
NEIGHBOUR_WEIGHT_POWER = 2.0

from IPython.core.debugger import Tracer

def sigmoid(x):
    y_scale = 2
    y_shift = -1
    x0 = MIN_OPERATION_NUMBER
    sharpness = 0.05
    return y_scale / (1 + np.exp(-sharpness*(x-x0))) + y_shift

def count_trust_v2(pos, neg):
    unclipped = pos * POS_WEIGHT - neg * NEG_WEIGHT

    clipped = sigmoid(unclipped)

    return clipped


def count_trust(pos, neg):
    return min(MAX_TRUST,
               max(MIN_TRUST, (pos * POS_WEIGHT - neg * NEG_WEIGHT)
                   / max(pos + neg, MIN_OPERATION_NUMBER)))



fig = plt.figure(num=None, figsize=(15,10), dpi=80, facecolor='w', edgecolor='k')
# ax = fig.add_subplot(111, projection='3d')
ax = fig.gca(projection='3d')


x_max = 100
y_max = 100

pos = np.arange(0, x_max, 1)
neg = np.arange(0, y_max, 1)
X, Y = np.meshgrid(pos, neg)
zs = np.array([count_trust_v2(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

# Plot the surface.
# surf = ax.contourf(X, Y, Z, cmap=cm.coolwarm,
#                    linewidth=0, antialiased=False)
# ax.clabel(surf, fontsize=9, inline=1)

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# surf = ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.9)
# cset = ax.contour(X, Y, Z, zdir='z', offset=0, cmap=cm.coolwarm)
# cset = ax.contour(X, Y, Z, zdir='x', offset=x_max, cmap=cm.coolwarm)
# cset = ax.contour(X, Y, Z, zdir='y', offset=y_max, cmap=cm.coolwarm)

# # Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_xlabel('positive')
ax.set_ylabel('negative')
ax.set_zlabel('reputation')

plt.show()