# -*- coding: utf-8 -*-
"""
Read streamed data from arduino using sketch 4
@author: Shane
"""

import serial #needed for serial communication
import numpy as np #needed for basic math functions
import time #needed for sleep function

#-----------------------------------------------------------------------------#
def get_valid_line(port):
    ''' Get one valid line form the serial port, ignoring erroneous data'''
    while True:
        try:
            #note in the case of serial port overflow some characters
            #left in it will not decode and throw exception
            return port.readline().decode(encoding="ASCII").strip()
        except:
            pass #ignore exception and try again on next line
#-----------------------------------------------------------------------------#
def obtainData(N):
    """Function to obtain N readings from Arduino over COM6
    will return array of timeStamps and POT positions"""
    t = np.empty(N)
    data = np.empty(N)

    with serial.Serial("COM6", baudrate=19200, timeout=2) as myport:
        #due to intermittent buffer problems this seems to help but not always
        time.sleep(2)
        while(get_valid_line(myport) != "START"):
            pass #wait until we get the start tag

        for i in range(N):
            line = get_valid_line(myport)

            if line == "START": #ignore any subsequent tags
                line = myport.readline()

            stamp, val = [float(a) for a in line.split()]
            t[i] = stamp/1e6 #convert to seconds
            data[i] = (val/1023) * 100 #convert POT raw reading to %

    return t, data
#-----------------------------------------------------------------------------#
def file_write(a, b, header, file_name):
    """Function takes in arrays a, b and header,
       also string filename and will then write to the file specified."""

    #specify filename and inform write
    out_file = open(file_name, "w")

    #add headers to file from list
    print("{0:>15}".format(header[0]) ,\
          "{0:>15}".format(header[1]), file = out_file)

    #add data to file form lists
    for i in range(len(a)):
        print("{0:>15.5f}".format(a[i]) ,\
              "{0:>15.5f}".format(b[i]), file = out_file)

    #close the file
    out_file.close()
#-----------------------------------------------------------------------------#

#-------------------------------Main Method-----------------------------------#
#inform the user what is happening
print("This program will read a stream of data from the arduino") 
print("up to 200 values this data will then be saved to EP305data23.txt")

print("Working...")

#create arrays for time and position%
timeStamp = np.empty(200)
POTpercent = np.empty(200)

#add values to array using obtainData function
timeStamp, POTpercent = obtainData(200)

#make header for file
header = ["timeStamp (s)", "POTpercent"]

#write data to file
file_write(timeStamp, POTpercent, header, "EP305data23.txt")

#inform the user the capture has finished
print("\aData capture finished check EP305data23.txt")