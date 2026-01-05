import sys
from io import StringIO


input = sys.stdin.readline
N, M = list(map(int, input().split()))
for i in range(N):
    print("".join(reversed(list(input().strip()))))
