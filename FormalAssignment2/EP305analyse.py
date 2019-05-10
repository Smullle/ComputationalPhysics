# -*- coding: utf-8 -*-
"""
Analyse data from EP305capture23.py, calculate mean, median, mode and
standard deviation of the data and make a graph.
@author: Shane
"""
import numpy as np #needed for many math functions
import statistics as stats #used for stat functions
import matplotlib.pyplot as plt #needed for plotting

#-----------------------------------------------------------------------------#
def file_read(file_name):
    """Function takes in file_name of type string
       and returns arrays containing data"""

    #open specified file in read mode
    in_file = open(file_name, "r")

    #create data lists
    a = []
    b = []

    #save header to string and split into list
    header_string = in_file.readline()
    header = header_string.split()

    #save revelent data to respective lists
    for line in in_file:
        values = line.split()
        a.append(float(values[0]))
        b.append(float(values[1]))

    #close the file
    in_file.close()

    #return 3D lists of lists containing data
    ans = [a, b, header]

    return ans
#-----------------------------------------------------------------------------#
def getStats(array):
    """This function will return the mean, meadian, mode and standard
    deviation of an array of data."""

    #calculate mean, meadian and stdDev using numpy
    mean = np.mean(array)
    #calculate median using statistics library
    median = np.median(array)
    #calculate mode using lower_mode for redundency
    modes = lower_mode(array)
    #use numpy to get standard deviation
    stdDev = np.std(array)

    #return all stats calculated
    return mean, median, modes, stdDev

#-----------------------------------------------------------------------------#
def percentile(data):
    """Function to calculate the percentiles of a passed array"""
    
    #number of percentiles
    groups = np.empty(25)
    data.sort() #sort array
    max = 4 #initial max value
    index = 0 #initial index
    count = 0 #initial count
    for i in range (len(groups)):
        for j in range (len(data)):
            if (data[j] <= max and data[j] >= index):
                #if value in current percentile increase count
                count += 1 
        max += 4 #increase roof by 4
        index += 4 #increase floor by 4
        groups[i] = count #add the number of values to percentile
        count = 0 #reset count

    #return the array of percentiles
    return groups
#-----------------------------------------------------------------------------#
def lower_mode(mode_array):
    """Function to catch no unique mode error, take lower mode and return this
    value insted, due to the number of values used this is common"""
    try:
        return stats.mode(mode_array)
    except stats.StatisticsError as e:
        return sorted(mode_array)[len(mode_array)//2 - 1]
#-----------------------------------------------------------------------------#
def printPercent(array, maxTime, minTime):
    """Function to print the percintiles, manx and min time. With the 
    percintiles being an array of ints and max and min taking ints"""
    
    header1 = "Percentile"
    header2 = "Number of Sensor Readings"
    print("{0:<10}".format(header1) ,\
          "{0:>30}".format(header2))

    index = 0
    for i in range (25):
        percentRange = ""
        percentRange += str(index)
        percentRange += " - "
        percentRange += str(index+4)
        percentRange += "%"
        print("{0:<10}".format(percentRange) ,\
              "{0:>30.0f}".format(array[i]))
        index += 4
    
    header1 = "Time of max value in seconds"
    header2 = "Time of min value in seconds"
    print("\n{0:<10}".format(header1) ,\
          "{0:>30}".format(header2))
    print("{0:<6}".format(maxTime) ,\
          "{0:>30}".format(minTime))
    
#-----------------------------------------------------------------------------#
def plot(time, percent, binsNo, mean, median, mode, stdDev):
    """"Function will take array of data called y and number of bins
    to produce a histogram plot"""

    #make histogram plot using data from user
    plt.hist(percent, bins = binsNo)
    #title the graph
    plt.title("Percentile Histogram", fontsize = 20, color="b")
    #title the axis
    plt.xlabel("Percentile", fontsize = 10, color="r")
    plt.ylabel("Number sensor readings", fontsize = 10, color="r")
    
    textstr = '\n'.join((
    r'$\mu=%.2f$' % (mean, ),
    r'$\mathrm{median}=%.2f$' % (median, ),
    r'$\mathrm{mode}=%.2f$' % (mode, ),
    r'$\sigma=%.2f$' % (stdDev, )))
    
    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    plt.text(110, 15, textstr, bbox=props)
    
    #finally print grpah
    plt.show()
    
    plt.plot(time ,percent)
    #title the graph
    title = "Plot of max potentiometer reading over time"
    plt.title(title, fontsize = 15, color="b")
    #title the axis
    plt.xlabel("Time is seconds", fontsize = 10, color="r")
    plt.ylabel("Percentage of potentiometer", fontsize = 10, color="r")
    #show the graph
    plt.show()

#-----------------------------------------------------------------------------#
def maxMinTime(time, data):
    """Function to calculate the occurance of max and min potentiometer
    reading, the result is returned in seconds as a tuple."""
    
    #obtain max and min values from array
    max_value = max(data)
    min_value = min(data)
    
    #find the index of max and min values
    max_index = data.index(max_value)
    min_index = data.index(min_value)
    
    #return the timestamp of max and min values
    return time[max_index], time[min_index]

#-------------------------------Main Method-----------------------------------#
#inform the user what is happening
print("This program will read EP305data23.txt, preform various calculations")
print("then a histogram of the data along with the statistics will be printed")

#read the data from file using file_read function
data = file_read("EP305data23.txt")

#obtain arrays returned from file_read
timeStamp = data[0] 
POTpercent = data[1]
header = data[2]

#obtain the mean, median, mode and stdDev using getStats
mean, median, mode, stdDev = getStats(POTpercent)

#calculate the percintiles using percentile function
percentiles = percentile(POTpercent)

#plot the potentiometer readings and pass stats to be displayes on graph
plot(timeStamp, POTpercent, 25, mean, median, mode, stdDev)

#calculate occurance of max and min position using function
maxTime, minTime = maxMinTime(timeStamp, POTpercent)

#print the percentile, maxTime and minTime in formatted output 
printPercent(percentiles, minTime, maxTime)
