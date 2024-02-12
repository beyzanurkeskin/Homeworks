#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Name: Beyza Nur
# Surname: Keskin
# ID: 150200320


# In[3]:


import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import binom
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Coding (40 pts)

# ## Question 1

# ### Roulette Experiment
# We will do an experiment with a roulette wheel. Remember that there are 37 numbers on a roulette wheel.
# 
# **Calculating the Expectation:** $E[X] = \sum_{x \in X}{x\cdot p(x)}$
# 
# **Calculating the Variance:** $\text{VAR}[X] = E[(x - E[x])^2]$

# In[4]:


def calculate_expectation(numbers, probs):
    
    result = 0
    
    for i,j in zip(numbers,probs):
            
            result += i * j
    
    return result


def calculate_variance(numbers, probs):
        
    var1 = 0
    var2 = 0
    
    for i,j in zip(numbers,probs):
            
            var1 += i ** 2 * j
            
    for i,j in zip(numbers,probs):
            
            var2 += i * j
            
    
            
    result = var1 - (var2 **2)
    
    
    return result


roulette = [x for x in range(0,37)]             # list of the numbers on the slots of the roulette wheel


roulette_probs = ([(1 / len(roulette))]*37)     # list of the probabilities for each number in the wheel

roulette_expected_value = calculate_expectation(roulette, roulette_probs)
roulette_variance_value = calculate_variance(roulette, roulette_probs)
print(f"Expected value for dice: {roulette_expected_value:.3f}")
print(f"Variance for dice: {roulette_variance_value:.3f}")


# **Finding the average with experiments**

# In[5]:


def spin_wheel(n):
    
    array = np.empty(shape=[n])
    
    for i in range(n):
        
        record = random.randint(1,37) 
        array[i] = record
        
    return array

ns = [1,5,10,50,100,500,1000,5000,10000, 50000, 100000]               # number of spins

for n in ns:
    
    spins = spin_wheel(n)                                             # spinning the wheel for n times
                                                                      # calculate the mean of the spins
    mean = np.sum(spins) / n
    
    print(f"Average of {n} wheel spins: {mean:.3f}")


# ## Question 2

# ### Binomial Experiment
# In this part we will visualize the PMF and CDF.
# 
# We will use binomial distribution with n = 60.
# 
# We use three different experiment with probability of success of 0.2, 0.5 and 0.8 in order.
# #### Visualizing Probability Mass Function (PMF)

# In[6]:


n = 60 # number of trials
probs = [0.2, 0.5, 0.8] # probabilities for each experiments' successful
x = np.arange(0, 51, 1) # range
plt.figure(figsize=(12,6))

for prob in probs:
    
    # generate a discrete random variable with binomial distribution
    rv = binom(n,prob)
    # calculate PMF
    pmf = rv.pmf(x)
    plt.scatter(x, pmf)


plt.legend(["$p=0.2$","$p=0.5$","$p=0.8$"],fontsize=15)
plt.title("Probability mass function: $\\binom{n}{k}\, p^k (1-p)^{n-k}$\n",fontsize=20)
plt.xlabel("Number of successful trials ($k$)",fontsize=15)
plt.ylabel("Probability of success",fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.grid(True)
plt.show()


# In[7]:


pmf


# #### Visualizing Cumulative  Distribution Function (CDF)

# In[14]:


n = 50 # number of trials
probs = [0.2, 0.5, 0.8] # probabilities for each experiments' successful
x = np.arange(0, 51, 1) # range
plt.figure(figsize=(12,6))

def my_cdf(pmf):
    
    cdf = np.empty(shape=[len(pmf)+1])
    
    for i in range(len(pmf)+1):
        
        if i == 0:
        
            cdf[i] = pmf[i]
            
        else:
            
            cdf[i] = pmf[i] + cdf[i]
        
    return cdf
    
for prob in probs:
    
    # generate a discrete random variable with binomial distribution
    rv = binom(n, prob)
    # calculate PMF
    pmf = rv.pmf(x)
    plt.scatter(x, pmf)
    # calculate CDF 
    cdf = my_cdf(pmf)
    plt.scatter(x, cdf)

    
plt.legend(["$p=0.2$","$p=0.5$","$p=0.8$"],fontsize=15)
plt.title("Cumulative distribution function:",fontsize=20)
plt.xlabel("Number of successful trials",fontsize=15)
plt.ylabel("Cumulative probability of success",fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.grid(True)
plt.show()


# ## Question 3

# ## Real World Problem
# The possible locations of an endangered animal are determined and an evil zoo owner wants to track down this species. There are 19 detected locations and the possibility of each location to contain the animals is 0.05. However, the zoo owner is not sure whether that animal will be found in all determined locations. What is the probability that the animal could not be found in all of the locations? Find the approximate probability.
# 
# **Note:** Find the probablity with code!.
# 
# **Hint:** Use binomial distribution. Try with 20000 trials.

# In[12]:


n = 20000 # number of trials
p = 0.05 # probabilities for each experiments' successful
x = np.arange(0, 20, 1) # range

rv = binom(n,p)
pmf = rv.pmf(x)
pmf
    


# ## Question 4

# ## Probability Integral Transform
# Data values that are modeled as random variables from any continuous distribution can be modeled as a uniform distribution by using CDF. In this question, you are asked to obtain a uniform distribution from an exponential random variable.
# 
# **Hint:** Try with 100000 samples.

# In[ ]:


def exponential_cdf(x):
  # Find the cdf of exponential rv

def plot_uniform():
  # Plot both exponential random and obtained uniform distribution as histograms


# In[ ]:


plot_uniform()

