import numpy as np
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(8051988)

fig, ax = plt.subplots()


resolution = 50  # the number of vertices
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_aspect('equal')


patches = []
circle = Circle((0, 0), 2)
patches.append(circle)
wedge = Wedge((3,0), 2, 30, 120)
patches.append(wedge)

offset = np.array([5,0])
vertices = np.array([(0,0), (1,2), (2, 0)])
patches.append(Polygon(offset + vertices, True))

offset = np.array([-7,-2])
vertices = np.array([(0,0), (0,4), (4, 4), (4, 0)])
patches.append(Polygon(offset + vertices, True))

offset = np.array([-11,0])
vertices = np.array([(0,0), (1,2), (2, 2), (3, 0), (2,-2), (1, -2)])
patches.append(Polygon(offset + vertices, True))

colors = 100 * np.random.rand(len(patches))
p = PatchCollection(patches, alpha=0.4)
p.set_array(colors)
ax.add_collection(p)

# line
ax.plot((-10, -5), (4, 6), marker = 'o')
plt.xlim([-11, 7])
plt.ylim(-2,6.5)
plt.savefig('pic_convex_sets.png', bbox_inches='tight')

