#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):

    new_n=n
    new_p=p

    if(n%2!=0):
        new_n=n-1
    if(p%2!=0):
        new_p=p-1
    
    if((new_n-new_p)<new_p):
        return int((new_n-new_p)/2)
    else:
        return int(new_p/2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
