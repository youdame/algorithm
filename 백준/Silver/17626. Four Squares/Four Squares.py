import sys
from io import StringIO

input = sys.stdin.readline

N = int(input())

dp = [4] * (N + 1)

for i in range(1, N + 1):
    if (i ** (0.5)).is_integer():
        dp[i] = 1
        continue
    for j in range(1, int(i**0.5) + 1):
        dp[i] = min(dp[i], dp[i - j * j] + 1)

print(dp[N])
