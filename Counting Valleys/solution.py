#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    dummy_dict= {
                    "level":0,
                    "valley_count":0
                }

    for i in range(n):
        if(dummy_dict["level"]==0 and s[i]=='D'):
            dummy_dict["valley_count"]=dummy_dict["valley_count"]+1
            dummy_dict["level"]=dummy_dict["level"]-1

        elif(s[i]=='D'):
            dummy_dict["level"]=dummy_dict["level"]-1

        elif(s[i]=='U'):
            dummy_dict["level"]=dummy_dict["level"]+1
    
    return dummy_dict["valley_count"]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
