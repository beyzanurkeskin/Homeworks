#!/usr/bin/env python
# coding: utf-8

# Beyza Nur Keskin
# 
# 150200320

# ### Source Code of Question 2

# In[14]:


# Calculate the divided difference table
def divided_difference(x_values, y_values):
    
    n = len(x_values)
    divided_diff_table = [[0] * n for _ in range(n)]
    
    for i in range(n):
        divided_diff_table[i][0] = y_values[i]
    
    for j in range(1, n):
        for i in range(n - j):
            divided_diff_table[i][j] = (divided_diff_table[i+1][j-1] - divided_diff_table[i][j-1]) / (x_values[i+j] - x_values[i])
    
    return divided_diff_table

# Perform interpolation using divided difference table
def interpolate(x, x_values, y_values):
    
    n = len(x_values)
    result = 0.0
    
    divided_diff_table = divided_difference(x_values, y_values)
    
    for i in range(n):
        term = divided_diff_table[0][i]
        for j in range(i):
            term *= (x - x_values[j])
        result += term
    
    return result

# Lets test our values
x_values = [0,1,2,4]
y_values = [1,9,23,93]

# Get an input from user
num = float(input("Enter a number: "))

#Print result
interpolated_value = interpolate(num, x_values, y_values)
print("The interpolated value at x = ", num,  f"is {interpolated_value}")

