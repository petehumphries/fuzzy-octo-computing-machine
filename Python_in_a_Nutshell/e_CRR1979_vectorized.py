
# coding: utf-8

# In[1]:


# Valuation of European Call Option in CRR1979 Model
# Vectorized Version (= NumPy-level Iterations)
# C:\Users\User1\BSM_valuation

# Python vectorized approach to valuation
# Val difference calculated at end

import numpy as np
from c_parameters import *

# Array Initialization for Index Levels
mu = np.arange(M + 1)
mu = np.resize(mu, (M + 1, M + 1))
md = np.transpose(mu)
mu = u ** (mu - md)
md = d ** md
S = S0 * mu * md

# Valuation by Risk-Neutral Discounting
pv = np.maximum(S - K, 0)  # present value array initialized with inner values
z = 0
for i in range(M - 1, -1, -1):  # backwards induction
    pv[0:M - z, i] = (q * pv[0:M - z, i + 1] +
                      (1 - q) * pv[1:M - z + 1, i + 1]) * df
    z += 1

# Result Output

print("Value of European call option using vectorized approach is %8.3f" % pv[0, 0])
print("--------------------------------------------------")
print("Bssed on the folowing input parameters:")
print("--------------------------------------------------")
print("S0 is " , S0, "   intial stock price") 
print("K is  ", K, "   strike")
print("T is  ", T, "     maturity")
print("r is   ", r, "   constant short rate")
print("vola is ", vola, "  constant volatility")
print("--------------------------------------------------")

#path sanity check
import os
print(os.path.abspath("BSM_valuation"))
print(os.path.abspath("c_parameters"))

# Comparing with C++ nested loop style valuation

from BSM_valuation import BSM_call_value
BSM_call_value(S0, K, T, r, vola)
val_diff = pv[0, 0] - BSM_call_value(S0, K, T, r, vola)
print("Vectorized vs Nested Loop Valuation difference  = ", val_diff)

