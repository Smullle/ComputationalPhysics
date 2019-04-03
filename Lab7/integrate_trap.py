#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:33:13 2019

This program will make use of two functions to calculate the integral of sin(x)
given limits entered by the user. Both the trapezoidal and Simpson's 1/3 rule.
The result of each will be compared with the analytical solution and an error 
will be calculated. 

@author: shane
"""

import numpy as np #needed for basic math functions
from scipy.integrate import quad #needed for integration

#-----------------------------------------------------------------------------#
def f(x):
    """
    This function will take in x and return sin(x)
    """
    return np.sin(x)
#-----------------------------------------------------------------------------#
def my_trap(a, b, acc):
    """
    This function will calculate the intergral using the trapezoidal method.
    It will use the limits entered by the user which are 
    passed into the function.
    """
    
    #get step size
    h = (b-a)/acc
    #set total length = 0
    tot = 0
    
    #first 2 parts of trap rule
    tot += f(a)
    tot += f(a + h)
    
    #increment step
    a += h
    
    #whilw loop to run through midde part of formula
    while((a + h) < b):
        tot += f(a)
        tot += f(a + h)
        a += h
        
    #last 2 parts of trap rule    
    tot += f(a)
    tot += f(b)
        
    #multiply by step/2
    h = h/2
     
    #return result
    return h*tot
#-----------------------------------------------------------------------------#
def my_simp(a, b, acc):
    """
    This function will calculate the intergral using Simpson's 1/3 method.
    It will use the limits entered by the user which are passed 
    into the function.
    """

    #get step size
    h = (b-a)/acc
    #set total length = 0
    tot = 0
    
    #first part of simp rule
    tot += f(a)
    tot += 4*f(a + h)
    
    #increment step
    a += h
    
    #while loop for middle part of simp rule
    while((a + h) < b):
        tot += 4*f(a)
        tot += 2*f(a + h)
        a += h
     
    #last part of simp rule    
    tot += 4*f(a)
    tot += f(b)
    
    #multiply by step/3    
    h = h/3
        
    #return result
    return (h*tot)/2
#-----------------------------------------------------------------------------#
def error(ans, a, b):
    """
    This function will calculate the analytical solution to the integral and
    the result will be used to calculate the error and the respective calculation
    https://stackoverflow.com/questions/50785188/numeric-integral-of-sinx-x
    """
    
    #use lambda function to set exuation and pass to quad funtion in scipy
    #quad will return an array only first value is needed so add [0] to end
    actual = quad(lambda x : np.sin(x), a, b)[0] 
    
    #return the abs of answer as simp rule overestimates
    return abs(actual - ans)
#-------------------------------Main Method-----------------------------------#

#inform the user that is happening
print("This programme estimates the integral of the function sin(x)")
print("in the intevral [a, b] using both the trapezoidal rule")
print("and simpsons 1/3 rule.")

check = "y"

#Keep running until user enters N
while(check =="y" or check == "Y"):

    #get input from user
    a = float(input("Enter the lower limit a (e.g, 0): "))
    b = float(input("Enter the lower limit b (e.g, 1.0): "))
    
    #used for formatted output
    title1 = "No. of intervals"
    title2 = "Trap Estimate"
    title3 = "Trap Error"
    title4 = "Simp Estimate"
    title5 = "Simp Error"
    
    #values required to enter loop
    n = 2
    simpError  = 2
    
    #print formatted titles
    print("{0:>20}".format(title1),\
          "{0:>20}".format(title2),\
          "{0:>20}".format(title3),\
          "{0:>20}".format(title4),\
          "{0:>20}".format(title5))
        
    #while loop will run until error is low enough
    while(simpError>1e-10):
        
        #obtain all values needed using given methods
        trapAns = my_trap(a, b, n)
        trapError = error(trapAns, a, b)
        simpAns = my_simp(a, b, n)
        simpError = error(simpAns, a, b)
        
        #print reults in formatted output
        print("{0:>20}".format(n),\
              "{0:>20.11f}".format(trapAns),\
              "{0:>20.11f}".format(trapError),\
              "{0:>20.11f}".format(simpAns),\
              "{0:>20.11f}".format(simpError))   
        
        #increase interval
        n *= 2
        
    #Ask the user if they wish to continue
    print("\nDo you want to enter another range?")
    check = input("Enter Y to continue or N to exti: ")
