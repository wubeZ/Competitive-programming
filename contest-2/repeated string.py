#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 

def repeatedString(s, n):
    ans = s.count("a")
    count , remainder = 0
    count = (n//len(s))*ans
    for i in range(n%len(s)):
       if s[i] == "a":
            remainder += 1
    count = count + remainder
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
