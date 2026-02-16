import sys 
from io import StringIO

input = sys.stdin.readline

N = int(input())
M = int(input())
arr = sorted(list(map(int, input().split())))

left = 0
right = N - 1

answer = 0
while left < right and right < N:
    if arr[left] + arr[right] < M:
        left += 1
    elif arr[left] + arr[right] > M:
        right -= 1
    else:
        answer += 1
        left += 1

print(answer)
        