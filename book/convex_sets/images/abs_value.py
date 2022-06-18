import matplotlib.pyplot as plt
import numpy as np
# 100 linearly spaced numbers
x = np.linspace(-5,5,101)

# the function
y = np.abs(x)
# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r')
plt.savefig('func_abs_value_1d.png')
