from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return np.sqrt(x ** 2 + y ** 2)

x = np.linspace(-6, 6, 31)
y = np.linspace(-6, 6, 31)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
plt.savefig('func_l2_norm_r2_contour3d.png')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# plots contour lines
ax.axis('equal')
ax.contour(X, Y, Z)
plt.savefig('func_l2_norm_r2_contour2d.png')

