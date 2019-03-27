#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:34:41 2019

This program computes the length of a semicircle 
by considering it as a number of straight sections joined together.

@author: shane
"""
#-----------------------------------------------------------------------------#
import numpy as np

def f(x):
    return np.sqrt(np.abs(1-(x*x)))
#-----------------------------------------------------------------------------#

def new_length(x, dx, c_y):
    y1 = f(x)
    y2 = f(x + dx)
    new_y = y2 - f(c_y)
    return np.sqrt(((dx)**2)+((y2 - y1)**2))
#-----------------------------------------------------------------------------#

r = int(input("Enter the radius of the semicircle: "))
n = int(input("Enter number of n sections to compute (accuracy): "))

c_length = 0
x = 0

dx = float(r/n)

for i in range(0,n):
    x = i*dx
    c_y = f(x - dx)
    c_length  += new_length(x, dx, c_y)
    c_length += c_length*2

print(c_length)