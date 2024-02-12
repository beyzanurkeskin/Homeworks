#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Name: Beyza Nur 
# Surname: Keskin
# ID: 150200320


# ## Coding

# ### Question 1

# A probability class has N students enrolled. What is the probability that at least two of the students will have the same birthday?
# 
# Calculate with python using random and matplotlib libraries only. N $\in [1, 100]$ and simulation should be done with $10000$ iterations. 
# 
# Plot the probabilities (x axis 0 to 100 N values, y axis probabilities).

# In[47]:


import random
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
random.seed(0)                             

# no other library is necessary

ntrials = 10000
N = 100
day = 365



def random_bday():                             # create a function to select a random birthday 
    
    bday = random.randint(1,day)               # select a random birthday 
    return bday                                # return a random birthday 




def all_bday(num):                              # create a function to select a random birthday each person up to N
    
    bdays = [random_bday() for i in range(num)] # create a list for saving these birtdays
    return bdays                                # return birthdays



def coincidence(bdays):                          # create a function to find people with the same birthday
    
    unique = set(bdays)                          # i created a set so i can separate the repeated birthdays
    num_bdays = len(bdays)
    num_unique= len(unique)
    coincidence = (num_bdays != num_unique)      # the #of unique and bdays will not be equal if they have the same birthday
    return coincidence                           # return coincidence




def find_samebdays(N):
    
    num_cdc = 0                                # in the beginning i created a value of 0 to find the number of coincidence
    
    for i in range (ntrials):                  # the code will set birthdays for N people the first time. But I want it to
                                               # try it ntrials times to give a more accurate estimate. so I wrote this loop
            
            
        bd = all_bday(N)                       # I call this function to assign random birthdays to N people
        cn = coincidence(bd)           # I call this function to check coincidence 
        if cn:                        # If it's a coincidence I increase the initial num_cdc by 1
            num_cdc += 1 
     
    prob = num_cdc / ntrials                   # I'm calculating the probability
    return prob                                # return probability
 

prob_same_birthday = find_samebdays(N)         # run my code


print(prob_same_birthday)                      # i print the result


xpoints = []                                   # I made a list for line x
ypoints = []                                   # I made a list for line y

for i in range(N+1):
    xpoints.append(i)                          # I placed the number N on the x-axis
    ypoints.append(find_samebdays(i))          # I placed its probabilities on the y-axis.
    
    
f = plt.figure()                               # I arrange the size
f.set_figwidth(6)      
f.set_figheight(6)
    
plt.plot(xpoints, ypoints)                     # I plot the probabilities
plt.show()


# ### Question 2

# In a restaurant, 7 friends sit around a table. Each one orders a different meal, but the waiter did not mark positions. He has the correct 7 orders but gives a random meal to each person
# (each of the assignments is equally likely).
# 
# What is the probability that a $i$ people have the dish they ordered placed in front of them where $i \in [0, 7]$?
# 
# Calculate with python with only matplotlib library and print the probabilities. Visualize the results via bar plot (x axis 0 to 7, y axis probabilities). 
# 
# Report and comment the results in your report.

# In[88]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from math import comb


# no other library is necessary                     it is said not necessary but not forbidden                          

N = 7                                                    # #of people

xpoints = []                                             # I made a list for line x
ypoints = []                                             # I made a list for line y

for i in range(1,8):
    
    xpoints.append(i)                                    # Append i to xpoints to draw plot
    
    c = comb(N,i) * (0.5 ** i) * (0.5 ** (N - i))        # I wrote Binomial Function
    
    ypoints.append(c)                                    # Append c to ypoints to draw plot
    
f = plt.figure()                                         # I arrange the size
f.set_figwidth(6)      
f.set_figheight(6)
    
plt.plot(xpoints, ypoints)                               # I plot the probabilities
plt.show()  



# In[ ]:




