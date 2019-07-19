
# coding: utf-8

# In[3]:


#input variable sanity check
import numpy as np
from c_parameters import *

# Easier to change input variables using notepad++ rather than using Jupyter
# Inputs are pulled in from c_parameters.py
# Will use K from c_parameters.py when using BSM_call_value(S0, K, T, r, vola), even though K is specified in BSM_valuation.py

# This method uses a nested loop in a manner similar to C++, utilizing the command np.zeros(i,j),dtype=np.float)
# which initializes a Numpy Array i x j where each number is of the double float variety

# Matrix S shows the evolution of stock price S
# Matrix iv shows the evolution of inner value max(St-K,0) given matrix S
# Matrix pv given the pv based on V

print("***Input parameter check***")
print("S0 is " , S0) 
print("K is ", K)
print("r is ", r)
print("T is ", T) # call option maturity
print("r is ", r) # constant short rate
print("vola is ", vola) # constant volatility factor of diffusion

#path sanity check
import os
print(os.path.abspath("c_parameters"))
print(os.path.abspath("d_CRR1979_loop"))


# Valuation of European Call Option in CRR1979 Model
# Loop Version (= C-like Iterations)
# C:\Users\User1\d_CRR1979_loop
#

import numpy as np
from c_parameters import *

# Array Initialization for Index Levels
S = np.zeros((M + 1, M + 1), dtype=np.float)  # index level array
S[0, 0] = S0
z = 0
for j in range(1, M + 1, 1):
    z += 1
    for i in range(z + 1):
        S[i, j] = S[0, 0] * (u ** j) * (d ** (i * 2))

# Array Initialization for Inner Values
iv = np.zeros((M + 1, M + 1), dtype=np.float)  # inner value array
z = 0
for j in range(0, M + 1, 1):
    for i in range(z + 1):
        iv[i, j] = round(max(S[i, j] - K, 0), 8)
    z += 1

# Valuation by Risk-Neutral Discounting
pv = np.zeros((M + 1, M + 1), dtype=np.float)  # present value array
pv[:, M] = iv[:, M]  # initialize last time step
z = M + 1
for j in range(M - 1, -1, -1):
    z -= 1
    for i in range(z):
        pv[i, j] = (q * pv[i, j + 1] + (1 - q) * pv[i + 1, j + 1]) * df

# Result Output
print("Value of European call option is %8.3f" % pv[0, 0])
print("--------------------------------------------------")
print("Bssed on the folowing input parameters:")
print("--------------------------------------------------")
print("S0 is " , S0, "  intial stock price") 
print("K is ", K, "  strike")
print("T is ", T, "  maturity")
print("r is ", r, "  constant short rate")
print("vola is ", vola, " constant volatility")
print("--------------------------------------------------")

import os
print("Parameters imported from ",os.path.abspath("c_parameters"))

