#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:24:45 2019

Program to test plots using matplotlib.pyplot

@author: shane
"""

import numpy as np
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,5.5]
y = [7,1,2,6,4,3,3]


xx = np.array(x)
yy = np.array(y)
zz = yy**2

plt.subplot(221)
plt.plot(x, y)

plt.subplot(222)
plt.plot(xx, yy, label="data")
plt.legend()

plt.subplot(223)
plt.plot(xx, zz, "ko--")

plt.subplot(224)
plt.plot(x, y, "bo", label="points") #use blue circle
plt.plot(x, y, "r--", label="line") #use red dotted line
plt.title("My second plot", color="b")
plt.xlabel("x-data", fontsize = 14, color="g")
plt.ylabel("measurements")
plt.axis([-1,7,0,8])
plt.text(2, 0.75, "this is some text")
plt.grid(True)
plt.legend(loc="best", fontsize=10)
plt.show()