#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 

def repeatedString(s, n):
    ans = Counter(s)
    count = 0
    remcount = 0
    maxcount = 0
    count = (n//len(s))*ans["a"]
    for i in range(n%len(s)):
       if s[i] == "a":
            remcount += 1
    maxcount = count + remcount
    return maxcount
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
