#!/bin/python3

import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    sumcount = 0
    m = 0
    for i,j in enumerate(bill):
        if i != k:
            sumcount += j
            m += 1
    if (sumcount//2) == b:
        print("Bon Appetit")
    else:
        print(b-(sumcount//2))
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
