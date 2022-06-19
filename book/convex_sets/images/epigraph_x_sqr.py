import matplotlib.pyplot as plt
import numpy as np
# 100 linearly spaced numbers
x = np.linspace(-5,5,101)

# the function
y = x**2
# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.spines['left'].set_position('center')
#ax.spines['left'].set_color('none')
#ax.spines['bottom'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_visible(False)
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'k')
plt.fill_between(x, y, np.max(y), color='#CCCCCC')
plt.savefig('pic_epigraph_x_sqr.png')
