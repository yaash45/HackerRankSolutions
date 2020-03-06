#!/bin/python3

# https://www.hackerrank.com/challenges/kangaroo/problem

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    a = x1 - x2
    b = v2 - v1

    if b == 0 and a == 0:
        return 'YES'
    elif b == 0 and a != 0:
        return 'NO'
    elif a/b < 0:
        return 'NO'
    elif a%b == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)