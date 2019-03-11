#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:41:57 2019

Converts input in degrees Celsius to Fahrenheit 

@author: shane
"""
#inform the user what is happening
print('\nThis program converts degrees centigrade to degrees Fahrenheit')
print('Then it prints the result')

#get input
celsius = float(input('Enter the temperature in degrees Centigrade: '))

#convert to Fahrenheit
fahr = (9/5)* celsius + 32.0

title1 = 'degrees Centigrade'
title2 = 'degrees Fahrenheit'
print('\n') # skip a line

#print the results in formatted output
print('{0:@<20}'.format(title1), \
      '{0:^7}'.format(':'), \
      '{0:>25}'.format(title2))
      # alpha is fill character
      
print('{0:$<20.2f}'.format(celsius), \
      '{0:^7}'.format('='), \
      '{0:>25.4e}'.format(fahr))
      # dollar is fill character
      
