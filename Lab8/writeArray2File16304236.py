#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:51:32 2019

This program will read in simple pendulem data, write it to a file, retrieve
the data from the file and re-print it on the screen.

@author: shane
"""

#-------------------------------Main Method-----------------------------------#
def main():
    print("Programme to read in simple pendulem data, write it to a file,") 
    print("retrieve the data from the file and re-print it on the screen.")
    
    data = getData()
    
    sp_length = data[0]
    sp_period = data[1]
    
    print("Original data \033[31mred from the keyboard\033[0m shown below")
    print_data(sp_length, sp_period)
    
    file_write(sp_length, sp_period, "pendulum.txt")
    
    sp_length_v2, sp_period_v2 = file_read("pendulum.txt")
    
    print("Data \033[35mretrieved from file\033[0m shown below")
    print_data(sp_length_v2, sp_period_v2)
#-----------------------------------------------------------------------------#
def getData():
    
    n = input("How many lines of data would you like to enter: ")
    
    sp_length = []
    sp_period = []
    
    for i in range (n):
        print("Enter length [", i, "] in cm (float): ", end = "")
        sp_length.append(float(input()))
        print("Enter period [", i, "] in seconds (float): ", end = "")
        sp_period.append(float(input()))
        
    ans = [sp_length,sp_period]   
    return ans
#-----------------------------------------------------------------------------#
def print_data(sp_length, sp_period):
    print("{0:>15}".format("index") ,\
          "{0:>15}".format("length (cm)") ,\
          "{0:>15}".format("period (s)"))
    
    for i in range(len(sp_length)):
        print("{0:>15}".format(i) ,\
              "{0:>15.3f}".format(sp_length[i]) ,\
              "{0:>15.3f}".format(sp_period[i]))
#-----------------------------------------------------------------------------#
def file_write(sp_length, sp_period):
    file_name = "pendulum.txt"
    
    out_file = open(file_name, "w")
    
    print("{0:>15}".format("index") ,\
          "{0:>15}".format("length (cm)") ,\
          "{0:>15}".format("period (s)"), file = out_file)
    
    for i in range(len(sp_length)):
        print("{0:>15}".format(i) ,\
              "{0:>15.3f}".format(sp_length[i]) ,\
              "{0:>15.3f}".format(sp_period[i]), file = out_file)
        
    out_file.close()
#-----------------------------------------------------------------------------#
def file_read():
    file_name = "pendulum.txt"
    
    in_file = open(file_name, "r")
    
    sp_length_v3 = []
    sp_period_v3 = []
    
    header  = in_file.readline()
    print(header)
    
    for line in in_file:
        values = line.split()
        sp_length_v3.append(float(values[1]))
        sp_period_v3.append(float(values[2]))
        
    in_file.close()
    
    return sp_length_v3
    return sp_period_v3
#-----------------------------------------------------------------------------#
