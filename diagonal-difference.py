#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    r = len(arr)
    c = len(arr[0])
    x = r if (r>c) else c
    
    # print(r)
    # print(c)
    # print(x)
    
    f_diag = 0
    l_diag = 0
    
    count = 0
    while (count<x):
        # print(arr[count][count])
        # print(arr[c-1-count][count])
        f_diag+=arr[count][count]
        l_diag+=arr[c-1-count][count]
        count+=1
    return abs(f_diag-l_diag)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
