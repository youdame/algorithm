import sys 
from io import StringIO



input = sys.stdin.readline

N = int(input())

# 이친수는 0으로 시작하지 않는다.
# 이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.

dp = [[0, 0] for _ in range(N+1)]


dp[1][0] = 0
dp[1][1] = 1

for index in range(2, N+1):
    dp[index][0] = dp[index - 1][1] + dp[index - 1][0]
    dp[index][1] = dp[index-1][0]
print(dp[N][0] + dp[N][1])
