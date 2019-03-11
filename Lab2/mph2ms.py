#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:03:08 2019

This program converts speed in miles per hour to metres per second

@author: shane
"""

#Conversion value
formula  = 2.2369362920544

#Inform the user of what is happening
print("This program converts speed in miles per hour to metres per second")

#Ask the user to input a speed in miles per hour
mph = float(input("Enter a value in miles per hour: "))

#Convert to metres per second by dividing by 2.2369362920544
ms = mph/formula

#Titles for output
title1 = "Speed in mph"
title2 = "Speed in m/s"

#Print the result in formatted output
print('{0:<15}'.format(title1) + '{0:>35}'.format(title2))
print('{0:<20.3f}'.format(mph) + '{0:<20.3f}'.format(ms))
print('{0:>25.5E}'.format(mph) + '{0:>25.5E}'.format(ms))