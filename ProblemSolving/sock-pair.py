#!/bin/python3

# https://www.hackerrank.com/challenges/sock-merchant/problem

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    freq_graph = [0]*101
    full_pair_count = 0

    for sock_number in ar:
        freq_graph[sock_number] += 1

    for i in freq_graph:
        full_pair_count += i//2

    return full_pair_count

if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
