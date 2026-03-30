n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
"""
dp[i][j]란 i, j까지 가기 위한 최솟값 
(1, N) -> (N, 1)

값이 오른쪽에서 오거나 위에서 오는 거임 

"""


dp = [[0] * n for _ in range(n)] 


