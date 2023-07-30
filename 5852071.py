#!/usr/bin/env python
# coding: utf-8

# # 

# Beyza Nur Keskin
# 
# 150200320

# # 

# In[4]:


import math                                                                 # imported necessary moduls
import time
import numpy as np
import matplotlib.pyplot as plt
                                                                            # I define x,y first so as not to write it again

x = [0.5 ,1, 1.5, 2 ,2.5, 3 ,3.5, 4 ,4.5, 5,5.5, 6, 6.5 ,7, 7.5, 8 ,8.5, 9, 9.5 ,10] 
y = [0.72, 1.63 ,1.88 ,3.39 ,4.02 ,3.89, 4.25, 3.99, 4.68, 5.03, 5.27, 4.82, 5.67 ,5.95 ,5.72, 6.01, 5.5, 6.41, 5.83 ,6.33]


# # 

# ### 4.d.a

# In[57]:


b = 0.5002 
a = 1.92345 

plt.figure(figsize=(10, 7))                                              # plotted the graph for seciton d
plt.scatter(x, y, color='green', label='data points',alpha = 0.5)
plt.plot(x, [a + b * xi for xi in x], color='purple', label='linear regression',alpha = 0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


# # 

# ### 4.d.b

# In[81]:


e = 0.603
d = 1.220
c = -0.069

plt.figure(figsize=(10, 7))                                                # plotted the graph for seciton d
plt.scatter(x, y, color='blue', label='Data points',alpha = 0.2)

xfit = np.linspace(0, 10, 20)
yfit = c*(xfit**2) + d*xfit + e
plt.plot(xfit, yfit, color='pink', label='Estimated polynomial')

plt.legend()
plt.show()


# # 

# ### 4.d.c

# In[86]:


k, m = 1.781 , 1.945                                # calling the function

plt.figure(figsize=(10, 7))                                              # plotted the graph for seciton d
x_vals = np.linspace(0.1, 10, 100)
y_vals = k + m * np.log(x_vals)

plt.plot(x, y, 'o',color= "black", label='Data Points',alpha=0.6)
plt.plot(x_vals, y_vals, label='Logarithmic Function',alpha=0.5)
plt.legend()
plt.show()

