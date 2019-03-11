#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:21:16 2019

Produces a table of n, sum(1..n), exp(n), n! and ln(n!)
where n is any integer entered by the user 

@author: shane
"""

#inform the user what is happening
print("This programme produces a table of n, sum(1..n), exp(n), n! and ln(n!)")
print("where n is any integer entered by the user.")
print("To exit enter a number less than 0")

import numpy as np #required for basic math functions
import math

#check used in while loop
check = 0;

#Ask the user to enter a positive integer n
n = int(input("Enter a positive integer n within range of (0-20): "))

#while loop will run until a valid number is entered
while(check == 0):
    #exit the program if a number < 0 is entered
    if(n < 0):
        break
    #keep asking for a number if not within required range
    if(n<=0 or n >= 20):
        print("\nNumber not in range, must be >= 0 and <= 20.")
        n = int(input("Enter a positive integer n within range of (0-20): "))
    #if valid number print output
    if(n>=0 and n <= 20):
        #needed to exit while loop
        check = 1
        
        #set the initial value of n to 0
        nBase = 0
            
        #put a header on the table of values
        title1, title2 = "n", "sum(1..n)"
        title3, title4, title5 = "exp(n)","n!", "ln(n!)", 
            
        #print the titles in a formatted output
        print("{0:>8}".format(title1), \
              "{0:>10}".format(title2), \
              "{0:>18}".format(title3), \
              "{0:>20}".format(title4), \
              "{0:>10}".format(title5))
        
        for i in range(0,n+1):
            fac = math.factorial(nBase)
            print("{0:>8}".format(nBase), \
                  "{0:>10.3f}".format(np.sum(nBase)), \
                  "{0:>18.3f}".format(np.exp(nBase)), \
                  "{0:>20}".format(fac), \
                  "{0:>10.5}".format(np.log(fac)))
            
            #increment the value of n
            nBase += 1

