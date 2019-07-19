
# coding: utf-8

# In[1]:


#
# Numerically Integrate a Function
# C:\Users\User1\k_INT
#
import numpy as np
from scipy.integrate import quad

# Numerical Integration


def f(x):
    ''' Function to Integrate. '''
    return np.exp(x)


int_value = quad(lambda u: f(u), 0, 1)[0]

# Output
print("Value of the integral is %10.9f" % int_value)

import os
print(os.path.abspath("k_INT"))

