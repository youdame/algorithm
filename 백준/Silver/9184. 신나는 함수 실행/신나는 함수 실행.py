import sys 
from io import StringIO

input = sys.stdin.readline


dp = [[[0]*21 for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        dp[0][i][j] = 1
        dp[i][0][j] = 1
        dp[i][j][0] = 1

for x in range(1, 21):
    for y in range(1, 21):
        for z in range(1, 21):
            if x < y and y < z:
                dp[x][y][z] = dp[x][y][z-1] + dp[x][y-1][z-1] - dp[x][y-1][z]
            else: 
                dp[x][y][z] = dp[x-1][y][z] + dp[x-1][y-1][z] + dp[x-1][y][z-1] - dp[x-1][y-1][z-1]
    

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return dp[20][20][20]
    return dp[a][b][c]
    
while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print(f"w{a, b, c} = {w(a,b,c)}")