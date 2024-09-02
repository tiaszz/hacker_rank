#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    minus = 0
    plus = 0
    zero = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            minus += 1
        elif arr[i] == 0:
            zero += 1
        else:
            plus += 1
    
    minus_total = minus / (i+1)
    plus_total = plus / (i+1)
    zero_total = zero / (i+1)

    print(f"{plus_total:.6f}")
    print(f"{minus_total:.6f}")
    print(f"{zero_total:.6f}")

if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

