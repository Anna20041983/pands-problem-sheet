# My solution to weekly task 8

# Program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes
# Author: Anna Kozakiewicz

# First we need to import and name numpy and matplotlib.pyplot

import numpy as np
import matplotlib.pyplot as plt

# Then we can change background color to dark 
# Resource of the code for dark background: https://matplotlib.org/3.1.0/gallery/style_sheets/dark_background.html

plt.style.use('dark_background')

# Next we write our functions and add names and colours to each of them

xpoints = np.array (range(0, 4))
gpoints = xpoints * xpoints
hpoints = xpoints * xpoints * xpoints

plt.plot (xpoints, xpoints, label = 'straight', color='yellow') 
plt.plot (xpoints, gpoints, label = 'xsquared', color = 'orange')
plt.plot (xpoints, hpoints, label = 'xcubed', color = 'red')

# The last step is to show the plot with assign legend

plt.legend()
plt.show()