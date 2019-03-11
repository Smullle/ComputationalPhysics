#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:51:12 2019

@author: shane
"""

import numpy as np

rolls = (input('Enter the number of rolls you want to simulate: '))

for x in rolls:
    print(np.rand(5))