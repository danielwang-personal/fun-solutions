# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

# https://www.hackerrank.com/challenges/absolute-permutation/problem?isFullScreen=true

def absolutePermutation(n, k):
    # Write your code here
    if k == 0:
        return [i for i in range(1,n+1)]
    
    if n % (2*k) != 0: 
        return [-1]
    
    groups = int(n / (2*k))
    res = []
    count = 0
    for group in range(groups):
        low = 2*k*group + 1
    
        med = low + k
        high = group * 2 * k
        for i in range(med, med + k):
            res.append(i)
        for j in range(low, med):
            res.append(j)
    
            
            
    return res
        
        
