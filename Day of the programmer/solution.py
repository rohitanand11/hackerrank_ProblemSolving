#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def checkleapYear(year):
    if(year>1918):
        if(year%4==0):
            if(year%100 !=0):
                return True
            elif(year%400==0):
                return True
            else:
                return False
        return False

    elif(year<1918):
        if(year%4==0):
            return True

def dayOfProgrammer(year):
    if(year==1918):
        return "25.09."+str(year)
    else:
        checkLeap = checkleapYear(year)
        if(checkLeap):
            return_date = "12.09."+str(year)
            return return_date
        else:
            return_date = "13.09."+str(year)
            return return_date





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
