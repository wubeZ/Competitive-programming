#!/bin/python3

import math
import os
import random
import re
import sys


def maximumToys(prices, k):
    prices.sort()
    totalSum = 0
    count = 0
    
    for i in prices:
        totalSum += i
        if totalSum > k:
            break
        else:
            count += 1
            
    return count    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
