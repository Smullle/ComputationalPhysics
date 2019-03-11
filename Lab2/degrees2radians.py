#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:32:50 2019

Converts an angle in degrees entered by the user to radians 

@author: shane
"""
import numpy as np

print('This program converts angle (theta) in degrees to angle in radians')
print('It then calculates the sin , cosine and tan of the angle and prints, \
      all five values in the console window.')

# ask the user to enter an angle in degrees
angleDeg = float(input('Enter the angle in degrees: '))

# Convert the angle to radians
theta = angleDeg*(np.pi/180)

# calculate sin
sinTheta = np.sin(theta)

# clculate cos
cosTheta = np.cos(theta)

# calculate tan
tanTheta = np.tan(theta)

title1 = 'theta (deg.)'
title2 = 'theta (rad.)'
title3 = 'sin(theta)'
title4 = 'cos(theta)'
title5 = 'tan(theta)'

#print the results in formatted output
print('{0:>15}'.format(title1), \
      '{0:>15}'.format(title2), \
      '{0:>15}'.format(title3), \
      '{0:>15}'.format(title4))

print('{0:>15.2f}'.format(angleDeg), \
      '{0:>15.4f}'.format(theta), \
      '{0:>15.4f}'.format(sinTheta), \
      '{0:>15.4f}'.format(cosTheta), \
      '{0:>15.4f}'.format(tanTheta))