import sys 
from io import StringIO


input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N)] 

arr = []
for _ in range(N):
    W, V = map(int, input().split())
    arr.append((W, V))

# i = 0 초기값
weight, value = arr[0]

for w in range(K+1):
    if w < weight:
        dp[0][w] = 0
    else:
        dp[0][w] = value

for i in range(1, N):
    weight, value = arr[i]
    for w in range(K+1):
        if w < weight:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w - weight] + value, dp[i-1][w]) 
print(dp[N-1][K])
    

