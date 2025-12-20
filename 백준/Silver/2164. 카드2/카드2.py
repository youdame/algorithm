import sys
from io import StringIO
from collections import deque


input = sys.stdin.readline
N = int(input())

큐 = deque([i + 1 for i in range(N)])

while len(큐) > 1:
    큐.popleft()
    큐.append(큐.popleft())
print(큐[0])
