import sys
from io import StringIO



input = sys.stdin.readline

N = int(input())

dp = [[0] * 3 for _ in range(N)]

for i in range(N):
    R, G, B = map(int, input().split())
    if i == 0:
        dp[0][0] = R
        dp[0][1] = B
        dp[0][2] = G

    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + R
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + B
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + G
print(min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))
