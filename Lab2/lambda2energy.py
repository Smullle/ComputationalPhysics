#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:56:22 2019

Converts wavelength entered by the user to frequency 
and energy in both J and eV

@author: shane
"""

# constants
speedL = 299792458
planck =  6.63e-34

# inform the user whats happening
print('This program converts photon wavelength entered by the user to', \
      ' frequency (Hz), energy in joules(J) and energy in eV.')
        
# get input
waveLen = float(input('Enter the wavelength in nm: '))

# convert nm to m
waveLenM = waveLen*(1e-9)

# calculate frequency
freq = speedL/waveLenM

# calculate energy
energyJ = planck*freq

# convert energy to eV
energyEV = energyJ*6.242e+18

title1 = 'w/l (nm)'
title2 = 'Frequency (Hz)'
title3 = 'energy (J)'
title4 = 'energy (eV)'

#print the results in formatted output
print('{0:>10}'.format(title1), \
      '{0:>15}'.format(title2), \
      '{0:>20}'.format(title3), \
      '{0:>20}'.format(title4))

print('{0:>10.1f}'.format(waveLen), \
      '{0:>15.2E}'.format(freq), \
      '{0:>20.3E}'.format(energyJ), \
      '{0:>20.4f}'.format(energyEV))

