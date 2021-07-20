#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    track = [0]
    count = 0
    vEnter = 0
    vExit = 0
    print("hi")
    for i,x in enumerate(path):
        if x=="U":
            count+=1
            if count == 0:
                vExit+=1
        elif x=="D":
            count-=1
        else:
            print("Error")
            
        track.append(count)    

    print(track)
    return vExit
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
