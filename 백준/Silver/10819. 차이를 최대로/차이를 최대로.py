import sys
from io import StringIO
from itertools import permutations

input = sys.stdin.readline

N = int(input())


# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
def calculate(arr):
    sum = 0
    for i in range(len(arr) - 1):
        sum += abs(arr[i] - arr[i + 1])
    return sum


arr = list(map(int, input().strip().split(" ")))
maxSum = 0

for element in list(permutations(arr, N)):
    result = calculate(element)
    if maxSum < result:
        maxSum = result
print(maxSum)
