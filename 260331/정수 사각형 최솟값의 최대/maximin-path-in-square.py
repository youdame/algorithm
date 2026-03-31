

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]



dp = [[0] * n for _ in range(n)]

dp[0][0] = arr[0][0]

# 맨 왼쪽 줄 
for i in range(1, n):
    dp[i][0] = min(dp[i-1][0], arr[i][0])

# 맨 윗 줄 
for j in range(1, n):
    dp[0][j] = min(dp[0][j-1], arr[0][j])

for i in range(1, n):
    for j in range(1, n):
        # 위쪽 길로 왔을 때의 최솟값
        path_from_up = min(dp[i-1][j], arr[i][j])
        # 왼쪽 길로 왔을 때의 최솟값
        path_from_left = min(dp[i][j-1], arr[i][j])
        
        # 두 길 중 최솟값이 더 큰(유리한) 길을 선택!
        dp[i][j] = max(path_from_up, path_from_left)

print(dp[n-1][n-1])