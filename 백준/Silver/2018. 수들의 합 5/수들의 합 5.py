import sys 
from io import StringIO


input = sys.stdin.readline

N = int(input())
left = 1
right = 1

sum = 1
answer = 0
while right <= N:
    if sum < N:
        right += 1
        sum += right
    elif sum > N:
        sum -= left
        left += 1
    elif sum == N:
        sum -= left
        left += 1
        answer += 1
print(answer)