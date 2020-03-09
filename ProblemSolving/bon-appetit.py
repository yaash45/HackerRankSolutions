#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    items_to_split = []

    for i in range(0, len(bill)):
        if i != k:
            items_to_split.append(bill[i])

    if int(sum(items_to_split)/2) == b:
        print('Bon Appetit')
    else:
        print(f'{int(b - sum(items_to_split)/2)}')


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

