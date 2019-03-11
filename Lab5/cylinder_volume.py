#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:45:45 2019

Program to calculate the surface area of a cone when the radius and height is
supplied by the user, using a user defined fumction.

@author: shane
"""
import numpy as np #required for basic math functions

#-----------------------------------------------------------------------------#
def cone_area(r_value, h_value):
    l = np.sqrt((r_value * r_value) + (h_value * h_value))
    return (np.pi * r_value * l) + (np.pi * (r_value * r_value))
#-----------------------------------------------------------------------------#


#Main program starts here
print("This program calculates the surface area of a cone of radius, r,")
print("and height, h. It uses a USER DEFINED function.")

ans = 'Y' #default value needed to enter while loop
#while loop will only work when user enters "Y"
while ans == 'Y':
    #ask user to input height
    h_value = float(input("Enter the height of the cone in meters: "))
    #ask user to input radius
    r_value = float(input("Enter the radius of the cone in meters: "))
    
    #call surface area method
    surface_area = cone_area(r_value, h_value)
    
    #print reault to the screen
    print("The surface area of the cone is:", \
          "{0:>10.3f}".format(surface_area), " meters")
    
    #ask the user if they want to continue
    ans = input("\nDo you want to try another cone (Y/N): ")