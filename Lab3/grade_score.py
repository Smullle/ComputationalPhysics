#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:46:57 2019

Program to print a grade based on the imputted %

@author: shane
"""

#Inform the user what is happening
print("This program will print a grade based on the imputted %")

#Value used in while loop
a = 1

#
while(a == 1):
    #Get the user to enter their grade
    grade = float(input("Enter your percent:"))
    
    if(grade < 0 or grade > 100):
        a = 1
        print("Enter a valid mark")
    
    elif(grade >= 85):
        print("A mark of" ,grade, "equals an A-grade")
        a = 0
        
    elif(grade <= 40):
        print("A mark of" ,grade, "equals an E-grade")
        a = 0
        
    elif(grade <= 55):
        print("A mark of" ,grade, "equals a D-grade")
        a = 0
        
    elif(grade <= 70):
        print("A mark of" ,grade, "equals a C-grade")
        a = 0
        
    elif(grade <= 85):
        print("A mark of" ,grade, "equals a B-grade")
        a = 0


    

    

    
    