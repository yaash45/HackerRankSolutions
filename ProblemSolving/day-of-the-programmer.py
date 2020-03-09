#!/bin/python3

# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

import math
import os
import random
import re
import sys

def isLeapYear(year):

    if year < 1917:
        return year % 4 == 0

    else:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):

    if year == 1918:
        return f'01.09.{year}'
    elif isLeapYear(year):
        return f'12.09.{year}'
    else:
        return f'13.09.{year}'

if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)