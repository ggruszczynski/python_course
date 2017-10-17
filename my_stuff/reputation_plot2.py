import numpy as np
# import matplotlib.pyplot as plt
# %matplotlib notebook

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


import matplotlib.pyplot as plt

POS_WEIGHT = 1.0
NEG_WEIGHT = 2.0
MIN_OPERATION_NUMBER = 0

UNKNOWN_TRUST = 0.0
MAX_TRUST = 1.0
MIN_TRUST = -1.0

NEIGHBOUR_WEIGHT_BASE = 2.0
NEIGHBOUR_WEIGHT_POWER = 2.0

from IPython.core.debugger import Tracer

def sigmoid(x, y_scale=2, y_shift= -1, sharpness = 0.1, x0 = MIN_OPERATION_NUMBER):
    return y_scale / (1 + np.exp(-sharpness*(x-x0))) + y_shift

def reputation_v1(pos, neg):
    result = (pos - neg )/(pos + neg)

    # ap = pos / max(pos + neg, MIN_OPERATION_NUMBER)
    # an = neg / max(pos + neg, MIN_OPERATION_NUMBER)
    #
    #
    # x0_pos = pos #max(0.95*pos, 1)
    # x0_neg = neg #max(0.9*neg, 1)
    #
    # y_pos = ap* sigmoid(pos, y_scale=1, y_shift=0, sharpness=pos/1000, x0 = x0_pos)
    # y_neg = an* sigmoid(neg, y_scale=-1, y_shift=0,  sharpness=neg/100, x0 = x0_neg )
    #
    #
    # # res = sigmoid(pos-neg, y_scale=2, y_shift=-1, sharpness=0.0001, x0_ = x0)
    #
    # result = y_pos + y_neg

    return result

def reputation_v2(pos, neg):
    ratio = (pos - neg )/(pos + neg)
    result=  sigmoid(ratio, y_scale=2, y_shift=-1, sharpness=5, x0 = 0)

    return result
    # return min(MAX_TRUST,
    #            max(MIN_TRUST, (pos * POS_WEIGHT - neg * NEG_WEIGHT)
    #                / max(pos + neg, MIN_OPERATION_NUMBER)))


step =0.01
y_max = x_max = 1


pos = np.arange(0, x_max, step)
neg = np.arange(0, y_max, step)
X, Y = np.meshgrid(pos, neg)
zs_v1 = np.array([reputation_v1(x, y) for x, y in zip(np.ravel
                                                       (X), np.ravel(Y))])
Z_v1 = zs_v1.reshape(X.shape)

zs_v2 = np.array([reputation_v2(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
Z_v2 = zs_v2.reshape(X.shape)

# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=(14,8))
# fig = plt.figure(figsize=plt.figaspect(2.))
fig.suptitle('Reputation')

# plt.title('Reputation' )
#===============
#  First subplot
#===============
# set up the axes for the first plot
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.set_xlabel('positive')
ax.set_ylabel('negative')
ax.set_zlabel('reputation_v1')
surf = ax.plot_surface(X, Y, Z_v1, rstride=5, cstride=5, cmap=cm.coolwarm,
                       alpha=0.5, antialiased=False, zorder = 0.5)



cset = ax.contour(X, Y, Z_v1, zdir='z', offset=0, cmap=cm.coolwarm)
# cset = ax.contour(X, Y, Z_new, zdir='x', offset=-np.pi, cmap=cm.coolwarm)
# cset = ax.contour(X, Y, Z_new, zdir='y', offset=3*np.pi, cmap=cm.coolwarm)



# ax.set_zlim(-1.01, 1.01)

# Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=10)

#===============
# Second subplot
#===============
# set up the axes for the second plot

ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.set_xlabel('positive')
ax.set_ylabel('negative')
ax.set_zlabel('reputation_v2')

ax.plot_surface(X, Y, Z_v2, rstride=5, cstride=5, cmap=cm.coolwarm,
                alpha=0.5, antialiased=False)

cset = ax.contour(X, Y, Z_v2, zdir='z', offset=0, cmap=cm.coolwarm)
# ax.set_zlim(-1.01, 1.01)

plt.show()
