#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:34:41 2019

This program computes the length of a semicircle 
by considering it as a number of straight sections joined together.

@author: shane
"""
import numpy as np #needed for basic math functions

#-----------------------------------------------------------------------------#

#used to get the y value in x^2 + y^2 = 1 when given x
def f(x):
    return np.sqrt(np.abs(1-(x*x)))
#-----------------------------------------------------------------------------#

#method to find the distance between two points
def new_length(x, dx):
    y1 = f(x)
    y2 = f(x + dx)
    return np.sqrt(((dx)**2)+((y2 - y1)**2))
#-----------------------------------------------------------------------------#

#-------------------------------Main Method-----------------------------------#

#inform the user what is happening
print("This programme estimates the length of a semicircle of radius r = 1")
print("By considering it as n straight sections.")

print("\nThe greater the value of n, the more accurate the answer.")

c_length = 0 #total length of semicircle
x = 0

#coordinates of semicircle
x_max = 1
x_min = -1

#used to find error and change step size
c_error = 1
n = 1

#used to print formatted output
title1 = "n"
title2 = "length"
title3 = "error"

#print the formatted titles
print('\n{0:>18}'.format(title1), ' | ', \
      '{0:>18}'.format(title2), ' | ', \
      '{0:>17}'.format(title3))

#while loop will run until error is above 1e-6
while(c_error >= 1e-6):

    dx = (x_max - x_min)/n #step size
    
    #calculate the length of n segments
    for i in range(0,n):
        #increment x with every new secion
        x = x_min + (i*dx) 
        
        #add each new length to total
        c_length  += new_length(x, dx) 
        
        #re-calculate error for each
        c_error = np.pi - c_length 
        
    #print the results in a formatted output
    print('{0:>18}'.format(n), ' | ', \
          '{0:>18.7f}'.format(c_length), ' | ', \
          '{0:>17.7f}'.format(c_error))
    
    c_length = 0 #reset total length
    n = n*2      #increment n as incrementing by 1 will take too long
    
    #incrementing by 10 will take too long and cause memory	
    #to fill before reaching required error.
    #n += 10     
		 
    
