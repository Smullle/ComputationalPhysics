#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:33:54 2019

Program to read data form sunspots.txt and output a hsitogram graph of the data
also the mean, median, mode and standard deviation of the data. 

@author: shane
"""

import numpy as np #needed for many math functions
import statistics as stats #used for stat functions
import matplotlib.pyplot as plt #needed for plotting

#-----------------------------------------------------------------------------#
def plot(y, binsNo):
    """"Function will take array of data called y and number of bins 
    to produce a histogram plot"""
    
    #make histogram plot using data from user
    plt.hist(y, bins = binsNo)
    #title the graph
    plt.title("Sunspot Histogram", fontsize = 20, color="b")
    #title the axis
    plt.xlabel("Months", fontsize = 14, color="r")
    plt.ylabel("Number of sunspots", fontsize = 14, color="r")
    #add text to show 11 year cycle of sunspots
    plt.text(40, 200, "This dip shows the 11 year cycle of sunspots.")

    #finally print grpah
    plt.show()
    
#-----------------------------------------------------------------------------#
def printStats(array):
    """This function will print the mean, meadian, mode and standard 
    deviation of an array of data."""
    
    #calculate mean, meadian and stdDev using numpy
    mean = np.mean(array) 
    #calculate median using statistics library
    median = np.median(array)
    modes = stats.mode(array)
    stdDev = np.std(array)
    
    #print results in formatted output
    print("\nMean: ",  "{0:>20.3f}".format(mean))
    print("Median: ", "{0:>18}".format(median))
    print("Mode/Modes: ", "{0:>14}".format(modes))
    print("Standard Deviation: ", "{0:>5.3f}".format(stdDev))
    
#-------------------------------Main Method-----------------------------------#
#read data from sunspot file
data = np.loadtxt("sunspots.txt", float)
#split data into 2 arrays
x = data[:,0]
y = data[:,1]

#inform the user what is happening
print("This program will read a text file called sunspots.txt")
print("It will then output a histogram of the results")
print("and also the mean, median, mode and standard deviation of the data.")

#ask the user how many bins wanted
binsNo = int(input("Enter the number of bins for the Histogram (e.g 40): "))

#call methods to print graph and stats
plot(y, binsNo)
printStats(y)


