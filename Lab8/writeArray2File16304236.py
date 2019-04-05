#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:51:32 2019

This program will read in simple pendulem data, write it to a file, retrieve
the data from the file and re-print it on the screen.

@author: shane
"""  
#-----------------------------------------------------------------------------#
def get_Data():
    """Function to obtain data entered by the user."""
    
    n = int(input("How many lines of data would you like to enter: "))
    
    #create three lists for data
    sp_length = []
    sp_period = []
    header = []
    
    #loop to obtain data from user using specifies number of lines
    for i in range (n):
        print("Enter length [", i, "] in cm (float): ", end = "")
        sp_length.append(float(input()))
        print("Enter period [", i, "] in seconds (float): ", end = "")
        sp_period.append(float(input()))
        
    #add headers needed to header list    
    header.append("index")
    header.append("length(cm)")
    header.append("period(s)")
        
    #return 3D list of lists containing data
    ans = [sp_length, sp_period, header]   
    return ans
#-----------------------------------------------------------------------------#
def print_data(sp_length, sp_period, header):
    """Function takes in array of lengths, period and headers 
       and will print data in formatted table."""
    
    #print formatted headers from header list
    print("{0:>15}".format(header[0]) ,\
          "{0:>15}".format(header[1]) ,\
          "{0:>15}".format(header[2]))
    
    #print data from sp_length[] and sp_period[]
    for i in range(len(sp_length)):
        print("{0:>15}".format(i) ,\
              "{0:>15.3f}".format(sp_length[i]) ,\
              "{0:>15.3f}".format(sp_period[i]))
#-----------------------------------------------------------------------------#
def file_write(sp_length, sp_period, header, file_name):
    """Function takes in arrays such as length, period and header, 
       also string filename and will then write to the file specified."""
    
    #specify filename and inform write
    out_file = open(file_name, "w")
    
    #add headers to file from list
    print("{0:>15}".format(header[0]) ,\
          "{0:>15}".format(header[1]) ,\
          "{0:>15}".format(header[2]), file = out_file)
    
    #add data to file form lists 
    for i in range(len(sp_length)):
        print("{0:>15}".format(i) ,\
              "{0:>15.3f}".format(sp_length[i]) ,\
              "{0:>15.3f}".format(sp_period[i]), file = out_file)
        
    #close the file
    out_file.close()
#-----------------------------------------------------------------------------#
def file_read(file_name):
    """Function takes in file_name of type string 
       and returns arrays containing data"""
    
    #open specified file in read mode
    in_file = open(file_name, "r")
    
    #create data lists
    sp_length_v3 = []
    sp_period_v3 = []    

    #save header to string and split into list
    header_string = in_file.readline()
    header_v3 = header_string.split()
    
    #save revelent data to respective lists
    for line in in_file:
        values = line.split()
        sp_length_v3.append(float(values[1]))
        sp_period_v3.append(float(values[2]))
        
    #close the file
    in_file.close()
    
    #return 3D lists of lists containing data
    ans = [sp_length_v3, sp_period_v3, header_v3]
    
    return ans
#-----------------------------------------------------------------------------#

#-------------------------------Main Method-----------------------------------#
print("Programme to read in simple pendulem data, write it to a file,") 
print("retrieve the data from the file and re-print it on the screen.")

#use getData function to obtain data from user and save to list
data = get_Data()

#obtain individual lists from 3D array
sp_length = data[0]
sp_period = data[1]
header = data[2]

#print data obtained from user
print("Original data \033[31mred from the keyboard\033[0m shown below")
print_data(sp_length, sp_period, header)

#write data to file
file_write(sp_length, sp_period, header, "pendulum.txt")

#read data back from file and save to list
dataBack = file_read("pendulum.txt")

#obtain data from returned 3D array
sp_length_v2 = dataBack[0]
sp_period_v2 = dataBack[1]
header_v2 = dataBack[2]

#print lists obtained from file
print("Data \033[35mretrieved from file\033[0m shown below")
print_data(sp_length_v2, sp_period_v2, header_v2)

