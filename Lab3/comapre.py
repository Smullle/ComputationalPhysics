#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:27:53 2019

This program compares two intergers and will determine if one is less than,
greater than or equal to the other.

@author: shane
"""

#Inform the user what is happening
print("This program compares two intergers and will determine if one is",\
      "less than, greaterthan or equal to the other.")

#Get two numbers to compare
x = float(input("Enter a number x:"))
y = float(input("Enter another number y:"))

if(x < y):
    print("x (" ,x, ") is less than y (" ,y, ")")
    
elif(x > y):
    print("x (" ,x, ") is greater than y (" ,y, ")")
    
elif(x == y):
    print("x (" ,x, ") is equal to y (" ,y, ")")



