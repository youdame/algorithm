import sys 
from io import StringIO


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    arr = []
    dp = [[0 for _ in range(n)] for _ in range(2)] 
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    # 뗄 수 있는 스티커 점수의 최댓값
    for i in range(1, n):
        if i > 1:
            dp[0][i] = max(dp[1][i-1], max(dp[0][i-2], dp[1][i-2])) + arr[0][i]
            dp[1][i] = max(dp[0][i-1], max(dp[0][i-2], dp[1][i-2])) + arr[1][i]
        else: 
            dp[0][i] = dp[1][i-1] + arr[0][i]
            dp[1][i] = dp[0][i-1] + arr[1][i]
    print(max(dp[0][n-1], dp[1][n-1]))