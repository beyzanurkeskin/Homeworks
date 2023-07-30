#!/usr/bin/env python
# coding: utf-8

#  

# #### Student name : Beyza Nur Keskin
# #### Student ID       : 150200320 

#  

# ### Question 4
# Construct a program implementing the bisection method so that its inputs are a, ϵ and
# output is x such that |a
# 1
# 5 − x| ≤ ϵ. Show that the implementation works by giving two
# examples.
# 

# In[14]:


# For the bisection method, it is necessary to specify a lower and upper limit.
# I could identify them more easily by hand, but on the machine things get a little more complicated.
# so I set the lower limit to 0. The program first selects a value in the middle of the lower and upper 
# limits as the calculated value and compares it with epsilon by taking the margin of error.
# It continues to do this until it reaches the desired result.

def bisec(a, epsilon):
    
    lower_bound = 0                           # i set a lower limit
    upper_bound = a                           # i set a upper limit
    
    
    calc = (lower_bound + upper_bound) / 2    # i set the value to be calculated
    
     
    while abs(a**(1/5) - calc) > epsilon:     # i wrote a loop where the operations will be executed
        
        if calc**5 < a:
            lower_bound = calc
        else:
            upper_bound = calc
        calc = (lower_bound + upper_bound) / 2s
    
    return calc                               # i printed the result


# #### EXAMPLES
# 

# In[16]:


x = bisec(100, 0.001)
print(x)


# In[17]:


x = bisec(33, 0.01)
print(x)


# ##### Thank you!
