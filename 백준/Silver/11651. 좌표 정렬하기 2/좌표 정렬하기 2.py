import sys
from io import StringIO


input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))
for element in sorted(arr, key=lambda x : (x[1], x[0])):
    print(*element)

