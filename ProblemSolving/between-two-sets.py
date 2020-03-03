#!/bin/python3

#https://www.hackerrank.com/challenges/between-two-sets/problem

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    aMax = max(a)
    bMin = min(b)

    a_areFactorsOf = []
    areFactorsOf_b = []

    if bMin < aMax:
        return 0

    for i in range(aMax, bMin+1):
        count_factors = 0

        for j in a:
            if i % j == 0:
                count_factors += 1

        if count_factors == len(a):
            a_areFactorsOf.append(i)

    for i in a_areFactorsOf:
        count_factors = 0

        for j in b:
            if j % i == 0:
                count_factors += 1

        if count_factors == len(b):
            areFactorsOf_b.append(i)

    return len(areFactorsOf_b)


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)