import sys 
from io import StringIO

input = sys.stdin.readline

T = int(input())

def binary_search(record_1, element):
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if record_1[mid] < element:
            left = mid + 1
        elif record_1[mid] > element:
            right = mid - 1 
        else:
            return 1
    return 0
            
    
for _ in range(T):
    N = int(input())
    record_1 = sorted(list(map(int, input().split())))
    M = int(input())
    record_2 = (list(map(int, input().split())))
    for element in record_2:
        print(binary_search(record_1, element))

        
