
# coding: utf-8

# In[10]:


#
# Valuation of European Call Option
# in Black-Scholes-Merton Model
# A_pyt/b_BSM_valuation.py
#
#input variable sanity check
import numpy as np
from c_parameters import *

from scipy import stats
import math

# Option Parameters
S0 = 105.00  # initial index level
K = 100.00  # strike price
T = 1.  # call option maturity
r = 0.05  # constant short rate
vola = 0.25  # constant volatility factor of diffusion

# Analytical Formula


def BSM_call_value(S0, K, T, r, vola):
    ''' Analytical European call option value for Black-Scholes-Merton (1973).
    Parameters
    ==========
    S0: float
        initial index level
    K: float
        strike price
    T: float
        time-to-maturity
    r: float
        constant short rate
    vola: float
        constant volatility factor
    Returns
    =======
    call_value
    '''
    S0 = float(S0)  # make sure to have float type
    d1 = (math.log(S0 / K) + (r + 0.5 * vola ** 2) * T) / (vola * math.sqrt(T))
    d2 = d1 - vola * math.sqrt(T)
    call_value = (S0 * stats.norm.cdf(d1, 0.0, 1.0) -
                  K * math.exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
    return call_value


if __name__ == '__main__':
    print("Value of European call option is %8.3f"
          % BSM_call_value(S0, K, T, r, vola))
    
# Result Output

print("Value of European call option using BSM valuation is %8.3f" % BSM_call_value(S0, K, T, r, vola))
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

