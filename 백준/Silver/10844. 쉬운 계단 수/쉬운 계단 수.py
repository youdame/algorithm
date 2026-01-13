import sys
from io import StringIO


input = sys.stdin.readline

N = int(input())
MOD = 10**9
# dp[길이][마지막 숫자]
dp = [[0 for j in range(10)] for i in range(101)]
for i in range(1, 10):
    dp[1][i] = 1

for j in range(2, 101):
    for k in range(10):
        if k == 0:
            dp[j][k] = dp[j - 1][k + 1] % MOD
        elif k == 9:
            dp[j][k] = dp[j - 1][k - 1] % MOD
        else:
            dp[j][k] = (dp[j - 1][k - 1] + dp[j - 1][k + 1]) % MOD
print(sum(dp[N]) % MOD)
