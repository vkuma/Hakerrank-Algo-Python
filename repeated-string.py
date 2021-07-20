#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    count_1 = 0
    count_2 = 0
    count_f = 0
    size = len(s)
    
    q = n // size
    mod = n % size
    print(q, mod)
    
    for x in s:
        if x=="a":
            count_1+=1
    
    temp = s[0:mod]
    for x in temp:
        if x=="a":
            count_2+=1
    count_f = (count_1*q) + count_2
    
    print(count_f)
    return count_f
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
