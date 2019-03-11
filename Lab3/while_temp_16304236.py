#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:21:13 2019

This program will ask for a temperature in Celsius 
this value will then be conveted to Fahrenheit.
The program will quit when a value less than 0 or greater than 100 is entered.

@author: shane
"""

def ColorText(text, color):
    CEND      = '\033[0m'
    CBOLD     = '\033[1m'
    CRED      = '\033[91m'
    CGREEN    = '\033[32m'
    CYELLOW   = '\033[33m'
    CBLUE     = '\033[34m'
    CVIOLET   = '\033[35m'
    CBEIGE    = '\033[36m'
    if color == 'red':
        return CRED + CBOLD + text + CEND
    elif color == 'green':
        return CGREEN + CBOLD + text + CEND
    elif color == 'yellow':
        return CYELLOW + CBOLD + text + CEND
    elif color == 'blue':
        return CBLUE + CBOLD + text + CEND
    elif color == 'voilet':
        return CVIOLET + CBOLD + text + CEND
    elif color == 'beige':
        return CBEIGE + CBOLD + text + CEND

#inform the user what is happening
print("This program will ask for a temperature in Celsius" ,\
      "this value will then be conveted to Fahrenheit.")
print("Enter a number less than 0 or greater than 100 to quit.")


#Temp value to get into while loop
celsius = 50

#While loop will run until a number over 100 or less than 0 is entered
while(celsius <= 100 and celsius >= 0):
    
    #Do not run one if the number is over 100 or less than 0
    if(celsius >= 100 and celsius <= 0):
        break
    
    #get input
    celsius = float(input('Enter the temperature in degrees Centigrade: '))
    
    #convert to Fahrenheit
    #https://www.rapidtables.com/convert/temperature/celsius-to-fahrenheit.html
    fahr = (9/5)* celsius + 32.0
    
    #Print the output of the conversion
    print(celsius, "degrees Centigrade =" ,fahr, "degrees Fahrenheit")
    
    #Conditional statements to check if it is cool, warm or comfortable
    if(celsius > 32):
        print(ColorText("The temperature is rather warm.", "red"))
        
    elif(fahr <= 59):
        print(ColorText("The temperature is quite cool.", "blue"))
    
    else:
        print(ColorText("The temperature is comfortable.", "green"))