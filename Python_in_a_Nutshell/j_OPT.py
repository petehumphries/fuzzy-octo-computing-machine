
# coding: utf-8

# In[1]:


#
# Finding a Minimum of a Function
# C:\Users\User1\j_OPT
#
import numpy as np
import scipy.optimize as sco

# Finding a Minimum


def y(x):
    ''' Function to Minimize. '''
    if x < -np.pi or x > 0:
        return 0.0
    return np.sin(x)


gmin = sco.brute(y, ((-np.pi, 0, 0.01), ), finish=None)  # global optimization
lmin = sco.fmin(y, -0.5)  # local optimization

# Result Output
print("Global Minimum is %8.6f" % gmin)
print("Local Minimum is  %8.6f" % lmin)

import os
print(os.path.abspath("j_OPT"))

