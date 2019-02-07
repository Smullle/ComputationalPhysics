# -*- coding: utf-8 -*-
import math
x = 7
#minTest = int(math.sqrt(x))+1
#print(minTest)

def isPrime(x):
    count = 0
    for i in range(2,int(x/2)+1):
        if (x%i == 0):
            count += 1

    if (count !=0):
        return False
    else:
        return True

print(isPrime(x))
