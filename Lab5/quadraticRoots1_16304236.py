#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:18:08 2019

Program to calculate the roots of a quadratic using 2 user defined functions.
Uder will enter A, B and C in the form A\xb2+Bx+C = 0

@author: shane
"""
import numpy as np # needed for basic math functions

#-----------------------------------------------------------------------------#
def root1(a, b, c):
    #let i = sqrt(b^2 - 4ac)
    i = (b*b) - (4*a*c)
    #check if complex
    if(i < 0):
        #get absolute value of i and square it
        i = np.sqrt(np.abs(i))
        #combine the real and imaginary part and return
        b = b*-1
        return (complex(b,i))/(2*a)
    #if i is not negative run formula as normal and return float
    else:
        return ((b*-1) + np.sqrt((b*b) - (4*a*c)))/(2*a)
#-----------------------------------------------------------------------------#
def root2(a, b, c):
    #let i = sqrt(b^2 - 4ac)
    i = (b*b) - (4*a*c)
    #check if complex
    if(i < 0):
        #get absolute value of i and square it
        i = np.sqrt(np.abs(i))
        #combine the real and imaginary part and return
        b = b*-1
        #root 2 is negative
        i = i*-1
        return (complex(b,i))/(2*a)
    #if i is not negative run formula as normal and return float
    else:
        return ((b*-1) - np.sqrt((b*b) - (4*a*c)))/(2*a)
#-----------------------------------------------------------------------------#
    
#Main method starts here
#inform the user what is happening
print("This programme will calculate the roots of a quadratic")
print("Using 2 user defined functions.")

ans = "Y" #default used to enter the loop
while (ans == "Y" or ans == "y"):
    #inform the user on how to enter the values
    print("Using a quadratic of the form Ax\xb2+Bx+C = 0")
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))

    #call the root methods and pass in a,b and c
    ans_root1 = root1(a, b, c)
    ans_root2 = root2(a, b, c)
    
    #print the result in a formatted output
    print("The roots of", a, "x\xb2 +", b, "x +", c, "are:")
    print("{0:>8}".format("x ="), \
          "{0:>2.3f}".format(ans_root1), \
          "{0:>8}".format("x ="), \
          "{0:<20.3f}".format(ans_root2))
    
    #ask the user if they want to continue
    ans = input("\nDo you want to try another cone (Y/N): ")
