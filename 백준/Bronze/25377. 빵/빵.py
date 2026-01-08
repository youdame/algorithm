import sys
from io import StringIO


input = sys.stdin.readline


N = int(input())
min_value = 1e9
for i in range(N):
    A, B = list(map(int, input().split()))
    if A <= B:
        min_value = min(min_value, B)
print(-1 if min_value == 1e9 else min_value)
