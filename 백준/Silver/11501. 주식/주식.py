import sys
from io import StringIO


T = int(input())

for _ in range(T):
    N = int(input())

    arr = list(map(int, input().split()))
    max_M = 0
    profit = 0
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > max_M:
            max_M = arr[i]
        else:
            profit += max_M - arr[i]
    print(profit)
                
        
        
        
                