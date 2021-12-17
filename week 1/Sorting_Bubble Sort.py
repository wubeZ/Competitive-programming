
import math
import os
import random
import re
import sys

def countSwaps(a):
    num = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                num = num + 1  
    print("Array is sorted in "+str(num)+" swaps.")
    print("First Element: "+str(a[0]) )
    print("Last Element: "+str((a[n-1])))
    return a

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
