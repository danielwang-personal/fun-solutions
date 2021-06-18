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
    
    # Create an array of all nonzero differences
    # i.e. an array of values not in their correct place
    for i in range(len(arr)):
        d = arr[i] - arr_sorted[i]
        if d != 0:
            nonzero[i+1] = d
    
    if len(nonzero) == 0:
        # Array is already sorted
        print('yes')
        return
    elif len(nonzero) == 2:
        # Only two values are out of place
        # So can swap
        print('yes')
        print(f'swap {list(nonzero.keys())[0]} {list(nonzero.keys())[1]}')
        return 
    
    # Check if you can reverse a subarray 
    if checkPalindrome(nonzero):
        print('yes')
        print(f'reverse {list(nonzero.keys())[0]} {list(nonzero.keys())[-1]}')
        return
    
    print('no')

    
"""
params: dictionary of values that are out of place
        => i: original index (1-indexed)
        => v: difference between current and correct index
"""
def checkPalindrome(d):
    l = len(d)
    # Calculate the mid element for efficiency !
    if l % 2 == 0:
        mid = (l / 2) - 1
    else:
        mid = (l // 2)
    
    keys = d.keys()
    maxKey = list(keys)[-1]
    for i, k in enumerate(keys):
        if i > mid:
            # Already checked 
            break
        
        # Get ith key from the end of list 
        if maxKey - i not in keys:
            # It's already in place, so you can't reverse the subarray 
            return False
        else:
            if d[k] != -1 * d[maxKey - i]:
                # Differences are nonsymmetric, so subarray not reversible
                return False
    
    return True
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
