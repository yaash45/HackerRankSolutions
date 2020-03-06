#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/grading/problem

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    roundedGrades = []

    for g in grades:
        if g < 38:
            roundedGrades.append(g)
        else:
            if (g+2)%5 == 0:
                roundedGrades.append(g+2)
            elif (g+1)%5 == 0:
                roundedGrades.append(g+1)
            else:
                roundedGrades.append(g)

    return roundedGrades

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)