import sys
from io import StringIO

input = sys.stdin.readline
arr = []
N = int(input())
for _ in range(N):
    name = input().strip()
    if len(name) == 3:
        arr.append(name)
print(sorted(arr)[0])
