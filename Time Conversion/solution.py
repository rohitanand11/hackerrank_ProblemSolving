#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):

    input_time = list(s)
    hr = (10 * int(input_time[0])) + int(input_time[1]);

    if((input_time[8]=='A') and hr == 12):
        output_string = "00"+''.join(input_time[2:8])
        return output_string

    elif((input_time[8]=='P') and hr != 12):
        new_hr = 12 + hr
        output_string= str(new_hr)+''.join(input_time[2:8])
        return output_string

    else:
        return ''.join(input_time[:8])

    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
