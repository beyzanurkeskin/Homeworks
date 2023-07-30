#!/usr/bin/env python
# coding: utf-8

# # 

# Beyza Nur Keskin
# 
# 150200320

# # 

# ### 1.d

# In[7]:


def f(x):                                                                    # defined my function                                             
    return 4*math.log(x) - x                           

def f_deriv(x):                                                              # defined my function's derivative
    return 4/x - 1

def newton_method(x0, tol, iter):
    
    x_prev = x0                                                              # defined initial value
    iterates = []                                                            # defined a list to keep iterations
    errors = []                                                              # defined a list to keep errors
    
    for n in range(1, iter+1):                                               # set the number of iterations

        
        fx = f(x_prev)                                                       # calculated the initial value
        fx_deriv = f_deriv(x_prev)                                           # calculated the initial value's derivative
        x_new = x_prev - (fx / fx_deriv )                                    # calculated the new x value w/ newton method
        error = abs(x_new - x_prev)                                          # calculated the error
        errors.append(error)                                                 # add error to list
        
        if error < tol:                                                      # wrote to stop the loop
            break
            
        iterates.append(x_new)                                               # add x_new to list
        x_prev = x_new                                                       # assigned it to use in the next step
        
    return iterates, errors                                                  # return the lists

def secant_method(x0, x1, tol, iter):
    
    x_prev = x0                                                              # defined initial value
    x_curr = x1                                                              # defined second value
    iterates = [ ]                                                           # defined a list to keep iterations
    errors = []                                                              # defined a list to keep errors
    
    for n in range(2, iter+1):
        
        fx_prev = f(x_prev)                                                   # calculated the initial value
        fx_curr = f(x_curr)                                                   # calculated the second value
        x_new = x_curr - (fx_curr * (x_curr - x_prev)) / (fx_curr - fx_prev)  # calculated the new x value w/ secant method
        error = abs(x_new - x_curr)                                           # calculated the error
        errors.append(error)                                                  # add error to list
        
        if error < tol:                                                       # wrote to stop the loop
            break
            
        iterates.append(x_new)                                                # add x_new to list
        
        x_prev = x_curr                                                       # assigned it to use in the next step
        x_curr = x_new
        
    return iterates, errors                                                   # return the lists

choise = input("Which method would you like to use? Newton(n) or Secant(s): ")# Since x1 is not necessary for newton,
                                                                              # I wrote separate functions for both methods

if choise == "n":
    
    x0 = int(input("Please enter the initial value: "))
    tol = 1e-6                                                                # defiend target margin of error
    iter = int(input("Please enter the maximum iterations: "))
    
    
    newton_iterates, newton_errors = newton_method(x0, tol, iter)             # assigned it to print my results
    print("Newton Method:\n")
    print("Iterates:\n ", newton_iterates)
    print("Errors:\n ", newton_errors)
    
elif choise == "s":
    
    x0 = int(input("Please enter the initial value: "))
    x1 = int(input("Please enter the second value: "))
    tol = 1e-6
    iter = int(input("Please enter the maximum iterations: "))
    
    secant_iterates, secant_errors = secant_method(x0, x1, tol, iter)        # assigned it to print my results
    print("\nSecant Method:\n")
    print("Iterates:\n ", secant_iterates)
    print("Errors:\n ", secant_errors)

print("End of the code...")                                                  # outputs print as a list


# # 
