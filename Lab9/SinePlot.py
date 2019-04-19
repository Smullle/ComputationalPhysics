#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:39:04 2019

Program to test plot of sine function

@author: shane
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1)

#res = list(map(lambda x:np.sin(x), x))
#plt.plot(res)
#print(res)

sin = lambda X:np.sin(x)
plt.plot(x,sin(x))


