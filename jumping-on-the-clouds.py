#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#



def jumpingOnClouds(c):
    print(c)
    count=0
    i=0
    waitFlag = False
    waitIndex = 0
    
    
    while i < len(c):
        print("-------------")
        if ((i+2) < len(c)) and (check(c[i+2])):
            i+=2
            count+=1
        elif ((i+1) < len(c)) and (check(c[i+1])):
            i+=1
            count+=1
        else:
            break
        print("i = "+ str(i))
        print("count = "+ str(count))
        
    return count  
  
def check(a):
    if a==0:
        return True
    else:
        return False
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
