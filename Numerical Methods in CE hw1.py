#!/usr/bin/env python
# coding: utf-8

#  

# #### Student name : Beyza Nur Keskin
# #### Student ID       : 150200320 

#  

# ### Question 2
# Construct a program whose input is a rational number and output is the corresponding
# binary. Implement the method that we saw in the class. Give some examples to show that
# your program works as expected.
# 

# In[9]:


#To convert a number to binary, we keep dividing until we get 1/2. By reading the rest from bottom to top,
#we learn the binary equivalent of that number.


def convert(num):
    
    integer = int(num)                              # i separated number to int 
    fractional = num - integer                      # and fractional part
    
    
    bin_int = ""                                    # i specify such an empty str variable so that I can write it as 
                                                    # 1010 later, otherwise it will return to
    bin_frac = ""                                   # addition and subtraction operations
                                      
  

    while integer != 0:                             # for the int part, I wrote a while loop to perform the operations 
                                                    # required to convert it to binary
        bin_int = str(integer % 2) + bin_int
        integer //= 2
      
    while fractional != 0:                          # for the fractional part, I wrote a while loop to apply the 
                                                    # necessary operations to convert it to binary      
        fractional *= 2
        
        if fractional >= 1:
            
            bin_frac += "1"
            fractional -= 1
            
        else:
            
            bin_frac += "0"
    
    
    binary = bin_int + "." + bin_frac              # i print the result
    
    return binary                                  # i return the result


# #### EXAMPLES 

# In[11]:


convert(16)


# In[12]:


convert(1625)


# In[13]:


convert(16.625)


# ##### Thank you!
