#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:44:35 2019

Calculates the value of the sine() and cosine functions at 12
equal intervals between 0 and 2*Pi

@author: shane
"""
import numpy as np #required for basic math functions

#inform the user whats happening
print("This programme calculates the value of the sine() and cosine")
print("functions at 12 equal intervals between 0 and 2*Pi.")

#get the number of intervals from the user
m = int(input("Enter the number of intervals (e.g., 12): "))

#calculate the step size
degrees = 0

#put a header on the table of values
title1, title2, title3, title4 = "x(rad)", "x(degrees)", "sin(x)", "cos(x)"

#print the titles in a formatted output
print("{0:>8}".format(title1), \
      "{0:>12}".format(title2), \
      "{0:>16}".format(title3), \
      "{0:>16}".format(title4))

for i in range(0,m+1):
    #convert the value to radians
    theta = degrees*(np.pi/180)
    
    #print the value of degrees
    #calculate sin
    #calculate cosine
    print("{0:>8.3f}".format(theta), \
          "{0:>12.3f}".format(degrees), \
          "{0:>16.3f}".format(np.sin(theta)), \
          "{0:>16.3f}".format(np.cos(theta)))
    
    #increment the value of degrees 
    degrees += (360/m)
    