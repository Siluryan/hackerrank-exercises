#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    pm_hour = s[0:2]
    pm_hour = int(pm_hour)      
    
    if s[-2:] == 'PM' and pm_hour == 12:        
        return(s[0:8])
    elif s[-2:] == 'PM':
        pm_hour = pm_hour + 12
        return(str(pm_hour) + s[2:8])
    elif s[-2:] == 'AM' and pm_hour == 12:
        return('00' + s[2:8])
    else:
        return(s[0:8]) 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()    
    result = timeConversion(s)

    fptr.write(str(result) + '\n')

    fptr.close()
