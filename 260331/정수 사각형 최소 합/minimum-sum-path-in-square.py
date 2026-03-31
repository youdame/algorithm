n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
"""
dp[i][j]란 i, j까지 가기 위한 최솟값 
(1, N) -> (N, 1)

오른쪽 or 위로부터 나에게 옴
즉, 이 말은 맨 오른쪽 열과 맨 위쪽 행은 

1) 맨 오른쪽 열 -> 위에서 오는 애들밖에 X 
2) 맨 위쪽 행 -> 오른쪽에서 오는 애들 밖에 X 
if-else로 하는 것보다 미리 이전 값을 채워두는 게 안전함
왜냐면 첫 값에서 인덱스 에러뜸 .. 

"""

dp = [[0] * n for _ in range(n)] 


dp[0][n-1] = grid[0][n-1]

# 맨 위 행
for j in range(n-2, -1, -1):
    dp[0][j] = dp[0][j+1] + grid[0][j]


# 맨 오른쪽 열
for i in range(1, n):
    dp[i][n-1] = dp[i-1][n-1] + grid[i][n-1]

# i는 1부터 , j는 n-2부터 시작
for i in range(1, n):
    for j in range(n-2, -1, -1):
        dp[i][j] = min(dp[i][j+1], dp[i-1][j]) + grid[i][j]
# print(dp)
print(dp[n-1][0])