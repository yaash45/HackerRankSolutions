#!/bin/python3

# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    num_of_pairs = 0

    for i in range(0, n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                num_of_pairs += 1

    return num_of_pairs


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)