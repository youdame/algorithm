import sys
from io import StringIO

input = sys.stdin.readline
T = int(input())


dp = [-1] * (1 + 100)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]
for i in range(T):
    print(dp[int(input())])
