#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:30:45 2019

This programme calculates values of the function y=x*x in the range [0,1]
in steps of size deltaX = 1/m where m is supplied by the user. 

@author: shane
"""

#inform the user what is happening
print("\nThis programme calculates values of the function y=x*x")
print("in steps of size deltaX = 1/m where m is supplied by the user.")

#declare and initalize the end points
x0, x1 = 0.0, 1.0

#get the number of intervals from the user
m = int(input("Enter the number of intervals (e.g., 10): "))

#set the step size
deltaX = ((x1-x0)/m)

#put a header on the table of values
title1, title2 = "x", "x*x"

print("{0:>5}".format(title1), \
      "{0:>10}".format(title2))

#Evaluate and print the function in a for loop
for i in range(1,m+1):
    #initial value is 1; want to include end point, default increment is 1
    x = x0 + i*deltaX
    #right justified
    print("{0:>5.3f}".format(x), \
          "{0:>10.3f}".format(x*x))