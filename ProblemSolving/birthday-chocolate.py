#!/bin/python3

# https://www.hackerrank.com/challenges/the-birthday-bar/problem

import math
import os
import random
import re
import sys


# Complete the birthday function below.
def birthday(s, d, m):
    start_index = 0
    end_index = m
    count = 0

    while end_index <= len(s):

        total_so_far = 0

        for i in range(start_index, end_index):
            total_so_far += s[i]

        if total_so_far == d:
            count += 1

        start_index += 1
        end_index += 1

    return count


if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)
