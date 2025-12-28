import sys
from io import StringIO


input = sys.stdin.readline

N = int(input())
scores = [0]

for i in range(N):
    scores.append(int(input()))

dp = [[0, 0] for _ in range(N + 1)]

# dp[i][0] = i번째 계단, 연속 1칸일 때 최대 점수
# dp[i][1] = i번째 계단, 연속 2칸일 때 최대 점수

dp[1][0] = scores[1]  # 1번 밟음 (연속 1칸)
dp[1][1] = 0  # 불가능


if N >= 2:
    dp[2][0] = scores[2]
    dp[2][1] = scores[1] + scores[2]

for i in range(3, N + 1):
    dp[i][0] = scores[i] + max(dp[i - 2][0], dp[i - 2][1])
    dp[i][1] = scores[i] + dp[i - 1][0]
print(max(dp[N]))
