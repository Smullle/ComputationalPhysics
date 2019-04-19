#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:05:43 2019

Program to graph sunspot data from a file

@author: shane
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("sunspots.txt", float)
x = data[:,0]
y = data[:,1]

xyr = 1749 + (x/12)

plt.scatter(xyr, y, s=10, marker=2, linewidths=1)
plt.xlabel("year")
plt.ylabel("sunspot number")
plt.xlim(1950, max(xyr))
plt.ylim(-5, max(y))
plt.show()