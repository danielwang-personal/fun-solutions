#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    arr_sorted = sorted(arr)
    nonzero = {}
    
    for i in range(len(arr)):
        d = arr[i] - arr_sorted[i]
        if d != 0:
            nonzero[i+1] = d
    
    if len(nonzero) == 0:
        print('yes')
        return
    elif len(nonzero) == 2:
        print('yes')
        print(f'swap {list(nonzero.keys())[0]} {list(nonzero.keys())[1]}')
        return 
    
    if checkPalindrome(nonzero):
        print('yes')
        print(f'reverse {list(nonzero.keys())[0]} {list(nonzero.keys())[-1]}')
        return
    
    print('no')

def checkPalindrome(d):
    l = len(d)
    if l % 2 == 0:
        mid = (l / 2) - 1
    else:
        mid = (l // 2)
    
    keys = d.keys()
    maxKey = list(keys)[-1]
    for i, k in enumerate(keys):
        if i > mid:
            break
        if maxKey - i not in keys:
            return False
        else:
            if d[k] != -1 * d[maxKey - i]:
                return False
    
    return True
        
        
            
    return True
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
