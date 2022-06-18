import numpy as np
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import matplotlib.pyplot as plt

rng = np.random.default_rng(1988)
points = rng.random((50, 2))
hull = ConvexHull(points)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    ax.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.savefig('pic_convex_hull_random_2d_points.png')
