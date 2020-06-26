#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count_dict ={}
    for i in range(n):
        if ar[i] in count_dict:
            count_dict[ar[i]] = count_dict[ar[i]] +1
        else:
            count_dict[ar[i]] =1
    
    total_pair = 0
    for key in count_dict:
        total_pair = total_pair + int(count_dict[key]/2)
    
    return total_pair
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
