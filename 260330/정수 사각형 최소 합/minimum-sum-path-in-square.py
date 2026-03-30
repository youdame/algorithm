n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
"""
dp[i][j]란 i, j까지 가기 위한 최솟값 
(1, N) -> (N, 1)

값이 오른쪽에서 오거나 위에서 오는 거임 

"""


dp = [[0] * n for _ in range(n)] 

for i in range(n):
    for j in range(n-1, -1, -1):
        if 0 <= j+1 < n and 0 <= i-1 < n:
            dp[i][j] = min(dp[i][j+1], dp[i-1][j]) + grid[i][j]
        elif 0 <= j+1 < n:
            dp[i][j] = dp[i][j+1] + grid[i][j]
        else:
            dp[i][j] = dp[i-1][j] + grid[i][j]

print(dp[n-1][0])