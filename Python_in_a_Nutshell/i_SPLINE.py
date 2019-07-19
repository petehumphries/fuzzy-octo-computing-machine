
# coding: utf-8

# In[1]:


# Cubic Spline Interpolation
# C:\Users\User1\i_SPLINE
#

import numpy as np
import scipy.interpolate as sci
import matplotlib.pyplot as plt

# Interpolation
x = np.linspace(0.0, np.pi / 2, 20)  # x values
y = np.cos(x)  # function values to interpolate
gp = sci.splrep(x, y, k=3)  # cubic spline interpolatiln
gy = sci.splev(x, gp, der=0)  # calculate interpolated values

# Graphical Output
plt.figure()
plt.plot(x, y, 'b', label='cosine')  # plot original function values
# plot interpolated function values
plt.plot(x, gy, 'ro', label='cubic splines')
plt.legend(loc=0) # label= "Approximation od cosine function....")
plt.title("Approximation of cosine function line by cubic splines interpolation (red dots)", y=-.20)
# negative y co-ordinate puts title below x-axis

plt.grid(True)
plt.show(True)

import os
print(os.path.abspath("i_SPLINE"))

