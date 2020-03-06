#!/bin/python3

# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    records = [0,0]
    cur_min = 0
    cur_max = 0

    for i in range(0, len(scores)):
        if (i == 0):
            cur_min = scores[i]
            cur_max = scores[i]
        elif (scores[i] < cur_min):
            cur_min = scores[i]
            records[1] += 1
        elif (scores[i] > cur_max):
            cur_max = scores[i]
            records[0] += 1

    return records

if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
