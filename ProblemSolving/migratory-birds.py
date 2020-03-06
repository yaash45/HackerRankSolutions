#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    frequency_graph = [0]*6

    for i in arr:
        frequency_graph[i] += 1;

    highest_id = 0
    highest_id_count = 0

    for j in range(0, len(frequency_graph)):

        if frequency_graph[j] > highest_id_count:
            highest_id = j
            highest_id_count = frequency_graph[j]

    return highest_id

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)

