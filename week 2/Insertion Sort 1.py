#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
                for k in arr:
                    print(k,end = " ")
                print()
        arr[j+1] = key
    for k in arr:
        print(k ,end = " ")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
