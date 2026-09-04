def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    puddles = [[y-1, x-1] for x, y in puddles]    
    

    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if (i== 0 and j == 0) or [i, j] in puddles:
                continue
            
            if i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000007
            
    # print(puddles)
    print(dp)
    return dp[n-1][m-1]