import sys
from io import StringIO


input = sys.stdin.readline


N, X = list(map(int, input().split()))

max_value = -1
for i in range(N):
    S, T = list(map(int, input().split()))
    if S + T <= X and max_value < S:
        max_value = S
print(max_value)
