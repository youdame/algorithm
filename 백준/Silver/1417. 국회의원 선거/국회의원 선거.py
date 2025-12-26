import sys
from io import StringIO
from collections import deque


input = sys.stdin.readline

N = int(input())
다솜 = int(input())
queue = [int(input()) for i in range(N - 1)]
q = deque(sorted(queue))

answer = 0
while True:
    q = deque(sorted(q))
    if len(q) == 0 or 다솜 > q[-1]:
        break
    q[-1] -= 1
    다솜 += 1
    answer += 1
print(answer)
