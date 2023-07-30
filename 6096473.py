#!/usr/bin/env python
# coding: utf-8

# Beyza Nur Keskin
# 
# 150200320

# ### Source Code of Question 3

# In[9]:


# Lagrange interpolation method to calculate interpolated value at x
def lagrange_interpolation(x, x_values, y_values):
    
    n = len(x_values)
    interpolated_value = 0.0
    
    for i in range(n):
        basis = 1.0
        for j in range(n):
            if i != j:
                basis *= (x - x_values[j]) / (x_values[i] - x_values[j])
        interpolated_value += basis * y_values[i]
    
    return interpolated_value

# Lets test our values
x_values = [-1.2, 0.3, 1.1]
y_values = [-5.76, -5.61, -3.69]

# Get an input from user
num = float(input("Enter a number: "))

#Print result
interpolated_value = lagrange_interpolation(num, x_values, y_values)
print("The interpolated value at x =", num, f"is {interpolated_value}")


# In[ ]:




