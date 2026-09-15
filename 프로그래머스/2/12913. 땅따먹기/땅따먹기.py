def solution(land):

    n = len(land)
    m = len(land[0])
    
    dp = [[0] * m for _ in range(n)]
    
    
    
    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = land[i][j]
            else:

                dp[i][j] = max(dp[i-1][:j] + dp[i-1][j+1:]) + land[i][j]
                
    return max(dp[n-1])
            