#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    n = 4
    temp = arr.sort()
    minSum = sum(arr[:n])   #get first n elements of array
    maxSum = sum(arr[-n:])  #get last n elements of array
    print(str(minSum)+" "+str(maxSum))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
