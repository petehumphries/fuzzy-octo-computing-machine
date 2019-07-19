
# coding: utf-8

# In[1]:


#
# Two Financial Option Classes
# C:\Users\User1\k_INT
#
#
import math
import scipy.stats as scs

# Class Definitions


class Option(object):
    ''' Black-Scholes-Merton European call option class.
    Attributes
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
    '''

    def __init__(self, S0, K, T, r, vola):
        ''' Initialization of Object. '''
        self.S0 = float(S0)
        self.K = K
        self.T = T
        self.r = r
        self.vola = vola

    def d1(self):
        ''' Helper function. '''
        d1 = ((math.log(self.S0 / self.K) +
               (self.r + 0.5 * self.vola ** 2) * self.T) /
              (self.vola * math.sqrt(self.T)))
        return d1

    def value(self):
        ''' Method to value option. '''
        d1 = self.d1()
        d2 = d1 - self.vola * math.sqrt(self.T)
        call_value = (self.S0 * scs.norm.cdf(d1, 0.0, 1.0) -
                      self.K * math.exp(-self.r * self.T) *
                      scs.norm.cdf(d2, 0.0, 1.0))
        return call_value


class Option_Vega(Option):
    ''' Black-Scholes-Merton class for Vega of European call option. '''

    def vega(self):
        ''' Method to calculate the Vega of the European call option. '''
        d1 = self.d1()
        vega = self.S0 * scs.norm.cdf(d1, 0.0, 1.0) * math.sqrt(self.T)
        return vega
    
import os
print(os.path.abspath("k_INT"))


# In[2]:


o1 = Option(105., 100., 1.0, 0.05, 0.25)


# In[3]:


o1.value()


# In[4]:


o1.vega() #fails to illustrate class vs attribute vs method


# In[5]:


o2 = Option_Vega(105., 100., 1.0, 0.05, 0.25)


# In[6]:


o2.value()


# In[7]:


o2.vega()

