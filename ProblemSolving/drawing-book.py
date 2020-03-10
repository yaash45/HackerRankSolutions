#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):

    distance_from_start = p//2
    distance_from_end = n//2 - p//2

    return int(min(distance_from_start, distance_from_end))

if __name__ == '__main__':

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print (result)