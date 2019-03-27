#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:14:47 2019

This program will convert energy in kilowatt-hours and convert it to
the energy in joules, and the energy in calories.

@author: shane
"""
#-----------------------------------------------------------------------------#

#function to convert kilowatt-hours to joules
def kiloToJoules(kilo_hours):
    #1 Kilowatt-hour = 6.6e6
    return kilo_hours*(6.6e6)

#-----------------------------------------------------------------------------#

#function to convert kilowatt-hours to calories
def kiloToCalories(kilo_hours):
    #1 kilowatt-hour = 860420.65
    return kilo_hours*860420.65
    
#-------------------------------Main Method-----------------------------------#

#inform the user what is happening
print("This program will convert energy in kilowatt-hours and convert it to")
print("the energy in joules, and the energy in calories.")
print("A range of values will be converted and is set by a and b below.")
print("A step size of 30 will be used.")

#used to enter the loop
check = "y"

#Keep running until user enters N
while(check =="y" or check == "Y"):

    #Get the values a and b from the user
    print("***Note a and b must be in range (0 <= a/b <= 360)***")
    a = int(input("Enter a value value a in kilowatt-hours: "))
    b = int(input("Enter a value value b in kilowatt-hours: "))
    
    #check if a and b are in the required range
    while(True):
        
        if(a < 0):
            print("\nPlease enter a valid value for a (0 <= a <= 360)")
            a = int(input("Enter a value value a in kilowatt-hours: "))
        if(b > 360):
            print("\nPlease enter a valid value for b (0 <= b <= 360)")
            b = int(input("Enter a value value b in kilowatt-hours: "))
        
        break #break out of while loop once values are correct
    
    #step size set by question
    step = 30
    
    #used to print formatted output
    title1 = "Kilowatt-Hours"
    title2 = "Joules"
    title3 = "Calories"
    
    #print the formatted titles
    print('\n{0:m<20}'.format(title1), ' ] ', \
          '{0:m<20}'.format(title2), ' ] ', \
          '{0:m<20}'.format(title3), ' ] ')
    
    #loop through entered range a and b, using step size = 30
    for i in range(a,b,step):
        print('{0:m<20.5f}'.format(i), ' ] ', \
              '{0:m<20.5f}'.format(kiloToJoules(i)), ' ] ', \
              '{0:m<20.5f}'.format(kiloToCalories(i)), ' ] ')
    
    #Ask the user if they wish to continue
    print("\nDo you want to enter another range?")
    check = input("Enter Y to continue or N to exti: ")
